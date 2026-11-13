import os
from playwright.sync_api import sync_playwright
D=os.path.dirname(os.path.abspath(__file__)); AS=f"file://{D}/../assets"; C=f"file://{D}/covers"
L=[("suluboya-masal",1,-3),("sinematik",0,2),("macera-cizgi-roman",0,-1.5)]
R=[("minyatur",0,1.5),("uzay-akademisi",0,-2),("renkli-cizgi-film",1,3)]
def side(items):
    out=""
    for s,sq,t in items:
        w=170 if sq else 168; h=w if sq else round(w*1.5)
        out+=(f"<div style='width:{w}px;height:{h}px;position:relative;transform:rotate({t}deg);transform-origin:50% 100%;filter:drop-shadow(0 14px 12px rgba(40,25,10,.3))'>"
              f"<img src='{C}/kapak-{s}.jpg' style='width:100%;height:100%;object-fit:cover;border-radius:3px 6px 6px 3px'>"
              f"<div style='position:absolute;left:0;top:0;bottom:0;width:10px;background:linear-gradient(to right,rgba(0,0,0,.25),rgba(255,255,255,.15))'></div></div>")
    return f"<div style='display:flex;gap:22px;align-items:flex-end'>{out}</div><div style='height:11px;margin-top:0;background:linear-gradient(#5b4130,#3b291d);border-radius:3px;box-shadow:0 8px 12px rgba(40,25,10,.22)'></div>"
html=f"""<html><head><meta charset=utf-8><style>*{{margin:0;box-sizing:border-box}}body{{width:1640px;height:624px;background:#F4EEE3;position:relative;overflow:hidden;font-family:'Liberation Serif',serif;color:#16181D}}</style></head><body>
<div style='position:absolute;inset:0;background:radial-gradient(ellipse at 50% 45%,rgba(255,255,255,.8),transparent 60%)'></div>
<div style='position:absolute;left:-40px;bottom:120px;width:610px'>{side(L)}</div>
<div style='position:absolute;right:-40px;bottom:120px;width:610px'>{side(R)}</div>
<div style='position:absolute;left:50%;top:150px;transform:translateX(-50%);width:640px;text-align:center'>
 <img src='{AS}/wordmark.png' style='height:46px'>
 <div style='font-size:21px;font-weight:700;letter-spacing:6px;color:#B5121B;margin-top:26px'>80 İLLÜSTRASYON TARZI</div>
 <div style='font-size:64px;font-weight:700;line-height:1.05;margin-top:8px'>Tarzını seç,<br><span style='color:#B5121B;font-style:italic'>kitabını bastır.</span></div>
 <div style='font-size:25px;color:#5a5148;margin-top:14px;font-style:italic'>Hikâyeni anlat · Tarzını seç · Kitabın basılsın</div>
</div></body></html>"""
open("/tmp/fbk.html","w").write(html)
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1640,"height":624},device_scale_factor=1)
    pg.goto("file:///tmp/fbk.html"); pg.wait_for_timeout(600)
    pg.screenshot(path=f"{D}/../../2026-11/profil/fb-kapak-tarz.jpg",type="jpeg",quality=94); b.close()
