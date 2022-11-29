import sys
import pygame

from settings import Settings
from star import Star

class ScreenStar:
	"""Main class"""

	def __init__(self):
		"""Initialize application resources"""
		pygame.init()

		self.settings = Settings()

		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption('Stars on screen')

		self.star = Star(self)
		self.stars = pygame.sprite.Group()

		self._create_fleet()

	def run(self):
		"""Start the main cycle"""
		while True:
			self._check_events()
			self._update_screen()


	def _check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()


	def _create_fleet(self):
		"""Create a grid of stars"""
		# Create a star and determine the number of stars in a row
		# The distance between the stars is equal to one star width
		star = Star(self)
		star_width, star_height = star.rect.size

		# determine how many stars fit in a row
		number_stars_x = self.settings.screen_width // (2 * star_width)

		# Determine how many rows of stars fit on the screen
		number_rows = self.settings.screen_height // (2 * star_height)

		# Create a grid of stars
		for row_number in range(number_rows):
			for star_number in range(number_stars_x):
				self._create_star(star_number, row_number)

	def _create_star(self, star_number, row_number):
			"""Create a star and line it up"""
			star = Star(self)
			star_width, star_height = star.rect.size
			star.x = star_width + (2 * star_width) * (star_number)
			star.rect.x = star.x
			star.rect.y = star.rect.height + (2 * star.rect.height) * (row_number)
			self.stars.add(star)

	def _update_screen(self):
		"""Refresh the screen image and switch to the new screen"""
		self.screen.fill(self.settings.bg_color)
		self.stars.draw(self.screen)

		# Refresh last screen
		pygame.display.flip()


if __name__ =='__main__':
	ss = ScreenStar()
	ss.run()