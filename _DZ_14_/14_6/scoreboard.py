import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard:
	"""A class that outputs a score"""

	def __init__(self, ai_game):
		"""Initialize account-related attributes"""
		self.ai_game = ai_game
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = ai_game.settings
		self.stats = ai_game.stats

		# Setting the font for displaying the invoice.
		self.tex_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)

		self.prep_images()


	def prep_images(self):
		"""Prepare the initial score images."""
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_ships()


	def prep_score(self):
		"""Convert image to bill"""
		rounded_score = round(self.stats.score, - 1)
		score_str ="{:,}".format(rounded_score)
		self.score_image = self.font.render(score_str, True,
			self.tex_color, self.settings.bg_color)

		# Show the score in the upper right corner of the screen.
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20


	def prep_high_score(self):
		"""Generate a record in the image"""
		high_score = round(self.stats.high_score, - 1)
		high_score_str = "{:,}".format(high_score)
		self.high_score_image = self.font.render(high_score_str, True,
			self.tex_color, self.settings.bg_color)

		# Center the record horizontally.
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top


	def check_high_score(self):
		"""	Check if a new record has been set"""
		if self.stats.score > self.stats.high_score:
			self.stats.high_score = self.stats.score
			self.prep_high_score()


	def prep_level(self):
		"""Convert layer to image"""
		level_str = str(self.stats.level)
		self.level_image = self.font.render(level_str, True,
			self.tex_color, self.settings.bg_color)

		# Location of the level under the account.
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 10


	def prep_ships(self):
		"""Shows how many ships are left."""
		self.ships = Group()
		for ship_number in range(self.stats.ships_left):
			ship = Ship(self.ai_game)
			ship.rect.x = 10 + ship_number * ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)


	def show_score(self):
		"""Draw the score, level and ship on the screen."""
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		self.ships.draw(self.screen)