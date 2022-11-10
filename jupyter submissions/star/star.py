import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    def __init__(self, ai_game):
        #initialize star and starting position
        super().__init__()
        self.screen = ai_game.screen

        #load star image and set its rect attribute
        self.image = pygame.image.load('../images/star.png')
        self.rect = self.image.get_rect()

        #start each new star at top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store star's decimal horizontal position
        self.x = float(self.rect.x)