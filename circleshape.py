import pygame
from pygame import Vector2, Surface

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]
    position: Vector2
    velocity: Vector2
    radius: float

    def __init__(self, x: float, y: float, radius: float) -> None:
        # Checks if child class has defined containers before initializing sprite groups
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()
        
        self.position = Vector2(x, y)
        self.velocity = Vector2(0, 0)
        self.radius = radius

    def draw(self, _screen: Surface) -> None:
        # Overriden
        pass

    def update(self, _dt: float) -> None:
        # Overriden
        pass
