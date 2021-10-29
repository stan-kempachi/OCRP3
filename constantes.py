# -*-coding:Latin-1 -*

import pygame
pygame.font.init()

"""Constantes du jeu de Mac Gyver escape"""

# Window settings
NUMBER_SPRITE_COTE = 15
SIZE_SPRITE = 30
DIMENSION_WINDOW = NUMBER_SPRITE_COTE * SIZE_SPRITE

# Personalization of the window
WINDOW_TITLE = "Mac Gyver Escapes"
IMAGE_ICONE = "images/mc_droite.png"

# Font choosen for the txt ingame
POLICE = pygame.font.Font("D:/User/Downloads/OCRP3-master/OCRP3-master/FreeSansBold.ttf", 17, bold=True)

# Lists of the game's images
IMAGE_BACKGROUND = "images/fond.jpg"
IMAGE_WALL = "images/wall.png"
IMAGE_START = "images/depart.png"
IMAGE_ARRIVAL = "images/gardien.png"
