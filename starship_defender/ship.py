"""Ship control module."""
import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """Class to describe ship."""

    def __init__(self, sd_game):
        """Initializing the ship."""
        super().__init__()
        self.screen = sd_game.screen
        self.settings = sd_game.settings
        self.screen_rect = sd_game.screen.get_rect()

        # Uploading ship image
        self.image = pygame.image.load('images/starship.bmp')
        self.rect = self.image.get_rect()

        # Ship location on the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Ship coordinates
        self.x = float(self.rect.x)

        # Moving trigger
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Renew ship position."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed_factor

        self.rect.x = self.x

    def blitme(self):
        """Draw current ship position."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Set new ship in the midbottom of the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
