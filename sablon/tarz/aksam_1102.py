import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tarz import style_card, outro
from tarz2 import theme_intro
from playwright.sync_api import sync_playwright
R = "<span style='color:var(--red)'>"
T = {
 "kg": (f"Korku ve<br>{R}gerilim</span><br>hikâyeleri için", "Uzun gölgeler, sisli sokaklar, kadim sırlar.", ["gerilim","gotik","karanlik-fantastik","distopya","gercekustu-ruya"], "GENÇ · YETİŞKİN"),
 "dr": (f"Dram ve<br>{R}duygu</span><br>hikâyeleri için", "Aşk, kayıp, büyüme: kalbe dokunan sayfalar.", ["manga-dram","romantik-suluboya","karakalem","yagli-boya","gokyuzu-manzaralari"], "GENÇ · YETİŞKİN"),
 "go": (f"Genç okurlar<br>{R}için 5 tarz</span>", "Müzik, şehir, yol ve biraz da isyan.", ["dijital-boya","fanzin","risograf","kara-mizah","yol-hikayesi"], "GENÇ OKUR"),
 "ro": (f"Roman ve<br>{R}öykü</span><br>kitapları için", "Zamansız, sade, edebî kapaklar.", ["klasik-gravur","linol-edebi","murekkep-firca","tipografik","empresyonist"], "YETİŞKİN"),
 "sd": (f"Sıra dışı<br>{R}hikâyeler</span><br>için", "Mitler, rüyalar ve cesur fikirler.", ["mitoloji","gercekustu-genc","modern-soyut","bauhaus","minimal-poster"], "GENÇ · YETİŞKİN"),
}
J = {}
for k,(t,sub,ss,kick) in T.items():
    J[f"{k}-00"] = theme_intro(t, sub, [ss[0],ss[1],ss[2]], kick)
    for i,s in enumerate(ss,1): J[f"{k}-0{i}-{s}"] = style_card(s)
    J[f"{k}-06"] = outro()
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../2026-11/tarz"); os.makedirs(out, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width":1080,"height":1350})
    for n,h in J.items():
        f = f"/tmp/{n}.html"; open(f,"w").write(h)
        pg.goto("file://"+f); pg.wait_for_timeout(300)
        pg.screenshot(path=os.path.join(out,n+".jpg"), type="jpeg", quality=90)
    b.close()
print(len(J))
