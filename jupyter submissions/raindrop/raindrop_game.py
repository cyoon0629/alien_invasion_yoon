import sys
import pygame

from settings import Settings
from raindrop import Raindrop

class RainGame:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Falling Rain")

        self.raindrops = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        while True:
            self._check_events()
            self._update_raindrops()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def _create_fleet(self):
        #make alien
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        #available space in x is width of screen minus the blank margins on either edge which is the width of one alien
        available_space_x = self.settings.screen_width - (2*raindrop_width)
        #each alien has its own width plus the blank space to its right which is also the width of an alien
        #number of aliens that will fit in the width of the screen
        self.number_raindrops_x = available_space_x // (2*raindrop_width)

        #^^ this variable, because it is a "self.", can now be accessed by any method in this class

        available_space_y = self.settings.screen_height
        number_rows = available_space_y // (2*raindrop_height)

        for row_number in range(number_rows):
            for raindrop_number in range(self.number_raindrops_x):
                self._create_raindrop(raindrop_number, row_number)

    def _create_raindrop(self, raindrop_number, row_number):
        #create row of aliens
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        #x and y position of alien
        raindrop.x = raindrop_width + 2*raindrop_width*raindrop_number
        raindrop.rect.x = raindrop.x
        raindrop.y = raindrop_height + 2*raindrop_height*row_number
        raindrop.rect.y = raindrop.y
        self.raindrops.add(raindrop)

    def _update_raindrops(self):
        #if fleet at edge, update positions of all aliens in the fleet
        self.raindrops.update()

        make_more_rain = False
        for raindrop in self.raindrops:
            if raindrop.is_gone():
                self.raindrops.remove(raindrop)
                make_more_rain = True

        if make_more_rain:
            for raindrop_number in range(self.number_raindrops_x):
                self._create_raindrop(raindrop_number,0)

    def _update_screen(self):
        # redraw screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)

        self.raindrops.draw(self.screen)
        # make most recently drawn screen visible
        pygame.display.flip()

if __name__=='__main__':
    #make a game instance from class AlienInvasion and run game
    ai = RainGame()
    ai.run_game()

