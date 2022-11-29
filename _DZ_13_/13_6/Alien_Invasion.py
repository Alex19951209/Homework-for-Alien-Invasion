import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
	"""A generic class that manages game resources and behavior."""

	def __init__(self):
		"""Initialize game, create game resources."""
		pygame.init()

		self.settings = Settings()

		self.screen = pygame.display.set_mode((self.settings.screen_width,
											self.settings.screen_height))
		pygame.display.set_caption("AlienInvasion")

		# Create an instance to save game statistics
		self.stats = GameStats(self) 

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()
		self.collis = pygame.sprite.Group()

		self._create_fleet()


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
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)

			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)


	def _check_keydown_events(self, event):
		"""Respond to keystrokes"""
		if event.key == pygame.K_q:
			sys.exit()		
		elif event.key == pygame.K_UP:
			self.ship.moving_up = True
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = True
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()		


	def _check_keyup_events(self, event):
		"""Respond when a key is not pressed"""
		if event.key == pygame.K_UP:
			self.ship.moving_up = False
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = False


	def _fire_bullet(self):
		"""Create a new sphere and add it to the sphere group"""
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)


	def _update_bullets(self):
		"""Update the position of balls and get rid of old balls."""
		# Update the positions of the balls
		self.bullets.update()


		# Get rid of bullets that have disappeared
		for bullet in self.bullets.copy():
			if bullet.rect.left >= self.settings.screen_width:
				self.bullets.remove(bullet)

		self._check_bullet_alien_collisions()


	def _check_bullet_alien_collisions(self):
		"""Reaction to collision of bullets with aliens"""
		# Remove all the bullets and aliens that collided.
		collisions = pygame.sprite.groupcollide(
			self.bullets, self.aliens, True, True)

		self.collis.add(collisions)

		# print(len(self.collis))

		if len(self.collis) >= 20:

			print('More that 100 mario hit./You win!')

			self.stats.game_active = False

		if not self.aliens:
			# Знащити наявні кулі та створити новий флот.
			self.bullets.empty()
			self._create_fleet()


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
		
		# Look for aliens that have reached the edge of the screen
		self._check_aliens_left()


	def _ship_hit(self):
		"""Respond to a collision between an alien and a ship"""
		if self.stats.ships_left > 0:
			# Decrease ships_left.
			self.stats.ships_left -= 1

			# Get rid of excess aliens and bullets
			self.aliens.empty()
			self.bullets.empty()

			# Create a new fleet and center the ship.
			self._create_fleet()
			self.ship.center_ship()

			# Pause
			sleep(0.7)
		else:
			self.stats.game_active = False


	def _check_aliens_left(self):
		"""Check whether one of the aliens has reached the left corner of the faucet"""
		screen_rect = self.screen.get_rect()
		for alien in self.aliens.sprites():
			if alien.rect.left <= 0:
				# Edit same as ship collision
				self._ship_hit()
				break


	def _create_fleet(self):
		"""Create a fleet of aliens"""
		# Create aliens and determine the number of aliens in a row.
		# The distance between aliens is equal to the width of one alien.
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		available_space_y = self.settings.screen_height - (2 * alien_height)
		number_aliens_y = available_space_y // (2 * alien_height)

		# Determine how many rows of aliens fit on the screen.
		ship_width = self.ship.rect.width
		available_space_x = (self.settings.screen_width - 
			(6 * alien_width) - ship_width)
		number_rows = available_space_x // (2 * alien_width)

		# Create a complete fleet of aliens.
		for row_number in range(number_rows):
			for alien_number in range(number_aliens_y):
				self._create_alien(row_number, alien_number)


	def _create_alien(self, row_number, alien_number):
		""" Create an alien and place it in a row"""
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		alien.y = alien_height + 2 * alien_height * alien_number
		alien.rect.y = alien.y 
		alien.rect.x = (self.settings.screen_width - 2 * alien.rect.width -
			(2 * alien_width) * row_number)
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
			alien.rect.x -= self.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1


	def _update_screen(self):
		"""Refresh the screen image and switch to the new screen"""
		self.screen.fill(self.settings.bg_color)
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.ship.blitme()
		self.aliens.draw(self.screen)

		# Show the last drawn screen.
		pygame.display.flip()

if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()