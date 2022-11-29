class Settings:
	"""Clash to save all game settings"""

	def __init__(self):
		"""Initialize game settings"""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 660
		self.bg_color = (230, 230, 230)

		# Ship settings
		self.ship_speed = 1.0

		# Bullet settings
		self.bullet_width = 15
		self.bullet_height = 5
		self.bullet_speed = 1.5
		self.bullets_alower = 5
		self.bullet_color = (255, 0, 0)
		
		self.bullet_limit = 3

		# Targe settings
		self.target_width = 15
		self.target_height = 200
		self.target_speed = 0.5
		self.target_color = (255, 100, 0)

		# target_direction 1 means the direction of movement down; -1 -- up.
		self.target_direction = 1