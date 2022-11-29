class Settings:
	"""Clash to save all game settings"""

	def __init__(self):
		"""Initialize game settings"""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 660
		self.bg_color = (230, 230, 230)

		# Bullet settings
		self.bullet_width = 15
		self.bullet_height = 5
		self.bullets_alower = 5
		self.bullet_color = (255, 0, 0)
		
		self.bullet_limit = 3

		# Targe settings
		self.target_width = 15
		self.target_height = 200
		self.target_color = (255, 100, 0)		

		# How fast the game should speed up
		self.speedup_scale = 1.1
		self.initialize_dynamic_settings()


	def initialize_dynamic_settings(self):
		"""Initialization of settings changes"""
		self.ship_speed = 1.0
		self.bullet_speed = 1.5
		self.target_speed = 0.5

		# target_direction 1 means the direction of movement down; -1 -- up.
		self.target_direction = 1


	def increase_speed(self):
		"""Increasing the speed setting"""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.target_speed *= self.speedup_scale	