import pygame
import sys

from settings import Settings
from drop import Drop

class RainDrop():
	"""General class that manages all resources and behavior of the program"""

	def __init__(self):
		"""Initialize application resources"""
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption('Rain Drops')

		self.drops = pygame.sprite.Group()

		self._create_fleat()


	def run_program(self):
		"""Start the main cycle"""
		while True:
			self._check_events()
			self._update_drops()
			self._update_screen()


	def _check_events(self):
		"""Respond to button presses and mouse behavior"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()


	def _create_fleat(self):
		"""Create a wall of drops"""
		# Create a blob and determine the number of blobs in the government
		# The distance of the drops is equal to the width of one drop
		drop = Drop(self)
		drop_width = drop.rect.width
		number_drop = self.settings.screen_width // (2 * drop_width)

		# Create a series of drops
		for drop_number in range(number_drop):
			# Create a blob and line it up
			drop = Drop(self)
			drop.x = drop_width + (2 * drop_width) * drop_number
			drop.rect.x = drop.x
			self.drops.add(drop)


	def _update_drops(self):
		"""Update the position of all drops on the screen"""
		self._check_fleet_edges()
		self.drops.update()


	def _check_fleet_edges(self):
		"""Follow the placement of drops"""
		for drop in self.drops.sprites():
			drop.check_edges()


	def _update_screen(self):
		"""Refresh the screen image and switch to the new screen"""
		self.screen.fill(self.settings.bg_color)
		self.drops.draw(self.screen)

		# Show the last normal screen
		pygame.display.flip()

if __name__ == '__main__':
	ai = RainDrop()
	ai.run_program()