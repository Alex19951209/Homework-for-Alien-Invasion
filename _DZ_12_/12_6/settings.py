class Settings:
	# A class to save all settings.
	def __init__(self):
		"""Initialize the application settings"""
		self.screen_width = 1200
		self.screen_height = 600
		self.bg_color = (230, 230, 230)

		# Ship settings
		self.ship_speed = 1.0

		# Bullet settings
		self.bullet_speed = 1.0
		self.bullet_width = 20
		self.bullet_height = 3
		self.bullet_color = (250, 0, 0)
		self.bullets_alower = 5