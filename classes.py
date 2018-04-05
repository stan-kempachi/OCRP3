"""Classes du jeu de :Mac Gyver escape"""

# -*-coding:Latin-1 -*

import pygame
from pygame.locals import *
pygame.init
from constantes import *
import random


class Level:        
	"""Class which initializes and displays the labyrinth on the screen"""
	def __init__(self, file):
		self.file = file # lvl.txt
		self.structure = []
                
	def gen(self):
		"""Method for generate level with a file"""
		# Open the file
		with open("n1.txt", "r") as file:
			structure_level = []
			# Reading the lines in file
			for line in file:
				line_of_level = []
				# Reading every letters in file
				for sprite in line:
					# Ignoring the last sprite to continue with the next line
					if sprite != '\n':
						# Adding every letters to the array
						line_of_level.append(sprite)
				# Adding every lines the the array
				structure_level.append(line_of_level)
			# Then the method save the entire structure of the level
			self.structure = structure_level

            

	def Show(self, Window):
		"""Method which shows the maze on the screen"""
		Wall = pygame.image.load(image_wall).convert()
		Escape = pygame.image.load(image_arrivee).convert()

		# Read the entire structure
		num_ligne = 0
		for line in self.structure:
			# Read every line
			num_case = 0
			for sprite in line:
				# Calculate the real position of the sprite
				x = num_case * taille_sprite
				y = num_ligne * taille_sprite
				if sprite == 'm':  # m = Wall
					Window.blit(Wall, (x, y))
				elif sprite == "a":  # a = Exit of the maze
					Window.blit(Escape, (x, y))
				num_case += 1
			num_ligne += 1
 
	
class Perso:
	"""Classe permettant de créer un personnage"""
	def __init__(self, droite, gauche, haut, bas, level):
		#Sprites du personnage
		self.droite = pygame.image.load(droite).convert_alpha()
		self.gauche = pygame.image.load(gauche).convert_alpha()
		self.haut = pygame.image.load(haut).convert_alpha()
		self.bas = pygame.image.load(bas).convert_alpha()
		#Position du personnage en cases et en pixels
		self.case_x = 0
		self.case_y = 0
		self.x = 0
		self.y = 0
		#Direction par défaut
		self.direction = self.droite
		#Niveau dans lequel le personnage se trouve 
		self.level = level
		
	def deplacer(self, direction):
		"""Methode permettant de déplacer le personnage"""
		
		#Déplacement vers la droite
		if direction == 'droite':
			#Pour ne pas dépasser l'écran
			if self.case_x < (nombre_sprite_cote - 1):
				#On vérifie que la case de destination n'est pas un mur
				if self.level.structure[self.case_y][self.case_x+1] != 'm':
					#Déplacement d'une case
					self.case_x += 1
					#Calcul de la position "réelle" en pixel
					self.x = self.case_x * taille_sprite
			#Image dans la bonne direction
			self.direction = self.droite
		
		#Déplacement vers la gauche
		if direction == 'gauche':
			if self.case_x > 0:
				if self.level.structure[self.case_y][self.case_x-1] != 'm':
					self.case_x -= 1
					self.x = self.case_x * taille_sprite
			self.direction = self.gauche
		
		#Déplacement vers le haut
		if direction == 'haut':
			if self.case_y > 0:
				if self.level.structure[self.case_y-1][self.case_x] != 'm':
					self.case_y -= 1
					self.y = self.case_y * taille_sprite
			self.direction = self.haut
		
		#Déplacement vers le bas
		if direction == 'bas':
			if self.case_y < (nombre_sprite_cote - 1):
				if self.level.structure[self.case_y+1][self.case_x] != 'm':
					self.case_y += 1
					self.y = self.case_y * taille_sprite
			self.direction = self.bas


# Class to create one of the items
class Potion:

    def __init__(self, obj, level):

        # Load the sprite of the item
        self.obj = pygame.image.load(obj).convert_alpha

        # Initial settings for the item
        self.level = level
        self.case_x, self.case_y = self.randpos()
        self.x = self.case_x * taille_sprite
        self.y = self.case_y * taille_sprite


    # Method that calculate a random pos to pop the item
    def randpos(self):
        count_max = 1
        count = 0

        # A loop to check of the position picked by random is a freespace
        while count < count_max:
            self.case_x = random.randint(0, 14)
            self.case_y = random.randint(0, 14)

            # If the sprite is a freespace
            if self.level.structure[self.case_y][self.case_x] == "0":

                # then change it to a mark where the program gonna pop the item.
                self.level.structure[self.case_y][self.case_x] = "o1"

                # And quit the loop
                count += 1
                break
        return self.case_x, self.case_y

    # Method that display the item on the map
    def display(self, Window):

        # Load the sprite
        c_potion = pygame.image.load("images/potion.png").convert()
        

        # Display the item on screen
        c_potion.set_colorkey((255,255,255))#Rend le blanc (valeur RGB : 255,255,255) de l'image transparent"
        Window.blit(c_potion, (self.x, self.y))
        # Refresh the window the display the background and the character
        pygame.display.flip()


# Class to create one of the items
class Key:
    def __init__(self, obj, level):
        self.obj = pygame.image.load(obj).convert_alpha
        self.level = level
        self.case_x, self.case_y = self.randpos()
        self.x = self.case_x * taille_sprite
        self.y = self.case_y * taille_sprite

    def randpos(self):
        count_max = 1
        count = 0
        while count < count_max:
            self.case_x = random.randint(0,14)
            self.case_y = random.randint(0,14)
            if self.level.structure[self.case_y][self.case_x] == '0':
                self.level.structure[self.case_y][self.case_x] = "o2"
                count += 1
                break
        return self.case_x, self.case_y

    def display(self, Window):
        c_key = pygame.image.load("images/key.png").convert()
        c_key.set_colorkey((255,255,255))#Rend le blanc (valeur RGB : 255,255,255) de l'image transparent"
        Window.blit(c_key, (self.x, self.y))
        


# Class to create one of the items
class Sword:
    def __init__(self, obj, level):
        self.obj = pygame.image.load(obj).convert_alpha
        self.level = level
        self.case_x, self.case_y = self.randpos()
        self.x = self.case_x * taille_sprite
        self.y = self.case_y * taille_sprite

    def randpos(self):
        count_max = 1
        count = 0
        while count < count_max:
            self.case_x = random.randint(0,14)
            self.case_y = random.randint(0,14)
            if self.level.structure[self.case_y][self.case_x] == '0':
                self.level.structure[self.case_y][self.case_x] = "o3"
                count += 1
                break
        return self.case_x, self.case_y

    def display(self, Window):
        c_sword = pygame.image.load("images/sword.png").convert()
        c_sword.set_colorkey((255,255,255))#Rend le blanc (valeur RGB : 255,255,255) de l'image transparent"        
        Window.blit(c_sword, (self.x, self.y))
        
