#main file

import pygame
from rocket import Rocket
import rocketfunctions as rf

#create a pygame window that responds to user input
def run_game():
    #initialize game and create screen object
    pygame.init() #initializes screen
    screen=pygame.display.set_mode((1200,700)) #set screen/surface dimensions 
    pygame.display.set_caption("The last rocket")
    #set background color
    bg_color=(0,0,0)


    #make rocket
    rocket=Rocket(screen)

    #start main loop for the game 
    while True:
        rf.check_events(rocket)
        screen.fill(bg_color)
        rocket.blitme()

        #make most recently drawn screen visible
        pygame.display.flip()
        rocket.update()
       
run_game()
