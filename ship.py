import pygame

class Ship:

    def __init__(self, ai_game):
        #initialize image and starting position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        #load image and get its rectangular parameters as if it were a rectangle
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()

        #start each new image at bottom center
        self.rect.midbottom = self.screen_rect.midbottom

        #store decimal value for image's horizontal position
        self.x = float(self.rect.x)

        #movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        #update image's position based on movement flag
        #update image's x value
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #update rect object from self.x
        self.rect.x = self.x
    def center_ship(self):
        #center ship on screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
    def blitme(self):
        #draw image at current location
        self.screen.blit(self.image, self.rect)