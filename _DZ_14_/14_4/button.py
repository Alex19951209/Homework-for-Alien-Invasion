import pygame.font

class Button:

	def __init__(self, ai_game, msg):
		"""Initialize button attributes"""
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()

		# Creating button dimensions and properties.
		self.width, self.height = 200, 50
		self.button_color = (255, 5, 0)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 40)

		# 	Create a button rect object and center it.
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center

		# The message on the button should be shown only once.
		self._prep_msg(msg)


	def _prep_msg(self, msg):
		"""Convert text to image and center the button"""
		self.msg_image = self.font.render(msg, True, self.text_color,
			self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center


	def _update_msg_position(self):
		"""If the button has been moved, the text needs to be moved as well."""
		self.msg_image_rect.center = self.rect.center


	def draw_button(self):
		""" Draw an empty button, and then a message"""
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)