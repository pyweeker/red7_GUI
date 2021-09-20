#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import arcade

from cst_file import *


class Card(arcade.Sprite):


    def __init__(self, idx, scale=1):

        self.idx = idx  # index of instanciation = his value
        
        self.image_file_name = f"./resources/images/cards/{self.idx}.jpg"
        self.is_face_up = False
        super().__init__(FACE_DOWN_IMAGE, scale, hit_box_algorithm="None")

    def face_down(self):
        self.texture = arcade.load_texture(FACE_DOWN_IMAGE)
        self.is_face_up = False

    def face_up(self):
        self.texture = arcade.load_texture(self.image_file_name)
        self.is_face_up = True

    @property
    def is_face_down(self):
        return not self.is_face_up