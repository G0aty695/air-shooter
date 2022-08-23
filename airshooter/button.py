import pygame.font

class Button:

    def __init__(self, game, msg):
        """Initilize button attributes"""
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        # set the dimensions and properties for the button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button rect and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw a blank button then draw the message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)