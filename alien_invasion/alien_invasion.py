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

	# set the initial screen to full screen and then get the width and height
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
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
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        """respons to key press down"""
        if event.key == pygame.K_RIGHT:
            # set the moving status to True
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # set the moving status and stop to move
           self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self,event):
        """respons to key press up"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
           self.ship.moving_left = False


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
