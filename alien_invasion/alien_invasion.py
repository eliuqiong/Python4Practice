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
        pygame.display.set_caption("Game of 2023: Alien Invasion. Co-Authors: PAN & LIU")
        self.ship = Ship(self)

    
    def run_game(self):
        """start the game"""
        while True:
            # monitor the mourse and keyboard events, update screen
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """check and respond to mouse and keyboard events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit() 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move the ship to the right
                    self.ship.moving_right = True
                elif event
                    self.ship.rect.x =+ 1

    def _update_screen(self):
        """update images on the screen and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        
        # display the most recent screen settings
        pygame.display.flip()

if __name__ == "__main__":
    # make a game instance and run the game
    new_game = AlienInvasion()
    new_game.run_game()