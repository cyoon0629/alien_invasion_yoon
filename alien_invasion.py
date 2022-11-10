import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        #create group of bullets and aliens that will have their positions updated
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()

    def _check_events(self):
        #respond to key and mouse presses
        #accesses keydown and keyup methods as its helper methods so this method is cleaner
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_q:
            sys.exit()

        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        #create new bullet and add to bullets group
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        #update position of bullets
        self.bullets.update()

        # get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        #check if bullet hit alien, if so, delete that bullet and alien
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        #checks if fleet has been destroyed then repopulates it
        if not self.aliens:
            #destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()

        self._check_bullet_alien_collisions()
    def _check_bullet_alien_collisions(self):
        

    def _create_fleet(self):
        #make alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        #available space in x is width of screen minus the blank margins on either edge which is the width of one alien
        available_space_x = self.settings.screen_width - (2*alien_width)
        #each alien has its own width plus the blank space to its right which is also the width of an alien
        #number of aliens that will fit in the width of the screen
        number_aliens_x = available_space_x // (2*alien_width)

        #find number of rows of aliens that fit on screen
        ship_height = self.ship.rect.height
        #put space between ship and first row of aliens equal to height of 3 aliens
        available_space_y = (self.settings.screen_height - (3*alien_height) - ship_height)
        number_rows = available_space_y // (2*alien_height)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        #create row of aliens
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        #x and y position of alien
        alien.x = alien_width + 2*alien_width*alien_number
        alien.rect.x = alien.x
        alien.y = alien_height + 2*alien_height*row_number
        alien.rect.y = alien.y
        self.aliens.add(alien)
    def _update_aliens(self):
        #if fleet at edge, update positions of all aliens in the fleet
        self._check_fleet_edges()
        self.aliens.update()
    def _check_fleet_edges(self):
        #respond if alien reaches edge
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    def _change_fleet_direction(self):
        #drop entire fleet and change fleet's direction
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    def _update_screen(self):
        # redraw screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)

        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)
        # make most recently drawn screen visible
        pygame.display.flip()

if __name__=='__main__':
    #make a game instance from class AlienInvasion and run game
    ai = AlienInvasion()
    ai.run_game()

