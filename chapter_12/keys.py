# Hector Delgado 5/28/2024

import sys
import pygame
from settings import Settings


class Keys:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Problem 12-5 - Keys")

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
            elif event.type == pygame.KEYDOWN:
                self._check_key_down_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_key_down_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            print(event.key)
        elif event.key == pygame.K_LEFT:
            print(event.key)
        elif event.key == pygame.K_UP:
            print(event.key)
        elif event.key == pygame.K_DOWN:
            print(event.key)
        elif event.key == pygame.K_q or pygame.K_ESCAPE:
            print(event.key)
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            pass
        elif event.key == pygame.K_LEFT:
            pass
        elif event.key == pygame.K_UP:
            pass
        elif event.key == pygame.K_DOWN:
            pass

    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = Keys()
    ai.run_game()
