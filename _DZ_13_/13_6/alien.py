import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""A class representing one alien from the fleet"""

	def __init__(self, ai_game):
		"""Initialize the alien to set its initial location"""
		super().__init__()
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		self.settings = ai_game.settings

		# Load the alien image and its rect attribute.
		self.image = pygame.image.load("images/alien.bmp")
		self.rect = self.image.get_rect()

		# Start each new alien near the top left of the screen.
		alien_width = self.rect.width

		self.rect.right = self.screen_rect.right - alien_width
		self.rect.y = self.rect.height

		# Store the alien's exact horizontal position.
		self.x = float(self.rect.x)


	def check_edges(self):
		"""Returns true if the visitor is at the edge of the screen."""
		if self.rect.bottom >= self.screen_rect.bottom or self.rect.top <= 0:
			return True


	def update(self):
		"""Displacement of aliens to the left"""
		self.y += (self.settings.alien_speed *
					self.settings.fleet_direction)
		self.rect.y = self.y