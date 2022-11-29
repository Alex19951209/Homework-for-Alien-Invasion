import pygame

class Ship:
	"""Controlling the ship"""

	def __init__(self, ai_game):
		"""Load an image of the ship and set its starting position"""
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		# Load the image of the ship and set it to rect
		self.image = pygame.image.load("images/ship.bmp")
		self.rect = self.image.get_rect()

		# Create each new ship inside the left side of the screen
		self.rect.midleft = self.screen_rect.midleft

		# Save the decimal value of the ship for the vertical
		self.y = float(self.rect.y)

		# Traffic indicator
		self.moving_up = False
		self.moving_down = False


	def update(self):
		"""Update the ship's current position based on the motion indicator"""
		# Update ship.x value to rect
		if self.moving_up and self.rect.top >= 0:
			self.y -= self.settings.ship_speed
		if self.moving_down and self.rect.bottom <= self.settings.screen_height:
			self.y += self.settings.ship_speed

		# Update the rect object from self.x
		self.rect.y = self.y


	def blitme(self):
		"""Draw the ship in its current location"""
		self.screen.blit(self.image, self.rect)