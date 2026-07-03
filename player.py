from typing import override
from pygame import Vector2, Surface, draw, key
import pygame
import circleshape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_SPEED, PLAYER_TURN_SPEED

class Player(circleshape.CircleShape):
    position: Vector2

    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation: float = 0

    def triangle(self) -> list[Vector2]:
        forward: Vector2 = Vector2(0,1).rotate(self.rotation)
        right: Vector2 = Vector2(0,1).rotate(self.rotation + 90) * self.radius / 1.5
        a: Vector2 = self.position + forward * self.radius
        b: Vector2 = self.position - forward * self.radius - right
        c: Vector2 = self.position - forward * self.radius + right
        return [a, b, c]
    
    @override
    def draw(self, screen: Surface) -> None:
        color: str = "white"
        points: list[Vector2] = self.triangle()
        width: int = LINE_WIDTH
        pygame.draw.polygon(screen, color, points, width)

    def rotate(self, dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    @override
    def update(self, dt: float) -> None:
        keys: key.ScancodeWrapper = key.get_pressed()
        
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_w]:
            self.move(dt)

    def move(self, dt: float) -> None:
        unit_vect: Vector2 = Vector2(0, 1)
        rotated_vect: Vector2 = unit_vect.rotate(self.rotation)
        self.position += rotated_vect * PLAYER_SPEED * dt
