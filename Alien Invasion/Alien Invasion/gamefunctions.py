import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_keydown_events(event,ai_settings,screen,ship,bullets,stats,sb,aliens):
 #Respond to keypresses.
 if event.key == pygame.K_RIGHT:
  ship.moving_right = True
 elif event.key == pygame.K_LEFT:
  ship.moving_left = True
 elif event.key==pygame.K_SPACE:
  fire_bullet(ai_settings,screen,ship,bullets)
 elif event.key==pygame.K_q:
  sys.exit()
 elif event.key==pygame.K_p and not stats.game_active:
  play_game(stats,sb,aliens,bullets,ai_settings,screen,ship)

def play_game(stats,sb,aliens,bullets,ai_settings,screen,ship):
    #hide mouse cursor
    pygame.mouse.set_visible(False)
    #reset game statistics
    stats.reset_stats()
    stats.game_active=True
    #reset scoreboard images
    sb.prep_score()
    sb.prep_high_score()
    sb.prep_level()
    sb.prep_ships()
    #Empty list of aliens and bullets
    aliens.empty()
    bullets.empty()
    #create a new fleet and center the ship
    create_fleet(ai_settings, screen,ship, aliens)
    ship.center_ship()

def fire_bullet(ai_settings,screen,ship,bullets):
  #fire bullets if limit not reached
  if len(bullets)<ai_settings.bullets_allowed:
    new_bullet=Bullet(ai_settings,screen,ship)
    bullets.add(new_bullet)

def check_keyup_events(event,ship):
 """Respond to key releases."""
 if event.key == pygame.K_RIGHT:
  ship.moving_right = False
 elif event.key == pygame.K_LEFT:
  ship.moving_left = False

def check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets):
 """Respond to keypresses and mouse events."""
 for event in pygame.event.get():
   if event.type == pygame.QUIT:
    sys.exit()
   elif event.type==pygame.KEYDOWN:
    check_keydown_events(event,ai_settings,screen,ship,bullets,stats,sb,aliens)
   elif event.type==pygame.KEYUP:
    check_keyup_events(event,ship)
   elif event.type==pygame.MOUSEBUTTONDOWN:
    mouse_x,mouse_y=pygame.mouse.get_pos()
    check_play_button(play_button,mouse_x,mouse_y,stats,ai_settings,sb,screen,ship,aliens,bullets)

def check_play_button(play_button,mouse_x,mouse_y,stats,ai_settings,sb,screen,ship,
aliens,bullets):
  #respond to mouse presses
  button_clicked=play_button.rect.collidepoint(mouse_x,mouse_y)
  if button_clicked and not stats.game_active:
    #reset game
    ai_settings.initialize_dynamic_settings()
    play_game(stats,sb,aliens,bullets,ai_settings,screen,ship)

def update_bullets(bullets,aliens,stats,ai_settings,sb,screen,ship):
  #update position of bullets and get rid of old bullets 
  #update bullet position
  bullets.update()
  #Get rid of bullets that have disappeared
  for bullet in bullets.copy():
   if bullet.rect.bottom<=0:
    bullets.remove(bullet)
  #check for bullets that hit an alien.If there are remove bullet and alien
  check_bullet_alien_collision(bullets,aliens,stats,ai_settings,sb,screen,ship)

def check_bullet_alien_collision(bullets,aliens,stats,ai_settings,sb,screen,ship):
  #respond to bullet alien collisions
  collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)
  start_new_level(aliens,bullets,ai_settings,screen,ship,stats,sb)
  if collisions:
    for aliens in collisions.values():
      stats.score+= ai_settings.alien_points*len(aliens)
      sb.prep_score()
    check_high_score(stats,sb)
    
def check_high_score(stats,sb):
  #Check to see if there's a new high score.
  if stats.score > stats.high_score:
    stats.high_score = stats.score
    sb.prep_high_score()


