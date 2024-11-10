import pygame
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(pygame.Color(0, 0, 0))
        pygame.display.flip()

        # limit the framerate to 60FPS
        dt = clock.tick(60.0)/1000


if __name__ == "__main__":
    main()
