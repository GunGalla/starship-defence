"""Scoreboard implement module."""
import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard:
    """Class to set and show score. Also shows other information."""

    def __init__ (self, sd_game):
        """Initializing score calculating."""
        self.sd_game = sd_game
        self.screen = sd_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = sd_game.settings
        self.stats = sd_game.stats

        # Display score
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        # Prepare image scores
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Transfer current score to image."""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True,
                self.text_color, self.settings.bg_color)

        # Set score position in the right top of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Transfer current high score to image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                    self.text_color, self.settings.bg_color)

        # High score position
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        """Draw score on the screen. Also draw amount of ships left."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def check_high_score(self):
        """Renew high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        """Transfer current level to image."""
        level_str = f"Level: {str(self.stats.level)}"
        self.level_image = self.font.render(level_str, True,
                self.text_color, self.settings.bg_color)

        # Display level under current score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Indicates amount of ships left."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.sd_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
