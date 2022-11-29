import sys
import pygame

from settings import Settings
from drop import Drop
from random import randint

class Rain:
	"""A generic class that controls the program's behavior and resources"""

	def __init__(self):
		"""Initialize the program to create program resources"""
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption('Rain')

		self.drops = pygame.sprite.Group()
		self._check_fleat()

	def run_program(self):
		"""Start the main cycle"""
		while True:
			self._check_events()
			self._update_drops()
			self._update_screen()

	def _check_events(self):
		"""Respond to keystrokes and mouse events"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

	def _check_fleat(self):
		"""Create a grid of drops"""
		# The distance between drops is equal to one drop width
		drop = Drop(self)
		drop_width, drop_height = drop.rect.size

		# Determine how many drops are placed in one row
		availble_space_x =  self.settings.screen_width 
		self.number_drop_x = availble_space_x // (2 * drop_width)

		# Determine how many rows will fit on the screen
		availble_space_y = self.settings.screen_height
		number_row = availble_space_y // (2 * drop_height)

		# Create a series of drops
		for row_number in range(number_row):
			self._create_row(row_number)

	def _create_row(self, row_number):
		"""Create a grid of drops"""
		for drop_number in range(self.number_drop_x):
			self._create_drop(drop_number, row_number)

	def _create_drop(self, drop_number, row_number):
			"""Create a blob and line it up"""
			drop = Drop(self)
			drop_width, drop_height = drop.rect.size
			drop.rect.x = drop_width + (2 * drop_width) * (drop_number)
			drop.y = 2 * drop.rect.height * row_number
			drop.rect.y = drop.y
			self.drops.add(drop)

	def _update_drops(self):
		"""Update the position of all drops on the screen"""
		self.drops.update()

		# Follow the location of the drops
		make_new_drops = False
		for drop in self.drops.copy():
			if drop._check_disappeared():
				# Delete the old row of drops
				self.drops.remove(drop)
				make_new_drops = True

		# Create a new row of drops if necessary
		if make_new_drops:
			self._create_row(0)

	def _update_screen(self):
		"""Refresh the screen image and switch to the new screen"""
		self.screen.fill(self.settings.bg_color)
		self.drops.draw(self.screen)

		# Refresh the last normal screen
		pygame.display.flip()

if __name__ == '__main__':
	ai = Rain()
	ai.run_program()