"""Alien control module."""
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Alien creation class."""

    def __init__(self, sd_game):
        """Initialize alien and gave him a position."""
        super().__init__()
        self.screen = sd_game.screen
        self.settings = sd_game.settings

        # Alien image load and set rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Alien start position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Alien float type coordinates
        self.x = float(self.rect.x)

    def check_edges(self):
        """Check if alien reach the edge of the screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move aliens to the right and to the left."""
        self.x += (self.settings.alien_speed_factor *
                   self.settings.fleet_direction)
        self.rect.x = self.x