def start_new_level(aliens,bullets,ai_settings,screen,ship,stats,sb):
  if len(aliens) == 0:
    #destroy existing bullets and create new fleet
    #if the whole fleet is destroyed,start a new level
    bullets.empty()
    create_fleet(ai_settings,screen,ship,aliens)
    #increase level
    ai_settings.increase_speed()
    stats.level+=1
    sb.prep_level()

def get_number_aliens_x(ai_settings, alien_width):
 """Determine the number of aliens that fit in a row."""
 available_space_x = ai_settings.screen_width - 2 * alien_width
 number_aliens_x = int(available_space_x / (2 * alien_width))
 return number_aliens_x
 
def create_alien(ai_settings, screen, aliens, alien_number,row_number):
 """Create an alien and place it in the row."""
 alien = Alien(ai_settings, screen)
 alien_width = alien.rect.width
 alien.x = alien_width + 2 * alien_width * alien_number
 alien.rect.x = alien.x
 alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
 aliens.add(alien)
 
def create_fleet(ai_settings, screen,ship, aliens):
 """Create a full fleet of aliens."""
 # Create an alien and find the number of aliens in a row.
 alien = Alien(ai_settings, screen)
 number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
 number_rows = get_number_rows(ai_settings, ship.rect.height,
 alien.rect.height)
 # Create the fleet of aliens.
 for row_number in range(number_rows):
  for alien_number in range(number_aliens_x):
    create_alien(ai_settings, screen, aliens, alien_number,
      row_number)

 # Create the first row of aliens.
 for alien_number in range(number_aliens_x):
  create_alien(ai_settings, screen, aliens, alien_number,row_number)

def get_number_rows(ai_setting,ship_height,alien_height):
  """Determine the number of rows of aliens that fit on the screen."""
  available_space_y = (ai_setting.screen_height -
  (3 * alien_height) - ship_height)
  number_rows = int(available_space_y / (2 * alien_height))
  return number_rows

def check_fleet_edges(ai_settings,aliens):
  #respond appropiately if aliens have reached an edge 
  for alien in aliens.sprites():
    if alien.check_edges():
      change_fleet_direction(ai_settings,aliens)
      break

def change_fleet_direction(ai_settings, aliens):
 """Drop the entire fleet and change the fleet's direction."""
 for alien in aliens.sprites():
  alien.rect.y += ai_settings.fleet_drop_speed
 ai_settings.fleet_direction *= -1
 
def update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets):
  """
  Check if the fleet is at an edge,
  and then update the postions of all aliens in the fleet.
  """
  check_fleet_edges(ai_settings, aliens)
  aliens.update()
  #look for ship alien collisions
  if pygame.sprite.spritecollideany(ship,aliens):
    ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets)

  #look if aliens have reached the bottom of the screen
  check_aliens_bottom(ai_settings,screen,stats,sb, ship, aliens, bullets)


def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button):
 #Update images on the screen and flip to the new screen.
 # Redraw the screen during each pass through the loop.
 screen.fill(ai_settings.bg_color)
 ship.blitme()
 aliens.draw(screen)
 #Draw screen information
 sb.show_score()
 
 #Redraw all bullets behind ships and aliens
 for bullet in bullets.sprites():
  bullet.draw_bullet()

 #Draw play button if game is inactive
 if not stats.game_active:
  play_button.draw_button()
  # Make the most recently drawn screen visible.
 pygame.display.flip()

def ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets):
  #Respond to ship being hit by aliens
  if stats.ship_left>0:
    #decrements ships left
    stats.ship_left-=1
    #update scoreboard
    sb.prep_ships()
    #empty list of bullets and aliens
    aliens.empty()
    bullets.empty()
    #create a new fleet and center it to screen]
    create_fleet(ai_settings,screen,ship, aliens)
    ship.center_ship()
    #pause
    sleep(1)
  else:
    stats.game_active=False
    pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings,screen,stats,sb,ship,aliens,bullets):
  #check if any aliens have reached the bottom of the screen
  screen_rect=screen.get_rect()
  for alien in aliens.sprites():
    if alien.rect.bottom>=screen_rect.bottom:
      #treat this as if ship got hit,its gameover mehn
      ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets)
      break

