#a class that deals with tank charactersistics and behaviour
import pygame

class Tank():
 def __init__(self,screen,game_settings):
    self.game_settings=game_settings
    self.screen=screen
    #initialize tank and its starting position
    self.image=pygame.image.load('images/tank1.bmp')
    self.rect=self.image.get_rect()#gets tank rect values
    self.screen_rect=screen.get_rect()#gets screen rect values

    #set tank start position at midleft center of screen
    self.rect.midleft=self.screen_rect.midleft

    #decimal value for tank center
    self.center=float(self.rect.centery)

    #movement flag
    self.moving_up=False
    self.moving_down=False

 def movement(self):
    #update tanks position based on movement flag
    if self.moving_up and self.rect.top>=0:
        self.center-=self.game_settings.speed_factor
    if self.moving_down and self.rect.bottom<=self.screen_rect.bottom:
        self.center+=self.game_settings.speed_factor

    #update rect object from self center
    self.rect.centery=self.center

 def center_tank(self):
      #center tank on screen
      self.center=self.screen_rect.centery

 def blitme(self):
    #draw tank image
    self.screen.blit(self.image,self.rect)


