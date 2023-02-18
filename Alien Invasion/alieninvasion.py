import pygame
from settings import Settings
from ship import Ship
import gamefunctions as gf
from pygame.sprite import Group
from gamestats import Gamestats

def run_game():
	# Initialize game and create a screen object.
	pygame.init()
	ai_settings=Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	#create an instance to store game stats
	stats=Gamestats(ai_settings)

	#make a ship
	ship=Ship(ai_settings,screen)
	
	#make a group to store bullets  and another aliens
	bullets=Group()
	aliens=Group()
	
	#create a fleet of aliens
	gf.create_fleet(ai_settings,screen,ship,aliens)

	#start the main loop for the game.
	while True:
		# Watch for keyboard and mouse events.
		gf.check_events(ai_settings,screen,ship,bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings,screen,ship,bullets,aliens)
			gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
		
		#Make the most recently drawn screen available
		gf.update_screen(ai_settings,screen,ship,aliens,bullets)

run_game()
