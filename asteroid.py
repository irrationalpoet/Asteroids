from typing import override
import pygame
from pygame import Surface
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    @override
    def draw(self, screen: Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    @override
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid split")
        new_asteroids_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_1 = Asteroid(self.position.x, self.position.y, new_asteroids_radius) # type: ignore
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_asteroids_radius) # type: ignore
       
        rand_angle = random.uniform(20, 50)

        asteroid_1.velocity = self.velocity.rotate(rand_angle)
        asteroid_2.velocity = self.velocity.rotate(-rand_angle)


