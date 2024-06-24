# Hector Delgado 6/17/2024

import sys
import pygame
from time import sleep
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button


class TargetPractice:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Problem 14-2 - Target Practice")
        # Create an instance to store game statistics.
        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_target()
        # Start Target Practice in an inactive state.
        self.game_active = False
        # Make the Play button.
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()  # check for player input

            if self.game_active:
                self.ship.update()  # update position of the ship
                self._update_bullets()  # update position of bullets
                self._update_target()  # update the position of target

            self._update_screen()  # refresh screen
            self.clock.tick(60)  # sets refresh rate

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_key_down_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_key_down_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.ship.moving_down = False

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        if self.play_button.rect.collidepoint(mouse_pos) and not self.game_active:
            # Reset the game statistics.
            self.stats.reset_stats()
            self.game_active = True
            # Get rid of any remaining bullets and target.
            self.bullets.empty()
            self.aliens.empty()
            # Create a new target.
            self._create_target()
            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullet_limit:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()
        # Get rid of bullets that have disappeared off the screen.
        for bullet in self.bullets.copy():
            if bullet.rect.left > self.ship.screen_rect.right:
                self.bullets.remove(bullet)
                self._bullet_miss()
        self._check_bullet_target_collisions()

    def _check_bullet_target_collisions(self):
        """Respond to bullet-target collisions."""
        # Remove any bullets that have collided with the target.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, False)

    def _update_target(self):
        """Update the positions of the target."""
        self._check_target_edges()
        self.aliens.update()

    def _create_target(self):
        """Create the target."""
        new_alien = Alien(self)
        alien_width, alien_height = new_alien.rect.size
        new_alien.y = alien_height
        new_alien.rect.x = self.settings.screen_width - 2*alien_width
        new_alien.rect.y = alien_height
        self.aliens.add(new_alien)

    def _check_target_edges(self):
        """Respond appropriately if the target has reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_target_direction()
                break

    def _change_target_direction(self):
        """Change the target's direction."""
        self.settings.fleet_direction *= -1  # reverses direction on next edge

    def _bullet_miss(self):
        """Respond to missing the target with a bullet."""
        if self.stats.ships_left > 0:
            # Decrease ships_left.
            self.stats.ships_left -= 1
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        # Draw the Play button if the game is inactive.
        if not self.game_active:
            self.play_button.draw_button()
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai_game = TargetPractice()
    ai_game.run_game()
