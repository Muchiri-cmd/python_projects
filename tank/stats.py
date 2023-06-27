class GameStats():
 #Track statistics for Wall Tank
 
 def __init__(self, game_settings):
    # Start game in an active state.
    self.game_active = True

    
    #Initialize statistics.
    self.game_settings = game_settings
    self.reset_stats()
 
 def reset_stats(self):
    #Initialize statistics that can change during the game.
    self.tank_left = self.game_settings.tank_limit