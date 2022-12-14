import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	"""A class for controlling a ship."""
	def __init__(self, ai_game):
		"""A class for controlling a spike."""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		# Download the image of the ship and get it rect
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()

		# Create each new ship at the bottom of the screen, in the middle
		self.rect.midbottom = self.screen_rect.midbottom

		# Store a decimal value for the horizontal position of the ship.
		self.x = float(self.rect.x)

		# Traffic indicators
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""
		Update the ship's current position on the base
		traffic indicators.
		"""
		# Update the value of ship.x instead of rect.
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed

		# Update the rect object from self.x
		self.rect.x = self.x

	def center_ship(self):
		"""Center the ship on the screen"""
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)

	def blitme(self):
		"""Draw the ship in its current location."""
		self.screen.blit(self.image, self.rect)