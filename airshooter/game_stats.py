class GameStats:
    """Track game statistics"""

    def __init__(self, game):
        self.settings = game.settings
        self.reset_stats()

        # Start the game inactive
        self.game_active = False

        self.score = 0

    def reset_stats(self):
        """Initilize changable statistics"""
        # Player Lives
        self.lives_left = self.settings.player_lives

