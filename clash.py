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
     ac = [0,0]
     arrow = []
     btimer = 100
     btimer1 = 0
     enemy = [[640,100]]
     healthvalue = 194
     screen=pygame.display.set_mode((width, height))

     #load image
     player = pygame.image.load("images/pussy.png")
     grass = pygame.image.load("images/grass.png")
     castle = pygame.image.load("images/cheese.png")
     arrows = pygame.image.load("images/bullet2.png")
     enemyimg = pygame.image.load("images/rat.png")
     redbar = pygame.image.load("images/redbar.png")
     greenbar = pygame.image.load("images/greenbar.png")
     gameover = pygame.image.load("images/gameover3.png")
     win = pygame.image.load("images/youwin2.png")
     icon= pygame.image.load("images/icon.png")
     enemyimg1 = enemyimg

     #load audio
     hitsound = pygame.mixer.Sound("audio/explode.wav")
     enemysound = pygame.mixer.Sound("audio/enemy.wav")
     shootingsound = pygame.mixer.Sound("audio/shoot.wav")
     hitsound.set_volume(0.05)
     enemysound.set_volume(0.05)
     shootingsound.set_volume(0.05)
     pygame.mixer.music.load('audio/moonlight.wav')
     pygame.mixer.music.play(-1, 0.0)
     pygame.mixer.music.set_volume(0.25)

     pygame.display.set_caption("Clash ++")
     pygame.display.set_icon(icon)

     run = 1
     exitcode = 0
     while run:
         btimer -= 1
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

         #draw the bullet
         for bullet in arrow:
            index = 0
            velx = math.cos(bullet[0])* 10
            vely = math.sin(bullet[0])* 10
            bullet[1] += velx
            bullet[2] += vely
            if bullet[1]<-64 or bullet[1]>640 or bullet[2]<-64 or bullet[2]>480:
                arrow.pop(index)
            index += 1
            for project in arrow:
                arrow1 = pygame.transform.rotate(arrows, 360-project[0]* 57.29)
                screen.blit(arrow1, (project[1], project[2]))

         #draw enemy
         if btimer == 0:
            enemy.append([640, random.randint(50,430)])
            btimer = 100 -(btimer1 * 2)
            if btimer1 >= 35:
                btimer1 = 35
            else:
                btimer1 += 5
         index = 0
         for bad in enemy:
             if bad[0]<-64:
                 enemy.pop(index)
             bad[0] -= 7
             #attack the cheese
             badrect = pygame.Rect(enemyimg1.get_rect())
             badrect.top = bad[1]
             badrect.left = bad[0]
             if badrect.left<64:
                 hitsound.play()
                 healthvalue -= random.randint(5,20)
                 enemy.pop(index)
             #bullet and enemy collision
             index1 = 0
             for bullet in arrow:
                 bullrect = pygame.Rect(arrows.get_rect())
                 bullrect.left = bullet[1]
                 bullrect.top = bullet[2]
                 if badrect.colliderect(bullrect):
                     enemysound.play()
                     ac[0] += 1
                     enemy.pop(index)
                     arrow.pop(index1)
                 index1 += 1
             index += 1
         for bad in enemy:
             screen.blit(enemyimg1, bad)

         #HUD
         font = pygame.font.Font(None, 24)
         survivetxt = font.render(str((90000-pygame.time.get_ticks())/60000)+":"+str((90000-pygame.time.get_ticks())/1000%60).zfill(2), True, (0,0,0))
         txtRect = survivetxt.get_rect()
         txtRect.topright = [635, 5]
         screen.blit(survivetxt, txtRect)

         #bar
         screen.blit(redbar, (5,5))
         for health in range(healthvalue):
             screen.blit(greenbar, (health+8,8))
            
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
              if event.type == pygame.MOUSEBUTTONDOWN:
                  shootingsound.play()
                  pos = pygame.mouse.get_pos()
                  ac[1] += 1
                  arrow.append([math.atan2(pos[1]-(playerpos[1]+32),pos[0]-(playerpos1[0]+26)),playerpos1[0]+32, playerpos[1]+32])
        
         if keys[0]:
             playerpos[1]-=5
         elif keys[2]:
              playerpos[1]+=5
         if keys[1]:
             playerpos[0]-=5
         elif keys[3]:
          playerpos[0]+=5

         #check if win or lose
         if pygame.time.get_ticks() >= 90000:
            run = 0
            exitcode = 1
         if healthvalue <= 0:
             run = 0
             exitcode = 0
         if ac[1] != 0:
             accuracy = ac[0] * 1.0/ac[1] * 100
         else:
             accuracy = 0

     #win/lose display
     if exitcode == 0:
         pygame.font.init()
         font = pygame.font.Font(None, 24)
         txt = font.render("Accuracy: "+str(accuracy)+"%", True, (255,0,0))
         txtRect = txt.get_rect()
         txtRect.centerx = screen.get_rect().centerx
         txtRect.centery = screen.get_rect().centery+24
         screen.blit(gameover, (0,0))
         screen.blit(txt, txtRect)

     else:
         pygame.font.init()
         font = pygame.font.Font(None, 24)
         txt = font.render("Accuracy: "+str(accuracy)+"%", True, (0,255,0))
         txtRect = txt.get_rect()
         txtRect.centerx = screen.get_rect().centerx
         txtRect.centery = screen.get_rect().centery+24
         screen.blit(win, (0,0))
         screen.blit(txt, txtRect)

     while 1:
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 pygame.quit()
                 exit(0)

         pygame.display.flip()

if __name__ == "__main__":
    main()
