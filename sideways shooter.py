import sys
import pygame

from settings import Settings
from sship import sShip
from sbullet import sBullet
from salien import sAlien

class SShooter:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Sideways Shooter")

        self.sship = sShip(self)
        #create group of bullets that will have their positions updated
        self.sbullets = pygame.sprite.Group()
        self.saliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        while True:
            self._check_events()
            self.sship.update()
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

        elif event.key == pygame.K_UP:
            self.sship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.sship.moving_down = True

        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.sship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.sship.moving_down = False

    def _fire_bullet(self):
        #create new bullet and add to bullets group
        if len(self.sbullets) < self.settings.bullets_allowed:
            new_bullet = sBullet(self)
            self.sbullets.add(new_bullet)

    def _update_bullets(self):
        #update position of bullets
        self.sbullets.update()

        # get rid of bullets that have disappeared
        for bullet in self.sbullets.copy():
            if bullet.rect.right >= self.settings.screen_width:
                self.sbullets.remove(bullet)
        self._check_bullet_alien_collisions()
    def _check_bullet_alien_collisions(self):
        #check if bullet hit alien, if so, delete that bullet and alien
        collisions = pygame.sprite.groupcollide(self.sbullets, self.saliens, True, True)

        #checks if fleet has been destroyed then repopulates it
        if not self.saliens:
            #destroy existing bullets and create new fleet
            self.sbullets.empty()
            self._create_fleet()
    def _create_fleet(self):
        #make alien
        salien = sAlien(self)
        alien_width, alien_height = salien.rect.size
        ship_width = self.sship.rect.width
        #available space in x is width of screen minus the blank margins on either edge which is the width of one alien
        available_space_x = (self.settings.screen_width - alien_width - ship_width)
        #each alien has its own width plus the blank space to its right which is also the width of an alien
        #number of aliens that will fit in the width of the screen
        number_aliens_x = available_space_x // (2*alien_width)

        #find number of rows of aliens that fit on screen
        #put space between ship and first row of aliens equal to height of 3 aliens
        available_space_y = self.settings.screen_height - (2*alien_height)
        number_rows = available_space_y // (2*alien_height)


        for alien_number in range(number_aliens_x):
            for row_number in range(number_rows):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        #create row of aliens
        salien = sAlien(self)
        alien_width, alien_height = salien.rect.size
        ship_width = self.sship.rect.width
        #x and y position of alien
        salien.x = self.settings.screen_width - 2*alien_width - 2*alien_width*alien_number
        salien.rect.x = salien.x
        salien.y = alien_height + 2*alien_height*row_number
        salien.rect.y = salien.y
        self.saliens.add(salien)
    def _update_aliens(self):
        #if fleet at edge, update positions of all aliens in the fleet
        self._check_fleet_edges()
        self.saliens.update()
    def _check_fleet_edges(self):
        #respond if alien reaches edge
        for salien in self.saliens.sprites():
            if salien.check_edges():
                self._change_fleet_direction()
                break
    def _change_fleet_direction(self):
        #drop entire fleet and change fleet's direction
        for salien in self.saliens.sprites():
            salien.rect.x -= self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    def _update_screen(self):
        # redraw screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)

        self.sship.blitme()

        for sbullet in self.sbullets.sprites():
            sbullet.draw_bullet()

        self.saliens.draw(self.screen)
        # make most recently drawn screen visible
        pygame.display.flip()

if __name__=='__main__':
    #make a game instance from class AlienInvasion and run game
    ai = SShooter()
    ai.run_game()

