"""Game's core engine"""
import sys

import pygame


class StarshipDefender:
    """General class to manage resources and game behavior."""

    def __init__(self):
        """Initializing the game and create game resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((1600, 900))
        pygame.display.set_caption("Starship Defender")

    def run_game(self):
        """Start the game"""
        while True:
            # Tracking mouse and keyboard events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                # display the last screen
                pygame.display.flip()


if __name__ == '__main__':
    # creating class object and game start
    sd = StarshipDefender()
    sd.run_game()
