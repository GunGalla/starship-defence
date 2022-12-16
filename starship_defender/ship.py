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

        # Moving trigger
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Renew ship position"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        """Draw current ship position"""
        self.screen.blit(self.image, self.rect)
