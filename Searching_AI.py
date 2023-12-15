import pygame
import math as m
from sys import exit
import time
import A_star
from collections import namedtuple
Point = namedtuple('Point', 'x, y')




width = 800 #20
height = 600 #15
RED = 'red'
delay = 0.4
RED2 = (235, 73, 52)
BLOCK_SIZE = 20
MINI_BLOCK = 0.8 * BLOCK_SIZE
SIZE = ((int)(height/BLOCK_SIZE), (int)(width/BLOCK_SIZE))

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("A-star")



def goal_block(p,board):
   x = m.floor(p[0]/BLOCK_SIZE)
   y = m.floor(p[1]/BLOCK_SIZE)
   board[y][x] = 2
   pygame.draw.rect(screen,'green',pygame.Rect(2+(x*BLOCK_SIZE),2+(y*BLOCK_SIZE),MINI_BLOCK,MINI_BLOCK))
  
def block(p,board):
   x = m.floor(p[0]/BLOCK_SIZE)
   y = m.floor(p[1]/BLOCK_SIZE)
   board[y][x] = 1
   pygame.draw.rect(screen,'red',pygame.Rect(2+(x*BLOCK_SIZE),2+(y*BLOCK_SIZE),MINI_BLOCK,MINI_BLOCK))

def make_path(board,x,y):
   pygame.draw.rect(screen,'grey',pygame.Rect(2+(x*BLOCK_SIZE),2+(y*BLOCK_SIZE),MINI_BLOCK,MINI_BLOCK))

def update(board):
   pos = []
   goal_pos = []
   key_pressed = False
   start = False
   while(True):  
    for event in pygame.event.get():    
      if(event.type == pygame.QUIT):
        pygame.quit()
        exit()
      # if(event.type == pygame.MOUSEBUTTONDOWN):
      #   if(event.button == 1):
      #       pos.append(event.pos)

 # Check if the goal button (g) is pressed
      if event.type == pygame.KEYDOWN:
        if(event.key == pygame.K_g):
            if key_pressed==False:
              key_pressed = True
            else: key_pressed = False

      if(event.type == pygame.MOUSEBUTTONDOWN):
         if(event.button == 1 & key_pressed):
            goal_pos.append(event.pos)
         elif(event.type == pygame.MOUSEBUTTONDOWN):
           if(event.button == 1):
             pos.append(event.pos)


      if event.type == pygame.KEYDOWN:
        if(event.key == pygame.K_RETURN):
          start = True
      if(start):
         print("hehe booi")
         par,x = A_star.solve(board)
         end = Point(-1,-1)
         while(x!=end):
          make_path(board,x.y,x.x)
          x=par[x]
         start = False
      # if(event.type ==pygame.KEYDOWN):
      #    if(event.key == pygame.K_ESCAPE):
      #       esc = True
        
      #       screen.fill('black')
            


            
       
    for p in pos:
        block(p,board)
    if(len(goal_pos)!=0):
      goal_block(goal_pos[0],board)
    
    
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)


board = A_star.initialize()
update(board)
