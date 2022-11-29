import pygame

from pygame.sprite import Sprite

class Drop(Sprite):
	"""A class representing one drop from a group"""

	def __init__(self, ai_game):
		"""Initialize the cluster and set its initial position"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings

		# Load the drop image and set its rect attribute
		self.image = pygame.image.load('images/drop.bmp')
		self.rect = self.image.get_rect()

		# Start each new drop near the top left of hte screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Store the drop's exact horizontal position
		self.y = float(self.rect.y)

	def _check_disappeared(self):
		"""If the drop has reached the bottom of the screen"""
		screen_rect = self.screen.get_rect()
		if self.rect.top >= screen_rect.bottom:
			return True
		else:
			return False

	def update(self):
		"""Wash the drop down"""
		self.y += self.settings.drop_speed
		self.rect.y = self.y


	