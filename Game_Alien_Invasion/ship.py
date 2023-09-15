import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """a class to manage all the ship behavior"""

    def __init__(self, new_game):
        """initial the ship cofig and set its position to the center of bottom"""
        # heritage the class of sprite
        super().__init__()
        self.screen = new_game.screen
        self.screen_rect = new_game.screen.get_rect()
        self.settings = new_game.settings

        # load ship image and its rectagularnew_game.screen.get_rect()
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)
        
        # movement flag
        self.moving_right = False
        self.moving_left = False


    def blitme(self):
        """draw ship at designated location(mid-bottom)"""
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        """update the ship's postion basing on the movement flag"""
        # update the ship'x value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # update rect object from self.x
        self.rect.x = self.x

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)