#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Optional

import random
import arcade

from cst_core import *
from cst_GUI import *

from klasses import *
from klasses_GUI import *

from random import shuffle

class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.deck = []  # numeric part
        self.Players = []

        self.card_list: Optional[arcade.SpriteList] = None   # GUI part
        arcade.set_background_color(arcade.color.AMAZON)

        self.held_cards = None
        self.held_cards_original_position = None

        self.pile_mat_list = None
        self.piles = None

        #self.PAL_P0_tab = None

    @property
    def PAL_P0_tab(self):
        return [self.piles[P0_PAL_0],self.piles[P0_PAL_1],self.piles[P0_PAL_2],self.piles[P0_PAL_3],self.piles[P0_PAL_4],self.piles[P0_PAL_5],self.piles[P0_PAL_6]]
    


    def setup(self):

        self.deck = [x for x in range(1,DECK_MAX_RANGE)]

        shuffle(self.deck)

        for i in range(PLAYERS_NB):
            newplayer = Player(i)
            self.Players.append(newplayer)



        self.held_cards = []
        self.held_cards_original_position = []

        self.pile_mat_list: arcade.SpriteList = arcade.SpriteList()

        
        # Create the seven middle piles      P0 HAND_0  MATS
        for i in range(7):
            pile = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
            #pile.position = START_X + i * X_SPACING, MIDDLE_Y
            pile.position = START_X + i * X_SPACING, P0_PAL_Y
            self.pile_mat_list.append(pile)

        # Create the top "play" piles       P0 TABLE_0  MATS
        #for i in range(4):
        for i in range(7):
            pile = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.GOLD)
            #pile.position = START_X + i * X_SPACING, TOP_Y
            pile.position = START_X + i * X_SPACING, HAND0_Y
            self.pile_mat_list.append(pile)





        # Create the seven middle piles      P1 HAND_1  MATS
        for i in range(7):
            pile = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.OLIVE_DRAB)
            
            pile.position = START_X + i * X_SPACING, HAND1_Y
            self.pile_mat_list.append(pile)



        #---- Enemy                        P1 TABLE_1  MATS
        for i in range(7):
            pile = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.GOLDENROD)
            #pile.position = START_X + i * X_SPACING, MIDDLE_Y
            pile.position = START_X + i * X_SPACING, P1_PAL_Y
            self.pile_mat_list.append(pile)

        # --- Create, shuffle, and deal the cards

        # Sprite list with all the cards, no matter what pile they are in.
        self.card_list = arcade.SpriteList()

                

        #for i in range(1,50):
        for i in self.deck:
            card = Card(i, CARD_SCALE)
            card.position = START_X, START_Y
            self.card_list.append(card)

        

        # Create a list of lists, each holds a pile of cards.
        PILE_COUNT = 30

        self.piles = [[] for _ in range(PILE_COUNT)]
        print("self.piles = [[] for _ in range(PILE_COUNT)]      ", PILE_COUNT)

        # Put all the cards in the bottom face-down pile
        for card in self.card_list:
            self.piles[MASTER_DECK_ASS_PILE].append(card)
            #print(card)

        # - Pull from that pile into the middle piles, all face-down
        # Loop for each pile
        for pile_no in range(PLAY_PILE_1, PLAY_PILE_7 + 1):
        #    # Deal proper number of cards for that pile

            card = self.piles[MASTER_DECK_ASS_PILE].pop()
            self.piles[pile_no].append(card)
            card.position = self.pile_mat_list[pile_no].position
            self.pull_to_top(card)


        #card = self.piles[MASTER_DECK_ASS_PILE].pop()
        #self.piles[pile_no].append(card)

        # Flip up the top cards
        for i in range(PLAY_PILE_1, PLAY_PILE_7 + 1):
            self.piles[i][-1].face_up()


        pile_no = P0_PAL_0
        card = self.piles[MASTER_DECK_ASS_PILE].pop()
        self.piles[pile_no].append(card)
        card.position = self.pile_mat_list[pile_no].position
        self.pull_to_top(card)
        card.face_up()




        #--- enemy P1



        for pile_no in range(P1_HAND_0, P1_HAND_6 + 1):
        #    # Deal proper number of cards for that pile

            card = self.piles[MASTER_DECK_ASS_PILE].pop()
            print(self.piles," ",len(self.piles),"  ",pile_no)
            self.piles[pile_no].append(card)
            card.position = self.pile_mat_list[pile_no].position
            self.pull_to_top(card)



        pile_no = P1_PAL_0
        card = self.piles[MASTER_DECK_ASS_PILE].pop()
        self.piles[pile_no].append(card)
        card.position = self.pile_mat_list[pile_no].position
        self.pull_to_top(card)
        card.face_up()

            #for j in range(pile_no - PLAY_PILE_1 + 1):
                # Pop the card off the deck we are dealing from
            #    card = self.piles[MASTER_DECK_ASS_PILE].pop()
                # Put in the proper pile
            #    self.piles[pile_no].append(card)
                # Move card to same position as pile we just put it in
            #    card.position = self.pile_mat_list[pile_no].position
                # Put on top in draw order
            #    self.pull_to_top(card)

        



        i = 1
        for card in self.card_list:
            print(f"-card {card.idx}  in {self.get_pile_for_card(card)}                  $  {i}")
            i += 1
        print(self.PAL_P0_tab)
        print("\n .")


    def draw_canvas_background(self, color = judge_dredd.last_canvas_color):

        #print(f"color   {color}")

        

        #arcade.draw_rectangle_filled(SCREEN_WIDTH - 50, SCREEN_HEIGHT - 50, SCREEN_WIDTH + 50, SCREEN_HEIGHT + 50, color)
        arcade.draw_rectangle_filled(SCREEN_WIDTH//2 - 5, SCREEN_HEIGHT//2 - 5, 150, 200, coloriz_dict[color])
        



        

    def on_draw(self):
        """ Render the screen. """
        # Clear the screen
        arcade.start_render()

        # Draw the mats the cards go on to
        self.pile_mat_list.draw()

        # Draw the cards
        self.card_list.draw()

        # Draw the canvas background
        self.draw_canvas_background()

    def pull_to_top(self, card: arcade.Sprite):
        """ Pull card to top of rendering order (last to render, looks on-top) """

        # Remove, and append to the end
        self.card_list.remove(card)
        self.card_list.append(card)

    def on_key_press(self, symbol: int, modifiers: int):
        """ User presses key """
        if symbol == arcade.key.R:
            # Restart
            self.setup()

    def on_mouse_press(self, x, y, button, key_modifiers):
        """ Called when the user presses a mouse button. """

        # Get list of cards we've clicked on
        cards = arcade.get_sprites_at_point((x, y), self.card_list)

        # Have we clicked on a card?
        if len(cards) > 0:

            # Might be a stack of cards, get the top one
            primary_card = cards[-1]
            assert isinstance(primary_card, Card)

            # Figure out what pile the card is in
            pile_index = self.get_pile_for_card(primary_card)

            # Are we clicking on the bottom deck, to flip three cards?
            

            if primary_card.is_face_down:
                # Is the card face down? In one of those middle 7 piles? Then flip up
                primary_card.face_up()
            else:
                # All other cases, grab the face-up card we are clicking on
                self.held_cards = [primary_card]
                # Save the position
                self.held_cards_original_position = [self.held_cards[0].position]
                # Put on top in drawing order
                self.pull_to_top(self.held_cards[0])

                # Is this a stack of cards? If so, grab the other cards too
                card_index = self.piles[pile_index].index(primary_card)
                for i in range(card_index + 1, len(self.piles[pile_index])):
                    card = self.piles[pile_index][i]
                    self.held_cards.append(card)
                    self.held_cards_original_position.append(card.position)
                    self.pull_to_top(card)

        else:

            # Click on a mat instead of a card?
            mats = arcade.get_sprites_at_point((x, y), self.pile_mat_list)

            if len(mats) > 0:
                mat = mats[0]
                mat_index = self.pile_mat_list.index(mat)

                # Is it our turned over flip mat? and no cards on it?
                

    def remove_card_from_pile(self, card):
        """ Remove card from whatever pile it was in. """
        for pile in self.piles:
            if card in pile:
                pile.remove(card)
                break

    def get_pile_for_card(self, card):
        """ What pile is this card in? """
        for index, pile in enumerate(self.piles):
            if card in pile:
                return index

    def move_card_to_new_pile(self, card, pile_index):
        """ Move the card to a new pile """
        self.remove_card_from_pile(card)
        self.piles[pile_index].append(card)

    def on_mouse_release(self, x: float, y: float, button: int,
                         modifiers: int):
        """ Called when the user presses a mouse button. """

        # If we don't have any cards, who cares
        if len(self.held_cards) == 0:
            return

        # Find the closest pile, in case we are in contact with more than one
        pile, distance = arcade.get_closest_sprite(self.held_cards[0], self.pile_mat_list)
        reset_position = True

        # See if we are in contact with the closest pile
        if arcade.check_for_collision(self.held_cards[0], pile):

            # What pile is it?
            pile_index = self.pile_mat_list.index(pile)

            #  Is it the same pile we came from?
            if pile_index == self.get_pile_for_card(self.held_cards[0]):
                # If so, who cares. We'll just reset our position.
                pass

            # Is it on a middle play pile?
            elif PLAY_PILE_1 <= pile_index <= PLAY_PILE_7:
                # Are there already cards there?
                if len(self.piles[pile_index]) > 0:
                    # Move cards to proper position
                    top_card = self.piles[pile_index][-1]
                    for i, dropped_card in enumerate(self.held_cards):
                        dropped_card.position = top_card.center_x, \
                                                top_card.center_y - CARD_VERTICAL_OFFSET * (i + 1)
                else:
                    # Are there no cards in the middle play pile?
                    for i, dropped_card in enumerate(self.held_cards):
                        # Move cards to proper position
                        dropped_card.position = pile.center_x, \
                                                pile.center_y - CARD_VERTICAL_OFFSET * i

                for card in self.held_cards:
                    # Cards are in the right position, but we need to move them to the right list
                    self.move_card_to_new_pile(card, pile_index)

                # Success, don't reset position of cards
                reset_position = False

            # Release on top play pile? And only one card held?
            #elif TOP_PILE_1 <= pile_index <= TOP_PILE_4 and len(self.held_cards) == 1:
            elif P0_PAL_0 <= pile_index <= P0_PAL_6 and len(self.held_cards) == 1:
                # Move position of card to pile
                self.held_cards[0].position = pile.position
                # Move card to card list
                for card in self.held_cards:
                    self.move_card_to_new_pile(card, pile_index)

                reset_position = False

                print("Coucou")
                self.menage_PAL_P0()

        if reset_position:
            # Where-ever we were dropped, it wasn't valid. Reset the each card's position
            # to its original spot.
            for pile_index, card in enumerate(self.held_cards):
                card.position = self.held_cards_original_position[pile_index]

        # We are no longer holding cards
        self.held_cards = []

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        """ User moves mouse """

        # If we are holding cards, move them with the mouse
        for card in self.held_cards:
            card.center_x += dx
            card.center_y += dy


    def menage_PAL_P0(self):

        #import copy

        print("        INSIDE menage_PAL_P0 !!")




        print(f"self.PAL_P0_tab  {self.PAL_P0_tab}")

        #PAL_P0_tab_copy = copy.deepcopy(PAL_P0_tab)
        
        for sublist in self.PAL_P0_tab:
            print(f"sublist  {sublist}")
            if sublist == []:
                sublist.append(None)


        

        print("\n ---")

        # PAL_P0 = [self.piles[P0_PAL_0][0],self.piles[P0_PAL_1][0],self.piles[P0_PAL_2][0],self.piles[P0_PAL_3][0],self.piles[P0_PAL_4][0],self.piles[P0_PAL_5][0],self.piles[P0_PAL_6][0]]

        #PAL_P0 = list(list)
        PAL_P0 = []

        PAL_P0.append(self.piles[P0_PAL_0][0])
        PAL_P0.append(self.piles[P0_PAL_1][0])
        PAL_P0.append(self.piles[P0_PAL_2][0])
        PAL_P0.append(self.piles[P0_PAL_3][0])
        PAL_P0.append(self.piles[P0_PAL_4][0])
        PAL_P0.append(self.piles[P0_PAL_5][0])
        PAL_P0.append(self.piles[P0_PAL_6][0])

        print("PAL_P0   ", PAL_P0)




        #print(f"PAL_P0  {PAL_P0}       type {type(PAL_P0)} ")


        #kill_nones = filter(None.__ne__, PAL_P0)
        #print(f"kill_nones {kill_nones}   type {type(kill_nones)}")
        #compact_PAL_P0 = [notnone for notnone in next(kill_nones)]

        #for foobar in PAL_P0:
        #    if foobar is None:
        #        del(foobar)

        PAL_P0 = [i for i in PAL_P0 if i]

        print(f"PAL_P0  {PAL_P0}       before sort. ")

        #print(f"compact_PAL_P0  {compact_PAL_P0}")

        positions_PAL_P0 = list()


        for card in PAL_P0:
            positions_PAL_P0.append(card.position)









        #PAL_P0_values = [val.idx for val[0] in PAL_P0]



        #print(f"PAL_P0_values  {PAL_P0_values}")

        # https://stackoverflow.com/questions/403421/how-to-sort-a-list-of-objects-based-on-an-attribute-of-the-objects

        #PAL_P0.sort(key=lambda x: x.idx, reverse=True)
        PAL_P0.sort(key=lambda x: x.idx, reverse=False)
        




        #PAL_P0.sort()
        print(f"PAL_P0  {PAL_P0}    after sort")

        print("\n ***")


        for i in range(P0_PAL_0,P0_PAL_6 + 1):
            #print(f"self.piles[i]  {self.piles[i]}")
            self.piles[i] = []


        for x in range(len(PAL_P0)):

            newlst = list()
            newlst.append(PAL_P0[x])

            #self.piles[P0_PAL_0 +x] = PAL_P0[x]
            self.piles[P0_PAL_0 +x] = newlst

            print(f" i {P0_PAL_0 +x}  __   self.piles[P0_PAL_0 +x] {self.piles[P0_PAL_0 +x]}")


        print("len(self.card_list)",len(self.card_list))



        print("\n __fin de menage on voit    self.PAL_P0_tab  =  ", self.PAL_P0_tab)


        #self.piles[P0_PAL_0][0]


        #PAL_P0_tab.index(bidul)


        for bidul in self.PAL_P0_tab:
            #if bidul == [None]:
            if not isinstance(bidul, Card):
                print(bidul,"   type ",type(bidul), "    not isinstance(bidul, Card) $$$ , len = ",len(bidul))
                print("self.piles[self.PAL_P0_tab.index(bidul) + P0_PAL_0]  =  ", self.piles[self.PAL_P0_tab.index(bidul) + P0_PAL_0])
                

                bidul = list()
                self.piles[self.PAL_P0_tab.index(bidul) + P0_PAL_0] = list()

                print(bidul,"   type ",type(bidul), "    not isinstance(bidul, Card) ??? , len = ",len(bidul))

                print("self.piles[self.PAL_P0_tab.index(bidul) + P0_PAL_0]  =  ", self.piles[self.PAL_P0_tab.index(bidul) + P0_PAL_0])


                

        print("\n    __>>>fin de menage on voit    self.PAL_P0_tab  =  ", self.PAL_P0_tab)


        for i in range(len(positions_PAL_P0)):
            print(i,"   ",self.PAL_P0_tab[i],"    ",positions_PAL_P0[i])

            print(i,"   ",self.PAL_P0_tab[i][0].__dict__)

            self.PAL_P0_tab[i][0].position = positions_PAL_P0[i]




        





        #or i in range(P0_PAL_0,P0_PAL_6 + 1):
        #    print(f"self.piles[i]  {self.piles[i]}")


        



        #for i in self.deck:
        #    card = Card(i, CARD_SCALE)
        #    card.position = START_X, START_Y
        #    self.card_list.append(card)




def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()