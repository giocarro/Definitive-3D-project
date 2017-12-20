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

pygame.init() #obligatory
screen = pygame.display.set_mode((1000,700))
screen.fill(SKY_BLUE)
pygame.display.set_caption("Cube")

def Cube(P_1,C,F,zmax,z,l,filled,cube_init,cube_final,cube_pos,Color): #[Point,Origin,Focus,zmax,z,side_length_cube]

        #3D Point coords
        if cube_init==1:
            P1=PointfromOrigin(P_1,C)
        else:
            P1=P_1

        #Cube corners
        Corners=CubeCorners(P1,l)
    
        #Initial Point-Focus ratio
        delta=Delta(F,P1,zmax)

        #Cube face ratio
        delta_cube=Delta(Corners[0],Corners[3],zmax)

        #Cube face size 
        Size=[l,l]

        Rectangle(P1,Size,delta_cube,z,filled)

        z=z+1

        New_3D_P=PointWithDepth(P1[0],P1[1],z,F,delta)
        New_2D_P=[New_3D_P[0],New_3D_P[1]]
        New_Face=Rectangle(New_2D_P,Size,delta_cube,z,filled) #[Point,[length,width],[delta_x,delta_y,z=depth]]
        new_l=New_Face[0] #new length size

        New_Corners=CubeCorners(New_2D_P,new_l) #new points P1,P2,P3,P4
        FillingFaces(Corners,New_Corners,Color,cube_init,cube_final,cube_pos)
        All_Corners=[Corners,New_Corners]
        return All_Corners

def CubeCorners(P1,l):
    P2=[P1[0]+l,P1[1]]
    P3=[P1[0],P1[1]+l]
    P4=[P1[0]+l,P1[1]+l]
    corners=[P1,P2,P3,P4] 
    return corners

def FillingFaces(Corners,New_Corners,Color,cube_init,cube_final,cube_pos):
    #Thickness
    th=5
    #Back Face
    BKF = pygame.draw.polygon(screen, BROWN, [New_Corners[0],New_Corners[1],New_Corners[3],New_Corners[2]])    
    #Lower Face
    UPF = pygame.draw.polygon(screen, WHITE, [New_Corners[2],New_Corners[3],Corners[3],Corners[2]])    
    if cube_pos==cube_init:
        #Left Side Face
        LFT = pygame.draw.polygon(screen, BROWN, [New_Corners[0],New_Corners[2],Corners[2],Corners[0]])
    if cube_pos==cube_final:    
        #Right Side Face
        RGT = pygame.draw.polygon(screen, BROWN, [New_Corners[1],New_Corners[3],Corners[3],Corners[1]])
    #Upper Face
    pygame.draw.polygon(screen, BLACK, [New_Corners[0],New_Corners[1],Corners[1],Corners[0]],th)    
    if Color==0:
        UPF = pygame.draw.polygon(screen, WHITE, [New_Corners[0],New_Corners[1],Corners[1],Corners[0]])
    else:
        UPF = pygame.draw.polygon(screen, BLACK, [New_Corners[0],New_Corners[1],Corners[1],Corners[0]])            
    #Front Face
    FRF = pygame.draw.polygon(screen, BROWN, [Corners[0],Corners[1],Corners[3],Corners[2]])

if __name__=='__main__': #Main function

    zmax=4 #Max Depth

    #Focus creation
    F=[500,100,zmax]
    
    #Origin creation
    C=[500,400]

    #Initial depth
    z=0

    #Side Length
    l=200

    #Initial Point
    #P_1=[-l/2,l/2]
    P_1=[-100,50]

    #Filled
    filled=0

    #Initial cube
    cube_init=1

    #Final cube
    cube_final=1

    #Cube position
    cube_pos=1

    #Color Options
    Color=1 #0 White / 1 Black

    Cube(P_1,C,F,zmax,z,l,filled,cube_init,cube_final,cube_pos,Color)
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
