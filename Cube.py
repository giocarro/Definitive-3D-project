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
pygame.display.set_caption("Cube")

def Cube(P_1,C,F,zmax,z,l,filled): #[Point,Origin,Focus,zmax,z,side_length_cube]

        #3D Point coords
        P1=PointfromOrigin(P_1,C)

        #Cube corners
        Corners=CubeCorners(P1,l)
        PointDrawing(Corners[0])
        PointDrawing(Corners[1])
        PointDrawing(Corners[2])
        PointDrawing(Corners[3])
    
        #Initial Point-Focus ratio
        delta=Delta(F,P1,zmax)

        #Cube face ratio
        delta_cube=Delta(Corners[0],Corners[3],zmax)

        #Cube face size 
        Size=[l,l]

        Rectangle(P1,Size,delta_cube,z,filled)

        print(P1)

        z=z+1

        New_P=PointWithDepth(P1[0],P1[1],z,F,delta)

        New_Face=Rectangle(New_P,Size,delta_cube,z,filled) #[Point,[length,width],[delta_x,delta_y,z=depth]]

        new_l=New_Face[0] #new length size

        New_Corners=CubeCorners(New_P,new_l) #new points P1,P2,P3,P4
        print 'New corners=',New_Corners
        PointDrawing(New_Corners[0])
        PointDrawing(New_Corners[1])
        PointDrawing(New_Corners[2])
        PointDrawing(New_Corners[3])

        FillingFaces(Corners,New_Corners)
    
        print(New_P)

def CubeCorners(P1,l):
    P2=[P1[0]+l,P1[1]]
    P3=[P1[0],P1[1]+l]
    P4=[P1[0]+l,P1[1]+l]
    corners=[P1,P2,P3,P4] 
    return corners

def FillingFaces(Corners,New_Corners):
    #Back Face
    BKF = pygame.draw.polygon(screen, WHITE, [[New_Corners[0][0],New_Corners[0][1]],[New_Corners[2][0],New_Corners[2][1]],[New_Corners[1][0],New_Corners[1][1]],[New_Corners[3][0],New_Corners[3][1]]],0)
    #Front Face
    #FRF = pygame.draw.polygon(screen, WHITE, [[v1_list[0][0],v1_list[0][1]],[v1_list[2][0],v1_list[2][1]],[v1_list[1][0],v1_list[1][1]],[v1_list[3][0],v1_list[3][1]]],0)
    #Upper Face
    #UPF = pygame.draw.polygon(screen, BLUE, [[v1_list[0][0],v1_list[0][1]],[v2_list[0][0],v2_list[0][1]],[v2_list[3][0],v2_list[3][1]],[v1_list[3][0],v1_list[3][1]]],0)
    #Lower Face
    #LOF = pygame.draw.polygon(screen, GREEN, [[v1_list[2][0],v1_list[2][1]],[v2_list[2][0],v2_list[2][1]],[v2_list[1][0],v2_list[1][1]],[v1_list[1][0],v1_list[1][1]]],0)
    #Right Side Face
    #RGT = pygame.draw.polygon(screen, PINK, [[v1_list[3][0],v1_list[3][1]],[v2_list[3][0],v2_list[3][1]],[v2_list[1][0],v2_list[1][1]],[v1_list[1][0],v1_list[1][1]]],0)
    #Left Side Face
    #LFT = pygame.draw.polygon(screen, YELLOW, [[v1_list[0][0],v1_list[0][1]],[v2_list[0][0],v2_list[0][1]],[v2_list[2][0],v2_list[2][1]],[v1_list[2][0],v1_list[2][1]]],0)

if __name__=='__main__': #Main function

    zmax=10 #Max Depth

    #Focus creation
    F=[500,100,zmax]
    
    #Origin creation
    C=[500,600]

    #Initial depth
    z=0

    #Side Length
    l=100

    #Initial Point
    P_1=[-l/2,l/2]

    #Filled
    filled=0

    Cube(P_1,C,F,zmax,z,l,filled)
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
