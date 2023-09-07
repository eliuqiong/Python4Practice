class Settings:
    """save initial settings of alien invasion game"""

    def __init__(self):
        self.screen_width =  1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed = 1.5