# a class that manages the raindrop
import pygame
from pygame.sprite import Sprite


class Raindrop(Sprite):
    def __init__(self,screen):
        super(). __init__()
        self.screen=screen
        #load image and get its rect
        self.image=pygame.image.load('images./raindrop.bmp')
        #get rect
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        #initialize start position
        self.rect.topright=self.screen_rect.topright
        #store raindrop exact value
        self.y=float(self.rect.y)
    
    def check_edge(self):
        #Returns true if raindrops hit the bottom of the screen
        screen_rect=self.screen.get_rect()
        if self.rect.top>screen_rect.bottom:
            return True
        else:
            return False

    def update(self):
        self.y+=1.5
        self.rect.y=self.y
        

   
        



