// Usage: node tools/render-video.cjs <page.html> <out.mp4> <seconds> [fps]
// The page must expose window.render(t) that draws the frame at time t (seconds).
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path'), { execFileSync } = require('child_process');
(async () => {
  const [html, out, secs, fpsArg] = process.argv.slice(2);
  const fps = Number(fpsArg || 30), N = Math.round(Number(secs) * fps);
  const frames = fs.mkdtempSync(path.join(require('os').tmpdir(), 'frames-'));
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.goto('file://' + path.resolve(html)); await p.evaluate(() => document.fonts.ready);
  for (let i = 0; i < N; i++) {
    await p.evaluate(t => window.render(t), i / fps);
    await p.screenshot({ path: path.join(frames, String(i).padStart(5, '0') + '.png') });
    if (i % 150 === 0) console.log('frame', i, '/', N);
  }
  await b.close();
  execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-framerate', String(fps), '-i', path.join(frames, '%05d.png'),
    '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-movflags', '+faststart', out]);
  fs.rmSync(frames, { recursive: true, force: true }); console.log('ok', out);
})();
