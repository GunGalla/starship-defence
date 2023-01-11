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
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """Checking any events through game."""
        # Tracking mouse and keyboard events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Check if any key pressed."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

    def _check_keyup_events(self, event):
        """Check any key released."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """Renew screen to show changes."""
        # redraw display every iteration
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # display the last screen
        pygame.display.flip()


if __name__ == '__main__':
    # creating class object and game start
    sd = StarshipDefender()
    sd.run_game()