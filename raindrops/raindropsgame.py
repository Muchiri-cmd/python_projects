import sys
import pygame
import rdfunctions as rd

def run_game():
    pygame.init()
    screen=pygame.display.set_mode((1200,700))
    pygame.display.set_caption("Raindrops")
    
    bg_color=(252,252,252)
    
    #create a shower of rain 
    raindrops=pygame.sprite.Group()
    
    #create a shower of raindrops
    rd.create_shower(screen,raindrops)
    
    #start main loop of the game
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        rd.update_drops(raindrops,screen,1)
        rd.update_screen(bg_color,screen,raindrops)
run_game()