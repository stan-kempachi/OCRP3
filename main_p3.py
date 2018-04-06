# -*-coding:Latin-1 -*

"""
Jeu Mac Gyver Escape
Jeu dans lequel on doit déplacer Mac Gyver jusqu'à l'arrivée à travers un labyrinthe.

Script Python
Fichiers : main_p3.py, classes.py, constantes.py, n1 et images
"""
import pygame
from pygame.locals import *

from classes import *
from constantes import *

import time

pygame.init()
pygame.font.init

# Opening the Pygame window (square: width = height)
window = pygame.display.set_mode((dimension_window, dimension_window))

# Icone
icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)
#Title
pygame.display.set_caption(window_title)

# Background image
background = pygame.image.load("images/fond.jpg").convert()

# Loading the sprite of the caracter
Chara = pygame.image.load("images/mc_droite.png").convert_alpha()

# Apply the background in the window
window.blit(background, (0, 0))

# Apply the caracter in the window
window.blit(Chara, (0, 0))

# Refresh the window the display the background and the character
pygame.display.flip()

# Create an instance of the Level
level = Level("n1.txt")

#Création de Mac Gyver
mc = Perso("images/mc_droite.png", "images/mc_gauche.png" , "images/mc_haut.png", "images/mc_bas.png", level)

# State of the game. 1 = running, 0 = closed
continue_game = 1

# Set for de movements of the character
pygame.key.set_repeat(5, 5)

# Refresh the window the display the background and the character
pygame.display.flip()

# Loading of the gameover's image
Gameover = pygame.image.load("images/gameove.png").convert_alpha()

# Loading of the Win's image
Win = pygame.image.load("images/win.jpg").convert_alpha()

# Generation of the level
level.gen()

# Creation of the instance of items
potion = Potion("images/potion.png", level)
key = Key("images/key.png", level)
sword = Sword("images/sword.png", level)

# Vars of items. When the character pick-up one of them, var pass to 1
Potinv = 0
Keyinv = 0
Sworinv = 0

# Font choosen for the txt ingame
police = pygame.font.SysFont("FreeSansBold.ttf", 15, bold=True)

# Txts about items
inventaire = police.render("Inventaire: ", 1, (255, 255, 255))
pot_ = police.render("Potion", 1, (255, 255, 255))
key_ = police.render("Clef", 1, (255, 255, 255))
swo_ = police.render("Epée", 1, (255, 255, 255))


# GAME LOOP

while continue_game:

	# Speed limitation of the loop
	pygame.time.Clock().tick(30)

	for event in pygame.event.get():

		# If the user leaves, we put the variable that continues the game to 0
	
		if event.type == QUIT:
			continue_game = 0
		
			if event.key == K_ESCAPE:
				continue_game = 0

			# Mac move keys
				
			elif event.key == K_RIGHT:
				mc.deplacer('droite')
			elif event.key == K_LEFT:
				mc.deplacer('gauche')
			elif event.key == K_UP:
				mc.deplacer('haut')
			elif event.key == K_DOWN:
				mc.deplacer('bas')

	window.blit(background, (0, 0))
	window.blit(mc.direction, (mc.x, mc.y))
	level.Show(window)				

		  
	# If item if was picked display it in the inventory at the top right of the window
	if Potinv == 1:
		window.blit(pot_, (350, 20))
		pygame.display.flip()
		pass
	elif Potinv == 0:
		potion.display(window)

	if Keyinv == 1:
		window.blit(key_, (350, 35))
		pygame.display.flip()
		pass
	elif Keyinv == 0:
		key.display(window)

	if  Sworinv == 1:
		window.blit(swo_, (350, 50))
		pygame.display.flip()
		pass
	elif Sworinv == 0:
		sword.display(window)

	# Display the "Inventaire" in the top right of the window
	window.blit(inventaire, (350, 5))
	pygame.display.flip()

	""" If Mac Gyver arrive at the end of maze and didn't collect one of the item,
		then the player loose """
	if level.structure[mc.case_y][mc.case_x] == 'a':
		if Potinv == 0:
			window.blit(Gameover, (100, 100))
			pygame.display.flip()
			time.sleep(3)
			if event.type == KEYDOWN:
				if event.key == K_RETURN:
					continue_game = 0
				elif event.key == K_ESCAPE:
					continue_game = 0
				elif event.key == K_DOWN:
					continue_game = 0
				elif event.key == K_UP:
					continue_game = 0
				elif event.key == K_LEFT:
					continue_game = 0
				elif event.key == K_RIGHT:
					continue_game = 0

		if Keyinv == 0:
			window.blit(Gameover, (100, 100))
			pygame.display.flip()
			time.sleep(3)
			if event.type == KEYDOWN:
				if event.key == K_RETURN:
					continue_game = 0
				elif event.key == K_ESCAPE:
					continue_game = 0
				elif event.key == K_DOWN:
					continue_game = 0
				elif event.key == K_UP:
					continue_game = 0
				elif event.key == K_LEFT:
					continue_game = 0
				elif event.key == K_RIGHT:
					continue_game = 0

		if Sworinv == 0:
			window.blit(Gameover, (100, 100))
			pygame.display.flip()
			time.sleep(3)
			if event.type == KEYDOWN:
				if event.key == K_RETURN:
					continue_game = 0
				elif event.key == K_ESCAPE:
					continue_game = 0
				elif event.key == K_DOWN:
					continue_game = 0
				elif event.key == K_UP:
					continue_game = 0
				elif event.key == K_LEFT:
					continue_game = 0
				elif event.key == K_RIGHT:
					continue_game = 0

		# If the play collect every items at the end of maze then he Win
		if Potinv == 1 and Keyinv == 1 and Sworinv == 1:
			pygame.time.Clock().tick(3000)
			window.blit(Win, (50, 100))
			pygame.display.flip()
			if event.key == K_RETURN:
				continue_game = 0
			else:
				time.sleep(3)
				continue_game = 0

	""" If the position of the player is the same of one of the items,
	then increase the var correspunding """
	if level.structure[mc.case_y][mc.case_x] == "o1":
		Potinv = 1

	if level.structure[mc.case_y][mc.case_x] == "o2":
		Keyinv = 1

	if level.structure[mc.case_y][mc.case_x] == "o3":
		Sworinv = 1




