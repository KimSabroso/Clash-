#import all needed library
import random, sys, pygame, time, copy
from pygame.locals import *
import math
import random
import constants

#initialize the game
def main():
     pygame.init()
     width = 800
     height = 600
     screen=pygame.display.set_mode((width, height))

     #load image
     player = pygame.image.load("images/ccc.jpg")

     while 1:
         #clear screen fill
         screen.fill(0)

if __name__ == "__main__":
    main()
