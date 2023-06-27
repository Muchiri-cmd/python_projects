class Gamestats():
    #track stats for alien invasion

    def __init__(self,ai_settings):
        #initialize statistics
        self.ai_settings=ai_settings
        self.reset_stats()
        #start alien invasion in an active state
        self.game_active=False
        #High score should never be reset
        self.high_score=0
        #set level to start
        self.level=1
        
        
    def reset_stats(self):
        #initailize stats that can change during the game
        self.ship_left=self.ai_settings.ship_limit
        self.score=0

