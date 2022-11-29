import pygame

from pygame.sprite import Sprite

class Drop(Sprite):
	"""A class representing one drop"""

	def __init__(self, ai_game):
		"""Load the blob and set its initial position"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings

		# Load the image and set it to rect
		self.image = pygame.image.load('Images/drop.bmp')
		self.rect = self.image.get_rect()

		# Set the initial position of the droplet
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Specify a decimal value 
		self.y = float(self.rect.y)

	def check_edges(self):
		"""Monitor the placement of the drop"""
		screen_rect = self.screen.get_rect()
		if self.rect.top >= screen_rect.bottom:
			self.y = 0

	def update(self):
		"""Place the drop down the screen"""
		self.y += self.settings.drop_speed
		self.rect.y = self.y