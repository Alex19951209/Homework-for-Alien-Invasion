import pygame
from pygame.sprite import Sprite

class Block(Sprite):
	"""A class for creating a shield."""
	def __init__(self, size, x, y):
		# Initialize the basic parameters of the shield.
		super().__init__()
		self.block_color = (241, 79, 80)
		self.image = pygame.Surface((size, size))
		self.image.fill(self.block_color)
		self.rect = self.image.get_rect(topleft =(x, y))

shape = [
'   xxxxxxxxxxx',
'  xxxxxxxxxxxxx',
' xxxxxxxxxxxxxxx',
'xxxxxxxxxxxxxxxxx',
'xxxxxxxxxxxxxxxxx',
'xxxxxxxxxxxxxxxxx',
'xxxxxxxxxxxxxxxxx',
'xxxxxx     xxxxxx',
'xxxxx       xxxxx',
'xxxx         xxxx']