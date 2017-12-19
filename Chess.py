import pygame, sys, time
from pygame.locals import *
from Points import *
from Rectangle import *
#from Cube import *

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
pygame.display.set_caption("Chess")

if __name__=='__main__': #Main function
    #Focus creation
    zmax=10 #Max Depth
    F=[500,100,zmax] #Focus
    
    #Origin creation
    C=[500,600]

    #Initial depth
    z=0
    
    #Cube side
    l=100

    #Initial Point
    P_1=[-l/2,l/2]

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
