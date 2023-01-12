"""Button 'Play' module."""
import pygame.font

class Button:
    """Class to describe buttons"""

    def __init__(self, sd_game, msg):
        """Initialize button attributes."""
        self.screen = sd_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set button's size and functions
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Set button's position
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Button's message
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Message for the button."""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Creates button on the screen."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
