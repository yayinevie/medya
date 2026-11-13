import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tarz import style_card, outro
from tarz2 import theme_intro, compare_card
from playwright.sync_api import sync_playwright
R = "<span style='color:var(--red)'>"
J = {}
# 10 ve 11 Kas 10:00 tek tarz
for s in ["kolaj-sanati", "linol-baski-cocuk"]:
    J[f"s-{s}"] = style_card(s)
# 10 Kas 13:30 macera tema karuseli
M = ["animasyon-filmi", "retro-cizgi-roman", "suluboya-macera", "gizemli-orman", "takim-ruhu"]
J["mc-00"] = theme_intro(f"Macera<br>{R}hikâyeleri</span><br>için 5 tarz", "Yollar, sırlar ve zafer anları.", [M[1], M[3], M[2]], "8-12 YAŞ")
for i, s in enumerate(M, 1):
    J[f"mc-0{i}-{s}"] = style_card(s)
J["mc-06"] = outro()
# 11 Kas 13:30 A mı B mi
J["ab-anilar"] = compare_card(f"Anılarının kitabı {R}hangisi?</span>", "Hikâyen seninle, tarzı sen seç.", "vintage-afis", "kentsel-eskiz")
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../2026-11/tarz"); os.makedirs(out, exist_ok=True)
tmp = os.environ.get("TMPDIR", "/tmp")
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1350})
    for n, h in J.items():
        f = os.path.join(tmp, n + ".html"); open(f, "w").write(h)
        pg.goto("file://" + f); pg.wait_for_timeout(300)
        pg.screenshot(path=os.path.join(out, n + ".jpg"), type="jpeg", quality=90)
    b.close()
print(len(J))
