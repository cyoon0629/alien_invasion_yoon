import sys
import pygame

from settings import Settings
from sship import sShip
from sbullet import sBullet

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

    def run_game(self):
        while True:
            self._check_events()
            self.sship.update()
            self._update_bullets()
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

    def _update_screen(self):
        # redraw screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)

        self.sship.blitme()

        for bullet in self.sbullets.sprites():
            bullet.draw_bullet()

        # make most recently drawn screen visible
        pygame.display.flip()

if __name__=='__main__':
    #make a game instance from class AlienInvasion and run game
    ai = SShooter()
    ai.run_game()

