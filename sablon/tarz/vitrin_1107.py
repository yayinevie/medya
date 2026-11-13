import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vitrin import vitrin
from playwright.sync_api import sync_playwright
OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../2026-11/tarz"))
J = {
 "v-37": vitrin("3-7 YAŞ · RESİMLİ KİTAP", "Kahraman o olsun!", "Çocuğunun hikâyesi, senin seçtiğin tarzda", ["renkli-cizgi-film","suluboya-masal","kuru-boya","kagit-kolaj","3d-oyuncak","klasik-masal","modern-sade","pastel-boya-ruyasi","uyku-vakti"]),
 "v-genc": vitrin("GENÇ · YETİŞKİN · ROMAN", "Romanın hazır mı?", "Kapağını ve tarzını sen seç", ["macera-cizgi-roman","sinematik","grafik-roman","gerilim","edebi-minimal","minyatur"]),
}
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width":1080,"height":1350})
    for n,h in J.items():
        open(f"/tmp/{n}.html","w").write(h); pg.goto(f"file:///tmp/{n}.html"); pg.wait_for_timeout(500)
        pg.screenshot(path=f"{OUT}/{n}.jpg", type="jpeg", quality=92)
    b.close()
print("ok")
