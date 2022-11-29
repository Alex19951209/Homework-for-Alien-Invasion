class Settings:
	"""A class for saving all game settings"""

	def __init__(self):
		"""Initialize game settings"""

		# Screen settings
		self.screen_width = 1350
		self.screen_height = 600
		self.bg_color = (230, 230, 230)

		# Ship settings
		self.ship_speed = 1.0
		self.ship_limit = 3

		# Bullet settings
		self.bullet_speed = 1.0
		self.bullet_width = 15
		self.bullet_height = 10
		self.bullet_color = (255, 0, 0)
		self.bullet_allowed = 5


		# Alien settings
		# alien_frequency controls how often a new alien apper.s
		# Higher values -> more  frequent aliens. Max = 1.0
		self.alien_frequency = 0.002
		self.alien_speed = 0.3
