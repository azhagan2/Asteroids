import pygame
from constants import *
from player import Player
from circleshape import CircleShape

def main():
    pygame.init()                           # Initialize the pygame module
    clock = pygame.time.Clock()             # Initialize the pygame.time.Clock 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Set the screen using the pygame.display.set_mode()


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)    # player object is created 
    dt = 0

    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  
                

        screen.fill("black")      # fill the screen with black
        
        for i in updatable:
            i.update(dt)       # will re-render players on each time frame 

        for i in drawable:
            i.draw(screen)     # will update when we press keys (w,s,a,d)

        pygame.display.flip()     # using flip method to refresh the screen

        dt = clock.tick(60) / 1000     # limit the framerate to 60 FPS


if __name__ == "__main__":
    main()