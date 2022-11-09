import pygame

class Rocket:

    def __init__(self, ai_game):
        #initialize image and starting position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        #load image and get its rectangular parameters as if it were a rectangle
        self.image = pygame.image.load('../../images/rocket.png')
        self.rect = self.image.get_rect()

        #start each new image at bottom center
        self.rect.center = self.screen_rect.center

        #store decimal value for image's horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        #update image's position based on movement flag
        #update image's x and y values
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed

        #update rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y
    def blitme(self):
        #draw image at current location
        self.screen.blit(self.image, self.rect)