# -*-coding:Latin-1 -*

"""Classes of the game: Mac Gyver escape"""

import pygame
from pygame.locals import *

from constantes import *
import random


class Level:
    """
        Class which initializes and displays the labyrinth on the screen
	"""
    def __init__(self, file):
        self.file = file # lvl.txt
        self.structure = []

    def gen(self):
        """Method for generate level with a file
		"""
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



    def show(self, window):
        """Method which shows the maze on the screen
		"""
        wall = pygame.image.load(IMAGE_WALL).convert()
        escape = pygame.image.load(IMAGE_ARRIVAL).convert()

        # Read the entire structure
        num_ligne = 0
        for line in self.structure:
            # Read every line
            num_case = 0
            for sprite in line:
                # Calculate the real position of the sprite
                x = num_case * SIZE_SPRITE
                y = num_ligne * SIZE_SPRITE
                if sprite == 'm':  # m = wall
                    window.blit(wall, (x, y))
                elif sprite == "a":  # a = Exit of the maze
                    window.blit(escape, (x, y))
                num_case += 1
            num_ligne += 1


class Perso:
    """Classe permettant de créer un personnage
	"""
    def __init__(self, right, left, up, down, level):
        # Sprites of the character
        self.right = pygame.image.load(right) .convert_alpha()
        self.left = pygame.image.load(left) .convert_alpha()
        self.up = pygame.image.load(up) .convert_alpha()
        self.down = pygame.image.load(down) .convert_alpha()
        # Position of the character in boxes and pixels
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        # Default direction
        self.direction = self.right
        # Level in which the character is
        self.level = level

    def deplacer(self, direction):
        """Methode permettant de déplacer le personnage
		"""

        # Move to the right
        if direction == 'right':
            # Not to exceed the screen
            if self.case_x < (NUMBER_SPRITE_COTE - 1):
                # We check that the destination sprite is not a wall
                if self.level.structure[self.case_y][self.case_x+1] != 'm':
                    # Moving a sprit
                    self.case_x += 1
                    # Calculation of the "real" position in pixels
                    self.x = self.case_x * SIZE_SPRITE
            # Image in the right direction
            self.direction = self.right

        # Moving to the left
        if direction == 'left':
            if self.case_x > 0:
                if self.level.structure[self.case_y][self.case_x-1] != 'm':
                    self.case_x -= 1
                    self.x = self.case_x * SIZE_SPRITE
            self.direction = self.left

        # Move up
        if direction == 'up':
            if self.case_y > 0:
                if self.level.structure[self.case_y-1][self.case_x] != 'm':
                    self.case_y -= 1
                    self.y = self.case_y * SIZE_SPRITE
            self.direction = self.up

        # Move down
        if direction == 'down':
            if self.case_y < (NUMBER_SPRITE_COTE - 1):
                if self.level.structure[self.case_y+1][self.case_x] != 'm':
                    self.case_y += 1
                    self.y = self.case_y * SIZE_SPRITE
            self.direction = self.down



class Potion:
    """ Class to create one of the items
    """
    def __init__(self, obj, level):

        # Load the sprite of the item
        self.obj = pygame.image.load(obj).convert_alpha

        # Initial settings for the item
        self.level = level
        self.case_x, self.case_y = self.randpos()
        self.x = self.case_x * SIZE_SPRITE
        self.y = self.case_y * SIZE_SPRITE


    def randpos(self):
        """ Method that calculate a random pos to pop the item
	    """
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


    def display(self, window):
        """ Method that display the item on the map
	    """
        # Load the sprite
        c_potion = pygame.image.load("images/potion.png").convert()


        # Display the item on screen
        c_potion.set_colorkey((255, 255, 255))# Makes the white of the image transparent"
        window.blit(c_potion, (self.x, self.y))
        # Refresh the window the display the background and the character
        pygame.display.flip()



class Key:
    """ Class to create one of the items
    """
    def __init__(self, obj, level):
        self.obj = pygame.image.load(obj).convert_alpha
        self.level = level
        self.case_x, self.case_y = self.randpos()
        self.x = self.case_x * SIZE_SPRITE
        self.y = self.case_y * SIZE_SPRITE

    def randpos(self):
        count_max = 1
        count = 0
        while count < count_max:
            self.case_x = random.randint(0, 14)
            self.case_y = random.randint(0, 14)
            if self.level.structure[self.case_y][self.case_x] == '0':
                self.level.structure[self.case_y][self.case_x] = "o2"
                count += 1
                break
        return self.case_x, self.case_y

    def display(self, window):
        c_key = pygame.image.load("images/key.png").convert()
        c_key.set_colorkey((255, 255, 255))
        window.blit(c_key, (self.x, self.y))



class Sword:
    """ Class to create one of the items
    """
    def __init__(self, obj, level):
        self.obj = pygame.image.load(obj).convert_alpha
        self.level = level
        self.case_x, self.case_y = self.randpos()
        self.x = self.case_x * SIZE_SPRITE
        self.y = self.case_y * SIZE_SPRITE

    def randpos(self):
        count_max = 1
        count = 0
        while count < count_max:
            self.case_x = random.randint(0, 14)
            self.case_y = random.randint(0, 14)
            if self.level.structure[self.case_y][self.case_x] == '0':
                self.level.structure[self.case_y][self.case_x] = "o3"
                count += 1
                break
        return self.case_x, self.case_y

    def display(self, window):
        c_sword = pygame.image.load("images/sword.png").convert()
        c_sword.set_colorkey((255, 255, 255))
        window.blit(c_sword, (self.x, self.y))
