class GameStats:
    """track the results and statistics of the game"""

    def __init__(self, new_game):
        """initial result and statistics"""
        self.settings = new_game.settings
        self.reset_stats()
        
        # set the game to de-active when the game begins
        self.game_active = False

        
    def reset_stats(self):
        """reset all result"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        