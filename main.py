#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


if __name__ == '__main__':
    from PIL import Image, ImageFont, ImageDraw

    NAME = 'Вася'

    font = ImageFont.truetype("arial.ttf", 26)
    big_font = ImageFont.truetype("arial.ttf", 65)

    im = Image.open('aliexpress_ad.jpg')

    draw = ImageDraw.Draw(im)
    draw.text((33, 384), NAME.title(), font=font, fill="black")
    draw.text((66, 455), NAME.upper(), font=font, fill="black")
    draw.text((431, 504), NAME.upper(), font=font, fill="white")
    draw.text((52, 637), NAME.upper(), font=big_font, fill="white")

    im.save("runaway.jpg")
