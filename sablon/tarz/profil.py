import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tarz import A
from playwright.sync_api import sync_playwright
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../2026-11/profil")
IMG = "file://" + os.path.abspath(os.path.join(os.path.dirname(__file__), "../../2026-11/tarz"))
INK="#16181D"; RED="#B5121B"; PAPER="#F4EEE3"
# simple white line icons (viewBox 0 0 100 100)
ICONS = {
 "tarzlar": "<path d='M50 18 C24 18 14 40 18 56 C22 72 38 70 42 76 C46 84 40 88 50 88 C74 88 86 68 86 50 C86 32 70 18 50 18 Z'/><circle cx='34' cy='42' r='5'/><circle cx='52' cy='32' r='5'/><circle cx='70' cy='44' r='5'/><circle cx='66' cy='64' r='5'/>",
 "nasil":   "<circle cx='22' cy='50' r='9'/><circle cx='50' cy='50' r='9'/><circle cx='78' cy='50' r='9'/><path d='M31 50H41M59 50H69'/>",
 "cocuk":   "<circle cx='50' cy='52' r='22'/><circle cx='30' cy='28' r='9'/><circle cx='70' cy='28' r='9'/><circle cx='42' cy='50' r='2.5' fill='#fff'/><circle cx='58' cy='50' r='2.5' fill='#fff'/><path d='M44 61 Q50 66 56 61' />",
 "genc":    "<path d='M50 18 L58 40 L82 40 L62 54 L70 78 L50 63 L30 78 L38 54 L18 40 L42 40 Z' fill='none'/>",
 "roman":   "<path d='M50 30 Q35 20 18 24 V76 Q35 72 50 80 Q65 72 82 76 V24 Q65 20 50 30 Z' fill='none'/><path d='M50 30V80'/>",
}
LABEL = {"tarzlar":"Tarzlar","nasil":"Nasıl?","cocuk":"Çocuk","genc":"Genç","roman":"Roman"}
def cover(k):
    return f"""<html><body style='margin:0;width:1080px;height:1920px;background:{PAPER};display:flex;align-items:center;justify-content:center'>
<div style='width:860px;height:860px;border-radius:50%;background:{RED};display:flex;align-items:center;justify-content:center;box-shadow:0 18px 0 #7d0c12 inset'>
<svg viewBox='0 0 100 100' width='440' height='440' stroke='#fff' stroke-width='5' stroke-linecap='round' stroke-linejoin='round' fill='none'>{ICONS[k]}</svg></div></body></html>"""
def story(img):
    return f"""<html><body style='margin:0;width:1080px;height:1920px;background:{PAPER};position:relative;overflow:hidden;font-family:"Liberation Serif",serif'>
<div style='position:absolute;inset:0;background:radial-gradient(ellipse at 50% 40%,rgba(255,255,255,.6),transparent 65%)'></div>
<img src='{IMG}/{img}.jpg' style='position:absolute;top:200px;left:40px;width:1000px;border-radius:18px;box-shadow:0 30px 50px rgba(40,25,10,.25)'>
<div style='position:absolute;bottom:150px;left:0;right:0;text-align:center;font-size:44px;font-weight:700;color:{INK}'>Kitabını bastırmak için <span style='color:{RED}'>DM'den yaz</span> ✍️</div>
</body></html>"""
STORIES = [("tarzlar-1","k00-giris"),("tarzlar-2","k02-suluboya-masal"),("tarzlar-3","k05-macera-cizgi-roman"),
 ("nasil-1","a01-adim"),("nasil-2","a02-adim"),("nasil-3","a03-adim"),("nasil-4","a04-adim"),("nasil-5","a05-adim"),
 ("cocuk-1","y37-00"),("cocuk-2","t-kuru-boya"),("genc-1","go-00"),("genc-2","kg-00"),("roman-1","ro-00"),("roman-2","dr-00")]
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1080,"height":1920})
    for k in ICONS:
        open("/tmp/c.html","w").write(cover(k)); pg.goto("file:///tmp/c.html"); pg.wait_for_timeout(200)
        pg.screenshot(path=f"{OUT}/kapak-{k}.jpg",type="jpeg",quality=92)
    for n,img in STORIES:
        open("/tmp/s.html","w").write(story(img)); pg.goto("file:///tmp/s.html"); pg.wait_for_timeout(300)
        pg.screenshot(path=f"{OUT}/hikaye-{n}.jpg",type="jpeg",quality=90)
    b.close()
print("ok")
