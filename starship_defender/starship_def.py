"""Game's core engine."""
import sys
from time import sleep

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


class StarshipDefender:
    """General class to manage resources and game behavior."""

    def __init__(self):
        """Initializing the game and create game resources."""
        pygame.init()
        self.settings = Settings()

        # Screen resolution
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        # Game name in the title
        pygame.display.set_caption("Starship Defender")

        # Stat and score object creations
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        # Ship, aliens and bullets creation
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Button 'Play' creation
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start the game."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _check_events(self):
        """Checking any events through game."""
        # Tracking mouse and keyboard events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_play_button(self, mouse_pos):
        """Start the game if mouse click on the button."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Dynamic settings reset
            self.settings.initialize_dynamic_settings()

            # Game stats reset
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()

            self._clear_and_restart()

            # Hide mouse cursor
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """Check if any key pressed."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Check any key released."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Creates new bullet and include it in bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Renew bullet position and delete them, when needed."""
        # Bullet position renew
        self.bullets.update()

        # Bullets deletion
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Register collisions between aliens and bullets. Create new fleet."""
        # Collisions between   aliens and bullets
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        # Remove bullets and create new fleet
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            # Level increase
            self.stats.level += 1
            self.sb.prep_level()

    def _ship_hit(self):
        """Processing ship-alien collision."""
        if self.stats.ships_left > 0:
            # Ship destroyed
            self.stats.ships_left -= 1
            self._clear_and_restart()

            # Pause
            sleep(0.5)
        else:
            self._clear_and_restart()
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _update_aliens(self):
        """
        Renew aliens position and change direction
        is fleet reach the edge of the screem.
        """
        self._check_fleet_edges()
        self.aliens.update()

        # Check if ship and alien collide
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Check if aliens reach bottom of the screen
        self._check_aliens_bottom()

    def _create_fleet(self):
        """Create invasion fleet."""
        # Alien fleet creation
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = int(available_space_x // (1.5 * alien_width))

        # Define number of rows on the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - ship_height)
        number_rows = int(available_space_y // (1.2 * alien_height))

        # Alien fleet creation
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Create separate alien and define its position."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 1.5 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 1.2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Check if alien reach the edge of the screen."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the fleet down and change direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_aliens_bottom(self):
        """Check if aliens reach bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Same reaction as ship hit
                self._ship_hit()
                break

    def _clear_and_restart(self):
        """Clear the screen and return objects to start point."""
        # Aliens and bullets remove
        self.aliens.empty()
        self.bullets.empty()

        # New fleet creation and ship respawn
        self._create_fleet()
        self.ship.center_ship()

    def _update_screen(self):
        """Renew screen to show changes."""
        # Redraw display every iteration
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Show score
        self.sb.show_score()

        # 'Play' button works if game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()

        # Display the last screen
        pygame.display.flip()


if __name__ == '__main__':
    # Creating class object and game start
    sd = StarshipDefender()
    sd.run_game()
