import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import test from "node:test";
import { runInNewContext } from "node:vm";

const template = readFileSync(
  new URL("../skills/logo-land/assets/comparison-gallery.template.html", import.meta.url),
  "utf8",
);
const scripts = [...template.matchAll(/<script>([\s\S]*?)<\/script>/g)];
assert.equal(scripts.length, 1, "Execute the single authored production script");
const source = scripts[0][1];
const kindsAndStyles = [
  ["app_icon", "mascot"], ["app_icon", "pictogram"],
  ["app_icon", "abstract"], ["app_icon", "abstract"],
  ["app_icon", "letterform"], ["app_icon", "pictogram"],
  ["app_icon", "pictogram"], ["brand", "combination"],
];

class Target {
  listeners = new Map();

  addEventListener(type, handler) {
    const handlers = this.listeners.get(type) ?? [];
    handlers.push(handler);
    this.listeners.set(type, handlers);
  }

  dispatch(type, detail = {}) {
    for (const handler of this.listeners.get(type) ?? []) handler(detail);
  }
}

function page(initial = {}) {
  const controls = new Map();
  for (const [, id, body] of template.matchAll(/<select id="([^"]+)">([\s\S]*?)<\/select>/g)) {
    const options = [...body.matchAll(/<option value="([^"]+)"/g)].map((match) => match[1]);
    if (id === "style") options.push(...new Set(kindsAndStyles.map(([, style]) => style)));
    controls.set(id, { value: options[0], defaultValue: options[0], options });
  }
  const form = new Target();
  const window = new Target();
  const timers = [];
  window.setTimeout = (callback) => timers.push(callback);
  const cards = kindsAndStyles.map(([kind, style]) => ({ dataset: { kind, style }, hidden: false }));
  const gallery = {
    dataset: { context: "artwork", surround: "light" },
    querySelectorAll(selector) {
      assert.equal(selector, ".candidate");
      return cards;
    },
  };
  const count = { textContent: "8 of 8 candidates" };
  const empty = { hidden: true };
  const status = { textContent: "" };
  const elements = new Map([...controls, ["controls", form], ["gallery", gallery],
    ["result-count", count], ["empty", empty]]);
  function restore(values) {
    for (const [id, value] of Object.entries(values)) {
      const control = controls.get(id);
      assert.ok(control, `Known select: ${id}`);
      assert.ok(control.options.includes(value), `Real finite select option: ${id}=${value}`);
      control.value = value;
    }
  }
  restore(initial);
  runInNewContext(source, {
    window,
    document: {
      getElementById(id) {
        assert.ok(elements.has(id), `Known element: ${id}`);
        return elements.get(id);
      },
      querySelectorAll(selector) {
        if (selector === "[data-copy]") return [];
        assert.equal(selector, ".copy-status");
        return [status];
      },
    },
  }, { timeout: 1000, filename: "comparison-gallery.template.html" });
  return {
    restore, form, window, cards, gallery, count, empty, status, controls,
    flushTimers() {
      while (timers.length) timers.shift()();
    },
    reset() {
      form.dispatch("reset");
      for (const control of controls.values()) control.value = control.defaultValue;
      this.flushTimers();
    },
  };
}

function expectView(view, visible, context = "artwork", surround = "light") {
  assert.equal(view.count.textContent, `${visible.length} of 8 candidates`);
  assert.deepEqual(view.cards.flatMap((card, index) => card.hidden ? [] : [index]), visible);
  assert.equal(view.empty.hidden, visible.length !== 0);
  assert.equal(view.gallery.dataset.context, context);
  assert.equal(view.gallery.dataset.surround, surround);
}

test("PIN: initialized controls filter kind and style, count empty matches, and reset after defaults", () => {
  const view = page();
  expectView(view, [0, 1, 2, 3, 4, 5, 6, 7]);
  view.restore({ kind: "brand" });
  view.form.dispatch("change");
  expectView(view, [7]);
  view.restore({ style: "abstract", context: "web-header", surround: "dark" });
  view.form.dispatch("change");
  expectView(view, [], "web-header", "dark");
  view.restore({ kind: "app_icon" });
  view.form.dispatch("change");
  expectView(view, [2, 3], "web-header", "dark");
  view.status.textContent = "Source and notes copied.";
  view.reset();
  expectView(view, [0, 1, 2, 3, 4, 5, 6, 7]);
  assert.equal(view.status.textContent, "");
});

test("PIN: values restored before script evaluation initialize a consistent view", () => {
  expectView(page({ kind: "brand", context: "favicon", surround: "dark" }), [7], "favicon", "dark");
});

for (const persisted of [false, true]) {
  test(`Back restores Brand logo after initialization; pageshow persisted=${persisted} keeps one card`, () => {
    const view = page();
    view.restore({ kind: "brand" });
    view.window.dispatch("pageshow", { persisted });
    view.flushTimers();
    assert.equal(view.controls.get("kind").value, "brand");
    expectView(view, [7]);
  });
}

test("Two history cycles restore kind/style intersection, empty state, count, and preview settings", () => {
  const view = page();
  for (let cycle = 0; cycle < 2; cycle += 1) {
    view.restore({ kind: "brand", style: "abstract", context: "app-home", surround: "dark" });
    view.window.dispatch("pageshow", { persisted: cycle === 1 });
    view.flushTimers();
    expectView(view, [], "app-home", "dark");
    view.restore({ kind: "app_icon", style: "abstract", context: "web-header", surround: "light" });
    view.window.dispatch("pageshow", { persisted: true });
    view.flushTimers();
    expectView(view, [2, 3], "web-header", "light");
    view.reset();
    expectView(view, [0, 1, 2, 3, 4, 5, 6, 7]);
  }
});

test("History restoration updates every preview and surround without changing selected values", () => {
  const view = page();
  for (const context of ["artwork", "app-home", "web-header", "favicon"]) {
    for (const surround of ["light", "dark"]) {
      view.restore({ context, surround });
      view.window.dispatch("pageshow", { persisted: true });
      view.flushTimers();
      expectView(view, [0, 1, 2, 3, 4, 5, 6, 7], context, surround);
      assert.equal(view.controls.get("context").value, context);
      assert.equal(view.controls.get("surround").value, surround);
    }
  }
});
