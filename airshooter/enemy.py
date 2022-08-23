import pygame
from pygame.sprite import Sprite
from random import randrange, choice

class Enemy(Sprite):

    def __init__(self, game):
        super().__init__()
        self.screen = game.screen

        # Load the image
        self.image = pygame.image.load('enemy-plane.png')
        self.rect = self.image.get_rect()

        self.rect.center = (1050, randrange(100, 500))

        self.game = game

        self.cooldown = 0

        self.speed = randrange(1, 5)

        self.distance = 0

    def update(self):
        """Update the enemy ship"""
        if self.distance == 0:
            self.distance = randrange(10, 30)
            self.direction = choice(("up", "down"))
        if self.direction == "up":
            if self.rect.y > 50:
                self.rect.y -= self.speed
            self.distance -= 1
        else:
            if self.rect.y < 550:
                self.rect.y += self.speed
            self.distance -= 1
        if self.cooldown <= 0 and not self.rect.y < self.game.player.rect.y - 20 and not self.rect.y > self.game.player.rect.y + 20:
            self.game._fire_bullet("enemy", self.rect.left, self.rect.centery)
            self.cooldown = randrange(30, 100)
            
        self.cooldown -= 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)

