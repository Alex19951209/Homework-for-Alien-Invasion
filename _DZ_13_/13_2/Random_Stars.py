import sys
import pygame

from settings import Settings
from star import Star
from random import randint


class StarsScreen:
	"""A generic class that manages the program's resources and behavior"""

	def __init__(self):
		"""Initialize the application, create the application resources"""
		pygame.init()

		self.settings = Settings()

		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption('Stars on Screen')

		self.star = Star(self)
		self.stars = pygame.sprite.Group()

		self._create_flet()

	def run(self):
		"""Run the main cycle of the program"""
		while True:
			self._check_events()
			self._update_screen()


	def _check_events(self):
		"""Monitor mouse and keystroke behavior"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

	def _create_flet(self):
		"""Create a grid of stars"""
		# The distance between the stars is equal to the width of the star
		star = Star(self)
		star_width, star_height = star.rect.size

		# Determine how many stars fit in one row on the screen
		number_stars_x = self.settings.screen_width // (2 * star_width)

		# Determine how many rows will fit on the screen
		number_row = self.settings.screen_height // (2 * star_height)

		# Creates a grid of stars
		for row_number in range(number_row):
			for star_number in range(number_stars_x):
				self._create_star(star_number, row_number)

	def _create_star(self, star_number, row_number):
		"""Create a star and line it up"""
		star = Star(self)
		star_width, star_height = star.rect.size

		# Generate a random number of stars
		random_number = randint(-20, 20)
		star.x = star_width + (2 * star_width) * (star_number) + (random_number)
		star.rect.x = star.x
		star.rect.y = star.rect.height + (2 * star.rect.height) * (row_number) + (random_number)
		self.stars.add(star)

	def _update_screen(self):
		"""Refresh the screen image and switch to a new screen"""
		self.screen.fill(self.settings.bg_color)
		self.stars.draw(self.screen)

		# show the last normal screen
		pygame.display.flip()

if __name__ == '__main__':
	ss = StarsScreen()
	ss.run()