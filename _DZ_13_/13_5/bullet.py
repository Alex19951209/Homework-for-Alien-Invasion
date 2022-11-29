import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""A class for controlling the orbs launched from the ship"""

	def __init__(self, ai_game):
		"""Creates a bullet object at the ship's current position"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.bullet_color

		# Create a rect sphere at (0, 0) and set the correct position
		self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
			self.settings.bullet_height)
		self.rect.center = ai_game.ship.rect.midleft

		# Save the positions of the balls as a decimal value

		self.x = float(self.rect.x)

	def update(self):
		"""Move the balls to the right of the screen"""
		# Update the decimal value of balls
		self.x += self.settings.bullet_speed
		# Оновити позицію rect
		self.rect.x = self.x

	def draw_bullet(self):
		"""Draw a ball on the screen"""
		pygame.draw.rect(self.screen, self.color, self.rect)