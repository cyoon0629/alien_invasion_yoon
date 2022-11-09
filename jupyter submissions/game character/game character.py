import sys
import pygame

from settings import Settings
from ghost import Ghost

class game_character:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Game Character")

        self.ghost = Ghost(self)

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        #respond to key and mouse presses
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        # redraw screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.ghost.blitme()

        # make most recently drawn screen visible
        pygame.display.flip()


if __name__=='__main__':
    #make a game instance from class game_character and run game
    ai = game_character()
    ai.run_game()

