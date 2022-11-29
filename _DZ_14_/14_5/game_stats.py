import json

class GameStats:
	"""Tracking game statistics"""

	def __init__(self, ai_game):
		"""Initialize statistics"""
		self.settings = ai_game.settings
		self.reset_stats()

		# Start game in an inactive state.
		self.game_active = False

		# The record is not canceled.
		self.high_score = self.get_saved_high_score()


	def get_saved_high_score(self):
		"""Gets high score from file, if it exists."""
		try:
			with open('high_score.json') as f:
				return json.load(f)
		except FileNotFoundError:
			return 0


	def reset_stats(self):
		"""Initialization of statistics that may change during the game."""
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.level = 1