import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""A class for controlling bullets fired from a ship"""

	def __init__(self, ai_game):
		"""Сcreate a bullet object at the current position of the ship"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.bullet_color


		# Create a rect ball at (0, 0) and set the correct position.
		self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
			self.settings.bullet_height)
		self.rect.midtop = ai_game.ship.rect.midtop

		# Store the ball position as a decimal value.
		self.y = float(self.rect.y) 

	def update(self):
		"""Move the ball up the screen"""
		# Update the decimal position of the ball.
		self.y -= self.settings.bullet_speed
		# Оновити позицію rect.
		self.rect.y = self.y

	def draw_bullet(self):
		"""Draw a ball on the screen"""
		pygame.draw.rect(self.screen, self.color, self.rect)