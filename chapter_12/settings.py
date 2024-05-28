# Hector Delgado 5/28/2024

class Settings:
    """A class to store all setings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5
