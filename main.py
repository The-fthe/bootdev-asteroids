import pygame
import player
import signal
import sys
from constants import *


def signal_handler(sig, frame):
    pygame.quit()
    sys.exit(0)


def main():
    pygame.init()
    signal.signal(signal.SIGTERM, signal_handler)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    clock = pygame.time.Clock()

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    ply = player.Player(x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                return
            elif event.type == pygame.KEYDOWN:
                # Add Q key handling
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        ply.update(dt)

        # render
        screen.fill(pygame.Color(0, 0, 0))
        ply.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60FPS
        dt = clock.tick(60.0)/1000


if __name__ == "__main__":
    main()
