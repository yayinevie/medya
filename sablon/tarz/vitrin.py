"""Rengârenk 'kitap vitrini' kartı: üstte el yazısı başlık, 3x3 (kare kapak) ya da 3x2 (dikey kapak) ızgara, çocuk çizimi süslemeler."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tarz import S
D = os.path.dirname(os.path.abspath(__file__)); AS = f"file://{D}/../assets"; C = f"file://{D}/covers"
FONT = f"""@font-face{{font-family:B;font-weight:800;src:url({AS}/baloo-800.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:B;font-weight:800;src:url({AS}/baloo-800-ext.woff2);unicode-range:U+0100-024F}}
@font-face{{font-family:B;font-weight:700;src:url({AS}/baloo-700.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:B;font-weight:700;src:url({AS}/baloo-700-ext.woff2);unicode-range:U+0100-024F}}"""
DOODLES = """
<svg style='position:absolute;left:20px;top:30px' width='170' height='110' viewBox='0 0 170 110' fill='none' stroke='#5B8FD9' stroke-width='4' stroke-linecap='round'><path d='M20 80 Q10 50 40 45 Q45 15 80 25 Q100 5 125 30 Q160 30 150 65 Q160 90 125 88 L35 90 Q15 92 20 80Z' fill='#DCE9FB'/><path d='M45 70 Q60 60 75 70 M90 62 Q105 52 120 64'/></svg>
<svg style='position:absolute;right:24px;top:40px' width='150' height='100' viewBox='0 0 170 110' fill='none' stroke='#5B8FD9' stroke-width='4' stroke-linecap='round'><path d='M20 80 Q10 50 40 45 Q45 15 80 25 Q100 5 125 30 Q160 30 150 65 Q160 90 125 88 L35 90 Q15 92 20 80Z' fill='#DCE9FB'/></svg>
<svg style='position:absolute;left:16px;top:250px;transform:rotate(-30deg)' width='96' height='96' viewBox='0 0 100 100' stroke='#E8833A' stroke-width='3.5' stroke-linejoin='round'><path d='M50 8 Q72 28 66 62 L34 62 Q28 28 50 8Z' fill='#FFB36B'/><circle cx='50' cy='34' r='7' fill='#fff'/><path d='M34 52 L20 70 L36 64 M66 52 L80 70 L64 64' fill='#F25C54'/><path d='M42 66 L50 92 L58 66' fill='#FFD166'/></svg>
<svg style='position:absolute;right:40px;bottom:230px' width='90' height='170' viewBox='0 0 60 120' fill='none' stroke='#E45D5D' stroke-width='3.5' stroke-linecap='round'><ellipse cx='30' cy='30' rx='24' ry='28' fill='#F7A1A1'/><path d='M30 58 Q22 75 32 88 Q42 100 28 116'/></svg>
<svg style='position:absolute;left:30px;bottom:150px' width='90' height='90' viewBox='0 0 100 100' stroke='#E8B53A' stroke-width='4' fill='#FFE08A'><circle cx='50' cy='28' r='14'/><circle cx='72' cy='50' r='14'/><circle cx='50' cy='72' r='14'/><circle cx='28' cy='50' r='14'/><circle cx='50' cy='50' r='10' fill='#fff'/></svg>
<svg style='position:absolute;right:30px;top:250px' width='70' height='70' viewBox='0 0 100 100' stroke='#E8B53A' stroke-width='4' fill='#FFE08A'><circle cx='50' cy='28' r='14'/><circle cx='72' cy='50' r='14'/><circle cx='50' cy='72' r='14'/><circle cx='28' cy='50' r='14'/><circle cx='50' cy='50' r='10' fill='#fff'/></svg>"""
def vitrin(kicker, line1, line2, slugs, foot="Tarzını seç, kitabını bastır"):
    """Raf vitrini: sitedeki gibi ince ahşap raflarda duran kapaklar, altta sade tarz adları, bol boşluk, çerçeve yok."""
    sq = S[slugs[0]][4] == "3-7"
    w = 218 if sq else 236; h = w if sq else round(w * 1.5)
    rows = [slugs[i:i+3] for i in range(0, len(slugs), 3)]
    tilt = [-2, 1.5, -1, 2, -1.5, 1, -2.5, 1.5, -1]
    def book(sl, k):
        return (f"<div style='display:flex;flex-direction:column;align-items:center;width:{w+40}px'>"
                f"<div style='width:{w}px;height:{h}px;position:relative;transform:rotate({tilt[k]}deg);transform-origin:50% 100%;filter:drop-shadow(0 18px 16px rgba(40,25,10,.28))'>"
                f"<img src='{C}/kapak-{sl}.jpg' style='width:100%;height:100%;object-fit:cover;border-radius:3px 7px 7px 3px'>"
                f"<div style='position:absolute;left:0;top:0;bottom:0;width:12px;border-radius:3px 0 0 3px;background:linear-gradient(to right,rgba(0,0,0,.25),rgba(255,255,255,.18))'></div></div></div>")
    shelves, k = "", 0
    for r in rows:
        books = ""
        for sl in r:
            books += book(sl, k); k += 1
        names = "".join(f"<div style='width:{w+40}px;text-align:center;font-size:24px;font-style:italic;color:#5a5148'>{S[sl][0]}</div>" for sl in r)
        shelves += (f"<div style='display:flex;justify-content:center;gap:34px;align-items:flex-end'>{books}</div>"
                    f"<div style='height:12px;margin:0 70px;background:linear-gradient(#5b4130,#3b291d);border-radius:3px;box-shadow:0 8px 14px rgba(40,25,10,.22)'></div>"
                    f"<div style='display:flex;justify-content:center;gap:34px;margin:10px 0 {26 if sq else 34}px'>{names}</div>")
    return f"""<html><head><meta charset=utf-8><style>*{{margin:0;box-sizing:border-box}}body{{width:1080px;height:1350px;background:#F4EEE3;position:relative;overflow:hidden;font-family:"Liberation Serif",serif;color:#16181D}}</style></head><body>
<div style='position:absolute;inset:0;background:radial-gradient(ellipse at 50% 25%,rgba(255,255,255,.7),transparent 65%)'></div>
<img src='{AS}/wordmark.png' style='position:absolute;top:44px;left:50%;transform:translateX(-50%);height:48px'>
<div style='position:absolute;top:118px;left:0;right:0;text-align:center'>
 <div style='font-size:22px;font-weight:700;letter-spacing:6px;color:#B5121B'>{kicker}</div>
 <div style='font-size:74px;font-weight:700;line-height:1.05;margin-top:8px'>{line1}</div>
 <div style='font-size:36px;font-style:italic;color:#B5121B;margin-top:6px'>{line2}</div>
</div>
<div style='position:absolute;top:{360 if sq else 372}px;left:0;right:0'>{shelves}</div>
<div style='position:absolute;bottom:40px;left:0;right:0;text-align:center'>
 <span style='background:#B5121B;color:#fff;font-weight:700;font-size:32px;padding:12px 30px;border-radius:8px;box-shadow:0 4px 0 #7d0c12'>{foot}</span>
</div></body></html>"""
