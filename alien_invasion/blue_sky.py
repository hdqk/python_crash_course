# Hector Delgado 5/24/2024

import pygame
import sys

pygame.init()
pygame.display.set_mode((800, 600)).fill((0, 0, 255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()
