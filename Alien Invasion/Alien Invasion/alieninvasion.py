import pygame
from settings import Settings
from ship import Ship
import gamefunctions as gf
from pygame.sprite import Group
from gamestats import Gamestats
from button import Button
from scoreboard import Scoreboard

def run_game():
	# Initialize game and create a screen object.
	pygame.init()
	ai_settings=Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	#make the play button
	play_button=Button(screen,"Play")

	#create an instance to store game stats
	stats=Gamestats(ai_settings)
	#create an instance of scoreboard
	sb=Scoreboard(ai_settings,screen,stats)

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
		gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(bullets,aliens,stats,ai_settings,sb,screen,ship)
			gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
		
		#Make the most recently drawn screen available
		gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,
		play_button)

run_game()
