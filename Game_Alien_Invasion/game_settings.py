class Settings:
    """a class to store all initial settings of alien invasion game"""

    def __init__(self):
        """initialize the game's static settings"""
        self.screen_width =  1400
        self.screen_height = 1000
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed = 1.0
        self.ship_limit =  2

        # initial bullet settings
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 6

        # initial alien settingsfleet_direction
        self.alien_speed = 10.0
        self.fleet_drop_speed = 100

        # 1 represent moving right, -1 represent moving left
        self.fleet_direction = 1

        # how quickly the game speed up if a whole fleet was shot down
        self.speedup_scale = 1.5

        # how quickly the player get points for each alien shot down
        self.alien_point_scale = 3

        self.initialize_dynamic_settings()
    
    
    def initialize_dynamic_settings(self):
        """initialize the speed settings which will change throughout the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet direction
        self.fleet_direction = 1

        # score per shot down
        self.alien_point = 50

    def increase_speed(self):
        """increase speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_point = int(self.alien_point * self.alien_point_scale)
        #print(self.alien_point)
