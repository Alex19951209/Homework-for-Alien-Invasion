class Settings:
	"""A class to store all program settings"""

	def __init__(self):
		"""Initialize the application settings"""
		# Settings screen
		self.screen_width = 1200
		self.screen_height = 600
		self.bg_color = (255, 255, 255)

		# Speed drop
		self.drop_speed = 0.5