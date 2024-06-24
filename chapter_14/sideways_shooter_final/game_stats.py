# Hector Delgado 6/24/2024

from pathlib import Path
import json


class GameStats:
    """Track statistics for Sideways Shooter."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        # High score should never be reset.
        self.high_score = self.load_game()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def load_game(self):
        """Loads the high score into memory when the game is launched."""
        path = Path('high_score.json')
        if path.exists():
            return json.loads(path.read_text())
        else:
            return 0
