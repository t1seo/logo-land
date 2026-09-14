import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { existsSync } from "node:fs";
import { mkdir, mkdtemp, readFile, rm, writeFile } from "node:fs/promises";
import { dirname, join, resolve } from "node:path";
import { spawnSync } from "node:child_process";
import { fileURLToPath, pathToFileURL } from "node:url";
import test from "node:test";

const root = process.env.LOGOPIA_GALLERY_QA_ROOT;
const repo = resolve(dirname(fileURLToPath(import.meta.url)), "../..");
const evidence = join(repo, "docs/qa/hermes-workflow/gallery");
const digest = (bytes) => createHash("sha256").update(bytes).digest("hex");

test("actual Chrome delivery ZIP bytes, selected PNG, guide and immutable snapshot", {
  skip: !root && "Set LOGOPIA_GALLERY_QA_ROOT to owned task-local Playwright tooling",
  timeout: 150000,
}, async () => {
  const { chromium } = await import(pathToFileURL(join(root, "node_modules/playwright-core/index.mjs")).href);
  const fixture = await mkdtemp(join(root, "fixture-delivery-"));
  const profile = await mkdtemp(join(root, "chrome-delivery-"));
  const downloads = await mkdtemp(join(root, "downloads-delivery-"));
  const receipt = { steps: [], resources: { fixture, profile, downloads }, cleanup: false };
  let context = null;
  let noScript = null;
  let page = null;
  try {
    await mkdir(evidence, { recursive: true });
    const setup = spawnSync("uv", ["run", "--locked", "python", "-c",
      "from pathlib import Path; import sys; from tests.hermes.test_gallery_delivery_fixture import prepare_delivery_browser_fixture; prepare_delivery_browser_fixture(Path(sys.argv[1]))", fixture],
      { cwd: repo, env: { ...process.env, PYTHONPATH: join(repo, "integrations/hermes") }, encoding: "utf8", timeout: 30000 });
    assert.equal(setup.status, 0, setup.stderr);
    const canonicalPath = join(fixture, "workspace/workflow.json");
    const canonical = await readFile(canonicalPath);
    const state = JSON.parse(canonical);
    const candidate = state.candidates.find((item) => item.id === state.selected_id);
    const packageBytes = await readFile(join(fixture, "workspace", state.delivery.zip_path));
    const guideBytes = await readFile(join(fixture, "workspace", state.delivery.path, "brand-guide.md"));
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
    const errors = [];
    const external = [];
    page.on("pageerror", (error) => errors.push(error.message));
    page.on("request", (request) => { if (/^https?:/.test(request.url())) external.push(request.url()); });
    await context.route(/^https?:\/\//, (route) => route.abort());
    await page.goto(url);
    await page.waitForFunction(() => [...document.images].every((image) => image.complete && image.naturalWidth > 0));
    assert.equal(await page.locator("#delivery-binding").innerText(), "gallery-fixture · r7 · candidate-2");
    assert.equal(await page.locator("[data-guide]").count(), 0);
    await page.screenshot({ path: join(evidence, "delivery-desktop.png") });
    for (let index = 0; index < 3; index += 1) {
      const pending = page.waitForEvent("download");
      await page.click("#download-package");
      const download = await pending;
      assert.equal(await download.failure(), null);
      const destination = join(downloads, `package-${index}.zip`);
      await download.saveAs(destination);
      const downloaded = await readFile(destination);
      assert.equal(digest(downloaded), state.delivery.zip_sha256);
      assert.deepEqual(downloaded, packageBytes);
      const inspect = spawnSync("uv", ["run", "--locked", "python", "-c",
        "import json,sys; from hashlib import sha256; from zipfile import ZipFile; z=ZipFile(sys.argv[1]); print(json.dumps({'pngSha256':sha256(z.read('logo.png')).hexdigest(),'members':z.namelist()})); z.close()", destination],
        { cwd: repo, encoding: "utf8", timeout: 15000 });
      assert.equal(inspect.status, 0, inspect.stderr);
      const payload = JSON.parse(inspect.stdout);
      assert.equal(payload.pngSha256, candidate.sha256);
      assert.deepEqual(payload.members.sort(), ["brand-guide.md", "logo.png", "manifest.json"]);
      receipt.zipSha256 = digest(downloaded);
      receipt.selectedPngSha256 = payload.pngSha256;
      receipt.packageBytes = downloaded.length;
      await page.reload();
    }
    receipt.steps.push("three completed downloads: exact ZIP bytes and selected PNG member hash, with reloads");
    const guideEvent = page.waitForEvent("download");
    await page.click("#download-guide");
    const guide = await guideEvent;
    assert.equal(await guide.failure(), null);
    await guide.saveAs(join(downloads, "guide.md"));
    assert.deepEqual(await readFile(join(downloads, "guide.md")), guideBytes);
    receipt.guideSha256 = digest(guideBytes);
    await page.locator(".delivery-record summary").focus();
    await page.keyboard.press("Enter");
    assert.equal(await page.locator(".delivery-record").getAttribute("open"), "");
    const manifestResponse = await page.goto(pathToFileURL(join(fixture, "published/delivery/manifest.json")).href);
    assert.equal(digest(await manifestResponse.body()), state.delivery.manifest_sha256);
    await page.goBack();
    const keyboardDownload = page.waitForEvent("download");
    await page.locator("#download-package").focus();
    await page.keyboard.press("Enter");
    const keyboardFile = await keyboardDownload;
    await keyboardFile.saveAs(join(downloads, "keyboard.zip"));
    assert.equal(digest(await readFile(join(downloads, "keyboard.zip"))), state.delivery.zip_sha256);
    receipt.steps.push("guide exact bytes, manifest open hash and keyboard package download after back");
    await page.click('[data-feedback="candidate-2"]');
    await page.fill("#keep", "색과 열린 중심");
    await page.fill("#change", "간격만 넓혀 주세요");
    await page.click("#copy-feedback");
    const feedback = JSON.parse(await page.inputValue("#feedback-output"));
    assert.equal(feedback.expected_revision, state.revision);
    assert.equal(feedback.candidate_id, candidate.id);
    assert.deepEqual(feedback.keep, ["색과 열린 중심"]);
    await page.goto(pathToFileURL(join(fixture, "newer/index.html")).href);
    assert.equal(await page.locator("#download-package").count(), 0);
    assert.equal(await page.inputValue("#feedback-output"), "");
    await page.goBack();
    assert.deepEqual(JSON.parse(await page.inputValue("#feedback-output")), feedback);
    assert.match(await page.locator("#snapshot-notice").innerText(), /자동 갱신되지 않습니다/);
    assert.equal(await page.locator("#delivery-binding").innerText(), "gallery-fixture · r7 · candidate-2");
    await page.goto(pathToFileURL(join(fixture, "unreviewed/index.html")).href);
    assert.equal(await page.locator("#download-package").count(), 0);
    assert.equal(await page.locator("#delivery").count(), 0);
    assert.equal(await page.locator("#canonical-selection").innerText(), "candidate-3");
    receipt.steps.push("unreviewed/newer snapshots have no package; back retains explicit old identity and draft");
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto(url);
    assert.equal(await page.evaluate(() => document.documentElement.scrollWidth), 390);
    await page.locator("#delivery").scrollIntoViewIfNeeded();
    assert.equal(await page.locator("#download-package").isVisible(), true);
    await page.screenshot({ path: join(evidence, "delivery-mobile.png") });
    receipt.mobileWidth = await page.evaluate(() => document.documentElement.scrollWidth);
    noScript = await context.browser().newContext({ javaScriptEnabled: false, acceptDownloads: true });
    const staticPage = await noScript.newPage();
    staticPage.setDefaultTimeout(7000);
    await staticPage.goto(url, { timeout: 10000 });
    const staticDownload = staticPage.waitForEvent("download");
    await staticPage.click("#download-package");
    const staticFile = await staticDownload;
    await staticFile.saveAs(join(downloads, "no-script.zip"));
    assert.equal(digest(await readFile(join(downloads, "no-script.zip"))), state.delivery.zip_sha256);
    receipt.steps.push("390px no horizontal overflow and actual package download without JavaScript");
    assert.deepEqual(await readFile(canonicalPath), canonical);
    assert.deepEqual(await readFile(join(fixture, "workspace", state.delivery.zip_path)), packageBytes);
    assert.deepEqual(errors, []);
    assert.deepEqual(external, []);
    receipt.canonicalUnchanged = true;
    receipt.externalRequests = external.length;
    receipt.pageErrors = errors.length;
  } catch (error) {
    receipt.failure = String(error);
    const first = join(evidence, "delivery-first-failure.json");
    if (!existsSync(first)) {
      await writeFile(first, JSON.stringify(receipt, null, 2));
      if (page) await page.screenshot({ path: join(evidence, "delivery-first-failure.png") });
    }
    throw error;
  } finally {
    if (noScript) await noScript.close();
    if (context) await context.close();
    for (const resource of [fixture, profile, downloads]) await rm(resource, { recursive: true, force: true });
    receipt.cleanup = true;
    await writeFile(join(evidence, "delivery-browser-receipt.json"), JSON.stringify(receipt, null, 2));
  }
});
