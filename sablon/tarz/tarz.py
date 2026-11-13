"""E-Yayınevi 'Tarzını seç, kitabını bastır' serisi: tarz kartları ve tanıtım karuseli (1080x1350)."""
import os, json
from playwright.sync_api import sync_playwright

D = os.path.dirname(os.path.abspath(__file__))
A = f"file://{D}/../assets"
C = f"file://{D}/covers"

AGE = {"3-7": "3-7 yaş", "8-12": "8-12 yaş", "genc": "Genç okur", "yetiskin": "Yetişkin"}

# slug: (ad, kısa tanım, uygun hikâyeler, palet, yaş grubu)
S = {
 "renkli-cizgi-film": ("Renkli Çizgi Film", "Canlı renkler, net çizgiler, neşeli yüzler.", "Tatil, macera ve komik hikâyeler", ["#2F80ED","#F2C94C","#EB5757","#6FCF97","#FFFFFF"], "3-7"),
 "suluboya-masal": ("Suluboya Masal", "Yumuşak pastel tonlar, rüya gibi sayfalar.", "Uyku masalları ve duygusal hikâyeler", ["#A8C5DA","#F4C7C3","#F7E1A1","#B9D7B0","#FFFDF8"], "3-7"),
 "kuru-boya": ("Kuru Boya El Çizimi", "Elle çizilmiş sıcaklık, çocuk çizimi hissi.", "Aile, okul ve arkadaşlık hikâyeleri", ["#E07A5F","#3D405B","#81B29A","#F2CC8F","#F4F1DE"], "3-7"),
 "kagit-kolaj": ("Kâğıt Kolaj", "Kesilmiş renkli kâğıtlardan sahneler.", "Hayvanlar, doğa ve öğretici kitaplar", ["#264653","#2A9D8F","#E9C46A","#F4A261","#E76F51"], "3-7"),
 "3d-oyuncak": ("3D Oyuncak", "Yumuşak, animasyon filmi gibi üç boyut.", "Fantastik, uzay ve robot hikâyeleri", ["#7B61FF","#00C2A8","#FFB800","#FF6B6B","#F5F7FF"], "3-7"),
 "klasik-masal": ("Klasik Masal", "Eski masal kitapları gibi, nostaljik ve zarif.", "Masallar, efsaneler ve klasik hikâyeler", ["#7A4E2D","#C9A227","#2F4858","#8C2F39","#F3E9D2"], "3-7"),
 "modern-sade": ("Modern Sade", "Düz renkler, az detay, şık kompozisyon.", "Kavram kitapları ve modern hikâyeler", ["#14181F","#B5121B","#F7F3EA","#A8812F","#6B7A8F"], "3-7"),
 "pastel-boya-ruyasi": ("Pastel Boya Rüyası", "Yumuşak pastel lekeler, sıcacık sayfalar.", "Uyku masalları ve sevgi hikâyeleri", ["#E9A6A6","#9FC5E8","#F6D78B","#B6D7A8","#FFF8EE"], "3-7"),
 "uyku-vakti": ("Uyku Vakti", "Gece mavisi, yıldızlar ve fısıltı gibi sayfalar.", "Uyku öncesi masallar", ["#1D3557","#457B9D","#F1C453","#A8DADC","#F1FAEE"], "3-7"),
 "deniz-alti": ("Deniz Altı", "Mercanlar, balıklar, kabarcıklar.", "Deniz ve keşif hikâyeleri", ["#0077B6","#00B4D8","#FF8FAB","#FFD166","#E0FBFC"], "3-7"),
 "macera-cizgi-roman": ("Macera Çizgi Romanı", "Dinamik paneller, cesur kahramanlar.", "Macera ve aksiyon hikâyeleri", ["#E63946","#1D3557","#F1C453","#457B9D","#FFF8E7"], "8-12"),
 "kasif-defteri": ("Kâşif Defteri", "Sahada tutulmuş bir keşif günlüğü.", "Keşif, doğa ve bilim hikâyeleri", ["#6B4226","#2A9D8F","#E9C46A","#264653","#FAF3E3"], "8-12"),
 "uzay-akademisi": ("Uzay Akademisi", "Gezegenler, roketler, büyük merak.", "Bilim kurgu ve uzay hikâyeleri", ["#0B132B","#3A86FF","#FFBE0B","#FB5607","#E0E7FF"], "8-12"),
 "piksel-dunyasi": ("Piksel Dünyası", "Oyun dünyasından fırlamış gibi.", "Oyun, teknoloji ve macera hikâyeleri", ["#2B2D42","#EF233C","#8AC926","#FFCA3A","#EDF2F4"], "8-12"),
 "ejderha-diyari": ("Ejderha Diyarı", "Şatolar, ejderhalar, büyülü yollar.", "Fantastik macera hikâyeleri", ["#2D6A4F","#9D0208","#E9C46A","#3A0CA3","#F8F4E3"], "8-12"),
 "genc-dedektif": ("Genç Dedektif", "İpuçları, gölgeler ve büyüteç.", "Gizem ve dedektif hikâyeleri", ["#14181F","#E63946","#F1FAEE","#A8DADC","#F7F3EA"], "8-12"),
 "doga-gozlemcisi": ("Doğa Gözlemcisi", "Yapraklar, böcekler, kuşlar: yakından.", "Doğa ve hayvan bilgisi", ["#606C38","#283618","#DDA15E","#BC6C25","#FEFAE0"], "8-12"),
 "sinematik": ("Sinematik", "Film karesi gibi ışık ve atmosfer.", "Macera, bilim kurgu, gerilim", ["#1D3557","#E63946","#F1FAEE","#A8DADC","#0B132B"], "genc"),
 "minyatur": ("Minyatür", "Osmanlı nakış sanatından ilhamla.", "Tarih, İstanbul ve dönem hikâyeleri", ["#9B2226","#005F73","#C9A227","#0A9396","#F6EEDF"], "yetiskin"),
 "noir-roman": ("Noir Roman", "Yağmur, sis ve tek bir kırmızı.", "Polisiye ve gerilim", ["#000000","#B5121B","#D9D9D9","#595959","#F2F2F2"], "yetiskin"),
}

