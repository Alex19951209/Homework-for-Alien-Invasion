class Settings:
	"""A class for saving all game settings"""

	def __init__(self):
		"""Initialize game settings"""
		# Settings screen
		self.screen_width = 1200
		self.screen_height = 600
		self.bg_color = (230, 230, 230)

		# Ship settings
		self.ship_speed = 1.0
		self.ship_limit = 3

		# Bullet settings 
		self.bullet_color = (255, 0, 0)
		self.bullet_width = 15
		self.bullet_height = 5
		self.bullet_spead = 0.7
		self.bullets_allowed = 5

		# Alien settings
		self.alien_speed = 0.5
		self.fleet_drop_speed = 15
		# fleet_direction 1 means the direction of movement to the right; -1 to the left.
		self.fleet_direction = 1