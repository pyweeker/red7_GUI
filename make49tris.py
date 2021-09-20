#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# https://stackoverflow.com/questions/54165439/what-are-the-exact-color-names-available-in-pils-imagedraw/54165440
# https://www.youtube.com/watch?v=rLZk7cWbycI  FONTS Linux

# On linux you can find fronts for example here :  /usr/share/fonts/truetype/freefont


from math import *
from PIL import Image, ImageFont, ImageDraw, ImageEnhance
import os

folder = "49"
os.mkdir(folder)

CARD_WIDTH = 140 
CARD_HEIGHT = 190 


#font = ImageFont.load_default()

fontsize_a = 40
fontsize_c = 80
fontsize_x = 25

font_a = ImageFont.truetype("./freefont/FreeSansBoldOblique.ttf", fontsize_a)
font_c = ImageFont.truetype("./freefont/FreeSansBoldOblique.ttf", fontsize_c)
font_x = ImageFont.truetype("./freefont/FreeSansBoldOblique.ttf", fontsize_x)


from itertools import cycle
colors = ["violet","indigo","blue","green","yellow","orange","red"]
len_colors = len(colors)

colors_cycle = cycle(colors)
print(colors_cycle)





for i in range(1,50):

	next_colors_cycle = next(colors_cycle)

	button_img = Image.new('RGB', (CARD_WIDTH,CARD_HEIGHT), next_colors_cycle)

	button_draw = ImageDraw.Draw(button_img)
	

	val = ceil(i/7)

	button_draw.text((0, 0), f"{val}", font=font_a)

	

	button_draw.text((CARD_WIDTH//3, CARD_HEIGHT//3), f"{val}", font=font_c)

	button_draw.text((CARD_WIDTH - fontsize_x -10, CARD_HEIGHT - fontsize_x -10), f"{i}", font=font_x)

	button_img.save(f"./49/{i}.jpg", "JPEG")


