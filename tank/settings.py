#a class that manages all settings which modify the game 
class Settings():
 def __init__(self):
    #Tank speed settings
    self.speed_factor=1.5
    # Bullet settings
    self.bullet_speed = 1
    #opp tank speed
    self.opp_speed_factor=0.025
    #battalion direction
    self.battalion_direction=-1
    #tank settings
    self.tank_limit=3
    #bullets limit
    self.bullets_allowed=3
    
