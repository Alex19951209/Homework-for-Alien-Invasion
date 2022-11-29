import sys
import pygame 

class CheckKey:
	"""Here we check whitch button is pressed and show it on the screen"""
	def __init__(self):
		"""initiate the program, create program resources"""
		pygame.init()

		# Create a screen
		self.screen = pygame.display.set_mode((700, 400))
		pygame.display.set_caption('Print key for screen')

		self.screen_rect = self.screen.get_rect()
		self.bg_color = (0, 50, 50)

		# text parameters
		self.font = pygame.font.Font('freesansbold.ttf', 40)
		self.on = 'Hello'

		# with attributes .font.renger did not understand
		self.text = self.font.render(self.on, True, (0, 255, 0))

		# we take the rect of the text and position it
		self.textRect = self.text.get_rect()

		self.textRect.center = self.screen_rect.center

	def run_game(self):
		"""Start the main cycle"""
		while True:
			self._check_events()
			self._update_screen()

	def _check_events(self):
		"""Monitor keyboard and mouse behavior"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				# check which key is pressed
				self.on = pygame.key.name(event.key)
				self.text = self.font.render(self.on ,True, (0, 255, 0))

	def _update_screen(self):
		"""Refresh the image on the screen and switch to a new screen"""
		self.screen.fill(self.bg_color)
		
		# text output
		self.screen.blit(self.text, self.textRect)

		# Show the last drawn screen
		pygame.display.flip()

if __name__ == "__main__":
	c = CheckKey()
	c.run_game()