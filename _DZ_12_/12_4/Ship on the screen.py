import sys

import pygame

from settings import Settings
from ship import Ship

class ShipScrean:
	"""A generic class that manages game resources and behavior"""

	def __init__(self):
		"""Initiate game create game resources"""
		pygame.init()
		self.settings = Settings()

		# Create a screen.
		self.screen = pygame.display.set_mode((
			self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption('Ship Game')

		self.ship = Ship(self)

	def run_game(self):
		"""Start the main cycle"""
		while True:
			self._check_events()
			self.ship.update()
			self._update_screen()



	def _check_events(self):
		"""Respond to keystrokes and mouse"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)


	def _check_keydown_events(self, event):
		"""Respond to keystrokes"""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		if event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		if event.key == pygame.K_UP:
			self.ship.moving_up = True
		if event.key == pygame.K_DOWN:
			self.ship.moving_down = True
		if event.key == pygame.K_q:
			sys.exit()


	def _check_keyup_events(self, event):
		"""React when the key is not pressed"""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		if event.key == pygame.K_LEFT:
			self.ship.moving_left = False
		if event.key == pygame.K_UP:
			self.ship.moving_up = False
		if event.key == pygame.K_DOWN:
			self.ship.moving_down = False
			



	def _update_screen(self):
		"""Refresh the screen image and switch to the new screen"""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()

		# Show the last drawn screen.
		pygame.display.flip()


if __name__ =="__main__":
	ss = ShipScrean()
	ss.run_game()
