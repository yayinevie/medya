import os
from playwright.sync_api import sync_playwright

D = os.path.dirname(os.path.abspath(__file__))
A = f"file://{D}/assets"

CSS = f"""
@font-face{{font-family:Frak;src:url({A}/frak.woff2)}}
*{{margin:0;padding:0;box-sizing:border-box}}
:root{{--paper:#F4EEE3;--ink:#16181D;--red:#B5121B;--gold:#B08A4A;--mute:#5a5148}}
body{{width:1080px;height:1350px;position:relative;overflow:hidden;background:var(--paper);
 font-family:'Liberation Serif',serif;color:var(--ink)}}
.paper{{position:absolute;inset:0;
 background:repeating-linear-gradient(to bottom,transparent 0 47px,rgba(80,60,30,.07) 47px 48px),
 radial-gradient(ellipse at 50% 35%,rgba(255,255,255,.55),transparent 70%);}}
.wm{{position:absolute;top:70px;left:0;right:0;text-align:center}}
.wm img{{height:62px}}
.foot{{position:absolute;bottom:58px;left:80px;right:80px;display:flex;justify-content:space-between;
 align-items:center;font-size:30px;font-weight:700;color:var(--mute)}}
.pill{{display:inline-block;background:var(--red);color:#fff;font-weight:700;font-size:34px;
 padding:10px 26px;border-radius:6px;box-shadow:0 3px 0 #7d0c12}}
.foot .pill{{font-size:26px;padding:8px 18px}}
.c{{position:absolute;left:80px;right:80px;text-align:center}}
.h{{font-weight:700;font-size:86px;line-height:1.06;letter-spacing:-1px}}
.h .r{{color:var(--red)}}
.f{{font-family:Frak;color:var(--red);font-weight:400}}
.b{{font-size:38px;line-height:1.45;color:#2b2925}}
.rule{{display:flex;align-items:center;justify-content:center;gap:18px;color:var(--gold);font-size:26px;margin:34px 0}}
.rule span{{width:130px;height:2px;background:var(--gold)}}
.eng{{position:absolute;bottom:0;height:640px;object-fit:cover;
 -webkit-mask-image:linear-gradient(to bottom,transparent 0,#000 38%);opacity:.95}}
.fade{{position:absolute;left:0;right:0;bottom:0;height:190px;background:linear-gradient(to bottom,transparent,var(--paper) 70%)}}
.dots{{font-size:30px;font-weight:700;color:var(--mute);margin-top:26px}}
.dots b{{color:var(--gold);margin:0 16px}}
"""

def page(body):
    return f"<html><head><meta charset=utf-8><style>{CSS}</style></head><body><div class=paper></div>" \
           f"<div class=wm><img src='{A}/wordmark.png'></div>{body}" \
           f"<div class=fade></div><div class=foot><span>@eyayinevi</span><span class=pill>Yayınevi 5.0</span></div></body></html>"

def era(city_year, num, title_html, body, img_side):
    eng = {
        "left": f"<img class=eng src='{A}/eng_left.png' style='left:50%;transform:translateX(-50%);width:1080px;object-position:50% 4%'>",
        "right": f"<img class=eng src='{A}/eng_right.png' style='left:50%;transform:translateX(-50%);width:1080px;object-position:60% 20%'>",
        "logo": f"<img src='{A}/logo_block.png' style='position:absolute;bottom:250px;left:50%;transform:translateX(-50%);width:300px;filter:drop-shadow(0 30px 30px rgba(0,0,0,.25))'>",
    }[img_side]
    return page(f"""{eng}
<div class=c style='top:190px'>
 <span class=pill>{city_year}</span>
 <div style='font-size:46px;font-weight:700;color:var(--mute);margin-top:34px;letter-spacing:6px'>{num}</div>
 <div class=h style='margin-top:10px'>{title_html}</div>
 <div class=rule><span></span>✦<span></span></div>
 <div class=b>{body}</div>
</div>""")

