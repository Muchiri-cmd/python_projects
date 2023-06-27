#main file
import pygame #contains functionality needed to make a game
from tank import Tank
from settings import Settings
import functions as f
from stats import GameStats
  
def run_game():
    #initialize screen and game
    pygame.init()#background settings
    game_settings=Settings()
    screen=pygame.display.set_mode((1200,700))#creates a display windw called screen 
    pygame.display.set_caption("Wall Tank")
    #make a gamestats instance 
    statistics=GameStats(game_settings)
    #make a tank instance
    tank=Tank(screen,game_settings)
    #make a group to store bullets and opp tanks in
    bullets=pygame.sprite.Group() 
    opps=pygame.sprite.Group()
    #create a tank battalion
    f.create_battalion(game_settings,screen,tank,opps)

    #start main loop of the game
    while True:
        f.game_events(game_settings,screen,tank,bullets)
        if statistics.game_active:
            tank.movement()
            f.update_bullets(game_settings,screen,tank,bullets,opps)  
            f.update_opps(bullets,game_settings,statistics,screen,tank,opps)
        f.screen_update(screen,tank,opps,bullets)

run_game()
