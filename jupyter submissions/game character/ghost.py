import pygame

class Ghost:

    def __init__(self, ai_game):
        #initialize ghost and starting position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #load ghost image and get its rectangular parameters as if it were a rectangle
        self.image = pygame.image.load('../../images/ghost.png')
        self.rect = self.image.get_rect()

        #start each new ghost at bottom center
        self.rect.center = self.screen_rect.center

    def blitme(self):
        #draw ghost at current location
        self.screen.blit(self.image, self.rect)