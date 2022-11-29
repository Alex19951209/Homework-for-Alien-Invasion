import pygame
from pygame.sprite import Sprite


class Laser(Sprite):
    """Class for controlling alien lasers"""

    def __init__(self, ai_game, x, y):
        """Creating laser  at an alien ship current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.laser_color

        # Creating laser
        self.rect = pygame.Rect(0, 0, self.settings.laser_width,
                                      self.settings.laser_height)

        self.rect.center = [x, y]
        # Store the lasers position as a decimal value.
        self.y = float(self.rect.y)

    def update(self):
        """Moving laser downwards"""
        self.y += self.settings.laser_speed
        # Update the rect position.
        self.rect.y = self.y

    def draw_laser(self):
        """Draw the laser to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)