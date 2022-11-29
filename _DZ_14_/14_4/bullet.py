import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
	"""A class for controlling spheres"""

	def __init__(self, ai_game):
		"""Creates a Bullet object at the ship's current position"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.bullet_color

		# Create a Rect(0, 0) sphere and set its initial position.
		self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
			self.settings.bullet_height)
		self.rect.midtop = ai_game.ship.rect.midtop

		# Save the ball position as a decimal value.
		self.y = float(self.rect.y)


	def update(self):
		"""Move the ball up the screen"""
		# Update the decimal position of the ball.
		self.y -= self.settings.bullet_speed

		# Update position rect.
		self.rect.y = self.y


	def draw_bullet(self):
		"""Draw a ball on the screen"""
		pygame.draw.rect(self.screen, self.color, self.rect)