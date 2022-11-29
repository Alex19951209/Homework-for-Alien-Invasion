import pygame

class Ship:
	"""A class for controlling a ship"""

	def __init__(self, ai_game):
		"""Initialize the ship and initialize its starting position"""

		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = self.screen.get_rect()

		# Load an image of the ship and set its rect.
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()

		# Set the initial position of the ship.
		self.rect.midbottom = self.screen_rect.midbottom

		# Save the decimal value of the ship horizontally.
		self.x = float(self.rect.x)

		# Traffic indicator.
		self.moving_right = False
		self.moving_left = False


	def update(self):
		"""Update the ship's current position based on the motion indicator"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed

		# Update the rect object from self.x.
		self.rect.x = self.x


	def center_ship(self):
		"""Place the new ship in the middle at the bottom of the screen"""		
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)


	def blitme(self):
		"""Draw the ship in its current location"""
		self.screen.blit(self.image, self.rect)