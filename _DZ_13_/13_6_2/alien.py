import pygame

from random import randint
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
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()

		# start each new alien at a random position on righr side
		# of the screen
		self.rect.left = self.screen_rect.right

		# The farthest down the screen we'll place the alien is the height
		# of the screen< minus height of the alien
		alien_top_max = self.settings.screen_height - self.rect.height
		self.rect.top = randint(0, alien_top_max)

		# Store the alien's exact horizontal position.
		self.x = float(self.rect.x)

	def update(self):
		"""Move the alien steadily to the left"""
		self.x -= self.settings.alien_speed
		self.rect.x = self.x