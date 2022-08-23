import pygame
from pygame.sprite import Sprite

class Player(Sprite):
    """A class to manage the player"""
    
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load("player-plane.png")
        self.rect = self.image.get_rect()

        self.rect.center = (40, 300)

        self.settings = game.settings

        # Movment flags
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ships position"""
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.settings.player_speed
        elif self.moving_down and self.rect.bottom < 600:
            self.rect.y += self.settings.player_speed
        else:
            if self.rect.bottom < 600:
                self.rect.y += 1


    def blitme(self):
        """Draw the player on the screen"""
        self.screen.blit(self.image, self.rect)