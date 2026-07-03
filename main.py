import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_state
import constants
from player import Player

def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)
    _asteroid_field = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        # Limits game to 60 FPS and calculates delta time in seconds
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
