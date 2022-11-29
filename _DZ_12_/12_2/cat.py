import  pygame

class Cat:
	"""A class for customizing a picture"""

	def __init__(self, i_game):
		"""initialize the drawing and set its current location"""
		self.screen = i_game.screen
		self.screen_rect = i_game.screen.get_rect()

		# Download image.
		self.image = pygame.image.load('images/cat.bmp')
		self.rect = self.image.get_rect()

		# Create each drawing in the center of the screen
		self.rect.center = self.screen_rect.center

	def blitme(self):
		"""Draw a picture in its current location"""
		self.screen.blit(self.image, self.rect)