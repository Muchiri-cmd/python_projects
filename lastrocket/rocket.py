#manages most behaviours of the rocket
import pygame 

class Rocket():
    def __init__(self,screen):
        #initialize screen and set starting position
        self.screen=screen
        #load rocket image and get its starting position
        self.image=pygame.image.load('images/amongus.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        #set starting position for each ship
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        

        #movement flag
        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False

    def update(self):
        """update rockets movement according to movement flag"""
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.rect.centerx+=1
        if self.moving_left and self.rect.left>0:
            self.rect.centerx-=1
        if self.moving_up and self.rect.top>0:
            self.rect.centery-=1
        if self.moving_down and self.rect.bottom<self.screen_rect.bottom:
            self.rect.centery+=1



        #draw rocket according to its position
    def blitme(self):
        self.screen.blit(self.image,self.rect)