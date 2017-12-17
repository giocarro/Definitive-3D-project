#Cube

import pygame, sys, time
from pygame.locals import *
from Points import *
from Rectangle import *

GREEN = (30,250,0)
BLACK = (0,0,0)
RED = (255,56,66)
SKY_BLUE = (204,255,229)
WHITE = (255,255,255)
PINK = (233,38,204)
BLUE = (38,44,233)
YELLOW = (250,255,88)
ORANGE = (255,205,0)
BROWN = (107,92,34)

def Cube_len(a):
    p=a/2
    return p

def CubeCorners(p):
    A1=[-p,p]
    P1=PointfromOrigin(A1,C)
    A2=[p,p]
    P2=PointfromOrigin(A2,C)
    A3=[-p,-p]
    P3=PointfromOrigin(A3,C)
    A4=[p,-p]
    P4=PointfromOrigin(A4,C)

    corners=[P1,P2,P3,P4] 
    return corners

if __name__=='__main__': #Main function
    #Focus creation
    zmax=10 #Max Depth
    F=[500,100,zmax] #Focus
    
    #Origin creation
    C=[500,600]

    #Initial depth
    z=0
    
    #Cube side
    a=100

    #Side/2
    p=Cube_len(a)

    #Cube corners
    Corners=CubeCorners(p)

    P_1=Corners[0]
    P1=P_1
    
    #Initial Point-Focus ratio
    delta=Delta(F,P_1,zmax)

    #Cube face ratio
    delta_rect=Delta(Corners[0],Corners[3],zmax)

    #Cube face size 
    Size=[a,a]

    Rectangle(P1,Size,delta_rect,z)

    z=z+1

    P1=PointWithDepth(P_1[0],P_1[1],z,F,delta)

    Rectangle(P1,Size,delta_rect,z)
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
