import pygame
import sys

pygame.init()

screen_width = 1000
screen_height = 600
bg_color = (0, 0, 230)

screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill(bg_color)
pygame.display.set_caption("blue sky")

while True:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
