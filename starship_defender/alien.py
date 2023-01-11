"""Alien control module."""
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Alien creation class."""

    def __init__(self, sd_game):
        """Initialize alien and gave him a position."""
        super().__init__()
        self.screen = sd_game.screen

        # Alien image load and set rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Alien start position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Alien float type coordinates
        self.x = float(self.rect.x)