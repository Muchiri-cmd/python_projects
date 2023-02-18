import pygame
from pygame.sprite import Sprite

# A class to manage tanks ammo
class Bullet(Sprite):
    def __init__(self,game_settings,screen,tank):
        #create a bullet object at tanks position
        super().__init__()
        self.screen=screen
        
         # Create a bullet rect at (0, 0) and then set correct position.
         #bullet width,bullet height
        self.rect = pygame.Rect(0,0,15,3)
        self.rect.midright= tank.rect.midright
 
        # Store the bullet's position as a decimal value.
        self.x = float(self.rect.x)
        self.color = (60,60,60)
        self.speed= game_settings.bullet_speed

    def update(self):
        #updates bullet trajectory across screen"""
        # Update the decimal position of the bullet.
        self.x += self.speed
        # Update the rect position.
        self.rect.x = self.x
    
    def draw_bullet(self):
        #show the bullet on screen
        pygame.draw.rect(self.screen, self.color, self.rect)




