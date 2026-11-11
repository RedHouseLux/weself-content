"""Build a self-saving Claude artifact page to edit a carousel's texts in place.

Usage: python3 tools/editor/build.py <marked.json> <carousel dir> <out.html> <deck name>
marked.json comes from tools/editor/mark.cjs. The page stores edits as JSON
({"sN-k": "<inner html>"}) inside <script id="state"> and republishes itself.
"""
import base64
import json
import re
import sys

marked, cdir, out, name = sys.argv[1:5]
d = json.load(open(marked))

css = d["css"]
css = re.sub(r"@font-face\{[^}]*\}", "", css)          # fonts come from Google Fonts
css = re.sub(r"(^|})\s*:root\s*\{", r"\1.deck{", css)
css = re.sub(r"(^|})\s*\*\s*\{", r"\1.deck *{", css)
css = re.sub(r"(^|})\s*body\s*\{", r"\1.deck{", css)

logo = "data:image/png;base64," + base64.b64encode(open(f"{cdir}/weself-mark.png", "rb").read()).decode()
slides = [x.replace('src="weself-mark.png"', f'src="{logo}"') for x in d["slides"]]
n = len(d["slides"])

page = f"""<title>{name}</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Literata:ital@0;1&family=Nunito:wght@600;800;900&display=swap">
<style>
/* Editor chrome: a quiet desk around the slides; the slides keep the WeSelf brand colours */
:root{{--bg:#F1EEF7;--panel:#FFFFFF;--fg:#1E2B5C;--muted:#5A6488;--line:#DCD8E8;--accent:#4A5BE8;--ok:#0F6F6F;--warn:#A64A30;
--ui:"Nunito",system-ui,sans-serif}}
@media (prefers-color-scheme: dark){{:root:not([data-theme="light"]){{--bg:#12162B;--panel:#1B2140;--fg:#E8EAF6;--muted:#AAB3DD;--line:#2E3660;--accent:#8B93E8;--ok:#5BC8BC;--warn:#F5B49C;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#12162B;--panel:#1B2140;--fg:#E8EAF6;--muted:#AAB3DD;--line:#2E3660;--accent:#8B93E8;--ok:#5BC8BC;--warn:#F5B49C;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font-family:var(--ui)}}
.wrap{{padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:0 48px;max-width:1240px;margin:0 auto}}
body::before{{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top,0px);z-index:10;background:var(--panel)}}
.bar{{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;background:var(--panel);border-bottom:1px solid var(--line);margin-bottom:24px}}
.bar .in{{display:flex;flex-wrap:wrap;gap:12px 20px;align-items:center;justify-content:space-between;padding-block:14px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));max-width:1240px;margin:0 auto}}
.bar h1{{font-size:20px;font-weight:900;margin:0;text-wrap:balance}}
.bar p{{margin:2px 0 0;font-size:14px;color:var(--muted)}}
.actions{{display:flex;gap:10px;align-items:center;flex-wrap:wrap}}
.status{{font-size:14px;font-weight:800;color:var(--muted)}}
.status.dirty{{color:var(--warn)}}.status.saved{{color:var(--ok)}}
button{{font:inherit;font-weight:900;font-size:15px;border-radius:999px;padding:10px 18px;border:2px solid var(--accent);cursor:pointer}}
button.primary{{background:var(--accent);color:var(--panel)}}
button.ghost{{background:transparent;color:var(--accent)}}
button:disabled{{opacity:.45;cursor:default}}
button:focus-visible{{outline:3px solid var(--fg);outline-offset:2px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,420px),1fr));gap:28px 24px}}
.cell{{display:flex;flex-direction:column;gap:8px;min-width:0}}
.cell .lab{{font-size:13px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}}
.frame{{width:100%;aspect-ratio:1080/1350;position:relative;overflow:hidden;border-radius:14px;box-shadow:0 2px 0 var(--line),0 12px 30px rgba(20,24,60,.12)}}
.frame>.deck{{position:absolute;left:0;top:0;width:1080px;height:1350px;transform-origin:0 0}}
.deck [data-e]{{cursor:text;border-radius:6px;transition:box-shadow .15s}}
.deck [data-e]:hover{{box-shadow:0 0 0 3px rgba(74,91,232,.35)}}
.deck [data-e]:focus{{outline:none;box-shadow:0 0 0 4px #4A5BE8}}
.deck [data-e].changed{{box-shadow:0 0 0 3px rgba(240,155,124,.75)}}
.note{{font-size:14px;color:var(--muted);margin:0 0 20px;max-width:70ch}}
@media (prefers-reduced-motion: reduce){{.deck [data-e]{{transition:none}}}}
/* ---- carousel CSS (scoped to .deck) ---- */
{css}
</style>
<div class="bar"><div class="in">
  <div><h1>{name}</h1><p>Clicca su un testo e riscrivilo. Poi premi «Salva modifiche».</p></div>
  <div class="actions"><span class="status" id="status">Nessuna modifica</span>
  <button class="ghost" id="undo" type="button" disabled>Annulla le modifiche non salvate</button>
  <button class="primary" id="save" type="button" disabled>Salva modifiche</button></div>
</div></div>
<div class="wrap">
<p class="note">I testi con il bordo corallo sono stati modificati. Dopo il salvataggio, Claude legge le modifiche e rigenera le immagini del carosello e il kit. Le grafiche (barre, riquadri, illustrazioni) restano quelle attuali: se una frase diventa molto più lunga, Claude adatta gli spazi.</p>
<div class="grid" id="grid">
{''.join(f'<div class="cell"><span class="lab">Slide {i+1} di {n}</span><div class="frame"><div class="deck">{x}</div></div></div>' for i, x in enumerate(slides))}
</div>
</div>
<script type="application/json" id="state">{{}}</script>
<script>
(function(){{
  var PRISTINE = document.body.innerHTML;
  var stateEl = document.getElementById('state');
  var saved = {{}};
  try {{ saved = JSON.parse(stateEl.textContent || '{{}}'); }} catch (e) {{ saved = {{}}; }}
  var els = Array.prototype.slice.call(document.querySelectorAll('.deck [data-e]'));
  var original = {{}};
  els.forEach(function(el){{
    original[el.dataset.e] = el.innerHTML;
    if (saved[el.dataset.e] != null) el.innerHTML = saved[el.dataset.e];
    el.setAttribute('contenteditable', 'true');
    el.setAttribute('spellcheck', 'true');
    el.setAttribute('lang', 'it');
  }});
  var base = {{}}; els.forEach(function(el){{ base[el.dataset.e] = el.innerHTML; }});
  var statusEl = document.getElementById('status'), saveBtn = document.getElementById('save'), undoBtn = document.getElementById('undo');
  function dirtyCount(){{ return els.filter(function(el){{ return el.innerHTML !== base[el.dataset.e]; }}).length; }}
  function refresh(msg, cls){{
    els.forEach(function(el){{ el.classList.toggle('changed', el.innerHTML !== original[el.dataset.e]); }});
    var n = dirtyCount();
    saveBtn.disabled = n === 0; undoBtn.disabled = n === 0;
    statusEl.className = 'status' + (cls ? ' ' + cls : (n ? ' dirty' : ''));
    statusEl.textContent = msg || (n ? (n === 1 ? '1 testo modificato, da salvare' : n + ' testi modificati, da salvare') : 'Nessuna modifica da salvare');
  }}
  function fit(){{
    document.querySelectorAll('.frame').forEach(function(f){{ f.firstElementChild.style.transform = 'scale(' + (f.clientWidth / 1080) + ')'; }});
  }}
  window.addEventListener('resize', fit); fit();
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(fit);
  document.addEventListener('input', function(e){{ if (e.target.closest && e.target.closest('[data-e]')) refresh(); }});
  document.addEventListener('paste', function(e){{
    var t = e.target.closest && e.target.closest('[data-e]'); if (!t) return;
    e.preventDefault();
    var text = (e.clipboardData || window.clipboardData).getData('text/plain');
    document.execCommand('insertText', false, text);
  }});
  document.addEventListener('keydown', function(e){{
    var t = e.target.closest && e.target.closest('[data-e]'); if (!t) return;
    if (e.key === 'Enter' && !e.shiftKey) {{ e.preventDefault(); t.blur(); }}
  }});
  undoBtn.addEventListener('click', function(){{ els.forEach(function(el){{ el.innerHTML = base[el.dataset.e]; }}); refresh(); }});
  var artifact = null;
  if (window.claude && window.claude.use) {{
    window.claude.use('artifact').then(function(a){{ artifact = a; if (!a) {{ saveBtn.title = 'Il salvataggio non è disponibile in questa vista'; }} }});
  }}
  saveBtn.addEventListener('click', function(){{
    if (!artifact) {{ refresh('Salvataggio non disponibile in questa vista: apri la pagina su claude.ai', 'dirty'); return; }}
    var next = {{}};
    els.forEach(function(el){{ if (el.innerHTML !== original[el.dataset.e]) next[el.dataset.e] = el.innerHTML; }});
    var json = JSON.stringify(next).replace(/</g, '\\\\u003c');
    var body = PRISTINE.replace(/(<script type="application\\/json" id="state">)[\\s\\S]*?(<\\/script>)/, function(m, a, b){{ return a + json + b; }});
    var reset = (document.head.querySelector('style') || {{}}).textContent || '';
    var html = '<!doctype html><html><head><meta charset=utf8><meta name=viewport content="width=device-width,initial-scale=1,viewport-fit=cover"><style>' + reset + '</style></head><body>' + body + '</body></html>';
    saveBtn.disabled = true; refresh('Salvataggio…');
    artifact.publish(html).then(function(){{ refresh('Salvato', 'saved'); }}).catch(function(err){{
      var code = err && err.code;
      if (code === 'conflict') refresh('Qualcun altro ha salvato nel frattempo: la pagina si ricarica con la sua versione', 'dirty');
      else if (code === 'not_granted' || code === 'not_writer') refresh('Non hai il permesso di salvare questa pagina', 'dirty');
      else refresh('Salvataggio non riuscito: riprova tra poco', 'dirty');
    }});
  }});
  refresh();
}})();
</script>
"""
open(out, "w").write(page)
print("ok", len(page))
