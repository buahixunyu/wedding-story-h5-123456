# -*- coding: utf-8 -*-
"""生成婚礼 H5 线上链接的二维码卡片。"""
import os

import segno
from PIL import Image, ImageDraw, ImageFont

URL = "https://xiaolikeke.vip"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "qrcode-invite.png")

TITLE = "我们的五幕小电影"
SUB = "扫码观看 · 婚礼邀请"

FONT_CANDIDATES = [
    "C:/Windows/Fonts/msyhbd.ttc",
    "C:/Windows/Fonts/msyh.ttc",
    "C:/Windows/Fonts/simhei.ttf",
]


def load_font(size):
    for path in FONT_CANDIDATES:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except OSError:
                continue
    return ImageFont.load_default()


def main():
    qr = segno.make(URL, error="h")
    tmp = os.path.join(os.path.dirname(OUT), "_qr_tmp.png")
    qr.save(tmp, scale=12, border=3, dark="#1A1A1A", light="#FFFFFF")
    qr_img = Image.open(tmp).convert("RGB")
    os.remove(tmp)

    qw, qh = qr_img.size
    pad = 56
    head = 150
    foot = 96
    W = qw + pad * 2
    H = qh + head + foot + pad

    card = Image.new("RGB", (W, H), "#FFFFFF")
    card.paste(qr_img, (pad, head))
    draw = ImageDraw.Draw(card)

    f_title = load_font(46)
    f_sub = load_font(24)
    f_url = load_font(18)

    def center(text, y, font, fill):
        box = draw.textbbox((0, 0), text, font=font)
        draw.text(((W - (box[2] - box[0])) / 2, y), text, font=font, fill=fill)

    center(TITLE, 44, f_title, "#1A1A1A")
    center(SUB, 104, f_sub, "#8A8A8A")
    center(URL, head + qh + pad - 12, f_url, "#B0B0B0")

    card.save(OUT)
    print("saved:", OUT, card.size)


if __name__ == "__main__":
    main()
