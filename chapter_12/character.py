# Hector Delgado 5/24/2024

import pygame


class Character:
    """A class to manage the character."""

    def __init__(self, char):
        """Initialize the character and set its starting position."""
        self.screen = char.screen
        self.screen_rect = char.screen.get_rect()

        # Load the character image and get its rect.
        self.image = pygame.image.load('images/character.bmp')
        self.rect = self.image.get_rect()

        # Start each new character at the center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the character at its current location."""
        self.screen.blit(self.image, self.rect)
