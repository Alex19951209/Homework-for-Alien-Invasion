import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from bullet import Bullet
from target import Target

class TargetPractice:
	"""A class to manage all game resources and behavior"""

	def __init__(self):
		"""Initialize game, create game resources"""
		pygame.init()

		self.settings = Settings()

		self.screen = pygame.display.set_mode((self.settings.screen_width,
			self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")

		# Create an instance for game statistics.
		self.stats = GameStats(self)

		self.ship = Ship(self)
		self.target = Target(self)
		self.bullets = pygame.sprite.Group()

		# Create a Play button
		self.play_button = Button(self, "Play")


	def run_game(self):
		"""Run the main loop of the game"""
		while True:

			self._check_events()

			if self.stats.game_active:
				self.ship.update()
				self._update_bullets()
				self.target.update()

			self._update_screen()


	def _check_events(self):
		"""Respond to mouse and keystrokes"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_play_button(mouse_pos)


	def _check_play_button(self, mouse_pos):
		"""Start a new game when the Play button is pressed"""
		button_clicked = self.play_button.rect.collidepoint(mouse_pos)
		if button_clicked and not self.stats.game_active:
			self._start_game()


	def _start_game(self):
		"""Start the game when you press the mouse or the 'p' button"""
		# Reset game statistics.
		self.settings.initialize_dynamic_settings()
		self.stats.reset_stats()
		self.stats.game_active = True

		# Remove the extra balls.
		self.bullets.empty()

		# Hide the mouse cursor.
		pygame.mouse.set_visible(False)


	def _check_keydown_events(self, event):
		"""Respond to button presses"""
		if event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_UP:
			self.ship.moving_up = True
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = True
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()
		elif event.key == pygame.K_p:
			self._start_game()


	def _check_keyup_events(self, event):
		"""React when the button is released"""
		if event.key == pygame.K_UP:
			self.ship.moving_up = False
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = False


	def _fire_bullet(self):
		"""Create a new sphere and add it to the sphere group"""
		if len(self.bullets) < self.settings.bullets_alower:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)


	def _update_bullets(self):
		"""Update ball position and get rid of old balls"""
		# Update the position of the balls.
		self.bullets.update()

		# Get rid of the balls that snuck.
		for bullet in self.bullets.copy():
			if bullet.rect.left > self.settings.screen_width:
				self._bullets_miss()

		self._check_bullet_target_collisions()


	def _check_bullet_target_collisions(self):
		"""Check if any of the bullets hit the target"""
		# If you hit, get rid of the bullet.
		collisions = pygame.sprite.spritecollide(
			self.target, self.bullets, True)

		# If the ball collides with the target, we speed up the game.
		if collisions:
			self.settings.increase_speed()

	def _bullets_miss (self):
		"""React to the collision of the ball with the edge of the screen"""
		if self.stats.bullet_left > 0:
			# Decrease bullet_left.
			self.stats.bullet_left -=1

			# Get rid of excess bullets
			self.bullets.empty()

			# Pause
			sleep(0.2)
		else:
			self.stats.game_active = False
			pygame.mouse.set_visible(True)


	def _update_target_direction(self):
		if self.target.check_edges():
			self.settings.target_direction *= -1


	def _update_screen(self):
		"""Refresh the screen image and switch to the new screen"""
		self.screen.fill(self.settings.bg_color)
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()

		self.ship.blitme()

		self.target.draw_target()
		self._update_target_direction()

		# Draw a Play button when the game is not active.
		if not self.stats.game_active:
			self.play_button.draw_button()

		# Show the last drawn screen.
		pygame.display.flip()


if __name__ == '__main__':
	# Create an instance of the game and run the game.
	ai = TargetPractice()
	ai.run_game()