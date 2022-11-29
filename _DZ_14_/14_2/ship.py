import pygame

class Ship:
	"""A class for controlling a ship"""

	def __init__(self, ai_game):
		"""Initialize the ship and set its starting position"""
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		# Load the image of the ship and set it to rect
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()

		# Create each new ship in the left middle of the screen.
		self.rect.midleft = self.screen_rect.midleft

		# Store the decimal value for the ship's vertical position.
		self.y = float(self.rect.y)

		# Traffic indicator
		self.moving_up = False
		self.moving_down = False


	def update(self):
		"""
		Update the ship's current position on the base
		traffic jammer
		"""
		# Update ship.x value to rect
		if self.moving_up and self.rect.top > 0:
			self.y -= self.settings.ship_speed
		if self.moving_down and self.rect.bottom < self.screen_rect.height:
			self.y += self.settings.ship_speed

		# Update the value of rect from self.y
		self.rect.y = self.y


	def blitme(self):
		"""Draw the ship in its original location"""
		self.screen.blit(self.image, self.rect)