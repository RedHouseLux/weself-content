// Render every <section class="slide"> (or "card") of an HTML file to PNG.
// Usage: node tools/render.cjs <folder> <name-prefix>   e.g. node tools/render.cjs carosselli/stress weself-stress
// Reads <folder>/slides.html; writes <folder>/<prefix>-01.png … and warns if text overflows a slide.
const path = require("path");
let pw;
try { pw = require("playwright"); } catch { pw = require(path.join(require("child_process").execSync("npm root -g").toString().trim(), "playwright")); }
(async () => {
  const [folder, prefix] = process.argv.slice(2);
  if (!folder || !prefix) { console.error("usage: node tools/render.cjs <folder> <prefix>"); process.exit(1); }
  const dir = path.resolve(folder);
  const browser = await pw.chromium.launch();
  const page = await browser.newPage({ viewport: { width: 2000, height: 2000 } });
  await page.goto("file://" + path.join(dir, "slides.html"));
  await page.evaluate(() => document.fonts.ready);
  const ids = await page.$$eval("section.slide, section.card", (s) => s.map((x) => x.id));
  let n = 0;
  for (const id of ids) {
    const el = await page.$("#" + id);
    const overflow = await el.evaluate((e) => {
      const R = e.getBoundingClientRect();
      return [...e.querySelectorAll("*")].filter((c) => !c.closest("svg")).some((c) => { const r = c.getBoundingClientRect(); return r.bottom > R.bottom + 1 || r.right > R.right + 1; });
    });
    n += 1;
    const out = path.join(dir, `${prefix}-${String(n).padStart(2, "0")}.png`);
    await el.screenshot({ path: out });
    console.log((overflow ? "OVERFLOW " : "ok       ") + path.basename(out));
  }
  await browser.close();
})();
