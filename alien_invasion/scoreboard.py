import pygame.font
from pygame.sprite import Group

from ship import Ship
    

class Scoreboard:
    """report scoring information"""

    def __init__(self, new_game):
        """initialize scoreboard attributes"""
        self.new_game = new_game
        self.screen = new_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = new_game.settings
        self.stats = new_game.stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # prepare initial scores, game level and ships left
        self.update_highest_score()
        self.prep_score()
        self.prep_highest_score()
        self.prep_game_level()
        self.prep_ships_left()


    def prep_ships_left(self):
        """update how many ships are left while playing"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.new_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)


    def prep_game_level(self):
        """turn game levl information into a rendered image"""
        game_level_str = "Game Level: " + str(self.stats.game_level)
        self.game_level_image = self.font.render(game_level_str, True, self.text_color, self.settings.bg_color)

        # display the score at the top right
        self.game_level_rect = self.game_level_image.get_rect()
        self.game_level_rect.right =self.score_rect.right
        self.game_level_rect.top = 60        
    
    def prep_score(self):
        """turn the score into a rendered image"game_level"""
        round_score = round(self.stats.score, -1)
        score_str = "Your score: " + "{:,}".format(round_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # display the score at the top right
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right =self.screen_rect.right - 20
        self.score_rect.top = 20


    def prep_highest_score(self):
        """turn the score into a rendered image"""
        self.round_highest_score = round(self.stats.highest_score, -1)
        highest_score_str = "Highest score: " + "{:,}".format(self.round_highest_score)
        self.highest_score_image = self.font.render(highest_score_str, True, self.text_color, self.settings.bg_color)

        # display the score at the center
        self.highest_score_rect = self.highest_score_image.get_rect()
        self.highest_score_rect.center =self.screen_rect.center
        self.highest_score_rect.top = 20

    
    def show_score(self):
        """draw both the current and highest score on the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.highest_score_image, self.highest_score_rect)
        self.screen.blit(self.game_level_image, self.game_level_rect)
        self.ships.draw(self.screen)


    def update_highest_score(self):
        if self.stats.score > self.stats.highest_score:
            self.stats.highest_score = self.stats.score
            self.prep_highest_score()
