# Hector Delgado 5/24/2024

import sys
import pygame
from character import Character


class CenterCharacter:
    """Draws the character at the center of the screen."""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Centered Character")
        self.char = Character(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""
        self.screen.fill((255, 255, 255))
        self.char.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    CenterCharacter().run_game()
