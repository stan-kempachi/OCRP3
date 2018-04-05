"""Constantes du jeu de Mac Gyver escape"""

# -*-coding:Latin-1 -*

import pygame
pygame.font.init()
from pygame.locals import *

from classes import *
from constantes import *

import time


#Paramètres de la fenêtre
nombre_sprite_cote = 15
taille_sprite = 30
cote_fenetre = nombre_sprite_cote * taille_sprite

#Personnalisation de la fenêtre
titre_fenetre = "Mac Gyver Escapes"
image_icone = "images/mc_droite.png"

# Levels of the game
levelGame1 = "n1"
levelGame2 = "n2"

# Font choosen for the txt ingame
police = pygame.font.Font("C:/Python/Lib/site-packages/pygame/freesansbold.ttf", 17, bold = True)

#Listes des images du jeu
image_accueil = "images/accueil.jpg"
image_fond = "images/fond.jpg"
image_wall = "images/wall.png"
image_depart = "images/depart.png"
image_arrivee = "images/gardien.png"




