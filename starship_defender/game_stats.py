"""Statistic module."""

class GameStats():
    """Starship defender statistic."""

    def __init__(self, sd_game):
        """Initialize statistics."""
        self.settings = sd_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Changing stat through the game."""
        self.ships_left = self.settings.ship_limit