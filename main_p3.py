# -*-coding:Latin-1 -*

"""
Jeu Mac Gyver Escape
Jeu dans lequel on doit déplacer Mac Gyver jusqu'à l'arrivée à travers un labyrinthe.

Script Python
Fichiers : main_p3.py, classes.py, constantes.py, n1 et images
"""

import time
import pygame
from pygame.locals import *

from classes import *
from constantes import *

pygame.init()


# Opening the Pygame WINDOW (square: width = height)
WINDOW = pygame.display.set_mode((DIMENSION_WINDOW, DIMENSION_WINDOW))

# Icone
ICONE = pygame.image.load(IMAGE_ICONE)
pygame.display.set_icon(ICONE)
#Title
pygame.display.set_caption(WINDOW_TITLE)

# Background image
BACKGROUND = pygame.image.load("images/fond.jpg").convert()

# Loading the sprite of the caracter
CHARA = pygame.image.load("images/mc_droite.png").convert_alpha()

# Apply the background in the window
WINDOW.blit(BACKGROUND, (0, 0))

# Apply the caracter in the window
WINDOW.blit(CHARA, (0, 0))

# Refresh the window the display the background and the character
pygame.display.flip()

# Refresh the window the display the background and the character
pygame.display.flip()

# Create an instance of the Level
LEVEL = Level("n1.txt")

#Création de Mac Gyver
MC = Perso("images/mc_droite.png", "images/mc_gauche.png",\
"images/mc_haut.png", "images/mc_bas.png", LEVEL)

# State of the game. 1 = running, 0 = closed
CONTINUE_GAME = 1

# Set for de movements of the character
pygame.key.set_repeat(5, 5)

# Loading of the gameover's image
GAMEOVER = pygame.image.load("images/gameove.png").convert_alpha()

# Loading of the Win's image
WIN = pygame.image.load("images/win.jpg").convert_alpha()

# Generation of the level
LEVEL.gen()

# Creation of the instance of items
POTION = Potion("images/potion.png", LEVEL)
KEY = Key("images/key.png", LEVEL)
SWORD = Sword("images/sword.png", LEVEL)

# Vars of items. When the character pick-up one of them, var pass to 1
POTINV = 0
KEYINV = 0
SWORINV = 0

# Font choosen for the txt ingame
POLICE = pygame.font.SysFont("FreeSansBold.ttf", 15, bold=True)

# Txts about items
INVENTAIRE = POLICE.render("Inventaire: ", 1, (255, 255, 255))
POT_ = POLICE.render("Potion", 1, (255, 255, 255))
KEY_ = POLICE.render("Clef", 1, (255, 255, 255))
SWO_ = POLICE.render("Epée", 1, (255, 255, 255))


# MAIN LOOP

while CONTINUE_GAME:

    # Speed limitation of the loop
    pygame.time.Clock().tick(20)

    for event in pygame.event.get():

        # If the user leaves, we put the variable that continues the game to 0

        if event.type == QUIT:
            CONTINUE_GAME = 0
        elif event.type == KEYDOWN:
           
            if event.key == K_ESCAPE:
                CONTINUE_GAME = 0

            # Mac move keys

            elif event.key == K_RIGHT:
                MC.deplacer('right')
            elif event.key == K_LEFT:
                MC.deplacer('left')
            elif event.key == K_UP:
                MC.deplacer('up')
            elif event.key == K_DOWN:
                MC.deplacer('down')

    WINDOW.blit(BACKGROUND, (0, 0))
    WINDOW.blit(MC.direction, (MC.x, MC.y))
    LEVEL.show(WINDOW)


    # If item if was picked display it in the inventory at the top right of the window
    if POTINV == 1:
        WINDOW.blit(POT_, (350, 20))
        pygame.display.flip()

    elif POTINV == 0:
        POTION.display(WINDOW)

    if KEYINV == 1:
        WINDOW.blit(KEY_, (350, 35))
        pygame.display.flip()

    elif KEYINV == 0:
        KEY.display(WINDOW)

    if  SWORINV == 1:
        WINDOW.blit(SWO_, (350, 50))
        pygame.display.flip()

    elif SWORINV == 0:
        SWORD.display(WINDOW)

    # Display the "Inventaire" in the top right of the window
    WINDOW.blit(INVENTAIRE, (350, 5))
    pygame.display.flip()

    """ If Mac Gyver arrive at the end of maze and didn't collect one of the item,
    then the player loose """
    if LEVEL.structure[MC.case_y][MC.case_x] == 'a':
        if POTINV == 0:
            WINDOW.blit(GAMEOVER, (100, 100))
            pygame.display.flip()
            time.sleep(3)
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    CONTINUE_GAME = 0
                elif event.key == K_ESCAPE:
                    CONTINUE_GAME = 0
                elif event.key == K_DOWN:
                    CONTINUE_GAME = 0
                elif event.key == K_UP:
                    CONTINUE_GAME = 0
                elif event.key == K_LEFT:
                    CONTINUE_GAME = 0
                elif event.key == K_RIGHT:
                    CONTINUE_GAME = 0

        if KEYINV == 0:
            WINDOW.blit(GAMEOVER, (100, 100))
            pygame.display.flip()
            time.sleep(3)
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    CONTINUE_GAME = 0
                elif event.key == K_ESCAPE:
                    CONTINUE_GAME = 0
                elif event.key == K_DOWN:
                    CONTINUE_GAME = 0
                elif event.key == K_UP:
                    CONTINUE_GAME = 0
                elif event.key == K_LEFT:
                    CONTINUE_GAME = 0
                elif event.key == K_RIGHT:
                    CONTINUE_GAME = 0

        if SWORINV == 0:
            WINDOW.blit(GAMEOVER, (100, 100))
            pygame.display.flip()
            time.sleep(3)
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    CONTINUE_GAME = 0
                elif event.key == K_ESCAPE:
                    CONTINUE_GAME = 0
                elif event.key == K_DOWN:
                    CONTINUE_GAME = 0
                elif event.key == K_UP:
                    CONTINUE_GAME = 0
                elif event.key == K_LEFT:
                    CONTINUE_GAME = 0
                elif event.key == K_RIGHT:
                    CONTINUE_GAME = 0

        # If the play collect every items at the end of maze then he Win
        if POTINV == 1 and KEYINV == 1 and SWORINV == 1:
            pygame.time.Clock().tick(3000)
            WINDOW.blit(WIN, (100, 100))
            pygame.display.flip()
            if event.key == K_RETURN:
                CONTINUE_GAME = 0
            else:
                time.sleep(3)
                CONTINUE_GAME = 0

    """ If the position of the player is the same of one of the items,
    then increase the var correspunding """
    if LEVEL.structure[MC.case_y][MC.case_x] == "o1":
        POTINV = 1

    if LEVEL.structure[MC.case_y][MC.case_x] == "o2":
        KEYINV = 1

    if LEVEL.structure[MC.case_y][MC.case_x] == "o3":
        SWORINV = 1
