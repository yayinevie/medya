"""Satış karuseli (5 kart, 1080x1350): Kitabın seni bekliyor → Hikâyeni yükle → Müteferrika AI → Tarzını seç → Kitabını bas.
Kullanım: python3 satis.py   (çıktı: 2026-11/tarz/satis-0N.jpg)"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tarz import doc, cover_html, C
from playwright.sync_api import sync_playwright

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
OUT = os.path.join(ROOT, "2026-11/tarz")
R = "<span style='color:var(--red)'>"


def head(n, title, body):
    dots = "".join(f"<i style='width:{46 if i == n else 14}px;height:14px;border-radius:7px;display:block;"
                   f"background:{'var(--red)' if i == n else '#d8cdbb'}'></i>" for i in range(1, 5))
    return f"""
<div style='position:absolute;top:160px;left:90px;right:90px'>
 <div style='display:flex;align-items:center;gap:22px'>
  <span class='chip r'>ADIM {n}</span><div style='display:flex;gap:10px'>{dots}</div>
 </div>
 <div style='font-size:92px;font-weight:700;line-height:1.02;letter-spacing:-1px;margin-top:34px'>{title}</div>
 <div style='font-size:42px;line-height:1.38;color:#2b2925;margin-top:26px'>{body}</div>
</div>"""


def foot(right="Kaydır →"):
    return f"<div class=foot><span>@eyayinevi</span><span style='color:var(--red)'>{right}</span></div>"


def manuscript(w=330, rot=-5, title="Hikâyem"):
    lines = "".join(f"<div style='height:9px;background:#d9d0c1;border-radius:5px;margin-top:17px;width:{x}%'></div>"
                    for x in (100, 92, 97, 80, 95, 88, 99, 70, 93, 85, 60))
    return f"""<div style='width:{w}px;height:{int(w*1.33)}px;background:#fffdf8;transform:rotate({rot}deg);
 box-shadow:0 26px 30px rgba(40,25,10,.25);border-radius:4px;padding:38px 34px;overflow:hidden'>
 <div style='font-size:34px;font-weight:700;font-style:italic'>{title}</div>{lines}</div>"""


def k1():
    books = ["suluboya-masal", "noir-roman", "macera-cizgi-roman", "minyatur", "3d-oyuncak"]
    hs = [210, 280, 340, 280, 210]
    row = "".join(f"<div style='margin:0 -4px;transform:rotate({r}deg)'>{cover_html(s, h)}</div>"
                  for s, h, r in zip(books, hs, (-6, -3, 0, 3, 6)))
    return doc(f"""
<div style='position:absolute;top:170px;left:70px;right:70px;text-align:center'>
 <div style='font-size:124px;font-weight:700;line-height:.98;letter-spacing:-2px'>Kitabın<br>{R}seni bekliyor.</span></div>
 <div style='font-size:38px;color:#2b2925;margin-top:34px;line-height:1.45'>Hikâyeni yükle · Müteferrika AI çalışsın<br>Tarzını seç · Kitabını bas</div>
</div>
<div style='position:absolute;top:760px;left:0;right:0;display:flex;justify-content:center;align-items:flex-end;height:400px'>{row}</div>
<div class=shelf style='top:1158px'></div>
{foot()}""")


def k2():
    arrow = ("<div style='width:120px;height:120px;border-radius:50%;background:var(--red);color:#fff;font-size:76px;"
             "font-weight:700;display:flex;align-items:center;justify-content:center;box-shadow:0 6px 0 #7d0c12'>↑</div>")
    return doc(f"""{head(1, f"Hikâyeni<br>{R}yükle.</span>", "Dosyan, defterin,<br>aklındaki masal.")}
<div style='position:absolute;top:730px;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:70px'>
 {manuscript(320, -6, "Romanım")}{arrow}{manuscript(320, 5, "Masalım")}
</div>
{foot()}""")


def k3():
    fan = "".join(f"<div style='margin:0 -22px;transform:rotate({r}deg) translateY({y}px)'>{cover_html(s, 260)}</div>"
                  for s, r, y in (("kece-masal", -10, 30), ("sinematik", 0, 0), ("dunya-masallari", 10, 30)))
    spark = "<div style='font-size:90px;color:var(--red);font-weight:700;line-height:1'>→</div>"
    return doc(f"""{head(2, f"{R}Müteferrika AI</span><br>senin için<br>çalışsın.", "Kapak, karakter ve sayfalar<br>senin için çizilsin.")}
<div style='position:absolute;top:840px;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:40px'>
 {manuscript(220, -4, "Hikâyem")}{spark}<div style='display:flex;align-items:flex-end'>{fan}</div>
</div>
{foot()}""")


def k4():
    grid = ["suluboya-masal", "noir-roman", "kuru-boya", "uzay-akademisi", "romantik-suluboya", "minyatur"]
    pick = "romantik-suluboya"
    cells = ""
    for s in grid:
        on = s == pick
        ring = ("outline:8px solid var(--red);outline-offset:8px;border-radius:6px;" if on else "opacity:.55;")
        badge = ("<div style='position:absolute;top:-26px;right:-26px;width:64px;height:64px;border-radius:50%;background:var(--red);"
                 "color:#fff;font-size:40px;font-weight:700;display:flex;align-items:center;justify-content:center;z-index:5'>✓</div>" if on else "")
        cells += f"<div style='position:relative;{ring}'>{badge}<img src='{C}/kapak-{s}.jpg' style='height:235px;display:block;border-radius:3px 6px 6px 3px;box-shadow:0 14px 18px rgba(40,25,10,.25)'></div>"
    return doc(f"""{head(3, f"Kendi<br>{R}tarzını</span> seç.", "80 tarzdan ruhuna uyanı seç,<br>kitabını kendi zevkine göre tasarla.")}
<div style='position:absolute;top:690px;left:90px;right:90px;display:flex;flex-wrap:wrap;justify-content:center;align-items:flex-end;gap:44px 46px'>{cells}</div>
{foot()}""")


def k5():
    stack = "".join(f"<div style='margin:0 -6px'>{cover_html('romantik-suluboya', h)}</div>" for h in (300, 340, 300))
    return doc(f"""{head(4, f"Kitabını<br>{R}bas.</span>", "Her sayfayı onayla,<br>kitabın elinde olsun.")}
<div style='position:absolute;top:740px;left:0;right:0;display:flex;justify-content:center;align-items:flex-end;height:345px'>{stack}</div>
<div class=shelf style='top:1082px'></div>
<div class=cta style='bottom:120px'>DM at · Kitabını birlikte başlatalım</div>
{foot("Hikâyen senin, kitabın senin")}""")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    jobs = {"satis-01": k1(), "satis-02": k2(), "satis-03": k3(), "satis-04": k4(), "satis-05": k5()}
    tmp = os.path.join(os.path.dirname(__file__), "out"); os.makedirs(tmp, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1350})
        for n, h in jobs.items():
            f = os.path.join(tmp, n + ".html"); open(f, "w").write(h)
            pg.goto("file://" + f); pg.wait_for_timeout(400)
            pg.screenshot(path=os.path.join(OUT, n + ".jpg"), type="jpeg", quality=90)
        b.close()
    print("ok", len(jobs))
