import pygame

class Ship:
	"""A class for controlling a ship."""

	def __init__(self, ai_game):
		"""Initialize the ship and set its starting position."""
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = self.screen.get_rect()

		# Download the image of the ship and get it rect
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()

		# Create each new ship at the bottom of the screen, in the middle
		self.rect.midleft = self.screen_rect.midleft

		# Store a decimal value for the horizontal position of the ship.
		self.y = float(self.rect.y)

		# Traffic indicators
		self.moving_up = False
		self.moving_down = False

	def update(self):
		"""
		Оupdate the ship's current position on the base
		traffic indicators.
		"""
		# Update the value of ship.x instead of rect.
		if self.moving_up and self.rect.top > 0:
			self.y -= self.settings.ship_speed

		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.settings.ship_speed

		# Update the rect object from self.x
		self.rect.y = self.y

	def center_ship(self):
		"""Center the ship on the screen"""
		self.rect.midleft = self.screen_rect.midleft
		
		# Store a decimal value for the horizontal position of the ship.
		self.y = float(self.rect.y)

	def blitme(self):
		"""Draw the ship in its current location."""
		self.screen.blit(self.image, self.rect)