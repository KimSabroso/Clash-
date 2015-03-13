#import all needed library
import random, sys, pygame, time, copy
from pygame.locals import *
import math
import random


#initialize the game
def main():
     pygame.init()
     width = 800
     height = 600
     screen=pygame.display.set_mode((width, height))

     #load image
     player = pygame.image.load("images/ccc.jpg")
     grass = pygame.image.load("images/grass.png")
     castle = pygame.image.load("images/cheese.png")

     while 1:
         #clear screen fill
         screen.fill(0)
         #draw screen element
         for x in range (grass.get_width()+1):
            for y in range (grass.get_height()+1):
                screen.blit(grass,(x*100,y*100))
    
    
    
         screen.blit(castle,(0,30))
         screen.blit(castle,(0,135))
         screen.blit(castle,(0,240))
         screen.blit(castle,(0,345))
         screen.blit(player, (100,100))
         #update screen
         pygame.display.flip()
         #loop
         for event in pygame.event.get(): 
              if event.type==pygame.QUIT:
                  pygame.quit() 
                  exit(0) 

if __name__ == "__main__":
    main()
