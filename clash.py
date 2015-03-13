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
     keys = [False, False, False,False]
     playerpos=[100,100]
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
         pos = pygame.mouse.get_pos()
         angle = math.atan2(pos[1]-(playerpos[1]+32),pos[0]-(playerpos[0]+26))
         playerrot = pygame.transform.rotate(player, 360-angle*57.29)
         playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
         screen.blit(playerrot, playerpos1)
         #update screen
         pygame.display.flip()
         #loop
         for event in pygame.event.get(): 
              if event.type==pygame.QUIT:
                  pygame.quit()
              if event.type == pygame.KEYDOWN:
                 if event.key==K_w:
                     keys[0]=True
                 elif event.key==K_a:
                     keys[1]=True
                 elif event.key==K_s:
                     keys[2]=True
                 elif event.key==K_d:
                     keys[3]=True
              if event.type == pygame.KEYUP:
                  if event.key==pygame.K_w:
                      keys[0]=False
                  elif event.key==pygame.K_a:
                      keys[1]=False
                  elif event.key==pygame.K_s:
                      keys[2]=False
                  elif event.key==pygame.K_d:
                      keys[3]=False
         if keys[0]:
             playerpos[1]-=5
         elif keys[2]:
              playerpos[1]+=5
         if keys[1]:
             playerpos[0]-=5
         elif keys[3]:
          playerpos[0]+=5
             

if __name__ == "__main__":
    main()
