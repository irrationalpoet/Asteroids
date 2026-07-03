import pygame
from pygame import Vector2, Surface

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]

    def __init__(self, x: float, y: float, radius: float) -> None:
        # Checks if child class has defined containers before initializing sprite groups
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()
        
        self.position = Vector2(x, y)
        self.velocity = Vector2(0, 0)
        self.radius = radius
    
    def collides_with(self, other: "CircleShape") -> bool:
        if self.position.distance_to(other.position) <= (self.radius + other.radius):
            return True
        return False

    def draw(self, _screen: Surface) -> None:
        # Overriden
        pass

    def update(self, _dt: float) -> None:
        # Overriden
        pass
