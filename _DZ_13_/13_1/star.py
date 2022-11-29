import pygame
from pygame.sprite import Sprite

class Star(Sprite):
	"""A class to control the stars"""

	def __init__(self, ai_game):
		"""Initialize the star and set its initial position"""
		super().__init__()
		self.screen = ai_game.screen
		
		# Download image and create it rect
		self.image = pygame.image.load('images/star.bmp')
		self.rect = self.image.get_rect()

		# Set the initial position of the star
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Set decimal values
		self.x = float(self.rect.x)