POSTS = {
 "08-cihannuma": era("İstanbul · 1732", "İLK KİTAPLARDAN",
    "Dünya<br><span class=r>sayfaya sığdı.</span>",
    "Kâtip Çelebi'nin Cihannüma'sı,<br>Müteferrika matbaasında<br>haritalarıyla birlikte basıldı.", "left"),
 "09-isbn": page(f"""
<img class=eng src='{A}/eng_right.png' style='left:50%;transform:translateX(-50%);width:1080px;height:480px;object-position:60% 20%;opacity:.45'>
<div class=c style='top:200px'>
 <span class=pill>Biliyor muydunuz?</span>
 <div style='font-size:330px;font-weight:700;color:var(--red);line-height:1;margin-top:30px'>13</div>
 <div class=h style='font-size:60px;margin-top:0'>Bugünkü ISBN numarası<br>13 haneden oluşur.</div>
 <div class=b style='margin-top:30px'>2007'ye kadar 10 haneliydi.<br>Her baskının kendi kimliği vardır.</div>
</div>"""),
 "10-yazar": page(f"""
<div class=c style='top:250px'>
 <div class=h style='font-size:100px'><span class=f style='font-size:146px'>İ</span>lk cümleni<br>yazdın.<br><span class=r>Gerisini konuşalım.</span></div>
 <div class=rule><span></span>✦<span></span></div>
 <div class=b>Taslak hâlindeki dosyan da,<br>yıllardır biriktirdiğin metinler de<br>bir yayın yolculuğunun başlangıcı olabilir.</div>
 <div style='margin-top:60px'><span class=pill style='font-size:38px'>Kitabını bizimle yayımla · DM</span></div>
</div>"""),
 "01-harf-devrimi": era("Ankara · 1 Kasım 1928", "BİR DÖNÜM NOKTASI",
    "Yeni harfler,<br><span class=r>yeni okurlar.</span>",
    "Türk harflerinin kabulüne dair kanun<br>1 Kasım 1928'de TBMM'de kabul edildi.<br>Kitap, yeni bir alfabeyle buluştu.", "right"),
 "02-editorluk": page(f"""
<div class=c style='top:200px'>
 <div style='font-size:40px;font-weight:700;color:var(--mute);letter-spacing:6px'>BİR KİTABIN YOLCULUĞU</div>
 <div class=h style='font-size:84px;margin-top:24px'>Adım 2:<br><span class=r>Editörlük</span></div>
 <div class=rule><span></span>✦<span></span></div>
 <div style='text-align:left;margin:10px auto 0;width:720px'>
 {''.join(f"<div style='display:flex;align-items:center;gap:30px;margin:0 0 26px'><span style='width:74px;height:74px;flex:none;border-radius:8px;background:{'var(--red)' if i==0 else 'var(--ink)'};color:#fff;font-size:40px;font-weight:700;display:flex;align-items:center;justify-content:center;box-shadow:0 4px 0 {'#7d0c12' if i==0 else '#000'}'>{i+1}</span><span style='font-size:44px;font-weight:700'>{t}</span></div>" for i,t in enumerate(['Kurgu ve bütünlük','Anlatım ve dil','Tutarlılık kontrolü','Yazım ve noktalama']))}
 </div>
 <div class=b style='margin-top:20px'>Editör metni değiştirmez, güçlendirir.</div>
</div>"""),
 "03-yirmi-sayfa": page(f"""
<img class=eng src='{A}/eng_left.png' style='left:-40px;width:600px;height:520px;object-position:40% 6%;opacity:.8'>
<img class=eng src='{A}/eng_right.png' style='right:-40px;width:600px;height:520px;object-position:70% 6%;opacity:.8'>
<div class=c style='top:190px'>
 <div style='font-size:40px;font-weight:700;color:var(--red);letter-spacing:4px'>OKUMA ALIŞKANLIĞI</div>
 <div class=h style='margin-top:26px;font-size:80px'>Günde<br><span class=r>20 sayfa</span></div>
 <div class=rule><span></span>✦<span></span></div>
 <div class=b>Bir yılda 7.300 sayfa eder.<br>300 sayfalık kitaplarla<br>yaklaşık <b style='color:var(--red)'>24 kitap</b>.</div>
</div>"""),
 "04-okur-sorusu": page(f"""
<div class=c style='top:270px'>
 <span class=pill>Sizce?</span>
 <div class=h style='font-size:96px;margin-top:50px'><span class=f style='font-size:140px'>H</span>ayatınızda<br>iz bırakan<br><span class=r>kitap hangisi?</span></div>
 <div class=rule><span></span>✦<span></span></div>
 <div class=b>Yorumlara yazın,<br>okur listemizi birlikte oluşturalım.</div>
</div>"""),
}

if __name__ == "__main__":
    out = os.path.join(D, "out"); os.makedirs(out, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1350})
        for name, html in POSTS.items():
            f = os.path.join(out, name + ".html"); open(f, "w").write(html)
            pg.goto("file://" + f); pg.wait_for_timeout(500)
            pg.screenshot(path=os.path.join(out, name + ".jpg"), type="jpeg", quality=92)
        b.close()
    print("ok")
