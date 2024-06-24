# Hector Delgado 6/24/2024

import sys
import pygame
import json
from time import sleep
from pathlib import Path
from pygame.mixer import Sound
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


class SidewaysShooter:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(
            "Problem 14-8 - Sideways Shooter, Final Version")
        # Create an instance to store game statistics and display score.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.laser_sfx = Sound("sounds/laser.wav")
        self.explosion_sfx = Sound("sounds/explosion.wav")
        self._create_fleet()
        # Start Sideways Shooter in an inactive state.
        self.game_active = False
        # Make the Play button.
        self.play_button = Button(self, "Play", 640, 360)
        self.help_menu = Button(
            self, "[ARROW KEYS] or [WASD] to move. [SPACE] to fire.", 640, 100)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()  # check for player input

            if self.game_active:
                self.ship.update()  # update position of the ship
                self._update_bullets()  # update position of bullets
                self._update_aliens()  # update the position of aliens

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
            self._save_game()
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.ship.moving_up = False
        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.ship.moving_down = False

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        if self.play_button.rect.collidepoint(mouse_pos) and not self.game_active:
            # Reset the game statistics.
            self.stats.reset_stats()
            self.sb.prep_images()
            self.settings.initialize_dynamic_settings()
            self.game_active = True
            self._reset_positions()
            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullet_limit:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.laser_sfx.play()

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()
        # Get rid of bullets that have disappeared off the screen.
        for bullet in self.bullets.copy():
            if bullet.rect.left > self.ship.screen_rect.right:
                self.bullets.remove(bullet)
        # print(len(self.bullets)) #Shows that the bullets are being deleted
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
            self.explosion_sfx.play()

        if not self.aliens:
            self.start_new_level()

    def start_new_level(self):
        """Increase the difficulty when all aliens have been destroyed."""
        self._reset_positions()
        # Increase level
        self.settings.increase_speed()
        self.stats.level += 1
        self.sb.prep_level()

    def _update_aliens(self):
        """Update the positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen
        self._check_aliens_bottom()

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and keep adding aliens until there is no room left.
        # Spacing between aliens is one alien width and one alien height.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x = self.settings.screen_width - 2*alien_width
        current_y = alien_height
        while current_x > (3*alien_width):
            while current_y < (self.settings.screen_height - 2*alien_height):
                self._create_alien(current_x, current_y)
                current_y += 2*alien_height

            # Finished a row; reset y value, and decrease x value.
            current_y = alien_height
            current_x -= 2*alien_width

    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the fleet."""
        new_alien = Alien(self)
        new_alien.y = y_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.x -= self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1  # reverses direction on next edge

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the left egde of the screen."""
        for alien in self.aliens.sprites():
            if alien.rect.left <= 0:
                self._ship_hit()
                break

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # Decrease ships_left.
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            self._reset_positions()
            # Short pause.
            sleep(1.0)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _save_game(self):
        """Saves the high score to a file when the game is closed."""
        path = Path('high_score.json')
        path.write_text(json.dumps(self.stats.high_score))

    def _reset_positions(self):
        """Clears bullets and aliens, creates new fleet and recenters ship."""
        self.bullets.empty()
        self.aliens.empty()
        self._create_fleet()
        self.ship.center_ship()

    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.aliens.draw(self.screen)
        # Draw the score information.
        self.sb.show_score()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        # Draw the Play button if the game is inactive.
        if not self.game_active:
            self.play_button.draw_button()
            self.help_menu.draw_button()
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai_game = SidewaysShooter()
    ai_game.run_game()
