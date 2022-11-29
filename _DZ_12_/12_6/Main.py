import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class ShepScreen:
	"""The main class."""

	def __init__(self):
		"""Initialize the program and create program resources"""

		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("The ship on the screen")

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()


	def run(self):
		"""Start the main cycle"""
		while True:
			self._check_events()
			self.ship.updete()
			self._update_bullets()
			self._update_screen()

			
	def _check_events(self):
		"""Respond to keystrokes and mouse behavior"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_event(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_event(event)


	def _check_keydown_event(self, event):
		"""respond to keystrokes"""
		if event.key == pygame.K_UP:
			self.ship.moving_up = True
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = True
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()


	def _check_keyup_event(self, event):
		"""react when the buttons are not pressed"""
		if event.key == pygame.K_UP:
			self.ship.moving_up = False
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = False

	def _fire_bullet(self):
		"""Create a new sphere and add it to the sphere group"""
		if len(self.bullets) < self.settings.bullets_alower:
			new_bulet = Bullet(self)
			self.bullets.add(new_bulet)


	def _update_bullets(self):
		"""Update ball positions and get rid of old balls"""
		# Update the bullet position
		self.bullets.update()

		# Get rid of old balls
		for bullet in self.bullets.copy():
			if bullet.rect.left > self.settings.screen_width:
				self.bullets.remove(bullet)
		print(len(self.bullets))



	def _update_screen(self):
		"""Refresh the screen image and switch to the new screen"""
		self.screen.fill(self.settings.bg_color)
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.ship.blitme()

		# Show the last normal screen
		pygame.display.flip()

if __name__ =='__main__':
	ss = ShepScreen()
	ss.run()