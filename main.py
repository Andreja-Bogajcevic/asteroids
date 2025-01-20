import pygame
from constants import *

def main():

    modules_succedded, modules_failed = pygame.init()
    if modules_failed > 0:
        raise Exception("modules failed to be initialized for pygame")
    
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(window, (0 ,0 ,0))
        pygame.display.flip()



if __name__ == "__main__":
    main()