_J = os.path.join(D, "tarzlar.json")
if os.path.exists(_J):  # 80 tarzın tamamı (proje veritabanından)
    for _r in json.load(open(_J)):
        S[_r["slug"]] = (_r["name"], _r["tagline"], _r["ideal_for"], _r["palette"], _r["age"][0])

CSS = f"""
@font-face{{font-family:Frak;src:url({A}/frak.woff2)}}
*{{margin:0;padding:0;box-sizing:border-box}}
:root{{--paper:#F4EEE3;--ink:#16181D;--red:#B5121B;--gold:#B08A4A;--mute:#6a5f53;--shelf:#4a3426}}
body{{width:1080px;height:1350px;position:relative;overflow:hidden;background:var(--paper);
 font-family:'Liberation Serif',serif;color:var(--ink)}}
.paper{{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 30%,rgba(255,255,255,.6),transparent 65%)}}
.wm{{position:absolute;top:56px;left:0;right:0;text-align:center}} .wm img{{height:54px}}
.chip{{display:inline-block;background:var(--ink);color:#fff;font-weight:700;font-size:26px;letter-spacing:3px;padding:8px 18px;border-radius:5px}}
.chip.r{{background:var(--red)}}
.book{{position:relative;display:inline-block;filter:drop-shadow(0 28px 26px rgba(40,25,10,.35))}}
.book img{{display:block;border-radius:3px 6px 6px 3px}}
.book:before{{content:"";position:absolute;left:0;top:0;bottom:0;width:22px;z-index:2;border-radius:3px 0 0 3px;
 background:linear-gradient(to right,rgba(0,0,0,.28),rgba(255,255,255,.18) 45%,rgba(0,0,0,.08))}}
.book:after{{content:"";position:absolute;right:-9px;top:6px;bottom:6px;width:10px;z-index:-1;border-radius:0 4px 4px 0;
 background:repeating-linear-gradient(to bottom,#fbf8f1 0 2px,#e6dfd1 2px 3px)}}
.shelf{{position:absolute;left:70px;right:70px;height:22px;background:linear-gradient(#5b4130,#3b291d);border-radius:3px;
 box-shadow:0 10px 18px rgba(40,25,10,.25)}}
.dots{{display:flex;gap:12px;justify-content:center}}
.dots i{{width:34px;height:34px;border-radius:50%;border:2px solid rgba(0,0,0,.18);display:block}}
.cta{{position:absolute;left:80px;right:80px;bottom:110px;background:var(--red);color:#fff;text-align:center;
 font-weight:700;font-size:40px;padding:22px 0;border-radius:8px;box-shadow:0 5px 0 #7d0c12}}
.foot{{position:absolute;bottom:44px;left:80px;right:80px;display:flex;justify-content:space-between;font-size:28px;font-weight:700;color:var(--mute)}}
"""

def doc(body):
    return f"<html><head><meta charset=utf-8><style>{CSS}</style></head><body><div class=paper></div>" \
           f"<div class=wm><img src='{A}/wordmark.png'></div>{body}</body></html>"

def cover_html(slug, h):
    return f"<div class=book><img src='{C}/kapak-{slug}.jpg' style='height:{h}px'></div>"

