import pygame
import circleshape
import constants
import random


class Asteroid(circleshape.CircleShape):
    h

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return

        # new angle radius and vector
        rand_angle = random.uniform(20, 50)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        vector_a = self.velocity.rotate(rand_angle)
        vector_b = self.velocity.rotate(-rand_angle)

        # create two new asteroids veloctiy
        asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)

        # set two new asteroids veloctiy
        asteroid_a.velocity = 1.2 * vector_a
        asteroid_b.velocity = 1.2 * vector_b
