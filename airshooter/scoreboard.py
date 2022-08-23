import pygame.font
from pygame.sprite import Group

from player import Player

class Scoreboard:
    """A class to show scoreing info"""

    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats

        # Font for scoring
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()

    def prep_score(self):
        """Render the score"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_lives(self):
        """Show how many lives are left with player ship sprites"""
        self.ships = Group()
        for ship_number in range(self.stats.lives_left):
            ship = Player(self.game)
            ship.rect.x = (10 + ship_number * ship.rect.width * 1.5) 
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """Draw the score on the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.ships.draw(self.screen)