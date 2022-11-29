class Settings:
	"""A class for saving all game settings."""

	def __init__(self):
		"""Initialize the game's static settings."""
		# Screen settings.
		self.screen_width = 1200
		self.screen_height = 750
		self.bg_color = (230, 230, 230)

		# Ship settings.
		self.ship_limit = 3

		# Bullet settings.
		self.bullet_width = 4
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 5

		# Block settings.
		self.block_size = 5
		self.obstacle_amount = 6

		# Laser settings.
		self.laser_width = 5
		self.laser_height = 17
		self.laser_color = (200, 10, 60)
		
		# Alien settings.
		self.fleet_drop_speed = 10

		# How quickly the game speeds up.
		self.speedup_scale = 1.1

		# How quickly the alien point values increase
		self.score_scale = 1.5

		self.initialize_dynamic_settings()


	def initialize_dynamic_settings(self):
		"""Initialize settings that change throughout the game."""
		self.ship_speed = 10.0
		self.bullet_speed = 10.0
		self.alien_speed = 5.0
		self.laser_speed = 9.0	

		# fleet_direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1

		# Scoring.
		self.alien_points = 10


	def increase_speed(self):
		"""Increase speed settings and alien point values."""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale
		self.laser_speed *= self.speedup_scale

		self.alien_points = int(self.alien_points * self.score_scale)