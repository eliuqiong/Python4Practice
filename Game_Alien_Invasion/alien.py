import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """a class to manage alien behaviors"""

    def __init__(self,new_game):
        """initial the alien config """
        # import from Sprite class
        super().__init__()
        # config position from game config
        self.settings = new_game.settings
        self.screen = new_game.screen
        self.screen_rect = new_game.screen.get_rect()

        # load alien image and its rect
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # set new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # set the x y into fxloat number to calculate
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """move the alien to the right"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
        
    
    def check_edges(self):
        """return true if alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
    