"""12-18 Kasım 2026 haftası: tek tarz kartları, tahmin, A/B, tema karuselleri, 5 adım, duyuru ve renkli vitrinler."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tarz import style_card, outro
from tarz2 import theme_intro, step_card, quiz_card, teaser_card, compare_card
from vitrin import vitrin
from playwright.sync_api import sync_playwright
R = "<span style='color:var(--red)'>"
J = {}
# 10:00 tek tarz (kalan son 4 tarz)
for s in ["kagit-oyma", "dergi-illustrasyonu", "dunya-masallari", "eskiz-defteri"]:
    J[f"s-{s}"] = style_card(s)
# tahmin oyunları
J["q3-risograf"] = quiz_card("risograf", ["Fanzin", "Dijital Boya", "Risograf"])
J["q4-murekkep-firca"] = quiz_card("murekkep-firca", ["Mürekkep Fırça", "Ebru", "Karakalem"])
J["q5-retro-cizgi-roman"] = quiz_card("retro-cizgi-roman", ["Macera Çizgi Romanı", "Retro Çizgi Roman", "Animasyon Filmi"])
# A mı B mi
J["ab-genc"] = compare_card(f"Seninki {R}hangisi?</span>", "İlk romanın için iki tarz.", "kara-mizah", "sinematik", kicker="SENİNKİ HANGİSİ?")
J["ab-masal"] = compare_card(f"Masal kitabı {R}hangisi?</span>", "Çocuğunun masalı, senin seçtiğin tarzda.", "kagit-oyma", "dunya-masallari", kicker="8-12 YAŞ")
J["ab-gezi"] = compare_card(f"Gezi kitabın {R}hangisi?</span>", "Yolda biriktirdiklerin bir kitap olsun.", "seyahat-suluboya", "yol-hikayesi", kicker="ANI · GEZİ")
# duyuru
J["d-takipte"] = teaser_card(["deniz-alti", "grafik-roman", "sevimli-hayvanlar", "art-deco"])
# tema karuselleri: (önek, başlık, alt yazı, 5 tarz, kicker, kart etiketi)
T = [
 ("bk", f"Bilim ve<br>{R}keşif</span><br>için 5 tarz", "Meraklı çocuklara kendi keşif kitabı.", ["kasif-defteri", "uzay-akademisi", "robot-atolyesi", "doga-gozlemcisi", "piksel-dunyasi"], "8-12 YAŞ", "BİLİM · KEŞİF"),
 ("pl", f"Polisiye<br>{R}romanın</span><br>için 5 tarz", "Sis, ipucu ve son sayfada gelen o an.", ["noir-roman", "art-deco", "genc-dedektif", "grafik-roman", "gerilim"], "POLİSİYE · GİZEM", "POLİSİYE"),
 ("rm", f"Aşk<br>{R}hikâyen</span><br>için 5 tarz", "Kalbinden geçenler bir kitap olsun.", ["romantik-suluboya", "manga-dram", "empresyonist", "lofi-gece", "edebi-minimal"], "ROMANTİK", "AŞK HİKÂYESİ"),
 ("bf", f"Bilimkurgu ve<br>{R}fantastik</span>", "Başka dünyalar, senin kalemin.", ["neon-bilimkurgu", "mitoloji", "gercekustu-genc", "karanlik-fantastik", "distopya"], "GENÇ · YETİŞKİN", "BAŞKA DÜNYALAR"),
 ("se", f"Şehir<br>{R}hikâyeleri</span><br>için 5 tarz", "Sokaklar, kafeler, gece otobüsleri.", ["kentsel-eskiz", "sokak-sanati", "bauhaus", "minimal-poster", "dergi-illustrasyonu"], "ŞEHİR", "ŞEHİR HİKÂYESİ"),
 ("th", f"Tarihî<br>{R}romanın</span><br>için 5 tarz", "Geçmişte geçen hikâyen, döneminin tarzında.", ["minyatur", "klasik-gravur", "yagli-boya", "linol-edebi", "tarihte-yolculuk"], "TARİH · DÖNEM", "DÖNEM ROMANI"),
 ("an", f"Anıların<br>{R}bir kitap</span><br>olsun", "Aile hikâyeleri, eski fotoğraflar, hatıralar.", ["kolaj-sanati", "karakalem", "vintage-afis", "gokyuzu-manzaralari", "botanik-atlas"], "ANI · AİLE", "ANI KİTABI"),
 ("ok", f"Okul ve<br>{R}arkadaşlık</span><br>için 5 tarz", "Sınıfın en güzel hikâyesi onunki olsun.", ["manga-esintisi", "takim-ruhu", "mizah-karikatur", "animasyon-filmi", "eskiz-defteri"], "8-12 YAŞ", "OKUL · ARKADAŞLIK"),
]
for p, t, sub, ss, kick, tag in T:
    J[f"{p}-00"] = theme_intro(t, sub, [ss[0], ss[2], ss[4]], kick)
    for i, s in enumerate(ss, 1):
        J[f"{p}-0{i}-{s}"] = style_card(s, cta="Bu tarzda bastır · DM'den yaz", tag=tag)
    J[f"{p}-06"] = outro()
# 5 adım (yeni örnek kapaklarla)
st = [("Hikâyeni anlat", "Kahramanı, yaşadıklarını, sevdiklerini anlat. Birkaç paragraf yeter.", "sicak-guaj"),
      ("Tarzını seç", "80 tarzdan hikâyene en çok yakışanı sen seç.", "iskandinav-masali"),
      ("Kahraman çizilsin", "Kahramanın seçtiğin tarzda çizilir; beğenince onaylarsın.", "renkli-cizgi-film"),
      ("Sayfalara bak", "Kapağı ve her sayfayı tek tek kontrol edip onaylarsın.", "kece-masal"),
      ("Kitabın basılsın", "Onayladığın kitap basılır, rafına yerleşir.", "uzay-akademisi")]
J["a2-00"] = theme_intro(f"Hikâyen<br>{R}5 adımda</span><br>kitap olsun", "Anlat, seç, onayla, bastır.", ["sicak-guaj", "uzay-akademisi", "kece-masal"], "NASIL ÇALIŞIR?")
for i, (t, b, s) in enumerate(st, 1):
    J[f"a2-0{i}-adim"] = step_card(i, 5, t, b, s)
J["a2-06"] = outro()
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../2026-11/tarz"); os.makedirs(out, exist_ok=True)
# renkli vitrinler
V = {
 "v-uyku": vitrin("3-7 YAŞ · UYKU MASALLARI", "İyi geceler, kahraman!", "Her gece onun masalı", ["suluboya-masal", "pastel-boya-ruyasi", "uyku-vakti", "sicak-guaj", "kece-masal", "iskandinav-masali", "klasik-masal", "linol-baski-cocuk", "modern-sade"]),
 "v-korku": vitrin("KORKU · GERİLİM", "Işıkları kapat…", "Korku romanın hazır mı?", ["gerilim", "gotik", "noir-roman", "gercekustu-ruya", "karanlik-fantastik", "distopya"]),
 "v-hayvan": vitrin("3-7 YAŞ · HAYVAN HİKÂYELERİ", "Patili kahramanlar!", "Hayvan dostları sayfada", ["sevimli-hayvanlar", "kagit-kolaj", "deniz-alti", "parmak-boya", "kuru-boya", "renkli-cizgi-film", "noktali-desen", "geometrik-sekiller", "tebesir-tahtasi"]),
 "v-macera": vitrin("8-12 YAŞ · MACERA", "Macera başlasın!", "Kahraman o olsun", ["macera-cizgi-roman", "ejderha-diyari", "uzay-akademisi", "gizemli-orman", "suluboya-macera", "piksel-dunyasi"]),
 "v-genc2": vitrin("GENÇ OKUR", "Defterindeki roman", "Artık bir kitap olsun", ["manga-dram", "lofi-gece", "dijital-boya", "fanzin", "risograf", "neon-bilimkurgu"]),
 "v-siir": vitrin("ŞİİR · DENEME · ÖYKÜ", "Şiirlerin kitap olsun", "Kapağını sen seç", ["ebru", "tipografik", "murekkep-firca", "edebi-minimal", "botanik-atlas", "modern-soyut"]),
 "v-yilbasi": vitrin("HEDİYE · YILBAŞI", "Yılbaşına kendi kitabı!", "En özel hediye", ["3d-oyuncak", "balon-dunyasi", "iskandinav-masali", "kece-masal", "renkli-cizgi-film", "klasik-masal", "pastel-boya-ruyasi", "sicak-guaj", "suluboya-masal"]),
}
J.update(V)
tmp = os.environ.get("TMPDIR", "/tmp")
only = sys.argv[1:]
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1350})
    for n, h in J.items():
        if only and n not in only: continue
        f = os.path.join(tmp, n + ".html"); open(f, "w").write(h)
        pg.goto("file://" + f); pg.wait_for_timeout(400)
        pg.screenshot(path=os.path.join(out, n + ".jpg"), type="jpeg", quality=90)
    b.close()
print(len(J))
