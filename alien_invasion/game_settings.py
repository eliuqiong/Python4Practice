class Settings:
    """a class to store all initial settings of alien invasion game"""

    def __init__(self):
        """initialize the game's settings"""
        self.screen_width =  1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed = 1.0
        self.ship_limit =  2

        # initial bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 20

        # initial alien settingsfleet_direction
        self.alien_speed = 3.0
        self.fleet_drop_speed = 20

        # 1 represent moving right, -1 represent moving left
        self.fleet_direction = 1
