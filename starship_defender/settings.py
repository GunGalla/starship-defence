"""Game settings."""


class Settings:
    """Here is all settings for Starship Defender"""

    def __init__(self):
        """Initializing game settings"""
        # Display settings
        self.screen_width = 1600
        self.screen_height = 900
        self.bg_color = (60, 60, 60)

        # Ship settings
        self.ship_speed = 1.75

        # Bullet settings
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 69, 0)
        self.bullets_allowed = 5
