import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    #A class to manage bullets fired from the ship

    def __init__(self,ai_settings,screen,ship):
        """create bullet at ships current position"""
        super(Bullet,self).__init__()
        self.screen=screen

        #create a  bullet rect at the ships current position 
        self.rect=pygame.Rect(0,0,ai_settings.bullet_width,
        ai_settings.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top

        #store ship bullet as a decimal value
        self.y=float(self.rect.y)

        self.color=ai_settings.bullet_color
        self.speed_factor=ai_settings.bullet_speed_factor

    def update(self):
        #manages bullet position on screen 
        self.y-=self.speed_factor
        #update the rect position 
        self.rect.y=self.y
    
    def draw_bullet(self):
        #Draw bullet to screen
        pygame.draw.rect(self.screen,self.color,self.rect)