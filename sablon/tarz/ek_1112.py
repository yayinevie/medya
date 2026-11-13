"""12-18 Kasım ek paylaşımlar (günde +3: 08:30 tahmin, 12:00 A/B, 21:30 vitrin) ve 12-14 Kasım hikâyeleri (günde 10)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tarz import S
from tarz2 import quiz_card, compare_card
from vitrin import vitrin
from playwright.sync_api import sync_playwright
D = os.path.dirname(os.path.abspath(__file__))
R = "<span style='color:var(--red)'>"
N = lambda s: S[s][0]
J = {}
Q = [("gizemli-orman","suluboya-macera","dunya-masallari"),("art-deco","vintage-afis","bauhaus"),("kece-masal","3d-oyuncak","kagit-kolaj"),
     ("lofi-gece","manga-dram","dijital-boya"),("yagli-boya","empresyonist","sicak-guaj"),("neon-bilimkurgu","piksel-dunyasi","uzay-akademisi"),
     ("ebru","modern-soyut","gercekustu-ruya")]
for i,(a,b,c) in enumerate(Q,6):
    opts=[N(b),N(a),N(c)] if i%2 else [N(a),N(c),N(b)]
    J[f"q{i}-{a}"]=quiz_card(a,opts)
AB=[("Romanının kapağı", "İlk romanın raflara hangi yüzle çıksın?", "edebi-minimal","yagli-boya","İLK ROMAN"),
    ("Çocuk kitabın", "Yazdığın masal hangi tarzda çizilsin?", "suluboya-masal","renkli-cizgi-film","ÇOCUK KİTABI"),
    ("Anı kitabın", "Ailenin hikâyesi hangi tarzda yaşasın?", "karakalem","kolaj-sanati","ANI · AİLE"),
    ("Şiir kitabın", "Dizelerine hangi kapak yakışır?", "tipografik","ebru","ŞİİR"),
    ("Polisiyen", "Gizemin kapağı hangisi olsun?", "noir-roman","gerilim","POLİSİYE"),
    ("Fantastik romanın", "Başka dünyan hangi tarzda?", "mitoloji","karanlik-fantastik","FANTASTİK"),
    ("Sınıfın kitabı", "Öğrencilerinin hikâyeleri hangi tarzda?", "tebesir-tahtasi","mizah-karikatur","ÖĞRETMENLER")]
for i,(t,sub,a,b,k) in enumerate(AB,1):
    J[f"ab2-{i}"]=compare_card(f"{t} {R}hangisi?</span>",sub,a,b,kicker=k)
V={
 "v-yazar": vitrin("YAZARLAR İÇİN","Kitabın çekmecede kalmasın","Adınla basılsın",["edebi-minimal","yagli-boya","tipografik","noir-roman","linol-edebi","murekkep-firca"]),
 "v-ilkroman": vitrin("İLK ROMAN","Yazar olma zamanı","Kapağını sen seç",["sinematik","gerilim","romantik-suluboya","grafik-roman","yol-hikayesi","art-deco"]),
 "v-cocukyaz": vitrin("ÇOCUK KİTABI YAZ","Masalını yazdın mı?","Çizimini biz yapalım",["renkli-cizgi-film","suluboya-masal","kuru-boya","kagit-kolaj","3d-oyuncak","klasik-masal","modern-sade","sevimli-hayvanlar","deniz-alti"]),
 "v-ogretmen": vitrin("ÖĞRETMENLER","Sınıfın kitabı olsun","Öğrencilerin yazsın",["tebesir-tahtasi","geometrik-sekiller","parmak-boya","noktali-desen","balon-dunyasi","linol-baski-cocuk","iskandinav-masali","kece-masal","pastel-boya-ruyasi"]),
 "v-aile": vitrin("ANI · AİLE","Ailenin hikâyesi","Kuşaktan kuşağa",["karakalem","kolaj-sanati","vintage-afis","seyahat-suluboya","botanik-atlas","gokyuzu-manzaralari"]),
 "v-fantastik": vitrin("FANTASTİK · BİLİMKURGU","Başka dünyalar","Senin kaleminden",["mitoloji","neon-bilimkurgu","karanlik-fantastik","distopya","gercekustu-genc","dijital-boya"]),
 "v-8-12": vitrin("8-12 YAŞ","Okuma kurdu kahraman","Kitabını birlikte yazın",["kasif-defteri","genc-dedektif","robot-atolyesi","animasyon-filmi","manga-esintisi","takim-ruhu"]),
}
J.update(V)
out=os.path.join(D,"../../2026-11/tarz")
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1080,"height":1350})
    for n,h in J.items():
        f=f"/tmp/{n}.html"; open(f,"w").write(h); pg.goto("file://"+f); pg.wait_for_timeout(400)
        pg.screenshot(path=os.path.join(out,n+".jpg"),type="jpeg",quality=90)
    b.close()
print(" ".join(J))
