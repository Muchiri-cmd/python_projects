# A class repping the stars
import pygame
from pygame.sprite import Sprite
from random import randint

x=randint(-10,10)

class Star(Sprite):
 def __init__(self,screen):
    super(). __init__()
    self.screen=screen

    #initialize star and its starting position
    self.image=pygame.image.load('images/bstar2.bmp')
    self.rect=self.image.get_rect()
    self.screen_rect=self.screen.get_rect()

    #set star starting position
    self.rect.topleft=self.screen_rect.topleft
    #store star exact vertical position
    self.x=float(self.rect.x)

 def blitme(self):
    self.screen.blit(self.image,self.rect)

