import pygame
import sys
from pygame.locals import *

# Initialize program
pygame.init()

# Assign FPS a value
FPS = 30
clock = pygame.time.Clock()

# Setting up color objects
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Setup a 300x300 pixel display with caption
DISPLAYSURF = pygame.display.set_mode((300, 300))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Example")

#                                       posX  posY size
# pygame.draw.rect(DISPLAYSURF, BLACK, (100, 100, 80, 5))


head = pygame.surface.Surface((10, 10))
# Beginning Game Loop


def main():
    while True:
        clock.tick(FPS)
        pygame.display.update()
        DISPLAYSURF.blit(head, (head.x, head.y))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()
