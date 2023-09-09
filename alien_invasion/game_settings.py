class Settings:
    """a class to store all initial settings of alien invasion game"""

    def __init__(self):
        """initialize the game's settings"""
        self.screen_width =  1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        self.ship_speed = 1.0

        # initial bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 6

        # initial alien settingsfleet_direction
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10

        # 1 represent moving right, -1 represent moving left
        self.fleet_direction = 1
