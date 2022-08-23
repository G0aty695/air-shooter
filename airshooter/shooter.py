

import sys, pygame

from settings import Settings
from player import Player
from bullet import Bullet
from enemy import Enemy
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

from time import sleep

class ShooterGame:
    """A class to manage the overall game"""

    def __init__(self):
        """Initilize the screen and everything on it"""
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Shooter")

        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.player = Player(self)
        self.play_button = Button(self, "Play")
        self.bullets = pygame.sprite.Group()
        self.enemys = pygame.sprite.Group()

    def run_game(self):
        """Games main loop"""
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.player.moving_up = True
                    elif event.key == pygame.K_DOWN:
                        self.player.moving_down = True
                    elif event.key == pygame.K_SPACE:
                        self._fire_bullet("player", self.player.rect.right, self.player.rect.centery)
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.player.moving_up = False
                    elif event.key == pygame.K_DOWN:
                        self.player.moving_down = False

            if self.stats.game_active:
                self.player.update()
                self._update_bullets()
                self.enemy_update()
                self.screen.fill(self.settings.bg_color)
                self.player.blitme()
                for bullet in self.bullets.sprites():
                    bullet.draw_bullet()
                for enemy in self.enemys.sprites():
                    enemy.update()
                    enemy.blitme()
                self.sb.show_score()
            else:
                self.play_button.draw_button()

            pygame.display.flip()

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_lives()

            for enemy in self.enemys.sprites():
                enemy.kill()
            for bullet in self.bullets.sprites():
                bullet.kill()
            self.player.rect.y = 300


    def _fire_bullet(self, type, x, y):
        if len(self.bullets) < 15:  
            new_bullet = Bullet(self, type, x, y)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.sprites():
            if bullet.rect.right < 0 or bullet.rect.left > 1200:
                self.bullets.remove(bullet)
            if bullet.type == "player":
                collisions = pygame.sprite.groupcollide(self.bullets, self.enemys, True, True)
                if collisions:
                    self.stats.score += 50
                    self.sb.prep_score()
            if pygame.Rect.colliderect(bullet.rect, self.player.rect) and bullet.type == "enemy":
                # Ship hit?

                # Delete bullet
                self.bullets.remove(bullet)

                # Lose a life
                self.stats.lives_left -= 1
                self.sb.prep_lives()

                # Lost?
                if self.stats.lives_left == 0:
                    self.stats.game_active = False
                    self.stats.score = 0

        

    def enemy_update(self):
        if len(self.enemys) < 4:
            new_enemy = Enemy(self)
            self.enemys.add(new_enemy)


if __name__ == '__main__':
    sg = ShooterGame()
    sg.run_game()