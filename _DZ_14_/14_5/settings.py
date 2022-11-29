class Settings:
	"""A class for saving all game settings."""

	def __init__(self):
		"""Initialize persistent game settings."""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 670
		self.bg_color = (230, 230, 230)

		# Ship settings.
		self.ship_limit = 3

		# Bullet settings
		self.bullet_width = 5
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 5

		# Alien settings.
		self.fleet_drop_speed = 10			

		# How fast the game should speed up
		self.speedup_scale = 1.1

		# How quickly the cost of newcomers increases
		self.score_scale = 1.5

		self.initialize_dynamic_settings()


	def initialize_dynamic_settings(self):
		"""Initialization of settings changes"""
		self.ship_speed = 1.5
		self.bullet_speed = 3.0
		self.alien_speed = 0.7

		# fleet_direction 1 means the direction of movement to the right; -1 -- to the left.
		self.fleet_direction = 1

		# Obtaining points.
		self.alien_points = 50

	def increase_speed(self):
		"""Increased alien speed and cost settings"""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale	

		self.alien_points = int(self.alien_points * self.score_scale)	