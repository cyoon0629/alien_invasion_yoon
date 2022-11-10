import sys
import pygame

from settings import Settings
from star import Star
from random import randint

class StarGrid:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Star Grid")

        self.stars = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        while True:
            self._update_screen()
            self._check_events()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def _create_fleet(self):
        #make star
        star = Star(self)
        star_width, star_height = star.rect.size
        #available space in x is width of screen minus the blank margins on either edge which is the width of one star
        available_space_x = self.settings.screen_width - (2*star_width)
        #each star has its own width plus the blank space to its right which is also the width of a star
        #number of stars that will fit in the width of the screen
        number_stars_x = available_space_x // (2*star_width)

        #find number of rows of stars that fit on screen
        available_space_y = self.settings.screen_height  #subtract one star???
        number_rows = available_space_y // (2*star_height)

        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                self._create_star(star_number, row_number)

    def _create_star(self, star_number, row_number):
        #create row of stars
        star = Star(self)
        star_width, star_height = star.rect.size
        #x and y position of star
        random_number1 = randint(-10, 10)
        star.rect.x = star_width + 2*star_width*star_number + random_number1
        random_number2 = randint(-10, 10)
        star.rect.y = star_height + 2*star_height*row_number + random_number2
        self.stars.add(star)

    def _update_screen(self):
        # redraw screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)

        self.stars.draw(self.screen)
        # make most recently drawn screen visible
        pygame.display.flip()

if __name__=='__main__':
    #make a game instance from class AlienInvasion and run game
    ai = StarGrid()
    ai.run_game()

