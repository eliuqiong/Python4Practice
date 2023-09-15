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
        self.game_level = 1
        # import history highest score from outside file
        with open("highest_score_ever.txt") as highest_score:
            self.highest_score = int(highest_score.read())
            highest_score.close()