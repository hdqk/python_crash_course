# Hector Delgado 6/7/2024

import pygame
from pygame.sprite import Sprite


class Drop(Sprite):
    """A class to represent a single drop."""

    def __init__(self, steady_rain):
        """Initialize the drop and set its starting position."""
        super().__init__()
        self.screen = steady_rain.screen
        self.settings = steady_rain.settings

        # Load the drop image and set its rect attribute.
        self.image = pygame.image.load('images/rain_drop_0.png')
        self.rect = self.image.get_rect()

        # Start each new drop near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the drop's exact horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if drop is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.bottom >= screen_rect.bottom)