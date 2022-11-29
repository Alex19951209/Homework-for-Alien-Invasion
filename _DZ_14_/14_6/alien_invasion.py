import sys
from time import sleep
import json

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
	"""A generic class that manages game resources and behavior."""

	def __init__(self):
		"""Initialize game, create game resources."""
		pygame.init()
		self.settings = Settings()

		# Run in full screen
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("Alien Invasion")

		# Create an instance to save game statistics
		# and scoreboard on the screen.
		self.stats = GameStats(self)
		self.sb = Scoreboard(self)

		self.ship = Ship(self)  	
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()

		self._create_fleet()

		# Create a Play button
		self.play_button = Button(self, "Play")


	def run_game(self):
		"""Start the main cycle of the game."""
		while True:
			self._check_events()
			if self.stats.game_active:
				self.ship.update()
				self._update_bullets()
				self._update_aliens()
			self._update_screen()


	def _check_events(self):
		"""Respond to keystrokes and mouse events"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self._close_game()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)					

			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_play_button(mouse_pos)

	def _check_play_button(self, mouse_pos):
		"""Start a new game when the user clicks the Play button."""
		button_clicked = self.play_button.rect.collidepoint(mouse_pos)
		if button_clicked and not self.stats.game_active:
			# Cancel game statistics.
			self.settings.initialize_dynamic_settings()
			self.stats.reset_stats()
			self.stats.game_active = True
			self.sb.prep_score()
			self.sb.prep_level()
			self.sb.prep_ships()

			# Get rid of excess aliens and bullets.
			self.aliens.empty()
			self.bullets.empty()

			# Create a new fleet and center the ship.
			self._create_fleet()
			self.ship.center_ship()

			# Hide the mouse cursor.
			pygame.mouse.set_visible(False)
					

	def _check_keydown_events(self, event):
		"""Respond to keystrokes"""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_q:
			self._close_game()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()


	def _check_keyup_events(self, event):
		"""React when the key is not pressed"""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False

	def _fire_bullet(self):
		"""Create a new sphere and add it to the sphere group"""
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _update_bullets(self):
		"""Update the position of balls and get rid of old balls."""
		# Update the position of the balls
		self.bullets.update()

		# Get rid of bullets that have disappeared
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)

		self._check_bullet_alien_collisions()


	def _check_bullet_alien_collisions(self):
		"""Reaction to collision of bullets with aliens"""
		# Remove all the bullets and aliens that collided.
		collisions = pygame.sprite.groupcollide(
			self.bullets, self.aliens, True, True)

		if collisions:
			for aliens in collisions.values():
				self.stats.score += self.settings.alien_points * len(aliens)
			self.sb.prep_score()
			self.sb.check_high_score()

		if not self.aliens:
			self._start_new_level()


	def _stats_new_level(self):
		"""Start a new level."""
		# Find existing orbs and create a new fleet.
		self.bullets.empty()
		self._create_fleet()
		self.settings.increase_speed()

		# Increase the level.
		self.stats.level += 1
		self.sb.prep_level()


	def _update_aliens(self):
		"""
		Check if the fleet is on edge,
		then update the positions of all aliens in the fleet.
		"""
		self._check_fleet_edges()
		self.aliens.update()

		# Look for collisions of bullets with aliens
		if pygame.sprite.spritecollideany(self.ship, self.aliens):
			self._ship_hit()

		# Look to see if any of the aliens have reached the bottom of the screen.
		self._check_aliens_bottom()
			


	def _ship_hit(self):
		"""Respond to a collision between an alien and a ship"""
		if self.stats.ships_left > 0:
			# Reduce ships_left and update scoreboard.
			self.stats.ships_left -= 1
			self.sb.prep_ships()

			# Get rid of excess aliens and bullets
			self.aliens.empty()
			self.bullets.empty()

			# Create a new fleet and center the ship.
			self._create_fleet()
			self.ship.center_ship()

			# Pause.
			sleep(0.5)
		else:
			self.stats.game_active = False
			pygame.mouse.set_visible(True)


	def _check_aliens_bottom(self):
		"""Check if any alien has reached the bottom edge of the screen."""
		screen_rect = self.screen.get_rect()
		for alien in self.aliens.sprites():
			if alien.rect.bottom >= screen_rect.bottom:
				# React as if the ship had been hit.
				self._ship_hit()
				break


	def _create_fleet(self):
		"""Create a fleet of aliens"""
		# Create aliens and determine the number of aliens in a row.
		# The distance between aliens is equal to the width of one alien.
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		available_space_x = self.settings.screen_width - (2 * alien_width)
		number_aliens_x = available_space_x // (2 * alien_width)

		# Determine how many rows of aliens fit on the screen.
		ship_height = self.ship.rect.height
		available_space_y = (self.settings.screen_height - 
							(3 * alien_height) - ship_height)
		number_rows = available_space_y // (2 * alien_height)


		# Create a complete fleet of aliens.
		for row_number in range(number_rows):
			for alien_number in range(number_aliens_x):
				self._create_alien(alien_number, row_number)	


	def _create_alien(self, alien_number, row_number):
			""" Create an alien and place it in a row"""
			alien = Alien(self)
			alien_width, alien_height = alien.rect.size
			alien.x = alien_width + 2 * alien_width * alien_number
			alien.rect.x = alien.x
			alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
			self.aliens.add(alien)


	def _check_fleet_edges(self):
		"""
		Responds to whether someone has reached
		from the edge of the screen aliens.
		"""
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break

	def _change_fleet_direction(self):
		"""Descent of the entire fleet and change of direction."""
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1


	def _close_game(self):
		"""Save the report to a file and close the game"""
		saved_high_score = self.stats.get_saved_high_score()
		if self.stats.high_score > saved_high_score:
			with open('high_score.json', 'w') as f:
				json.dump(self.stats.high_score, f)
		sys.exit()

  
	def _update_screen(self):
		"""Refresh the screen image and switch to the new screen"""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.aliens.draw(self.screen)

		# Draw account information.
		self.sb.show_score()

		# Draw the Play button if the game is not active.
		if not self.stats.game_active:
			self.play_button.draw_button()

		# Show the last drawn screen.
		pygame.display.flip()

if __name__ == '__main__':
	# Create game instances and run the game.
	ai = AlienInvasion()
	ai.run_game()