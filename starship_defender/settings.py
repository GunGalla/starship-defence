"""Game settings."""


class Settings:
    """Here is all settings for Starship Defender."""

    def __init__(self):
        """Initializing game settings."""
        # Display settings
        self.screen_width = 1600
        self.screen_height = 900
        self.bg_color = (60, 60, 60)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = (255, 69, 0)
        self.bullets_allowed = 5

        # Alien settings
        self.fleet_drop_speed = 15

        # Next level difficulty upgrade settings
        self.speedup_scale = 1.1
        self.bullet_size_scale = 1.15
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Set settings, which changes through game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 0.8
        self.bullet_width = 10

        # fleet_direction = 1 means move right, (-1) means left
        self.fleet_direction = 1

        # Score counting
        self.alien_points = 30

    def increase_speed(self):
        """Level up speed settings and bullet width."""
        speed_up = self.speedup_scale
        self.ship_speed_factor *= speed_up
        self.bullet_speed_factor *= speed_up
        self.alien_speed_factor *= speed_up
        self.bullet_width *= self.bullet_size_scale
        self.alien_points = int(self.alien_points * self.score_scale)


