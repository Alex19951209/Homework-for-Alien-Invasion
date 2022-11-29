import pygame

class Ship:
	"""a ship control class"""
	def __init__(self, ai_game):
		"""Initialize the ship and set its starting position"""
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		# Upload image and get its rect
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()

		# Set the initial position of the ship
		self.rect.midleft = self.screen_rect.midleft

		# Store a decimal value for the ship's position
		self.y = float(self.rect.y)

		# Traffic indicator
		self.moving_up = False
		self.moving_down = False


	def updete(self):
		"""
		Update the position of the ship on the base traffic indicator
		"""
		if self.moving_up and self.rect.top > 0:
			self.y -= self.settings.ship_speed
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.settings.ship_speed

		# Update the rect object from self.y
		self.rect.y = self.y

	def blitme(self):
		"""Draw the ship in its current position"""
		self.screen.blit(self.image, self.rect)