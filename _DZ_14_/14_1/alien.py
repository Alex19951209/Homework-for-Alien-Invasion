import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""A class representing one alien from the fleet"""
	
	def __init__(self, ai_game):
		"""Initialize the alien to set its initial location"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings

		# Load the alien image and its rect attribute.
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()
 
		# Start each new alien near the top left of the screen.
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Store the alien's exact horizontal position.
		self.x = float(self.rect.x)


	def check_edges(self):
		"""Initialize the alien to set its initial location"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right or self.rect.left <= 0:
			return True


	def update(self):
		"""Place the alien on the right or left"""
		self.x += (self.settings.alien_speed *
				   self.settings.fleet_direction)
		self.rect.x = self.x