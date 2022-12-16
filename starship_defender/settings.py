"""Game settings."""


class Settings:
    """Here is all settings for Starship Defender"""

    def __init__(self):
        """Initializing game settings"""
        # Display settings
        self.screen_width = 1600
        self.screen_height = 900
        self.bg_color = (59, 68, 75)

        # Ship settings
        self.ship_speed = 1.75
