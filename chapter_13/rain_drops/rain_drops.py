# Hector Delgado 6/7/2024

import sys
import pygame
from settings import Settings
from drop import Drop


class RainDrops:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Rain Drops")
        self.drops = pygame.sprite.Group()
        self._create_rain()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()  # check for player input
            self._update_drops()  # update the position of drops
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

    def _update_drops(self):
        """Update the positions of all drops."""
        self._rain_drop_direction()
        self.drops.update()

    def _rain_drop_direction(self):
        """Lower all drops on the screen."""
        for drop in self.drops.sprites():
            drop.rect.y += self.settings.rain_speed

    def _create_rain(self):
        """Create the fleet of drops."""
        # Create an drop and keep adding drops until there is no room left.
        # Spacing between drops is one drop width and one drop height.
        drop = Drop(self)
        drop_width, drop_height = drop.rect.size

        current_x, current_y = drop_width, drop_height
        while current_y < (self.settings.screen_height - 3*drop_height):
            while current_x < (self.settings.screen_width - 2*drop_width):
                self._create_drop(current_x, current_y)
                current_x += 2*drop_width

            # Finished a row; reset x value, and increment y value.
            current_x = drop_width
            current_y += 2*drop_height

    def _create_drop(self, x_position, y_position):
        """Create an drop and place it in the fleet."""
        new_drop = Drop(self)
        new_drop.x = x_position
        new_drop.rect.x = x_position
        new_drop.rect.y = y_position
        self.drops.add(new_drop)

    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.drops.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    rain_drops = RainDrops()
    rain_drops.run_game()
