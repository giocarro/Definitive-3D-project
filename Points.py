#Points

import pygame, sys, time
from pygame.locals import *

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

pygame.init() #obligatory
screen = pygame.display.set_mode((1000,700))
pygame.display.set_caption("Dots")

def PointfromOrigin(A,C):
    P=[C[0]+A[0],C[1]-A[1]]
    return P

#Changing coords parameters
def Delta(F,P,zmax):
    delta_x=abs(F[0]-P[0])/zmax
    delta_y=abs(F[1]-P[1])/zmax
    delta=[delta_x,delta_y]
    return delta

#Drawing of the initial points
def InitialDrawing(F,C):
    pygame.draw.circle(screen,ORANGE,[F[0],F[1]],3,0) #Drawing Focus
    pygame.draw.circle(screen,YELLOW,[C[0],C[1]],3,0) #Drawing Origin

def PointDrawing(P):
    pygame.draw.circle(screen,GREEN,[P[0],P[1]],3,0) #Drawing Initial Point

#2D point to 3D point
def PointWithDepth(x,y,z,F,delta):
    if x<F[0] and y>F[1]:
        x_n=x+z*delta[0]
        y_n=y-z*delta[1]
    elif x<F[0] and y<F[1]:
        x_n=x+z*delta[0]
        y_n=y+z*delta[1]
    elif x>F[0] and y>F[1]:
        x_n=x-z*delta[0]
        y_n=y-z*delta[1]
    elif x>F[0] and y<F[1]:
        x_n=x-z*delta[0]
        y_n=y+z*delta[1]

    P=[x_n,y_n,z]
    return P

if __name__=='__main__': #Main function

    #Focus creation
    zmax=50 #Max Depth
    F=[500,100,zmax] #Focus
    
    #Origin creation
    C=[500,600]

    #Initial depth
    z=0
    
    #Initial point coords
    A=[-200,100]
    
    P=PointfromOrigin(A,C)

    #Changing coords parameters
    delta=Delta(F,P,zmax)

    #Counter to stop iterations
    counter=0

    #Drawing of the initial points
    InitialDrawing(F,C)
    PointDrawing(P)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        time.sleep(0.1)
        if counter==0:
            P_n=PointWithDepth(P[0],P[1],z,F,delta) #[x,y,z,zmax,F,delta]
            pygame.display.update() #The window is going to be updating
            screen.fill(BLACK)
            InitialDrawing(F,C)
            PointDrawing(P_n)
            if P_n==F:
                counter=1
            print (P_n)
            z=z+1

