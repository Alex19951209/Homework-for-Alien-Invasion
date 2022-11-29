import pygame

class Settings:
	"""A class for saving all program parameters"""
	def __init__(self):
		"""Initialize the application settings"""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 650
		self.bg_color = (255, 255, 255)
		self.ship_speed = 1.5