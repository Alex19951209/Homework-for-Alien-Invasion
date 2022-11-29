import pygame

class Ship:
	"""A class for controlling a ship"""
	def __init__(self, ss_game):
		"""Initialize the ship and set its starting position"""
		self.screen = ss_game.screen
		self.settings = ss_game.settings
		self.screen_rect = ss_game.screen.get_rect()

		# Download the image of the ship and get its rect
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()

		# Build each ship in the middle of the screen
		self.rect.center = self.screen_rect.center

		# Save the decimal value of the corribal horizontally and vertically
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		# Traffic indicator
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def update(self):
		"""
		Update the ship's current positionbased on the motion indicator
		"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed
		if self.moving_up and self.rect.top > 0:
			self.y -= self.settings.ship_speed
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.settings.ship_speed

		# Update the rect object from self.x
		self.rect.x = self.x
		self.rect.y = self.y

	def blitme(self):
		"""Draw the ship in its original location"""
		self.screen.blit(self.image, self.rect)