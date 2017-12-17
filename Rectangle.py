#Rectangle

import pygame, sys, time
from pygame.locals import *
from Points import *

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
pygame.display.set_caption("Rectangle")

def RectangleSize(P1,P2):
    len_rect=abs(P2[0]-P1[0]) #x2-x1
    wid_rect=abs(P2[1]-P1[1]) #y2-y1
    Size=[len_rect,wid_rect]
    return Size

def Rectangle(P1,Size,delta_rect,z,filled):
    l=Size[0]-z*delta_rect[0] #new rectangle length
    w=Size[1]-z*delta_rect[1] #new rectangle width
    if filled:
        pygame.draw.rect(screen,GREEN,(P1[0],P1[1],l,w)) #(x1,y1,length,width)
    else:
        pygame.draw.rect(screen,GREEN,(P1[0],P1[1],l,w),1) #(x1,y1,length,width)
    New_Size=[l,w]
    return New_Size

if __name__=='__main__': #Main function

    #Focus creation
    zmax=50 #Max Depth
    F=[500,100,zmax] #Focus
    
    #Origin creation
    C=[500,550]

    #Initial depth
    z=0
    
    #Initial upper left rectangle coords
    A=[-200,100]
    P_1=PointfromOrigin(A,C)
    
    #Initial Lower right rectangle coords
    B=[200,-100]
    P_2=PointfromOrigin(B,C)

    #Rectangle length and width
    Size=RectangleSize(P_1,P_2)

    #Defining changing parameters
    delta=Delta(F,P_1,zmax)

    #Rectangle ratio
    delta_rect=Delta(P_1,P_2,zmax)

    #Choosing if the rectangle will be filled
    filled=0 #If yes: '1', if not '0'

    P1=P_1
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        if z<=zmax:
            PointDrawing(P1)
            #Rectangle drawing
            Rectangle(P1,Size,delta_rect,z,filled)

            z=z+1

            #Making the new corner of the new rectangle

            P1=PointWithDepth(P_1[0],P_1[1],z,F,delta)

        time.sleep(0.1)
        pygame.display.update() #The window is going to be updating
        screen.fill(BLACK)
