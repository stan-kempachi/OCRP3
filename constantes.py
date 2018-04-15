"""Constantes du jeu de Mac Gyver escape"""

# -*-coding:Latin-1 -*

import pygame
pygame.font.init()
from pygame.locals import *

from classes import *
from constantes import *

import time


# Window settings
number_sprite_cote = 15
size_sprite = 30
dimension_window = number_sprite_cote * size_sprite

# Personalization of the window
window_title = "Mac Gyver Escapes"
image_icone = "images/mc_droite.png"

# Levels of the game
levelGame1 = "n1"

# Font choosen for the txt ingame
police = pygame.font.Font("../OCRP3/freesansbold.ttf", 17, bold = True)

# Lists of the game's images
image_background = "images/fond.jpg"
image_wall = "images/wall.png"
image_start = "images/depart.png"
image_arrival = "images/gardien.png"




