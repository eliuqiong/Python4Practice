import pygame.font

class Button:
    def __init__(self, new_game, msg):
        """initialize the button attributes"""
        self.screen = new_game.screen
        self.screen_rect = self.screen.get_rect()

        # set the default para of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #prep the message once
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """turn message into imgage to put it on top of the bottom"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_buttom(self):
        # draw blank button and put message image on top of it
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        