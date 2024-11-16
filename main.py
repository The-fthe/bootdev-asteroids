import pygame
import signal
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def signal_handler(sig, frame):
    pygame.quit()
    sys.exit(0)


def main():
    pygame.init()
    signal.signal(signal.SIGTERM, signal_handler)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_WIDTH / 2)

    dt = 0

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

        for u in updatable:
            u.update(dt)

        for a in asteroids:
            if a.collision_with(player):
                print("Game over!")
                pygame.quit()
                sys.exit()
            for s in shots:
                if s.collision_with(a):
                    s.kill()
                    a.kill()

        # render
        screen.fill(pygame.Color(0, 0, 0))
        for d in drawable:
            d.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60FPS
        dt = clock.tick(60.0)/1000


if __name__ == "__main__":
    main()
