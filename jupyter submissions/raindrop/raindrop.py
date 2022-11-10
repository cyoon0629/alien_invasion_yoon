import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    def __init__(self, ai_game):
        #initialize alien and starting position
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #load alien image and set its rect attribute
        self.image = pygame.image.load('../images/ghost.png')
        self.rect = self.image.get_rect()

        #start each new alien at top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store alien's decimal horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def is_gone(self):
        if self.rect.top > self.screen.get_rect().bottom:
            return True
        else:
            return False

    def update(self):
        #move alien right
        self.y += self.settings.raindrop_speed
        self.rect.y = self.y