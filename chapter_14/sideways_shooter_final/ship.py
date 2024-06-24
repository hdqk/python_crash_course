# Hector Delgado 6/24/2024

import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image, rotate, and get its rect.
        image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.rotate(image, 270)
        self.rect = self.image.get_rect()

        # Start each new ship at the left of the screen.
        self.rect.left = self.screen_rect.left

        # Store a float for the ship's exact vertical position.
        self.y = float(self.rect.y)

        # Movement flag; start with a ship that's not moving.
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's y values, not the rect.
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed

        # Update rect object from self.y
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.left = self.screen_rect.left
        self.y = float(self.rect.y)
