// node render.cjs  -> mp4 + png per clip (animations stepped frame by frame)
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path'), { execSync } = require('child_process');
const dir = __dirname, out = path.join(dir, 'export'), FPS = 30, DUR = 6;
(async () => {
  fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.goto('file://' + path.join(dir, 'cards.html')); await p.evaluate(() => document.fonts.ready);
  const ids = await p.$$eval('section', s => s.map(e => e.id));
  for (const id of ids) {
    const el = await p.$('#' + id);
    const ov = await el.evaluate(e => { const r = e.getBoundingClientRect(); return [...e.querySelectorAll(':scope > :not(.blob)')].some(c => { const q = c.getBoundingClientRect(); return q.bottom > r.bottom + 1 || q.right > r.right + 1; }); });
    if (ov) console.log('OVERFLOW', id);
    await p.evaluate(() => document.getAnimations().forEach(a => a.pause()));
    const set = t => p.evaluate(t => document.getAnimations().forEach(a => { a.currentTime = t; }), t);
    if (id.startsWith('b')) { await el.screenshot({ path: path.join(out, `sfondo-${id.slice(1)}.png`) }); continue; }
    const fd = path.join(out, 'f_' + id); fs.mkdirSync(fd, { recursive: true });
    for (let f = 0; f < FPS * DUR; f++) { await set(f * 1000 / FPS); await el.screenshot({ path: path.join(fd, String(f).padStart(4, '0') + '.png') }); }
    await set(DUR * 1000); await el.screenshot({ path: path.join(out, `clip-${id.slice(1)}.png`) });
    execSync(`ffmpeg -y -loglevel error -framerate ${FPS} -i ${fd}/%04d.png -c:v libx264 -pix_fmt yuv420p -crf 16 ${out}/clip-${id.slice(1)}.mp4`);
    fs.rmSync(fd, { recursive: true });
    console.log('ok', id);
  }
  await b.close();
})();
