import pygame

class Target:
	"""A class for controlling the mouse"""
	def __init__(self, ai_game):
		"""Create a target and set its location"""
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = self.screen.get_rect()
		self.color = self.settings.target_color
		self.change_direction = self.settings.target_direction

		# Create a target and set its exact position
		self.rect = pygame.Rect(0, 0, self.settings.target_width,
			self.settings.target_height)

		# Create a target in the middle from the right of the screen.
		self.rect.midright = self.screen_rect.midright	

		# Store the target position as a decimal value
		self.y = float(self.rect.y)

		
	def update(self):
		"""Move the target to the right or left"""
		# Update the decimal value of the target.
		self.y += (self.settings.target_speed * self.settings.target_direction)

		# Store the target position as a decimal value.			
		self.rect.y = self.y


	def check_edges(self):
		"""Returns true if the target is on the edge of the screen."""
		screen_rect = self.screen_rect
		if self.rect.bottom >= self.screen_rect.bottom or self.rect.top <= 0:
			return True
		

	def draw_target(self):
		"""Draw a target on the screen"""
		pygame.draw.rect(self.screen, self.color, self.rect)