"""Creates bullets for ship armory."""
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Ship's bullets control class."""

    def __init__(self, sd_game):
        """Create bullet object in current ship position."""
        super().__init__()
        self.screen = sd_game.screen
        self.settings = sd_game.settings
        self.color = self.settings.bullet_color

        # Creating a bullet in start position and correct position assignment
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = sd_game.ship.rect.midtop

        # Bullet coordinates
        self.y = float(self.rect.y)

    def update(self):
        """Imitates bullet moving."""
        # Renew bullet position in float type
        self.y -= self.settings.bullet_speed_factor
        # Renew bullet position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw a bullet on the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)


