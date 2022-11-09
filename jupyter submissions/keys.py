import sys
import pygame

from settings import Settings

class keys:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("keys")

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        #respond to key and mouse presses
        #accesses keydown and keyup methods as its helper methods so this method is cleaner
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_q:
            sys.exit()
        print(event.key)

    def _update_screen(self):
        # redraw screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)

        # make most recently drawn screen visible
        pygame.display.flip()

if __name__=='__main__':
    #make a game instance from class AlienInvasion and run game
    ai = keys()
    ai.run_game()

