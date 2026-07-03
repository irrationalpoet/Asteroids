from typing import override
import pygame
from pygame import Vector2, Surface
import circleshape
from shot import Shot
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_SHOOT_COOLDOWN_SECONDS, PLAYER_SHOOT_SPEED, PLAYER_SPEED, PLAYER_TURN_SPEED 

class Player(circleshape.CircleShape):
    position: Vector2

    def __init__(self, x: float, y: float, shot_timer=0.0) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0.0
        self.shot_timer = shot_timer

    def triangle(self) -> list[Vector2]:
        # Calculates the three vertices of the player's triangle based on current rotation.
        forward = Vector2(0,1).rotate(self.rotation)
        right = Vector2(0,1).rotate(self.rotation + 90) * self.radius / 1.5

        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right

        return [a, b, c]
    
    @override
    def draw(self, screen: Surface) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    @override
    def update(self, dt: float) -> None:
        self.shot_timer -= dt

        keys =  pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt: float) -> None:
        unit_vector = Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        self.position += rotated_vector * PLAYER_SPEED * dt

    def shoot(self) -> None:
        if self.shot_timer <= 0:
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.shot_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
        else:
            return
