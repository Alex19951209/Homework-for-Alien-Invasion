import sys
from time import sleep
import json
import pygame
import obstacle

import random

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien
from laser import Laser


FPS = 60

class AlienInvasion:
	"""Overall class to manage game assets and behavior."""

	def __init__(self):
		"""Initialize the game, and create game resources."""
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("Alien Invasion")

		self.clock = pygame.time.Clock()

		# Play music while playin.
		pygame.mixer.music.load('sounds/background.wav')
		pygame.mixer.music.play(-1)

		# Create an instance to store game statistics,
		#  and create a scoreboard.
		self.stats = GameStats(self)
		self.sd = Scoreboard(self)

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()
		self.lasers = pygame.sprite.Group()
		self.blocks = pygame.sprite.Group()
		self.alien_lasers = pygame.sprite.Group()

		self._create_fleet()
		self._create_obstacle()

		# Make the Play button.
		self.play_button = Button(self, "Play")

		

	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			self._check_events()
			self.clock.tick(FPS)
			
			if self.stats.game_active:
				self.ship.update()
				self._update_bullets()
				self._shots_aliens()
				self._update_laser()			
				self._update_aliens()
			self._update_screen()


	def _check_events(self):
		"""Respond to keypresses and mouse events."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self._close_game()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_play_button(mouse_pos)


	def _check_play_button(self, mouse_pos):
		""""Start a new game when the player clicks Play"""
		button_clicked = self.play_button.rect.collidepoint(mouse_pos)
		if button_clicked and not self.stats.game_active:
			self._start_game()


	def _start_game(self):
		"""Start a new game."""
		# Reset the game settings.
		self.settings.initialize_dynamic_settings()

		# Reset the game statistics.
		self.stats.reset_stats()
		self.stats.game_active = True
		self.sd.prep_score()
		self.sd.prep_level()
		self.sd.prep_ships()

		# Get rid of any remaining aliens and bullets.
		self.aliens.empty()
		self.blocks.empty()
		self.bullets.empty()

		# Create a new fleet and center the ship.
		self._create_fleet()
		self._create_obstacle()
		self.ship.center_ship()

		# Hide the mouse cursor.
		pygame.mouse.set_visible(False)


	def _check_keydown_events(self, event):
		"""Respond to keypresses."""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_q:
			self._close_game()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()
		elif event.key == pygame.K_p and not self.stats.game_active:
			self._start_game()


	def _check_keyup_events(self, event):
		""""Respond to key releases."""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False


	def _fire_bullet(self):
		"""Create a new bullet and add it to the bullets group."""
		if len(self.bullets) < self.settings.bullets_allowed:
			# Play gunshot sound with each shot.
			bullet_sound = pygame.mixer.Sound('sounds/shoot.wav')
			bullet_sound.play()

			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)


	def _update_bullets(self):
		"""Update position of bullets and get rid of old bullets."""
		# Update bullet positions.
		self.bullets.update()

		# Get rid of bullets that have disappeared.
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)

		self._check_bullet_alien_collisions()
		self._check_bullet_blocks_collisions()


	def _check_bullet_alien_collisions(self):
		"""Respond to bullet-alien collisions."""
		# Remove any bullets and aliens that have collided.
		collisions = pygame.sprite.groupcollide(
			self.bullets, self.aliens, True, True)

		if collisions:
			for aliens in collisions.values():
				# Play the sound when a bullet and an alien collide.
				explosion_sound = pygame.mixer.Sound('sounds/invaderkilled.wav')
				explosion_sound.play()

				self.stats.score += self.settings.alien_points * len(aliens)
			self.sd.prep_score()
			self.sd.check_high_score()

		if not self.aliens:
			self._start_new_level()


	def _stats_new_level(self):
		"""Start a new level."""
		# Destroy existing bullets and create new fleet.
		self.bullets.empty()
		self.blocks.empty()
		self._create_fleet()
		self._create_obstacle()

		self.settings.increase_speed()

		# Increase level.
		self.stats.level += 1
		self.sd.prep_level()


	def _check_bullet_blocks_collisions(self):
		"""Respond to bullet-block collisions """
		# Remove any balls and pieces of the obstacle that collided.
		colisions = pygame.sprite.groupcollide(
			self.bullets, self.blocks, True, True)


	def _create_obstacle(self):
		# We set the number and location of obstacles.
		self.obstacle_x_position =[
		num * (self.settings.screen_width / self.settings.obstacle_amount) 
		for num in range(self.settings.obstacle_amount)]	
		ship_height = self.ship.rect.height	

		self._create_multiple_obstacle(self.obstacle_x_position, 
			x_start = self.settings.screen_width / 15,
			y_start = self.settings.screen_height - (3 * ship_height))


	def create_block(self, x_start, y_start, offset_x):
		# We create an obstacle from blocks.
		self.shape = obstacle.shape
		for row_index, row in enumerate(self.shape):
			for col_index, col in enumerate(row):
				if col == 'x':
					x = x_start + col_index * self.settings.block_size + offset_x
					y = y_start + row_index * self.settings.block_size
					block = obstacle.Block(self.settings.block_size, x, y)
					self.blocks.add(block)


	def _create_multiple_obstacle(self, offset, x_start, y_start):
		# Follow the placement of obstacless.
		for offset_x in offset:
			self.create_block(x_start, y_start, offset_x)


	def _update_aliens(self):
		"""
		Check if the fleet is at an edge,
        then update the positions of all aliens in the fleet.
		"""
		self._check_fleet_edges()
		self.aliens.update()

		#  Look for alien ship collisions.
		if pygame.sprite.spritecollideany(self.ship, self.aliens):
			self._ship_hit()

		# Look for aliens hitting the bottom of the screen.
		self._check_aliens_bottom()
		self._check_aliens_block()


	def _check_aliens_bottom(self):
		""""Check if any aliens have reached the bottom of the screen."""
		screen_rect = self.screen.get_rect()
		for alien in self.aliens.sprites():
			if alien.rect.bottom >= screen_rect.bottom:
				# Treat this the same as if the ship got hit.				
				self._ship_hit()
				break


	def _check_aliens_block(self):
		"""Check for collisions of aliens and obstacles."""
		# Remove obstacles when encountering aliens.
		colisions = pygame.sprite.groupcollide(
			self.aliens, self.blocks, None, True)


	def _shots_aliens(self):
		""" Create a new laser and add it to the lasers group 
		    and give it a location."""
		if len(self.lasers) < 1 and len(self.aliens) > 0:
			attacking_alien = random.choice(self.aliens.sprites())
			laser = Laser(self, attacking_alien.rect.centerx,
							    attacking_alien.rect.centery)
			self.lasers.add(laser)


	def _update_laser(self):
		"""Update position of lasers and get rid of old blasers."""
		# Update lasers positions.
		self.lasers.update()

		# Get rid of lasers that have disappeared.
		for laser in self.lasers.copy():
			if laser.rect.top >= self.settings.screen_height:
				self.lasers.remove(laser)

		self._check_lasers_blocks_collisions()
		self._check_lasers_bullets_collisions()
		self._check_lasers_ship_collisions()		


	def _check_lasers_blocks_collisions(self):
		"""React to collisions of the bullet with an obstacle."""
		# Remove any balls and pieces of the obstacle that collided.
		colisions = pygame.sprite.groupcollide(
			self.lasers, self.blocks, True, True)


	def _check_lasers_bullets_collisions(self):
		"""Respond to the collision of the ship's balls and alien balls."""
		# Remove all the balls that have collided.
		collisions = pygame.sprite.groupcollide(
			self.bullets, self.lasers, True, True)
		if collisions:
			# Play the sound when a bullet and a laser collide.
			explosion_sound = pygame.mixer.Sound('sounds/invaderkilled.wav')
			explosion_sound.play()


	def _check_lasers_ship_collisions(self):
		"""Check the collision of the laser of the aliens and the ship."""
		# Remove all lasers and enable ship destruction.
		if pygame.sprite.spritecollideany(self.ship, self.lasers):			
			self.lasers.empty()
			self._ship_hit()

   
	def _ship_hit(self):
		"""Respond to the ship being hit by an alien."""
		if self.stats.ships_left > 0:

			# Play the sound of a ship explosion.
			explosion_sound = pygame.mixer.Sound('sounds/shipexplosion.wav')
			explosion_sound.play()

			# Decrement ships_left.
			self.stats.ships_left -= 1
			self.sd.prep_ships()

			# Get rid of any remaining aliens and bullets.
			self.aliens.empty()
			self.blocks.empty()
			self.bullets.empty()

			# Create a new fleet and center the ship.
			self._create_fleet()
			self._create_obstacle()
			self.ship.center_ship()

			# Pause.
			sleep(0.5)
		else:
			self.stats.game_active = False
			pygame.mouse.set_visible(True)


	def _check_fleet_edges(self):
		"""Respond appropriately if any aliens have reached an edge."""
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break


	def _change_fleet_direction(self):
		"""Drop the entire fleet and change the fleet's direction."""
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1


	def _create_fleet(self):
		"""Create the fleet of aliens."""
		# Create an alien and find the number of aliens in a row.
		# Spacing between each alien is equal to one alien width.
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		available_space_x = self.settings.screen_width - (2 * alien_width)
		number_aliens_x = available_space_x // (2 * alien_width)

		# Determine the number of rows of aliens that fit on the screen.
		ship_height = self.ship.rect.height
		available_space_y = (self.settings.screen_height -
							(5 * alien_height) - ship_height)
		number_rows = available_space_y // (2 * alien_height)

		# Create the full fleet of aliens.
		for row_number in range(number_rows):
			for alien_number in range(number_aliens_x):
				self._create_alien(alien_number, row_number)


	def _create_alien(self, alien_number, row_number):
		"""Create an alien and place it in the row."""
		# Create an alien and place it in a row.
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
		self.aliens.add(alien)


	def _close_game(self):
		"""Save high score and exit."""
		saved_high_score = self.stats.get_saved_high_score()
		if self.stats.high_score > saved_high_score:
			with open('high_score.json', 'w') as f:
				json.dump(self.stats.high_score, f)
		sys.exit()


	def _update_screen(self):
		"""Update images on the screen, and flip to the new screen."""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()

		for laser in self.lasers.sprites():
			laser.draw_laser()

		self.aliens.draw(self.screen)
		self.blocks.draw(self.screen)
		self.alien_lasers.draw(self.screen)

		# Draw the score information.
		self.sd.show_score()

		# Draw the play button if the game is inactive.
		if not self.stats.game_active:
			self.play_button.draw_button()

		# Show the last normal screen.
		pygame.display.flip()


if __name__ == '__main__':
	# Create an instance of the game and run the game.
	ai = AlienInvasion()
	ai.run_game()