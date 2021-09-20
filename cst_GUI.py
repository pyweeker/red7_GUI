# Screen title and size
#SCREEN_WIDTH = 1024
#SCREEN_HEIGHT = 768
#SCREEN_TITLE = "Drag and Drop Cards"

SCREEN_WIDTH = 1800 #1000
SCREEN_HEIGHT = 1000 #650
SCREEN_TITLE = "RED 7"

import arcade
coloriz_dict = {"red" : arcade.color.RED, "orange" : arcade.color.ORANGE, "yellow" : arcade.color.YELLOW, "green" : arcade.color.GREEN, "blue": arcade.color.BLUE,"indigo": arcade.color.INDIGO, "violet": arcade.color.VIOLET}
# add cyan magenta grey

# Constants for sizing
CARD_SCALE = 0.6

# How big are the cards?
CARD_WIDTH = 140 * CARD_SCALE
CARD_HEIGHT = 190 * CARD_SCALE

# How big is the mat we'll place the card on?
MAT_PERCENT_OVERSIZE = 1.25
MAT_HEIGHT = int(CARD_HEIGHT * MAT_PERCENT_OVERSIZE)
MAT_WIDTH = int(CARD_WIDTH * MAT_PERCENT_OVERSIZE)

# How much space do we leave as a gap between the mats?
# Done as a percent of the mat size.
VERTICAL_MARGIN_PERCENT = 0.10
HORIZONTAL_MARGIN_PERCENT = 0.10

# The Y of the bottom row (2 piles)
BOTTOM_Y = MAT_HEIGHT / 2 + MAT_HEIGHT * VERTICAL_MARGIN_PERCENT



# The Y of the top row (4 piles)
#MASTER_DECK_Y = SCREEN_HEIGHT - MAT_HEIGHT / 2 - MAT_HEIGHT * VERTICAL_MARGIN_PERCENT
#MASTER_DECK_Y = SCREEN_HEIGHT - MAT_HEIGHT / 2 - MAT_HEIGHT * VERTICAL_MARGIN_PERCENT - 200
MASTER_DECK_Y = SCREEN_HEIGHT - MAT_HEIGHT / 2 - MAT_HEIGHT * VERTICAL_MARGIN_PERCENT - 300


# The X of where to start putting things on the left side
START_X = MAT_WIDTH / 2 + MAT_WIDTH * HORIZONTAL_MARGIN_PERCENT

START_Y = MASTER_DECK_Y - MAT_HEIGHT - MAT_HEIGHT * VERTICAL_MARGIN_PERCENT


# The Y of the middle row (7 piles)
MIDDLE_Y = MASTER_DECK_Y - MAT_HEIGHT - MAT_HEIGHT * VERTICAL_MARGIN_PERCENT

# How far apart each pile goes
X_SPACING = MAT_WIDTH + MAT_WIDTH * HORIZONTAL_MARGIN_PERCENT



#P0_Y = MAT_HEIGHT / 2 + MAT_HEIGHT * VERTICAL_MARGIN_PERCENT
P0_PAL_Y = MAT_HEIGHT / 2 + MAT_HEIGHT * VERTICAL_MARGIN_PERCENT
#PIOCHE = MASTER_DECK_Y - MAT_HEIGHT - MAT_HEIGHT * VERTICAL_MARGIN_PERCENT
HAND0_Y = P0_PAL_Y + MAT_HEIGHT + 20

#----------------------
#P1_PAL_Y = 800
P1_PAL_Y = 700
HAND1_Y = 900

DECK_MAX_RANGE = 50



# Card constants
CARD_VALUES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
CARD_SUITS = ["Clubs", "Hearts", "Spades", "Diamonds"]

# If we fan out cards stacked on each other, how far apart to fan them?
CARD_VERTICAL_OFFSET = CARD_HEIGHT * CARD_SCALE * 0.3

# Face down image
FACE_DOWN_IMAGE = ":resources:images/cards/cardBack_red2.png"

# Constants that represent "what pile is what" for the game
"""
PILE_COUNT = 13
BOTTOM_FACE_DOWN_PILE = 0
BOTTOM_FACE_UP_PILE = 1
PLAY_PILE_1 = 2
PLAY_PILE_2 = 3
PLAY_PILE_3 = 4
PLAY_PILE_4 = 5
PLAY_PILE_5 = 6
PLAY_PILE_6 = 7
PLAY_PILE_7 = 8
TOP_PILE_1 = 9
TOP_PILE_2 = 10
TOP_PILE_3 = 11
TOP_PILE_4 = 12
"""

#PILE_COUNT = 13
#PILE_COUNT = 27  buggy ?!?
#PILE_COUNT = 30  ?


MASTER_DECK_ASS_PILE = 28
MASTER_DECK_NOSE_PILE = 29
PLAY_PILE_1 = 0
PLAY_PILE_2 = 1
PLAY_PILE_3 = 2
PLAY_PILE_4 = 3
PLAY_PILE_5 = 4
PLAY_PILE_6 = 5
PLAY_PILE_7 = 6
TOP_PILE_1 = 7
TOP_PILE_2 = 8
TOP_PILE_3 = 9
TOP_PILE_4 = 10

P0_PAL_0 = 7
P0_PAL_1 = 8 
P0_PAL_2 = 9
P0_PAL_3 = 10
P0_PAL_4 = 11
P0_PAL_5 = 12
P0_PAL_6 = 13



P1_HAND_0 = 14
P1_HAND_1 = 15
P1_HAND_2 = 16
P1_HAND_3 = 17
P1_HAND_4 = 18
P1_HAND_5 = 19
P1_HAND_6 = 20

P1_PAL_0 = 21
P1_PAL_1 = 22 
P1_PAL_2 = 23
P1_PAL_3 = 24
P1_PAL_4 = 25
P1_PAL_5 = 26
P1_PAL_6 = 27

