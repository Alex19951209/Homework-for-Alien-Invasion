import sys

import pygame

class BlueScreen:
	"""A general class that controls the behavior of the program."""

	def __init__(self):
		"""Create a screen and set its color."""
		pygame.init()

		self.screen = pygame.display.set_mode((1200, 650))
		pygame.display.set_caption("Blue screen")

		self.bg_color = (0, 0, 255)

	def run(self):
		"""Start the program cycle."""
		while True:
			# Monitor mouse and keyboard behavior.
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			# Draw a screen on each loop interpretation.
			self.screen.fill(self.bg_color)

			# Show the last drawn screen.
			pygame.display.flip()

if __name__ =='__main__':
	# Create an instance of the screen and run it
	s = BlueScreen()
	s.run()