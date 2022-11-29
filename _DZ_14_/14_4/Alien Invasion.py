import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
	"""A class for managing the game's behavior and resources"""

	def __init__(self):
		"""Initialize game resources"""
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("Alien Invasion")

		# Create an instance to save game statistics
		self.stats = GameStats(self)

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()

		self._create_fleet()		

		# Create a Play button with different difficulty levels.
		self._make_difficulty_buttons()


	def _make_difficulty_buttons(self):
		"""Create buttons with different levels of complexity."""
		self.easy_play_button = Button(self, "Easy Play")
		self.medium_play_button = Button(self, "Medium Play")
		self.hard_play_button = Button(self, "Hard Play")


		self.medium_play_button.rect.top = (self.easy_play_button.rect.top +
		 1.5 * self.easy_play_button.rect.height)
		self.medium_play_button._update_msg_position()

		self.hard_play_button.rect.top = (self.medium_play_button.rect.top +
		 1.5 * self.medium_play_button.rect.height)
		self.hard_play_button._update_msg_position()


	def run_game(self):
		"""Run the main loop of the game"""
		while True:
			self._check_events()
			if self.stats.game_active:
				self.ship.update()
				self._update_bullets()
				self._update_aliens()

			self._update_screen()


	def _check_events(self):
		"""Monitor key and mouse events"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_play_button(mouse_pos)


	def _check_play_button(self, mouse_pos):
		"""Start a new game after pressing the Play button"""
		easy_clicked = self.easy_play_button.rect.collidepoint(mouse_pos)
		medium_clicked = self.medium_play_button.rect.collidepoint(mouse_pos)
		hard_clicked = self.hard_play_button.rect.collidepoint(mouse_pos)

		if easy_clicked and not self.stats.game_active:
			self._start_game()
			self.settings.initialize_dynamic_settings_easy()

		elif medium_clicked and not self.stats.game_active:
			self.settings.initialize_dynamic_settings_medium()
			self._start_game()

		elif hard_clicked and not self.stats.game_active:
			self.settings.initialize_dynamic_settings_hard()
			self._start_game()


	def _start_game(self):
		"""Run the game"""		
		# Reset initial game data.
		self.stats.reset_stats()
		self.stats.game_active = True

		# Remove all aliens and bullets.
		self.aliens.empty()
		self.bullets.empty()

		# Creating a new fleet and centering the ship
		self._create_fleet()
		self.ship.center_ship()

		# Hide the mouse cursor.
		pygame.mouse.set_visible(False)


	def _check_keydown_events(self, event):
		"""React when a key is pressed"""
		if event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
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
		"""Update the ball position and get rid of old balls"""
		# Update the position of the balls
		self.bullets.update()

		# Get rid of old balls.
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)

		self._check_bullet_alien_collisions()


	def _check_bullet_alien_collisions(self):
		"""The reaction to the collision of a bullet with an alien"""
		# Removal of all bullets and aliens that collided.
		collisions = pygame.sprite.groupcollide(
			self.bullets, self.aliens, True, True)

		if not self.aliens:
			# Removal of the old cult to create a new fleet of aliens.
			self.bullets.empty()
			self._create_fleet()
			self.settings.increase_speed()


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


	def _update_aliens(self):
		"""The movement of a whole fleet of aliens"""
		self._check_fleet_edges()
		self.aliens.update()

		# Collision check between the alien and the ship.
		if pygame.sprite.spritecollideany(self.ship, self.aliens):
			self._ship_hit()

		# Look to see if any of the aliens have reached the bottom of the screen.
		self._check_aliens_bottom()


	def _ship_hit(self):
		"""Reaction to a collision between an alien and a ship"""
		if self.stats.ships_left > 0:
			# Reduce the number of lives in the ship.
			self.stats.ships_left -= 1

			# Remove old aliens and bullets.
			self.aliens.empty()
			self.bullets.empty()

			# Create a new fleet of aliens and center the ship.
			self._create_fleet()
			self.ship.center_ship()

			# Pause.
			sleep(0.5)
		else:
			self.stats.game_active = False
			pygame.mouse.set_visible(True)


	def _check_aliens_bottom(self):
		"""Checking whether any of the aliens has reached the bottom of the screen"""
		screen_rect = self.screen.get_rect()
		for alien in self.aliens.sprites():
			if alien.rect.bottom >= screen_rect.bottom:
				# React as if the ship had been hit.
				self._ship_hit()
				break


	def _check_fleet_edges(self):
		"""React when the newcomer has reached the edge of the screen"""
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break


	def _change_fleet_direction(self):
		"""Shifting the entire fleet to the bottom and changing the direction of movement of the fleet"""
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1

	def _update_screen(self):
		"""Refresh the screen image and show the last screen"""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.aliens.draw(self.screen)

		# Draw Play buttons if the game is not active.
		if not self.stats.game_active:
			self.easy_play_button.draw_button()
			self.medium_play_button.draw_button()
			self.hard_play_button.draw_button()

		# Show the last normal screen
		pygame.display.flip()


if __name__ == "__main__":
	ai = AlienInvasion()
	ai.run_game()