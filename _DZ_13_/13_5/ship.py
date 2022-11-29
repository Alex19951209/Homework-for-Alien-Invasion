import pygame

class Ship:
	"""A class for controlling a ship"""

	def __init__(self, ai_game):
		"""Initialize the ship and set its initial position"""
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		# Load the image of the ship and set it to rect
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()

		# Create each new ship on the left side of the screen, in the middle
		self.rect.midleft = self.screen_rect.midleft

		# collapse the decimal value of the ship vertically
		self.y = float(self.rect.y)

		# Traffic indicator
		self.moving_up = False
		self.moving_down = False

	def update(self):
		"""
		Update the ship's current position on the base traffic indicator
		"""
		# Update Ship.x value to rect.x
		if self.moving_up and self.rect.top >= 0:
			self.y -= self.settings.ship_speed
		if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
			self.y += self.settings.ship_speed

		# Update the rect object to self.y
		self.rect.y = self.y

	def blitme(self):
		"""Draw the ship in its current location"""
		self.screen.blit(self.image, self.rect)