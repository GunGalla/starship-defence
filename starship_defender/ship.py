"""Ship control module"""
import pygame


class Ship:
    """Class to describe ship"""

    def __init__(self, sd_game):
        """Initializing the ship"""
        self.screen = sd_game.screen
        self.screen_rect = sd_game.screen.get_rect()

        # Uploading ship image
        self.image = pygame.image.load('images/starship.bmp')
        self.rect = self.image.get_rect()
        # New ship appears at the middle bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw current ship position"""
        self.screen.blit(self.image, self.rect)
