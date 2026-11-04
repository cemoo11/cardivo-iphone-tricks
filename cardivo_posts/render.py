"""Slide renderer: 1080x1920 grainy-gradient cards with white text."""
import os
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1080, 1920
WHITE = (255, 255, 255)
SOFT = (228, 230, 236)
ROOT = Path(__file__).resolve().parent.parent
ICON = ROOT / "assets" / "cardivo-icon.png"

# Inter (OFL) is downloaded in CI into fonts/. Locally, SF Pro is used if present.
_FONT_CANDIDATES = {
    "Heavy": ["Inter-ExtraBold.otf", "SF-Pro-Display-Heavy.otf"],
    "Bold": ["Inter-Bold.otf", "SF-Pro-Display-Bold.otf"],
    "Semibold": ["Inter-SemiBold.otf", "SF-Pro-Display-Semibold.otf"],
    "Medium": ["Inter-Medium.otf", "SF-Pro-Display-Medium.otf"],
    "Regular": ["Inter-Regular.otf", "SF-Pro-Display-Regular.otf"],
}
_FONT_DIRS = [os.environ.get("CARDIVO_FONT_DIR", ""), str(ROOT / "fonts"), "/Library/Fonts"]


def font(weight: str, size: int) -> ImageFont.FreeTypeFont:
    for name in _FONT_CANDIDATES[weight]:
        for d in _FONT_DIRS:
            p = Path(d) / name
            if d and p.exists():
                return ImageFont.truetype(str(p), size)
    raise FileNotFoundError(f"No font for weight {weight}")


PALETTES = [
    [(46, 92, 120), (224, 108, 84), (70, 190, 175), (30, 110, 150)],
    [(40, 30, 90), (200, 90, 170), (90, 110, 230), (240, 150, 190)],
    [(15, 60, 80), (40, 170, 140), (20, 90, 140), (150, 210, 170)],
    [(50, 25, 80), (240, 120, 60), (200, 50, 120), (70, 60, 170)],
    [(15, 30, 90), (40, 170, 220), (170, 140, 230), (30, 80, 180)],
    [(70, 30, 60), (240, 160, 130), (220, 90, 120), (120, 60, 140)],
    [(10, 60, 55), (40, 160, 120), (220, 180, 80), (30, 120, 140)],
    [(30, 50, 110), (110, 180, 240), (240, 120, 100), (70, 70, 170)],
    [(60, 15, 40), (230, 70, 80), (250, 140, 150), (110, 40, 120)],
    [(20, 40, 70), (250, 190, 90), (240, 110, 90), (60, 130, 190)],
    [(35, 20, 60), (120, 220, 200), (150, 90, 220), (40, 90, 150)],
    [(50, 40, 30), (230, 150, 80), (180, 90, 60), (90, 140, 160)],
]


def background(seed: int) -> Image.Image:
    rng = np.random.default_rng(seed)
    pal = PALETTES[int(rng.integers(len(PALETTES)))]
    sw, sh = 108, 192
    small = Image.new("RGB", (sw, sh), pal[0])
    dr = ImageDraw.Draw(small)
    for c in pal[1:] + pal[1:]:
        cx, cy = rng.uniform(-10, sw + 10), rng.uniform(-10, sh + 10)
        rx, ry = rng.uniform(25, 60), rng.uniform(35, 80)
        dr.ellipse((cx - rx, cy - ry, cx + rx, cy + ry), fill=c)
    small = small.filter(ImageFilter.GaussianBlur(22))
    img = np.asarray(small.resize((W, H), Image.BICUBIC)).astype(np.float32) * 0.82
    img += rng.normal(0, 22, (H, W, 1)).astype(np.float32)
    return Image.fromarray(np.clip(img, 0, 255).astype(np.uint8))


def _wrap(d, text, fnt, maxw):
    lines, cur = [], ""
    for word in text.split():
        t = (cur + " " + word).strip()
        if d.textlength(t, font=fnt) <= maxw:
            cur = t
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def _block(d, text, fnt, y, color=WHITE, maxw=880, gap=1.22, x=100):
    for line in _wrap(d, text, fnt, maxw):
        d.text((x, y), line, font=fnt, fill=color)
        y += int(fnt.size * gap)
    return y


def _footer(d, i, n):
    d.text((100, H - 170), "cardivo", font=font("Bold", 40), fill=WHITE)
    t = f"{i}/{n}"
    fo = font("Medium", 36)
    d.text((W - 100 - d.textlength(t, font=fo), H - 166), t, font=fo, fill=SOFT)


def _pill(im, y, text):
    d = ImageDraw.Draw(im)
    fo = font("Semibold", 40)
    lines = _wrap(d, text, fo, 800)
    ph = 60 + len(lines) * 54
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(ov).rounded_rectangle((100, y, 980, y + ph), radius=36,
                                         fill=(255, 255, 255, 46), outline=(255, 255, 255, 110), width=2)
    im.paste(Image.alpha_composite(im.convert("RGBA"), ov).convert("RGB"))
    d = ImageDraw.Draw(im)
    yy = y + 30
    for line in lines:
        d.text((140, yy), line, font=fo, fill=WHITE)
        yy += 54
    return d


def cover(seed, big, headline, sub, i, n):
    im = background(seed)
    d = ImageDraw.Draw(im)
    d.text((100, 560), big, font=font("Heavy", 300), fill=WHITE)
    y = _block(d, headline, font("Bold", 104), 900, gap=1.12)
    _block(d, sub, font("Medium", 48), y + 60, SOFT)
    _footer(d, i, n)
    return im


def tip(seed, num, title, body, path, i, n):
    im = background(seed)
    d = ImageDraw.Draw(im)
    d.text((100, 420), f"{num:02d}", font=font("Heavy", 170), fill=WHITE)
    y = _block(d, title, font("Bold", 92), 680, gap=1.12)
    y = _block(d, body, font("Regular", 54), y + 50, gap=1.35)
    d = _pill(im, y + 70, path)
    _footer(d, i, n)
    return im


def cardivo(seed, label, headline, body, i, n):
    im = background(seed)
    d = ImageDraw.Draw(im)
    d.text((100, 420), label, font=font("Heavy", 120), fill=WHITE)
    y = _block(d, headline, font("Bold", 92), 600, gap=1.12)
    y = _block(d, body, font("Regular", 54), y + 50, gap=1.35)
    icon = Image.open(ICON).convert("RGBA").resize((200, 200))
    mask = Image.new("L", (200, 200), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, 199, 199), radius=46, fill=255)
    im.paste(icon, (100, y + 90), mask)
    d.text((340, y + 112), "Cardivo", font=font("Bold", 64), fill=WHITE)
    d.text((340, y + 192), "Free on the App Store", font=font("Medium", 44), fill=SOFT)
    _footer(d, i, n)
    return im
