"""12-14 Kasım hikâyeleri: mevcut kartlar 9:16 hikâye çerçevesinde, dönüşümlü çağrı."""
import os
from playwright.sync_api import sync_playwright
D=os.path.dirname(os.path.abspath(__file__)); IMG="file://"+os.path.abspath(f"{D}/../../2026-11/tarz"); OUT=os.path.abspath(f"{D}/../../2026-11/hikaye"); os.makedirs(OUT,exist_ok=True)
CTA=["Kitabını bastırmak için <span style='color:#B5121B'>DM'den yaz</span> ✍️",
     "Hikâyeni yükle · Tarzını seç · <span style='color:#B5121B'>Kitabını bas</span>",
     "Her gün yeni tarz → <span style='color:#B5121B'>Takip et</span>"]
L="v-37 v-genc v-genc2 v-hayvan v-korku v-macera v-siir v-uyku k01-renkli-cizgi-film k07-minyatur s-art-deco s-ebru s-sinematik s-kece-masal t-deniz-alti t-ejderha-diyari t-uyku-vakti t-piksel-dunyasi bk-00 pl-00 rm-00 th-00 an-00 se-00 ok-00 bf-00 a2-00 d-takipte ab-genc ab-anilar".split()
def h(img,c): return f"""<html><body style='margin:0;width:1080px;height:1920px;background:#F4EEE3;position:relative;overflow:hidden;font-family:"Liberation Serif",serif'>
<div style='position:absolute;inset:0;background:radial-gradient(ellipse at 50% 40%,rgba(255,255,255,.6),transparent 65%)'></div>
<img src='{IMG}/{img}.jpg' style='position:absolute;top:200px;left:40px;width:1000px;border-radius:18px;box-shadow:0 30px 50px rgba(40,25,10,.25)'>
<div style='position:absolute;bottom:160px;left:40px;right:40px;text-align:center;font-size:44px;font-weight:700;color:#16181D'>{c}</div></body></html>"""
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1080,"height":1920})
    for i,n in enumerate(L):
        open("/tmp/h.html","w").write(h(n,CTA[i%3])); pg.goto("file:///tmp/h.html"); pg.wait_for_timeout(250)
        pg.screenshot(path=f"{OUT}/h{i+1:02d}-{n}.jpg",type="jpeg",quality=88)
    b.close()
print(len(L))
