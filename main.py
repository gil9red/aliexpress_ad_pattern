#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


if __name__ == '__main__':
    from PIL import Image, ImageFont, ImageDraw

    NAME = 'Вася'

    font = ImageFont.truetype("arial.ttf", 26)

    im = Image.open('aliexpress_ad.jpg')

    draw = ImageDraw.Draw(im)
    draw.text((33, 384), NAME, font=font, fill="black")
    draw.text((66, 455), NAME, font=font, fill="black")
    draw.text((431, 504), NAME, font=font, fill="white")

    im.save("runaway.jpg")
