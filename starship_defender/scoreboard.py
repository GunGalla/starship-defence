"""Scoreboard implement module."""
import pygame.font

class Scoreboard:
    """Class to set and show score. Also shows other information."""

    def __init__ (self, sd_game):
        """Initializing score calculating."""
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
        """Draw score on the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

    def check_high_score(self):
        """Renew high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
