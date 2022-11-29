import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
	"""A class for controlling bullets fired from a ship"""

	def __init__(self, ai_game):
		"""Creates a bullet object at the current position of the ship"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.bullet_color

		# Create a rect ball at (0, 0) and set the correct position
		self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
			self.settings.bullet_height)
		self.rect.center = ai_game.ship.rect.midright

		# Save the ball position as a decimal value
		self.x = float(self.rect.x)

	def update(self):
		"""Push the ball to the side of the screen"""
		# Update the decimal position of the ball
		self.x += self.settings.bullet_speed
		
		# Update position rect
		self.rect.x = self.x

	def draw_bullet(self):
		"""Draw balls on the screen"""
		pygame.draw.rect(self.screen, self.color, self.rect)