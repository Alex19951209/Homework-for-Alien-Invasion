import sys

import pygame

from settings import Settings
from cat import Cat

class Images:
	"""Main class"""

	def __init__(self):
		"""Initialize the data"""

		pygame.init()

		self.settings = Settings()

		# Create screen.
		self.screen = pygame.display.set_mode((
			self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Images cat")

		self.cat = Cat(self)

	def run_program(self):
		"""Start the main cycle"""
		while True:
			self._check_events()
			self._update_screen()

	def _check_events(self):
		"""Respond to keystrokes and mouse"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

	def _update_screen(self):
		"""Refresh the screen image and switch to the new screen"""

		# Fill the screen. 
		self.screen.fill(self.settings.bg_color)
		self.cat.blitme()

		# Refresh the image on the screen.
		pygame.display.flip()

if __name__ =='__main__':
	i = Images()
	i.run_program()