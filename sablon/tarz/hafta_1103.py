import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tarz import style_card, outro
from tarz2 import theme_intro, step_card, quiz_card, teaser_card
from playwright.sync_api import sync_playwright
J = {}
# 10:00 tek tarz
for s in ["kece-masal","sinematik","ebru","sevimli-hayvanlar","robot-atolyesi","art-deco","balon-dunyasi"]:
    J[f"s-{s}"] = style_card(s)
# 3 Kas 13:30 adım karuseli
st = [("Hikâyeni anlat","Kahramanını, macerasını, sevdiği şeyleri yaz. Kısa bir anlatım yeter.","kuru-boya"),
      ("Tarzını seç","80 tarz arasından hikâyene yakışanı seç: masaldan çizgi romana.","suluboya-masal"),
      ("Kahramanın çizilsin","Kahramanın seçtiğin tarzda çizilir, beğenince onaylarsın.","3d-oyuncak"),
      ("Sayfaları kontrol et","Kapağa ve her sayfaya tek tek bakar, son onayı verirsin.","klasik-masal"),
      ("Kitabın basılsın","Onayladığın kitap basılır ve eline ulaşır.","macera-cizgi-roman")]
J["a00-giris"] = theme_intro("Kitabın<br><span style='color:var(--red)'>5 adımda</span><br>hazır", "Hikâyeden basılı kitaba giden yol.", ["kuru-boya","suluboya-masal","klasik-masal"], "NASIL ÇALIŞIR?")
for i,(t,b,s) in enumerate(st,1): J[f"a0{i}-adim"] = step_card(i,5,t,b,s)
J["a06-son"] = outro()
# 4 + 7 Kas tahmin
J["q1-parmak-boya"] = quiz_card("parmak-boya", ["Suluboya Masal","Parmak Boya","Kuru Boya El Çizimi"])
J["q2-botanik-atlas"] = quiz_card("botanik-atlas", ["Empresyonist","Klasik Gravür","Botanik Atlas"])
# 5, 8, 9 Kas yaş karuselleri
G = {"y37": ("3-7 yaş için<br><span style='color:var(--red)'>5 tarz</span>", "Resimli kitaplar, ilk okuma masalları.", ["noktali-desen","iskandinav-masali","tebesir-tahtasi","geometrik-sekiller","sicak-guaj"], "3-7 YAŞ"),
     "y812": ("8-12 yaş için<br><span style='color:var(--red)'>5 tarz</span>", "Macera, keşif ve bol kahkaha.", ["doga-gozlemcisi","manga-esintisi","mizah-karikatur","tarihte-yolculuk","sokak-sanati"], "8-12 YAŞ"),
     "ygy": ("Genç ve yetişkin<br><span style='color:var(--red)'>okurlar için</span>", "Roman, öykü, şiir ve anı kitapları.", ["grafik-roman","lofi-gece","neon-bilimkurgu","edebi-minimal","seyahat-suluboya"], "ROMAN · ÖYKÜ · ŞİİR")}
for k,(t,sub,ss,kick) in G.items():
    J[f"{k}-00"] = theme_intro(t, sub, [ss[0],ss[2],ss[4]], kick)
    for i,s in enumerate(ss,1): J[f"{k}-0{i}-{s}"] = style_card(s)
    J[f"{k}-06"] = outro()
# 6 Kas duyuru
J["d-cok-yakinda"] = teaser_card(["suluboya-masal","uzay-akademisi","minyatur","pastel-boya-ruyasi"])
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../2026-11/tarz"); os.makedirs(out, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width":1080,"height":1350})
    for n,h in J.items():
        f = f"/tmp/{n}.html"; open(f,"w").write(h)
        pg.goto("file://"+f); pg.wait_for_timeout(300)
        pg.screenshot(path=os.path.join(out,n+".jpg"), type="jpeg", quality=90)
    b.close()
print(len(J))
