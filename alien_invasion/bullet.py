import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """manage bullets fired from ship"""

    def __init__(self, new_game):
        """create a bullet object at the ship's current position"""
        super().__init__()
        self.screen = new_game.screen
        self.settings = new_game.settings
        self.color = self.settings.bullet_color

        # create a bullet and (0,0) and then to the middle
        self.rect = pygame.Rect(0,0,self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = new_game.ship.rect.midtop

        # store the bullet's position as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        """move the bullet up the screen"""
        # update the bullet position
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """draw the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)