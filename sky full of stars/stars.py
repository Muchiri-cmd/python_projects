#main file
import pygame 
import sys
import starfunctions as sf

def run_game():
    #initialize game and screen
    pygame.init()
    screen=pygame.display.set_mode((1200,700))
    pygame.display.set_caption("stars align")
    
   #set background color 
    #Black,default is fine (haha),anyways
    bg_color=(0,0,0)
    
    #make a group of stars
    stars=pygame.sprite.Group()
    #create a constellation of stars
    sf.create_constellation(stars,screen)
    
    #start the main loop of the game
    while True:
        #watch for any events 
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()

        sf.update_screen(bg_color,screen,stars)

run_game()

