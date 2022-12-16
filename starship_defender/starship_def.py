"""Game's core engine"""
import sys

import pygame

from settings import Settings
from ship import Ship


class StarshipDefender:
    """General class to manage resources and game behavior."""

    def __init__(self):
        """Initializing the game and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Starship Defender")

        self.ship = Ship(self)

    def run_game(self):
        """Start the game"""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        # Tracking mouse and keyboard events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.rect.x += 5
                elif event.key == pygame.K_LEFT:
                    self.ship.rect.x -= 5

    def _update_screen(self):
        # redraw display every iteration
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # display the last screen
        pygame.display.flip()


if __name__ == '__main__':
    # creating class object and game start
    sd = StarshipDefender()
    sd.run_game()
