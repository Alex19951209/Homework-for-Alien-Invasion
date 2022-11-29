import sys
from time import sleep

from random import random
import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
	"""A generic class that controls game settings and behavior"""

	def __init__(self):
		"""Initialize game, create game resources"""
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode((self.settings.screen_width,
			self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")

		# Create an instance to save game statistics
		self.stats = GameStats(self)

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()
		self.collids = pygame.sprite.Group()


	def run_game(self):
		"""Start the main cycle"""
		while True:
			self._check_events()	

			if self.stats.game_active:
				self._create_alien()
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
		if len(self.bullets) < self.settings.bullet_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _update_bullets(self):
		"""Update the position of balls and get rid of old balls."""
		# Update the positions of the balls
		self.bullets.update()

		# Get rid of bullets that have disappeared
		for bullet in self.bullets.copy():   
			if bullet.rect.left > self.settings.screen_width:
				self.bullets.remove(bullet)

		self._check_bullet_alien_collisions()


	def _check_bullet_alien_collisions(self):
		"""Reaction to the collision of a bullet and an alien"""
		# Remove the alien on collision with a bullet.
		collisions = pygame.sprite.groupcollide(
			self.bullets, self.aliens, True, True)

		self.collids.add(collisions)

		if len(self.collids) >= 50:

			print("You win!!!")

			self.stats.game_active = False


	def _create_alien(self):
		"""Create an alien, if conditions are right."""
		if random() < self.settings.alien_frequency:
			alien = Alien(self)
			self.aliens.add(alien)


	def _update_aliens(self):
		"""Update alien positions, and look for collisions with ship."""
		self.aliens.update()

		# Check the collision between the alien and the ship
		if pygame.sprite.spritecollideany(self.ship, self.aliens):
			self._ship_hit()

		# Follow the newcomer who has reached the left edge of the screen
		self._check_aliens_left()


	def _check_aliens_left(self):
		"""Check if any of the aliens have reached the left edge of the screen"""
		for alien in self.aliens.sprites():
			if alien.rect.left < 0:
				# Act in the same way as in the case of a collision between a ship and an alien.
				self._ship_hit()
				break


	def _ship_hit(self):
		"""Respond to a collision between an alien and a ship"""
		if self.stats.ships_left > 0:
			# Reducing the number of lives of the ship
			self.stats.ships_left -= 1

			# Remove all aliens and bullets
			self.aliens.empty()
			self.bullets.empty()

			# Creating a new fleet of aliens and centering the ship
			self.ship.center_ship()

			# Pause
			sleep(0.7)
		else:
			self.stats.game_active = False


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