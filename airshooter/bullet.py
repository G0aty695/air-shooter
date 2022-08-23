import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage the players and enemys bullets"""

    def __init__(self, game, type, x, y):
        """Create a bullet"""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.type = type
        
        if self.type == "player":
            self.color = self.settings.player_bullet_color
        if self.type == "enemy":
            self.color = self.settings.enemy_bullet_color

        # Create a bullet at (0, 0) then take it to the right spot
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.center = (x, y)


    def update(self):
        """Move the bullets across the screen"""
        if self.type == "player":
            self.rect.x += self.settings.player_bullet_speed
        if self.type == "enemy":
            self.rect.x -= self.settings.enemy_bullet_speed

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)