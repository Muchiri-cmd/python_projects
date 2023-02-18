# A file that deals with functions and fuctionality of game
import sys
import pygame
from Ammo import Bullet
from opptank import Opp
from time import sleep

def game_events(game_settings,screen,tank,bullets):
    #checks game events and executes
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
          keydown_events(event,game_settings,screen,tank,bullets)
        elif event.type==pygame.KEYUP:
          keyup_events(tank,event)

def keydown_events(event,game_settings,screen,tank,bullets):
    #responds to key presses
    if event.key==pygame.K_UP:
        tank.moving_up=True
    elif event.key==pygame.K_DOWN:
        tank.moving_down=True
    elif event.key==pygame.K_SPACE:
        # Create a new bullet and add it to the bullets group.
        new_bullet=Bullet(game_settings,screen,tank)
        bullets.add(new_bullet)
   
    elif event.key==pygame.K_q:
        sys.exit()

def keyup_events(tank,event):
    #responds to key releases 
    if event.key==pygame.K_UP:
        tank.moving_up=False
    elif event.key==pygame.K_DOWN:
        tank.moving_down=False

def get_number_rows(tank_width,opp_width,):
    #determine no of opp rows on the screen
    available_space=(1200-(2*opp_width)-tank_width)
    number_rows=int(available_space/(2*opp_width))
    return number_rows

def get_number_of_tanks(opp_height):
        """determines how many tanks fit a column and to leave
        a margin 0.5 opp tank height""" 
        available_space_y = 700- (1* opp_height)
        number_of_opps= int(available_space_y / (1.5* opp_height))
        return number_of_opps

def create_opp(game_settings, screen, opps, opp_number,row_number):
    """Create an opp tank and place it in the column."""
    opp= Opp(game_settings, screen)
    opp_height = opp.rect.height
    """each tank is pushed down one tank height and we multiply by 1.5
    to account for space taken up by half of each tank"""
    opp.y = opp_height + 1.5* opp_height * opp_number
    opp.rect.y = opp.y
    """each tank is pushed 1 tank width from the next and we multiply by 2 
    to account for space taken by each including spacing"""
    opp.x=opp.rect.width*5+ 2 * opp.rect.width * row_number
    opp.rect.x=opp.x
    opps.add(opp)

def create_battalion(game_settings, screen,tank,opps):
    """Create a battalion of opptanks"""
    #margin from top screen and bottom screen is equal to 1 tank width
    # Spacing between each tank is equal to tank height.
    opp= Opp(game_settings, screen)
    number_of_opps=get_number_of_tanks(opp.rect.height)
    number_rows = get_number_rows(tank.rect.width,
    opp.rect.width)
    #create battalion of tanks
    for row_number in range(number_rows):
        # Create the first row of tanks
        for opp_number in range(number_of_opps):
            # Create a tank  and place it in the column and rows .
            create_opp(game_settings,screen,opps,opp_number,row_number)
      
def check_batallion_edges(game_settings,opps,
    screen,statistics,tank,bullets):
    #Respond when a battalion row reaches end by adding new row of tanks
    for opp in opps.sprites():
        if opp.check_edges():
            opps.remove(opp)
            tank_hit(game_settings,statistics,screen,tank,opps,bullets)
            break

def update_opps(bullets,game_settings,statistics,screen,tank,opps):
    #updates position of all opp tanks in the battalion
    check_batallion_edges(game_settings,opps,screen,
    statistics,tank,bullets)
    opps.update()
    #look for opp,tank collisions
    if pygame.sprite.spritecollideany(tank,opps):
        tank_hit(game_settings,statistics,screen,tank,opps,bullets)
    
def update_bullets(game_settings,screen,tank,bullets,opps):
    #update bullet position
    bullets.update()
    #delete old bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullet.remove(bullet)
    #update bullets position and rids old ones
    """check if bullet has hit opp tank and get rid of it if so"""
    collisions=pygame.sprite.groupcollide(bullets,opps,True,True)
    if len(opps)==0:
        #destroy exisiting bullet,create new batllion
        bullets.empty()
        create_battalion(game_settings,screen,tank,opps)

def tank_hit(game_settings,statistics,screen,tank,opps,bullets):
    #Respond to tank being hit by opp.
    #Decrement tank_left.
    if statistics.tank_left>0:
        statistics.tank_left -= 1
 
        # Empty the list of tanks and bullets.
        opps.empty()
        bullets.empty()
        # Create a new batallion and center the tank.
        create_battalion(game_settings, screen,tank,opps)
        tank.center_tank()
        # Pause.
        sleep(0.5)
    else:
        statistics.game_active=False

def screen_update(screen,tank,opps,bullets):
    #redraws screen on each pass of loop
    bg_color=(252,252,252)
    screen.fill(bg_color)
    tank.blitme()
    opps.draw(screen)
    #redraw all bullets 
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    #display the last image on screen
    pygame.display.flip()
