"""Tarz serisinin ek kartları: tema karuseli girişi, adım kartları, tahmin oyunu, açılış duyurusu."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tarz import doc, cover_html, style_card, outro, S, A, CSS  # noqa: F401


def theme_intro(title_html, sub, trio, kicker=""):
    """Tema karuselinin ilk kartı. trio: 3 tarz slug'ı (ortadaki büyük)."""
    return doc(f"""
<div style='position:absolute;top:165px;left:70px;right:70px;text-align:center'>
 {f"<span class='chip r'>{kicker}</span>" if kicker else ""}
 <div style='font-size:88px;font-weight:700;line-height:1.04;letter-spacing:-1px;margin-top:26px'>{title_html}</div>
 <div style='font-size:36px;color:#2b2925;margin-top:24px;line-height:1.35'>{sub}</div>
</div>
<div style='position:absolute;top:735px;left:0;right:0;height:420px'>
 <div style='position:absolute;left:90px;top:90px;transform:rotate(-6deg)'>{cover_html(trio[0], 290)}</div>
 <div style='position:absolute;left:50%;top:0;transform:translateX(-50%)'>{cover_html(trio[1], 390)}</div>
 <div style='position:absolute;right:90px;top:90px;transform:rotate(6deg)'>{cover_html(trio[2], 290)}</div>
</div>
<div class=shelf style='top:1133px'></div>
<div class=foot><span>@eyayinevi</span><span style='color:var(--red)'>Kaydır →</span></div>""")


def step_card(n, total, title, body, slug):
    """Kitabın yapım adımı: büyük numara, başlık, açıklama, altta küçük örnek kapak."""
    dots = "".join(f"<i style='width:{46 if i == n else 14}px;height:14px;border-radius:7px;display:block;background:{'var(--red)' if i == n else '#d8cdbb'}'></i>" for i in range(1, total + 1))
    return doc(f"""
<div style='position:absolute;top:175px;left:90px;right:90px'>
 <div style='display:flex;gap:10px'>{dots}</div>
 <div style='font-size:250px;font-weight:700;color:var(--red);line-height:1;margin-top:30px'>{n}</div>
 <div style='font-size:84px;font-weight:700;line-height:1.05;margin-top:10px'>{title}</div>
 <div style='font-size:40px;line-height:1.45;color:#2b2925;margin-top:28px;max-width:560px'>{body}</div>
</div>
<div style='position:absolute;right:80px;bottom:130px;transform:rotate(4deg)'>{cover_html(slug, 400 if S[slug][4] == '3-7' else 470)}</div>
<div class=foot><span>@eyayinevi</span><span style='color:var(--red)'>Yayınevi 5.0</span></div>""")


def quiz_card(slug, options):
    """'Bu kapak hangi tarz?' tahmin oyunu. options: 3 tarz adı (biri doğru)."""
    letters = "ABC"
    opts = "".join(f"<div style='display:flex;align-items:center;gap:22px;background:#fff;border:2px solid #e2d7c4;border-radius:10px;padding:16px 22px'>"
                   f"<span style='width:54px;height:54px;flex:none;border-radius:8px;background:var(--ink);color:#fff;font-size:32px;font-weight:700;display:flex;align-items:center;justify-content:center'>{letters[i]}</span>"
                   f"<span style='font-size:38px;font-weight:700'>{o}</span></div>" for i, o in enumerate(options))
    square = S[slug][4] == "3-7"
    return doc(f"""
<div style='position:absolute;top:150px;left:0;right:0;text-align:center'><span class='chip r'>TAHMİN ET</span></div>
<div style='position:absolute;top:215px;left:0;right:0;text-align:center;font-size:72px;font-weight:700'>Bu kapak hangi tarz?</div>
<div style='position:absolute;top:330px;left:0;right:0;text-align:center'>{cover_html(slug, 470 if square else 500)}</div>
<div style='position:absolute;top:{830 if square else 860}px;left:110px;right:110px;display:flex;flex-direction:column;gap:16px'>{opts}</div>
<div class=foot><span>@eyayinevi</span><span style='color:var(--red)'>Cevabını yorumlara yaz</span></div>""")


def teaser_card(covers):
    """Açılış duyurusu: koyu zemin, kapak yığını, 'Çok yakında'."""
    row = "".join(f"<div style='transform:rotate({r}deg);margin:0 -6px'>{cover_html(s, 250)}</div>" for s, r in zip(covers, (-8, -3, 3, 8)))
    return f"""<html><head><meta charset=utf-8><style>{CSS}
body{{background:#1b1d22;color:#fff}}</style></head><body>
<div class=wm><img src='{A}/wordmark.png'></div>
<div style='position:absolute;top:200px;left:70px;right:70px;text-align:center'>
 <span class='chip r'>ÇOK YAKINDA</span>
 <div style='font-size:96px;font-weight:700;line-height:1.04;margin-top:30px'>Kendi kitabını<br><span style='color:#ff8a8a'>bastırmanın</span><br>yeni yolu</div>
 <div style='font-size:38px;color:#d9d4cb;margin-top:28px'>Hikâyeni anlat · Tarzını seç · Kitabını bastır</div>
</div>
<div style='position:absolute;top:900px;left:0;right:0;display:flex;justify-content:center'>{row}</div>
<div class=foot style='color:#9a948a'><span>@eyayinevi</span><span style='color:#e8b4b4'>Takipte kal</span></div>
</body></html>"""


def compare_card(title_html, sub, a, b, kicker="SEN SEÇ", cta="Yorumlara A ya da B yaz"):
    """İki kapağı yan yana gösteren 'A mı, B mi?' kartı. a, b: tarz slug'ı."""
    def col(slug, letter):
        return (f"<div style='width:440px;text-align:center'>"
                f"<div style='height:520px;display:flex;align-items:flex-end;justify-content:center'>{cover_html(slug, 500)}</div>"
                f"<div style='margin:44px auto 0;width:66px;height:66px;border-radius:8px;background:var(--ink);color:#fff;font-size:40px;font-weight:700;display:flex;align-items:center;justify-content:center'>{letter}</div>"
                f"<div style='font-size:40px;font-weight:700;margin-top:14px;line-height:1.1'>{S[slug][0]}</div>"
                f"<div style='font-size:27px;font-style:italic;color:var(--mute);margin-top:8px;line-height:1.2'>{S[slug][1]}</div></div>")
    return doc(f"""
<div style='position:absolute;top:140px;left:60px;right:60px;text-align:center'>
 <span class='chip r'>{kicker}</span>
 <div style='font-size:70px;font-weight:700;line-height:1.05;margin-top:18px'>{title_html}</div>
 <div style='font-size:32px;color:#2b2925;margin-top:10px'>{sub}</div>
</div>
<div style='position:absolute;top:400px;left:0;right:0;display:flex;justify-content:center;gap:60px'>{col(a,"A")}{col(b,"B")}</div>
<div class=shelf style='top:928px'></div>
<div class=cta style='bottom:100px'>{cta}</div>
<div class=foot><span>@eyayinevi</span><span style='color:var(--red)'>Yayınevi 5.0</span></div>""")
