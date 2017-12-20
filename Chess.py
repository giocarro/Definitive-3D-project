import pygame, sys, time
from pygame.locals import *
from Points import *
from Rectangle import *
from Cube import *

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
pygame.display.set_caption("Chess")

if __name__=='__main__': #Main function
    zmax=25 #Max Depth

    #Focus creation
    F=[500,100,zmax] #Focus
    
    #Origin creation
    C=[500,600]

    #Initial depth
    z=8
    
    #Cube side
    l=100

    #Initial Point
    P_1=[-400,50]

    filled=0

    cube_init=1 #I am at initial position
    cube_init_pos=-3
    cube_pos=cube_init_pos
    cubes_row=8
    cube_final_pos=cube_init_pos + cubes_row
    Color=0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        if z>0:
            while cube_pos<cube_final_pos:
                All_Corners=Cube(P_1,C,F,zmax,z,l,filled,cube_init,cube_init_pos,cube_final_pos,cube_pos,Color)
                if Color==0:
                    Color=1
                else:
                    Color=0
                if cube_pos==cube_init_pos:
                    P1=All_Corners[0][0] #Cube front face Upper left corner
                    P2=All_Corners[0][3] #Cube front facel lower right corner
                    new_l=abs(All_Corners[0][0][0]-All_Corners[0][3][0]) #new length according front face size
                    cube_init=0 #I am not at initial position
                P_1=All_Corners[0][1]
                cube_pos=cube_pos+1

            if Color==0:
                Color=1
            else:
                Color=0
            z=z-1
            P_1=P1
            cube_pos=cube_init_pos
            l=new_l
        #cubes=-3
        