def style_card(slug, cta="Tarzını seç, kitabını bastır", tag=None):
    name, tagline, ideal, pal, age = S[slug]
    square = slug in {k for k, v in S.items() if v[4] == "3-7"}
    h = 560 if square else 620
    top = 150
    shelf_y = top + 70 + h + 8
    return doc(f"""
<div style='position:absolute;top:{top}px;left:0;right:0;text-align:center'>
 <span class='chip r'>{tag or AGE[age].upper()}</span>
</div>
<div style='position:absolute;top:{top+70}px;left:0;right:0;text-align:center'>{cover_html(slug, h)}</div>
<div class=shelf style='top:{shelf_y}px'></div>
<div style='position:absolute;top:{shelf_y+52}px;left:70px;right:70px;text-align:center'>
 <div style='font-size:70px;font-weight:700;line-height:1.05'>{name}</div>
 <div style='font-size:34px;color:#2b2925;margin-top:12px'>{tagline}</div>
 <div class=dots style='margin-top:20px'>{''.join(f"<i style='background:{c}'></i>" for c in pal)}</div>
 <div style='font-size:28px;font-style:italic;color:var(--mute);margin-top:14px'>{ideal}</div>
</div>
<div class=cta>{cta}</div>
<div class=foot><span>@eyayinevi</span><span style='color:var(--red)'>Yayınevi 5.0</span></div>""")

def intro():
    trio = ["suluboya-masal", "macera-cizgi-roman", "klasik-masal"]
    return doc(f"""
<div style='position:absolute;top:170px;left:70px;right:70px;text-align:center'>
 <div style='font-size:96px;font-weight:700;line-height:1.02;letter-spacing:-1px'>Kitabın<br><span style='color:var(--red)'>hangi tarzda</span><br>olsun?</div>
 <div style='font-size:38px;color:#2b2925;margin-top:26px'>Masaldan çizgi romana, minyatürden noire.<br>Hikâyeni anlat, tarzını seç; kitabın o tarzda çizilsin.</div>
</div>
<div style='position:absolute;top:720px;left:0;right:0;height:420px'>
 <div style='position:absolute;left:90px;top:90px;transform:rotate(-6deg)'>{cover_html(trio[0], 300)}</div>
 <div style='position:absolute;left:50%;top:0;transform:translateX(-50%)'>{cover_html(trio[1], 400)}</div>
 <div style='position:absolute;right:90px;top:90px;transform:rotate(6deg)'>{cover_html(trio[2], 300)}</div>
</div>
<div class=shelf style='top:1128px'></div>
<div class=foot><span>@eyayinevi</span><span style='color:var(--red)'>Kaydır →</span></div>""")

def outro():
    return f"""<html><head><meta charset=utf-8><style>{CSS}
body{{background:#1b1d22;color:#fff}}</style></head><body>
<div style='position:absolute;top:250px;left:90px;right:90px;text-align:center'>
 <img src='{A}/logo_block.png' style='width:190px;filter:drop-shadow(0 20px 24px rgba(0,0,0,.5))'>
 <div style='font-size:92px;font-weight:700;margin-top:56px;line-height:1.05'>Seninki<br>hangisi?</div>
 <div style='font-size:40px;color:#d9d4cb;margin-top:34px;line-height:1.4'>Kitabını anlat, tarzını seç;<br>kahramanın bu tarzda çizilsin.</div>
</div>
<div class=cta style='bottom:200px'>Kitabımı bastır · DM'den yaz</div>
<div class=foot style='color:#9a948a'><span>@eyayinevi</span><span style='color:#e8b4b4'>Yayınevi 5.0</span></div>
</body></html>"""

CAROUSEL = ["renkli-cizgi-film", "suluboya-masal", "klasik-masal", "3d-oyuncak",
            "macera-cizgi-roman", "uzay-akademisi", "minyatur", "noir-roman"]
DAILY = ["kuru-boya", "kagit-kolaj", "kasif-defteri", "pastel-boya-ruyasi", "piksel-dunyasi",
         "uyku-vakti", "genc-dedektif", "deniz-alti", "ejderha-diyari", "modern-sade"]

if __name__ == "__main__":
    out = os.path.join(D, "out"); os.makedirs(out, exist_ok=True)
    jobs = [("k00-giris", intro())]
    jobs += [(f"k{i+1:02d}-{s}", style_card(s)) for i, s in enumerate(CAROUSEL)]
    jobs += [("k09-seninki", outro())]
    jobs += [(f"t-{s}", style_card(s)) for s in DAILY]
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1350})
        for n, h in jobs:
            f = os.path.join(out, n + ".html"); open(f, "w").write(h)
            pg.goto("file://" + f); pg.wait_for_timeout(350)
            pg.screenshot(path=os.path.join(out, n + ".jpg"), type="jpeg", quality=90)
        b.close()
    print(len(jobs))
