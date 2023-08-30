import sys

import pygame

class AlienInvasion:
    """define the resource of the game"""

    def __init__(self):
        """initial setting of the game"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Best Game of the Year: Alien Invasion")

        # set background color
        self.bg_color = (230, 230, 230)

    
    def run_game(self):
        """start the game loop"""
        while True:
            # monitor the mourse and keyboard
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                # reset background every time
                self.screen.fill(self.bg_color)

                # display the most recent screen settings
                pygame.display.flip()


if __name__ == "__main__":
    # create the game and start to play
    new_game = AlienInvasion()
    new_game.run_game()