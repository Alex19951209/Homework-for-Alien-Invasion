import pygame

from pygame.sprite import Sprite

class Drop(Sprite):
	"""A class that represents one drop from the program"""

	def __init__(self, ai_game):
		"""Initialize the blob and set its initial position"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings

		# Load the drop image and set its rect attribute
		self.image = pygame.image.load('images/drop.bmp')
		self.rect = self.image.get_rect()

		# Start each new drop near the top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Store the drop's exact horizontal position
		self.y = float(self.rect.y)

	def update(self):
		"""place the drop down"""
		self.y += self.settings.drop_speed
		self.rect.y = self.y