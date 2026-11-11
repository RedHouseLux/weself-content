// Apply text edits saved in the editor artifact back to a carousel's body.html.
// Usage: node tools/editor/apply.cjs <carousel dir> <edits.json>
// Ids are assigned with the same rule as mark.cjs. Writes body.html in place
// (slides.html must be up to date: cat head.html [extra] body.html > slides.html).
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

(async () => {
  const dir = process.argv[2];
  const edits = JSON.parse(fs.readFileSync(process.argv[3], 'utf8'));
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + path.resolve(dir, 'slides.html'));
  const sections = await page.evaluate((edits) => {
    const out = [];
    document.querySelectorAll('section.slide').forEach((sec, si) => {
      const chosen = [];
      for (const el of sec.querySelectorAll('*')) {
        if (el.closest('svg') || el.closest('.brand')) continue;
        if (chosen.some((c) => c.contains(el))) continue;
        const direct = [...el.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim());
        if (!direct) continue;
        chosen.push(el);
      }
      chosen.forEach((el, k) => {
        const id = 's' + (si + 1) + '-' + (k + 1);
        if (Object.prototype.hasOwnProperty.call(edits, id)) el.innerHTML = edits[id];
      });
      out.push(sec.outerHTML);
    });
    return out;
  }, edits);
  await browser.close();
  const body = fs.readFileSync(path.join(dir, 'body.html'), 'utf8');
  const styleEnd = body.indexOf('</style>') + '</style>'.length;
  const head = body.slice(0, styleEnd);
  fs.writeFileSync(path.join(dir, 'body.html'), head + '\n\n' + sections.join('\n\n') + '</body></html>\n');
  console.log('applied', Object.keys(edits).length, 'edits to', sections.length, 'slides');
})();
