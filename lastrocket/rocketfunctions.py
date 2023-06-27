import sys
import pygame

def check_keydown_events(event,rocket):
    """Responds to key presses"""
    if event.key==pygame.K_RIGHT:
        rocket.moving_right=True
    elif event.key==pygame.K_LEFT:
        rocket.moving_left=True
    elif event.key==pygame.K_UP:
        rocket.moving_up=True
    elif event.key==pygame.K_DOWN:
        rocket.moving_down=True


def check_keyup_events(event,rocket):
    """responds to key releases"""
    if event.key==pygame.K_RIGHT:
        rocket.moving_right=False
    elif event.key==pygame.K_LEFT:
        rocket.moving_left=False
    elif event.key==pygame.K_UP:
        rocket.moving_up=False
    elif event.key==pygame.K_DOWN:
        rocket.moving_down=False

        
    
def check_events(rocket):
    """Responds to key presses"""
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,rocket)
        
        elif event.type==pygame.KEYUP:
            check_keyup_events(event,rocket)

        
            
       

