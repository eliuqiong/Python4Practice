import sys

import pygame

from game_settings import Settings
from ship import Ship

class AlienInvasion:
    """define the resource of the game"""

    def __init__(self):
        """initial setting of the game"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Best Game of the Year: Alien Invasion. Author: PAN & LIU")
        self.ship = Ship(self)

    
    def run_game(self):
        """start the game loop"""
        while True:
            # monitor the mourse and keyboard
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit() 

                # set background color
                self.bg_color = (230, 230, 230)
                    
                # reset background every time
                self.screen.fill(self.settings.bg_color)
                self.ship.blitme()

                # display the most recent screen settings
                pygame.display.flip()


if __name__ == "__main__":
    # create the game and start to play
    new_game = AlienInvasion()
    new_game.run_game()