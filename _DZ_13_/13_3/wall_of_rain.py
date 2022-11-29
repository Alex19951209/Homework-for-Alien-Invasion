import sys
import pygame

from settings import Settings
from drop import Drop

class DropsScreen:
	"""A generic class that manages the resources and behavior of the program"""

	def __init__(self):
		"""Initialize the application and create its resources"""
		pygame.init()

		self.settings = Settings()

		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption('Rein')

		self.drops = pygame.sprite.Group()

		self._check_fleat()


	def run(self):
		"""Run the main cycle of the program"""
		while True:
			self._check_events()
			self._update_drops()
			self._update_screen()


	def _check_events(self):
		"""Monitor button and mouse behavior"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

	def _check_fleat(self):
		"""Create a series of drops"""
		# The distance between drops is equal to one drop width
		drop = Drop(self)
		drop_width = drop.rect.width

		# Determine how many drops are placed in one row
		availble_space_x =  self.settings.screen_width - (2 * drop_width)
		number_drop_x = availble_space_x // (2 * drop_width)

		# Create a series of drops
		for drop_number in range(number_drop_x):
			# Створити краплю та поставити її у ряд
			drop = Drop(self)
			drop.x = drop_width + (2 * drop_width) * (drop_number)
			drop.rect.x = drop.x
			self.drops.add(drop)

	def _update_drops(self):
		"""Update the position of all drops on the screen"""
		self.drops.update()


	def _update_screen(self):
		"""Refresh the screen image and switch to the new screen"""
		self.screen.fill(self.settings.bg_color)
		self.drops.draw(self.screen)

		# Show the last normal screen
		pygame.display.flip()


if __name__ == '__main__':
	ds = DropsScreen()
	ds.run()