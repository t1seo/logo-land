import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { existsSync } from "node:fs";
import { mkdir, mkdtemp, readFile, rm, writeFile } from "node:fs/promises";
import { dirname, join, resolve } from "node:path";
import { spawnSync } from "node:child_process";
import { fileURLToPath, pathToFileURL } from "node:url";
import test from "node:test";

const toolRoot = process.env.LOGOPIA_GALLERY_QA_ROOT;
const repo = resolve(dirname(fileURLToPath(import.meta.url)), "../..");
const evidence = process.env.LOGOPIA_GALLERY_QA_EVIDENCE || join(repo, "docs/qa/hermes-workflow/gallery");
const digest = (bytes) => createHash("sha256").update(bytes).digest("hex");

test("actual Chrome offline comparison, feedback, original bytes and recovery", {
  skip: !toolRoot && "Set LOGOPIA_GALLERY_QA_ROOT to isolated task-local playwright-core tooling",
  timeout: 180000,
}, async () => {
  // Given: a real publication, separate canonical workflow and a fresh owned Chrome profile.
  const { chromium } = await import(pathToFileURL(join(toolRoot, "node_modules/playwright-core/index.mjs")).href);
  await mkdir(evidence, { recursive: true });
  const fixture = await mkdtemp(join(toolRoot, "fixture-"));
  const profile = await mkdtemp(join(toolRoot, "chrome-"));
  const downloads = await mkdtemp(join(toolRoot, "downloads-"));
  const receipt = { steps: [], resources: { fixture, profile, downloads }, cleanup: false };
  let context = null;
  let page = null;
  try {
  const setup = spawnSync("uv", ["run", "--locked", "python", "-c",
    "from pathlib import Path; import sys; from tests.hermes.test_gallery_fixture import prepare_browser_fixture; prepare_browser_fixture(Path(sys.argv[1]))", fixture],
    { cwd: repo, env: { ...process.env, PYTHONPATH: join(repo, "integrations/hermes") }, encoding: "utf8", timeout: 30000 });
  assert.equal(setup.status, 0, setup.stderr);
  const canonicalPath = join(fixture, "workspace/workflow.json");
  const canonical = await readFile(canonicalPath);
  const state = JSON.parse(canonical);
  const original = state.candidates[1];
  const url = pathToFileURL(join(fixture, "published/index.html")).href;
  context = await chromium.launchPersistentContext(profile, {
    executablePath: "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    headless: false, viewport: { width: 1440, height: 1080 }, deviceScaleFactor: 1,
    downloadsPath: downloads, acceptDownloads: true, timeout: 20000,
    args: ["--no-first-run", "--disable-background-networking"],
  });
  page = context.pages()[0];
  receipt.browserVersion = context.browser().version();
  page.setDefaultTimeout(7000);
  page.setDefaultNavigationTimeout(10000);
  const pageErrors = [];
  const externalRequests = [];
  page.on("pageerror", (error) => pageErrors.push(error.message));
  page.on("request", (request) => { if (/^https?:/.test(request.url())) externalRequests.push(request.url()); });
  await context.route(/^https?:\/\//, (route) => route.abort());
    // When: the actual required user flow is driven through the file URL.
    await page.goto(url);
    await page.waitForFunction(() => [...document.images].every((image) => image.complete && image.naturalWidth > 0));
    assert.equal(await page.locator("[data-candidate]").count(), 4);
    assert.equal(await page.locator("#canonical-selection").innerText(), "candidate-1");
    assert.match(await page.locator('[data-candidate="candidate-2"] .review-state').innerText(), /192px 조건 통과/);
    assert.equal(await page.locator('[data-candidate="candidate-2"] .target-image').evaluate((el) => el.getBoundingClientRect().width), 192);
    await page.screenshot({ path: join(evidence, "desktop-overview.png") });
    await page.locator("#candidates").screenshot({ path: join(evidence, "desktop-comparison.png") });
    await page.click('[data-feedback="candidate-2"]');
    await page.fill("#keep", "색과 열린 중심");
    await page.fill("#change", "간격만 넓혀 주세요");
    await page.click("#copy-feedback");
    const expected = {
      schema_version: 1, workflow_id: "gallery-fixture", expected_revision: 7,
      candidate_id: "candidate-2", candidate_sha256: original.sha256,
      action: "revise", keep: ["색과 열린 중심"], change: "간격만 넓혀 주세요",
    };
    // Then: exact core feedback identity/notes and unchanged canonical bytes are observed.
    assert.deepEqual(JSON.parse(await page.inputValue("#feedback-output")), expected);
    assert.equal(await page.locator("#feedback-output").evaluate((el) => el.scrollHeight <= el.clientHeight), true);
    assert.deepEqual(await readFile(canonicalPath), canonical);
    assert.equal(await page.locator("#canonical-selection").innerText(), "candidate-1");
    await page.locator("#feedback").screenshot({ path: join(evidence, "desktop-feedback.png") });
    receipt.steps.push("required click/fill/copy flow: exact envelope; canonical bytes unchanged");
    receipt.feedback = expected;

    for (let index = 0; index < 3; index += 1) {
      await page.reload();
      assert.deepEqual(JSON.parse(await page.inputValue("#feedback-output")), expected);
      await page.click('[data-feedback="candidate-2"]');
      assert.equal(await page.inputValue("#change"), expected.change);
    }
    await page.evaluate(() => Object.defineProperty(navigator, "clipboard", {
      configurable: true, value: { writeText: async () => { throw new DOMException("fixture denial", "NotAllowedError"); } },
    }));
    await page.click("#copy-feedback");
    await page.waitForFunction(() => document.querySelector("#feedback-status").textContent.includes("자동 복사를 사용할 수 없습니다"));
    assert.equal(await page.locator("#feedback-output").evaluate((el) => el.selectionEnd - el.selectionStart), (await page.inputValue("#feedback-output")).length);
    receipt.steps.push("three reloads/repeated draft activation; denied clipboard selects full exact output");

    const downloadEvent = page.waitForEvent("download");
    await page.click('[data-download="candidate-2"]');
    const download = await downloadEvent;
    const downloadedPath = join(downloads, "received-original.png");
    await download.saveAs(downloadedPath);
    assert.equal(await download.failure(), null);
    const downloaded = await readFile(downloadedPath);
    assert.equal(digest(downloaded), original.sha256);
    receipt.originalSha256 = digest(downloaded);
    const originalResponse = page.waitForResponse((response) => response.url().endsWith("/originals/candidate-2.png"));
    await page.click('[data-candidate="candidate-2"] .original-stage');
    const opened = await originalResponse;
    assert.equal(digest(await opened.body()), original.sha256);
    await page.goBack();
    assert.deepEqual(JSON.parse(await page.inputValue("#feedback-output")), expected);
    receipt.steps.push("actual browser download and opened PNG response bytes match canonical SHA-256; back restores draft");

    await page.focus('[data-feedback="candidate-3"]');
    await page.keyboard.press("Enter");
    assert.equal(await page.locator("#keep").evaluate((el) => el === document.activeElement), true);
    await page.keyboard.type("shape");
    await page.keyboard.press("Tab");
    assert.equal(await page.locator("#change").evaluate((el) => el === document.activeElement), true);
    await page.keyboard.type("spacing");
    await page.keyboard.press("Tab");
    assert.equal(await page.locator("#copy-feedback").evaluate((el) => el === document.activeElement), true);
    await page.keyboard.press("Enter");
    assert.equal(JSON.parse(await page.inputValue("#feedback-output")).candidate_id, "candidate-3");
    await page.focus('[data-candidate="candidate-4"] .lineage summary');
    await page.keyboard.press("Enter");
    assert.equal(await page.locator('[data-candidate="candidate-4"] .lineage details').getAttribute("open"), "");
    await page.locator('[data-candidate="candidate-4"]').screenshot({ path: join(evidence, "parent-child.png") });
    await page.click('[data-candidate="candidate-4"] .lineage a');
    assert.equal(new URL(page.url()).hash, "#candidate-2");
    receipt.steps.push("keyboard Enter/Tab draft interaction; parent comparison disclosure/link");

    await page.setViewportSize({ width: 390, height: 844 });
    await page.evaluate(() => window.scrollTo(0, 0));
    assert.equal(await page.evaluate(() => document.documentElement.scrollWidth), 390);
    await page.screenshot({ path: join(evidence, "mobile-overview.png") });
    await page.locator('[data-candidate="candidate-2"]').screenshot({ path: join(evidence, "mobile-candidate.png") });
    assert.equal(await page.locator('[data-candidate="candidate-2"] .target-image').evaluate((el) => el.getBoundingClientRect().width), 192);
    await page.click('[data-feedback="candidate-2"]');
    await page.fill("#keep", expected.keep[0]);
    await page.fill("#change", expected.change);
    await page.locator("#feedback").screenshot({ path: join(evidence, "mobile-feedback.png") });
    await page.goto(pathToFileURL(join(fixture, "wide/index.html")).href);
    assert.equal(await page.evaluate(() => document.documentElement.scrollWidth), 390);
    assert.equal(await page.locator('[data-candidate="candidate-2"] .target-image').evaluate((el) => el.getBoundingClientRect().width), 1024);
    receipt.steps.push("390px document has no horizontal overflow; previews remain 192px/1024px with bounded inner scrolling");

    await page.goto(url);
    await page.goto(pathToFileURL(join(fixture, "newer/index.html")).href);
    assert.equal(await page.inputValue("#feedback-output"), "");
    assert.match(await page.locator("#snapshot-binding").innerText(), /r8/);
    await page.goBack();
    assert.deepEqual(JSON.parse(await page.inputValue("#feedback-output")), expected);
    assert.match(await page.locator("#snapshot-notice").innerText(), /최신 상태와 다를 수/);
    await page.evaluate((draft) => localStorage.setItem("logopia:feedback:gallery-fixture:r7", JSON.stringify({ ...draft, expected_revision: 8 })), expected);
    await page.reload();
    assert.equal(await page.inputValue("#feedback-output"), "");
    assert.match(await page.locator("#feedback-status").innerText(), /맞지 않아 불러오지 않았습니다/);
    receipt.steps.push("visible snapshot binding; new revision does not borrow old draft; stale stored revision rejected");

    await page.click('[data-feedback="candidate-2"]');
    await page.selectOption("#feedback-action", "choose");
    assert.equal(JSON.parse(await page.inputValue("#feedback-output")).action, "choose");
    assert.equal(await page.locator("#canonical-selection").innerText(), "candidate-1");
    await page.click("#clear-feedback");
    assert.equal(await page.inputValue("#feedback-output"), "");
    await page.reload();
    assert.equal(await page.inputValue("#feedback-output"), "");
    receipt.steps.push("choice remains a draft; clearing and reload leave canonical selection intact");

    await page.goto(pathToFileURL(join(fixture, "hostile/index.html")).href);
    assert.equal(await page.locator('[data-fixture="inert"]').count(), 0);
    assert.match(await page.locator("#brand-title").innerText(), /<b data-fixture="inert">/);
    await page.goto(pathToFileURL(join(fixture, "empty/index.html")).href);
    assert.match(await page.locator(".empty-state").innerText(), /아직 비교할 원본이 없습니다/);
    assert.equal(await page.locator("#copy-feedback").isDisabled(), true);
    await page.screenshot({ path: join(evidence, "empty-state.png"), fullPage: true });
    const nojs = await context.browser().newContext({ javaScriptEnabled: false });
    try {
      const staticPage = await nojs.newPage();
      await staticPage.goto(url);
      assert.equal(await staticPage.locator('[data-download="candidate-2"]').isVisible(), true);
      assert.match(await staticPage.locator("noscript").innerText(), /JavaScript/);
    } finally { await nojs.close(); }
    receipt.steps.push("inert HTML-looking instructions, empty state and no-JavaScript originals");
    assert.deepEqual(await readFile(canonicalPath), canonical);
    assert.deepEqual(pageErrors, []);
    assert.deepEqual(externalRequests, []);
    receipt.steps.push("no page errors, no external requests, canonical bytes unchanged after all actions");
  } catch (error) {
    receipt.firstFailure = String(error);
    const firstFailure = join(evidence, "browser-first-failure.json");
    if (!existsSync(firstFailure)) {
      await writeFile(firstFailure, JSON.stringify(receipt, null, 2));
      if (page && !page.isClosed()) await page.screenshot({ path: join(evidence, "browser-first-failure.png"), fullPage: true });
    }
    throw error;
  } finally {
    try {
      if (context) await context.close();
      receipt.contextClosed = true;
    } finally {
      await rm(profile, { recursive: true });
      await rm(downloads, { recursive: true });
      await rm(fixture, { recursive: true });
      receipt.cleanup = receipt.contextClosed === true;
      await writeFile(join(evidence, "browser-receipt.json"), JSON.stringify(receipt, null, 2));
    }
  }
});
