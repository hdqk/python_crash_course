# Hector Delgado 6/6/2024

import sys
import pygame
from settings import Settings
from star import Star


class StarGrid:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Star Grid")
        self.stars = pygame.sprite.Group()
        self._create_grid()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()  # check for player input
            self._update_screen()  # refresh screen
            self.clock.tick(60)  # sets refresh rate

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_key_down_events(event)

    def _check_key_down_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_q or pygame.K_ESCAPE:
            sys.exit()

    def _create_grid(self):
        """Create the fleet of stars."""
        # Create an star and keep adding stars until there is no room left.
        # Spacing between stars is half the star's width and height.
        star = Star(self)
        star_width, star_height = star.rect.size

        current_x, current_y = 0.5*star_width, 0.5*star_height
        while current_y < (self.settings.screen_height - star_height):
            while current_x < (self.settings.screen_width - star_width):
                self._create_star(current_x, current_y)
                current_x += 1.5*star_width

            # Finished a row; reset x value, and increment y value.
            current_x = 0.5*star_width
            current_y += 1.5*star_height

    def _create_star(self, x_position, y_position):
        """Create an star and place it in the fleet."""
        new_star = Star(self)
        new_star.x = x_position
        new_star.rect.x = x_position
        new_star.rect.y = y_position
        self.stars.add(new_star)

    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    star_game = StarGrid()
    star_game.run_game()
