# Hector Delgado 6/7/2024

class Settings:
    """A class to store all settings for Steady Rain."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (230, 230, 230)

        # drop settings
        self.rain_speed = 1
        self.drop_limit = 120
