#manages all functions to stars.py
from star import Star
import pygame
from random import randint

def update_screen(bg_color,screen,stars):
    #redraw screen during each pass of the loop
    screen.fill(bg_color)
    stars.draw(screen)
    #make most recently drawn screen 
    pygame.display.flip()

def get_no_of_rows(star_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (700 )
    number_rows = int(available_space_y / (2 * star_height))
    return number_rows

def get_no_of_stars(star_width):
    #determines no os stars that fit in a row
    available_space_x=1200-2*star_width
    number_of_stars=int(available_space_x/(2*star_width))
    return number_of_stars

def create_star(screen,stars,star_number,row_number):
    #create a star and place it in a row
    star=Star(screen)
    star_width,star_height=star.rect.size
    star.x=star_width+2*star_width*star_number
    star.rect.x=star.x
    star.rect.y = star.rect.height + 2 * star.rect.height * row_number
    star.rect.x+=randint(-50,60)
    star.rect.y+=randint(-40,30)
    stars.add(star)

def create_constellation(stars,screen):
    #create a sky full of stars
    #create a star and find number of stars that can fit a row
    #spacing is equal to 1 star width
    star=Star(screen)
    number_of_stars=get_no_of_stars(star.rect.width)
    number_rows=get_no_of_rows(star.rect.height)

    for row_number in range(number_rows):
        #create first row of stars
        for star_number in range(number_of_stars):
            create_star(screen,stars,star_number,row_number)
       
