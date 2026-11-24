// Usage: node render.cjs  (from meme/agenda-voglia/3d) -> p1.png..p4.png
const {chromium}=require('playwright');const path=require('path'),fs=require('fs'),http=require('http');
(async()=>{const root=__dirname;
const srv=http.createServer((q,s)=>{const f=path.join(root,decodeURIComponent(q.url.split('?')[0]));try{const d=fs.readFileSync(f);s.writeHead(200,{'Content-Type':f.endsWith('.js')?'text/javascript':f.endsWith('.woff2')?'font/woff2':'text/html'});s.end(d);}catch(e){s.writeHead(404);s.end();}}).listen(8766);
const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader']});
for(const p of ['1','2','3','4']){const pg=await b.newPage({viewport:{width:940,height:1000}});pg.on('pageerror',e=>console.log('err',p,e.message));
await pg.goto('http://localhost:8766/scene.html?p='+p);await pg.waitForFunction(()=>window.done,{timeout:60000});await pg.screenshot({path:path.join(root,'p'+p+'.png')});await pg.close();console.log('ok p'+p);}
await b.close();srv.close();})();
