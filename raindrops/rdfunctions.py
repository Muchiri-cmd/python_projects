#Manages all game functionalites
import pygame
from raindrop import Raindrop

def get_number_rows(raindrop_height):
        """Determine the number of rows of raindrops that fit on the screen."""
        available_space_y = (700-(2*raindrop_height))
        number_rows = int(available_space_y / (2 * raindrop_height))
        return number_rows

def get_number_raindrops(raindrop_width):
        #get the number of raindrops that fit on a row
        available_space_x=1200-(raindrop_width*2)
        number_raindrops_x=int(available_space_x/(2*raindrop_width))
        return number_raindrops_x

def create_raindrop(screen,raindrops,raindrop_number,row_number):
        raindrop=Raindrop(screen)
        raindrop_width,raindrop_height=raindrop.rect.size
        raindrop.x=raindrop_width+2*raindrop_width*raindrop_number
        raindrop.rect.x=raindrop.x
        raindrop.y=raindrop.rect.height + 2*raindrop.rect.height *row_number
        raindrop.rect.y=raindrop.y
        raindrops.add(raindrop)

def create_shower(screen,raindrops):
        raindrop=Raindrop(screen)
        #find number of raindrops that can fit a row
        number_raindrops_x=get_number_raindrops(raindrop.rect.width)
        number_rows=get_number_rows(raindrop.rect.height)
        
        #draw first row 
        for row_number in range(number_rows):
         for raindrop_number in range(number_raindrops_x):
            #create first row and add to screen showers 
            create_raindrop(screen,raindrops,raindrop_number,row_number)

def update_screen(bg_color,screen,raindrops):
        screen.fill(bg_color)
        raindrops.draw(screen)
        #draw scrren on each pass of the loop
        pygame.display.flip()

def check_row_edges(raindrops,screen,row_number):
        for raindrop in raindrops.sprites():
                if raindrop.check_edge():
                        raindrops.remove(raindrop)
                        make_new_row(raindrop,screen,raindrops,row_number)
                        break

def make_new_row(raindrop,screen,raindrops,row_number):
        number_raindrops_x=get_number_raindrops(raindrop.rect.width)
        for raindrop_number in  range(number_raindrops_x):
                create_raindrop(screen,raindrops,raindrop_number,row_number)

def update_drops(raindrops,screen,row_number):
        check_row_edges(raindrops,screen,row_number)
        raindrops.update()

