import pygame.font

class Button():

	def __init__(self, ai_game, msg):
		"""Initialize button attributes"""
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()

		# Download button dimensions and properties.
		self.width, self.height = 200,50
		self.button_color = (100, 200, 100)
		self.tex_color = (0, 0, 0)
		self.font = pygame.font.SysFont(None, 48)

		# Create a button rect object and display it.
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center

		# The message on the button should be shown only once.
		self._prep_msg(msg)


	def _prep_msg(self, msg):
		"""Convert the text to an image and place in the middle of the button"""
		self.msg_image = self.font.render(msg, True, self.tex_color,
			self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center


	def draw_button(self):
		"""Draw a button, and then draw a message"""
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)