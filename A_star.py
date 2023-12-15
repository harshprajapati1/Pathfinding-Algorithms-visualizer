##############################################################

import math as m
from collections import namedtuple
# from Searching_AI import make_path
width = 800#20
height = 600 #15
BLOCK_SIZE = 20
SIZE = ((int)(height/BLOCK_SIZE), (int)(width/BLOCK_SIZE))
Point = namedtuple('Point', 'x, y')

def initialize(size = SIZE):
  board = []
  for i in range(size[0]):
    les = []
    for j in range(size[1]):
      les.append(0)  
    board.append(les) 
  return board


def h(board,x,y,goal):
     return m.sqrt((goal.x - x)**2 + (goal.y - y)**2)
  # h + g  = f 

def f(board,x,y,goal):
    return (m.sqrt((goal.x - x)**2 + (goal.y - y)**2) + (m.sqrt(x**2 + y**2)))

def key(s):
     return -s[1]
#sorting Fn
def isValid(board,x,y):
    valid = False
    if(x >= 0 and x < SIZE[0] and y >=0 and y < SIZE[1] and board[x][y] != 1):
        valid = True
    return valid

def A_star(board,curr,goal):
    openList = [(curr,0)]
    closedlist = []
    cnt = 0
    parent = {}
    parent[curr] = Point(-1,-1)
    while(len(openList)!=0 and cnt < 1000):  
        cnt+=1
        openList.sort(key=key)
#         print(openList)
        node = openList.pop()
        q = node[0]
        closedlist.append(q)
        if(q == goal):
            break
            
        childs = []
#         print(f"curr node is {q}")
    
        #generating all the childs

        if(isValid(board,q.x+1,q.y)):
            t=(Point(q.x+1,q.y),h(board,q.x+1,q.y,goal))
            if t[0] not in closedlist:
#                 print(f"1 inserted {t}")
                childs.append(t)
                parent[t[0]] = q
        if(isValid(board,q.x-1,q.y)):
            x=(Point(q.x-1,q.y),h(board,q.x-1,q.y,goal))
            if x[0] not in closedlist:
#                 print(f"2 inserted {x}")
                childs.append(x)
                parent[x[0]] = q
        if(isValid(board,q.x,q.y+1)):
            x=(Point(q.x,q.y+1),h(board,q.x,q.y+1,goal))
            if x[0] not in closedlist:
#                 print(f"3 inserted {x}")
                childs.append(x)
                parent[x[0]] = q

        if(isValid(board,q.x,q.y-1)):
            x=(Point(q.x,q.y - 1),h(board,q.x,q.y - 1,goal))
            if x[0] not in closedlist:
#                 print(f"4 inserted {x}")
                childs.append(x)
                parent[x[0]] = q
     
        if(isValid(board,q.x-1,q.y-1)):
            x=(Point(q.x-1,q.y - 1),h(board,q.x-1,q.y - 1,goal))
            if x[0] not in closedlist:
#                 print(f"5 inserted {x}")
                childs.append(x)
                parent[x[0]] = q

        if(isValid(board,q.x+1,q.y-1)):
            x=(Point(q.x+1,q.y - 1),h(board,q.x+1,q.y - 1,goal))
            if x[0] not in closedlist:
#                 print(f"6 inserted {x}")
                childs.append(x)
                parent[x[0]] = q

        if(isValid(board,q.x-1,q.y+1)):
            x = (Point(q.x-1,q.y + 1),h(board,q.x-1,q.y + 1,goal))
            if x[0] not in closedlist:
#                 print(f"7 inserted {x}")
                childs.append(x)
                parent[x[0]] = q

        if(isValid(board,q.x+1,q.y+1)):
            x = (Point(q.x+1,q.y + 1),h(board,q.x+1,q.y + 1,goal))
            if x[0] not in closedlist:
#                 print(f"8 inserted {x}")
                childs.append(x)
                parent[x[0]] = q

        openList+=childs
    return closedlist,parent


def solve(board):
  goal = Point(0,0)
  curr = Point(0,0)
  for i in range(len(board)):
     for j in range(len(board[0])):
        if(board[i][j] == 2):
           goal = Point(i,j)
  answer,par = A_star(board,curr,goal)
  for i in answer:
    board[i.x][i.y] = 8
  
  x = goal
  return par,x
  
  
   
##############################################################