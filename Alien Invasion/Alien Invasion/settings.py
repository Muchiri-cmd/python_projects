class Settings:
 """A class to store all settings for Alien Invasion."""
 def __init__(self):
  #Initialize the game's settings.
  # Screen settings
  self.screen_width = 1200
  self.screen_height = 700
  self.bg_color = (230, 230, 230)
  #ship settings
  self.ship_limit=3
  #bullet settings
  self.bullet_width=3
  self.bullet_height=15
  self.bullet_color=(60,60,60)
  self.bullets_allowed=3
  #Alien settings
  self.fleet_drop_speed=45
  #How quickly the game speeds up
  self.speedup_scale=1.1
  #How quickly alien point values increase
  self.score_scale = 1.5


  self.initialize_dynamic_settings()

 def initialize_dynamic_settings(self):
    #initialize dynamic settings that change throughout the game
    self.ship_speed_factor=1.5
    self.bullet_speed_factor=2
    self.alien_speed_factor = 0.75
    # fleet_direction of 1 represents right; -1 represents left.
    self.fleet_direction = 1
    #points for shooting down an alien
    self.alien_points=50
    

 def increase_speed(self):
    #increase speed settings
    self.ship_speed_factor*=self.speedup_scale
    self.bullet_speed_factor *= self.speedup_scale
    self.alien_speed_factor *= self.speedup_scale
    self.alien_points = int(self.alien_points * self.score_scale)
    
