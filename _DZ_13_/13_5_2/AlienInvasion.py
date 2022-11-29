import sys
from random import random

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
	"""Main class"""
	
	def __init__(self):
		"""Initialize game, create game resources"""
		pygame.init()

		self.settings = Settings()

		self.screen = pygame.display.set_mode((self.settings.screen_width,
									self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()


	def run_game(self):
		"""Run the main loop of the game"""
		while True:
			self._check_events()
			self._create_alien()
			self.ship.update()
			self._update_bullets()
			self.aliens.update()
			self._update_screen()


	def _check_events(self):
		"""Respond to the behavior of the mouse and buttons"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)


	def _check_keydown_events(self, event):
		"""React when the button is pressed"""
		if event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_UP:
			self.ship.moving_up = True
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = True
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()


	def _check_keyup_events(self, event):
		"""React when the button is released"""
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

		self._check_aliens_collisions()


	def _check_aliens_collisions(self):
		"""Reaction to the collision of a bullet and an alien"""
		collisions = pygame.sprite.groupcollide(
			self.bullets, self.aliens, True, True)


	def _create_alien(self):
		"""Create an alien, if conditions are right."""
		if random() < self.settings.alien_frequency:
			alien = Alien(self)
			self.aliens.add(alien)
			print(len(self.aliens))


	def _update_screen(self):
		"""Refresh the screen and switch to the new screen"""
		self.screen.fill(self.settings.bg_color)
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.ship.blitme()

		self.aliens.draw(self.screen)

		# Show the last normal screen
		pygame.display.flip()

if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()