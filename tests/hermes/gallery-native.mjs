import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { existsSync } from "node:fs";
import { mkdir, mkdtemp, readFile, rm, writeFile } from "node:fs/promises";
import { dirname, join, resolve } from "node:path";
import { spawnSync } from "node:child_process";
import { fileURLToPath, pathToFileURL } from "node:url";
import test from "node:test";

const root = process.env.LOGOPIA_GALLERY_QA_ROOT;
const baseline = process.env.LOGOPIA_GALLERY_NATIVE_BASELINE === "1";
const repo = resolve(dirname(fileURLToPath(import.meta.url)), "../..");
const evidence = join(repo, "docs/qa/hermes-workflow/gallery");
const source = join(repo, ".logo-generator/workflows/offcut-hermes-demo/workflow.json");
const digest = (bytes) => createHash("sha256").update(bytes).digest("hex");

test("actual native long strategy stays compact with complete keyboard disclosure", {
  skip: (!root || !existsSync(source)) && "Requires owned Playwright tooling and read-only OFFCUT sample",
  timeout: 90000,
}, async () => {
  const { chromium } = await import(pathToFileURL(join(root, "node_modules/playwright-core/index.mjs")).href);
  const profile = await mkdtemp(join(root, "chrome-native-"));
  const fixture = await mkdtemp(join(root, "fixture-native-"));
  const receipt = { baseline, profile, fixture, cleanup: false };
  let context = null;
  let page = null;
  try {
    await mkdir(evidence, { recursive: true });
    const canonical = await readFile(source);
    const publication = baseline ? join(root, "baseline-native") : join(fixture, "published");
    if (!baseline) {
      const setup = spawnSync("uv", ["run", "--locked", "python", "-c",
        "from pathlib import Path; import sys; from logopia_studio.models import Workflow; from logopia_studio.gallery import publish_gallery; p=Path(sys.argv[1]); s=Workflow.model_validate_json(p.read_bytes()); publish_gallery(Path.cwd(),s,Path(sys.argv[2]))", source, publication],
        { cwd: repo, env: { ...process.env, PYTHONPATH: join(repo, "integrations/hermes") }, encoding: "utf8", timeout: 30000 });
      assert.equal(setup.status, 0, setup.stderr);
    }
    const snapshot = JSON.parse(await readFile(join(publication, "workflow.json"), "utf8"));
    context = await chromium.launchPersistentContext(profile, {
      executablePath: "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
      headless: false, viewport: { width: 1440, height: 1080 }, deviceScaleFactor: 1,
      timeout: 20000, args: ["--no-first-run", "--disable-background-networking"],
    });
    page = context.pages()[0];
    page.setDefaultTimeout(7000);
    page.setDefaultNavigationTimeout(10000);
    await context.route(/^https?:\/\//, (route) => route.abort());
    await page.goto(pathToFileURL(join(publication, "index.html")).href);
    await page.waitForFunction(() => [...document.images].every((image) => image.complete && image.naturalWidth > 0));
    receipt.candidateTopDesktop = await page.locator("#candidates").evaluate((el) => el.getBoundingClientRect().top + scrollY);
    receipt.strategyHeightDesktop = await page.locator(".strategy").evaluate((el) => el.getBoundingClientRect().height);
    receipt.workflow = snapshot.id;
    receipt.revision = snapshot.revision;
    receipt.candidateCount = snapshot.candidates.length;
    receipt.strategySha256 = digest(Buffer.from(JSON.stringify(snapshot.strategy)));
    await page.screenshot({ path: join(evidence, `native-strategy-${baseline ? "before" : "after"}.png`) });
    assert.ok(receipt.candidateTopDesktop < 1150, `Candidates begin at ${receipt.candidateTopDesktop}px`);
    const disclosure = page.locator("#strategy-details");
    assert.equal(await disclosure.getAttribute("open"), null);
    await disclosure.locator("summary").focus();
    await page.keyboard.press("Enter");
    assert.equal(await disclosure.getAttribute("open"), "");
    const fullText = await disclosure.innerText();
    for (const value of Object.values(snapshot.strategy)) {
      for (const text of Array.isArray(value) ? value : [value]) assert.ok(fullText.includes(text));
    }
    await page.keyboard.press("Enter");
    assert.equal(await disclosure.getAttribute("open"), null);
    for (const candidate of snapshot.candidates) {
      assert.equal(digest(await readFile(join(publication, "originals", `${candidate.id}.png`))), candidate.sha256);
    }
    await page.locator("#candidates").scrollIntoViewIfNeeded();
    await page.screenshot({ path: join(evidence, "native-strategy-originals.png") });
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto(pathToFileURL(join(publication, "index.html")).href);
    assert.equal(await page.evaluate(() => document.documentElement.scrollWidth), 390);
    receipt.candidateTopMobile = await page.locator("#candidates").evaluate((el) => el.getBoundingClientRect().top + scrollY);
    assert.ok(receipt.candidateTopMobile < 1450, `Mobile candidates begin at ${receipt.candidateTopMobile}px`);
    await page.locator(".strategy").scrollIntoViewIfNeeded();
    await page.screenshot({ path: join(evidence, "native-strategy-mobile.png") });
    assert.deepEqual(await readFile(source), canonical);
    receipt.canonicalUnchanged = true;
    receipt.originalsExact = true;
    receipt.keyboardDisclosure = true;
  } catch (error) {
    receipt.failure = String(error);
    throw error;
  } finally {
    if (context) await context.close();
    await rm(profile, { recursive: true, force: true });
    await rm(fixture, { recursive: true, force: true });
    receipt.cleanup = true;
    await writeFile(join(evidence, `delivery-native-${baseline ? "first-failure" : "receipt"}.json`), JSON.stringify(receipt, null, 2));
  }
});
