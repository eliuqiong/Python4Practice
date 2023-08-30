import pygame

class Ship:
    """alien ship related definition"""

    def __init__(self, new_game):
        """initial the ship cofigration"""
        self.screen = new_game.screen
        self.screen_rect = new_game.screen.get_rect()

        # load ship image and its rectagular
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # place every new ship at the center of the screen bottom
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """place ship at designated location"""
        self.screen.blit(self.image, self.rect)
    