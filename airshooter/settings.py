class Settings:
    """A class to store the games settings"""

    def __init__(self):
        """Game settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (135, 206, 235)
        
        # Player settings
        self.player_speed = 7
        self.player_lives = 3

        # Player bullet settings
        self.player_bullet_speed = 12
        self.player_bullet_color = (0, 0, 255)
        self.enemy_bullet_speed = 8
        self.enemy_bullet_color = (255, 0, 0)
        self.bullet_width = 15
        self.bullet_height = 3