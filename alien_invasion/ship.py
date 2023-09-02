import pygame

class Ship:
    """a class to manage all the ship behavior"""

    def __init__(self, new_game):
        """initial the ship cofig and set its position"""
        self.screen = new_game.screen
        self.screen_rect = new_game.screen.get_rect()

        # load ship image and its rectagular
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        
        # movement flag
        self.moving_right = False

    def blitme(self):
        """draw ship at designated location(mid-bottom)"""
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        """update the ship's postion basing on the movement flag"""
        if self.moving_right:
            self.rect.x += 1