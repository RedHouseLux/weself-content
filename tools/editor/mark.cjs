// Mark the editable text blocks of a rendered carousel with data-e="sN-k" ids.
// Usage: node tools/editor/mark.cjs <carousel dir> <out.json>
// Writes {css: "...", slides: ["<section ...>", ...]} with ids added.
// The same rule is used to apply edits back, so ids stay stable.
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

(async () => {
  const dir = process.argv[2];
  const out = process.argv[3];
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
  await page.goto('file://' + path.resolve(dir, 'slides.html'));
  const data = await page.evaluate(() => {
    const slides = [];
    document.querySelectorAll('section.slide').forEach((sec, si) => {
      const chosen = [];
      for (const el of sec.querySelectorAll('*')) {
        if (el.closest('svg') || el.closest('.brand')) continue;
        if (chosen.some((c) => c.contains(el))) continue;
        const direct = [...el.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim());
        if (!direct) continue;
        chosen.push(el);
      }
      chosen.forEach((el, k) => el.setAttribute('data-e', 's' + (si + 1) + '-' + (k + 1)));
      slides.push(sec.outerHTML);
    });
    const css = [...document.querySelectorAll('style')].map((s) => s.textContent).join('\n');
    return { css, slides };
  });
  fs.writeFileSync(out, JSON.stringify(data));
  await browser.close();
})();
