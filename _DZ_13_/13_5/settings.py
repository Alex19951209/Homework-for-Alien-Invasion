class Settings:
	"""A class for saving all game settings"""

	def __init__(self):
		"""Initialize game settings"""

		# Settings screen
		self.screen_width = 1300
		self.screen_height = 700
		self.bg_color = (230, 230, 230)

		# Ship settings
		self.ship_speed = 1.8

		# Bullet settings
		self.bullets_allowed = 9
		self.bullet_speed = 1.0
		self.bullet_width = 15
		self.bullet_height = 3
		self.bullet_color = (0, 0, 0)

		# Alien settings
		self.alien_speed = 0.7
		self.fleet_drop_speed = 10
		# fleet_direction 1 means the direction of movement to the right; -1 - to the left.
		self.fleet_direction = 1