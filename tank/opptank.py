#A class to manage opp tanks
import pygame
from pygame.sprite import Sprite

class Opp(Sprite):
    def __init__(self,game_settings,screen):
        #initialize tank and its start position
        super().__init__()
        self.screen=screen
        self.game_settings=game_settings

        #load the opp tank image and its starting position
        self.image=pygame.image.load('images/R.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=self.screen.get_rect()
        
        #draw each tank at top right of screen
        self.rect.topright=self.screen_rect.topright
        
        #store opp tank exact position
        self.x=float(self.rect.x)

    def check_edges(self):
        #returns true if opp tanks hit screen edges 
        if self.rect.left<=0:
            return True

    def update(self):
        #move the opp tank foward
        self.x+=(self.game_settings.opp_speed_factor*
        self.game_settings.battalion_direction)
        self.rect.x=self.x

    def blitme(self):
        self.screen.blit(self.image,self.rect)
