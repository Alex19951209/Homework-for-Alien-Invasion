class GameStats:
	"""Tracking game statistics"""

	def __init__(self, ai_game):
		"""Initialize statistical data"""
		self.settings = ai_game.settings
		self.reset_stats()

		# Starting the game in an active state
		self.game_active = True
		

	def reset_stats(self):
		"""Initialize statistics that may change during gameplay"""
		self.ships_left = self.settings.ship_limit