import pygame.font

class Scoreboard:
    """report scoring information"""

    def __init__(self, new_game):
        """initialize scoreboard attributes"""
        self.screen = new_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = new_game.settings
        self.stats = new_game.stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # prepare initial score image
        self.update_highest_score()
        self.prep_score()
        self.prep_highest_score()
    
    def prep_score(self):
        """turn the score into a rendered image"""
        round_score = round(self.stats.score, -1)
        score_str = "Your score is: " + "{:,}".format(round_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # display the score at the top right
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right =self.screen_rect.right - 20
        self.score_rect.top = 20


    def prep_highest_score(self):
        """turn the score into a rendered image"""
        round_highest_score = round(self.highest_score, -1)
        highest_score_str = "Highest score: " + "{:,}".format(round_highest_score)
        self.highest_score_image = self.font.render(highest_score_str, True, self.text_color, self.settings.bg_color)

        # display the score at the center
        self.highest_score_rect = self.highest_score_image.get_rect()
        self.highest_score_rect.center =self.screen_rect.center
        self.highest_score_rect.top = 20

    
    def show_score(self):
        """draw both the current and highest score on the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.highest_score_image, self.highest_score_rect)


    def update_highest_score(self):
        self.highest_score = 0
        if self.stats.score > self.highest_score:
            self.highest_score = self.stats.score
            self.prep_highest_score()
