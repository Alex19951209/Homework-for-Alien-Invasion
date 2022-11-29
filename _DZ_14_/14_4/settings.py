class Settings:
	"""A class for saving all game settings."""

	def __init__(self):
		""""Initialize persistent game settings."""

		# Screen settings
		self.screen_width = 1200
		self.screen_height = 650
		self.bg_color = (230, 230, 230)

		# Bullet settings
		self.bullet_width = 5
		self.bullet_height = 15
		self.bullet_color = (50, 50, 50)

		# Alien settings
		self.fleet_drop_speed = 10

		# How fast the game should speed up
		self.speedup_scale = 1.2

		self.initialize_dynamic_settings_easy()
		self.initialize_dynamic_settings_medium()
		self.initialize_dynamic_settings_hard()


	def initialize_dynamic_settings_easy(self):
		"""Initialization of settings changes for the Easy level"""
		self.ship_limit = 5
		self.bullets_allowed = 10
		self.ship_speed = 1.0
		self.bullet_speed = 1.5
		self.alien_speed = 0.5


	def initialize_dynamic_settings_medium(self):
		"""Initializing variable settings for the Medium level"""
		self.ship_limit = 3
		self.bullets_allowed = 5
		self.ship_speed = 1.5
		self.bullet_speed = 3.0
		self.alien_speed = 1.0


	def initialize_dynamic_settings_hard(self):
		"""Initialization of settings changes for the Hard level"""
		self.ship_limit = 2
		self.bullets_allowed = 3
		self.ship_speed = 3.0
		self.bullet_speed = 6.0
		self.alien_speed = 2.0


		# fleet_direction 1 means the direction of movement to the right; -1 -- to the left.
		self.fleet_direction = 1


	def increase_speed(self):
		"""Increasing the speed setting"""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale