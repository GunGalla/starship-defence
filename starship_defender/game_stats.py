"""Statistic module."""

class GameStats:
    """Starship defender statistic."""

    def __init__(self, sd_game):
        """Initialize statistics."""
        self.settings = sd_game.settings
        self.reset_stats()

        # Game starts inactive
        self.game_active = False

        # High score!
        self.high_score = 0

    def reset_stats(self):
        """Changing stat through the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0