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
            # Tracking mouse and keyboard events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # redraw display every iteration
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # display the last screen
            pygame.display.flip()


if __name__ == '__main__':
    # creating class object and game start
    sd = StarshipDefender()
    sd.run_game()
