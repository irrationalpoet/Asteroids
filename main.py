import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_state
import constants
from player import Player

def main() -> None:
    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode(
        (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
    )
    clock: pygame.time.Clock = pygame.time.Clock()
    dt: float = 0.0
    
    updatable: pygame.sprite.Group = pygame.sprite.Group()
    drawable: pygame.sprite.Group = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    
    asteroids: pygame.sprite.Group = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)
    _asteroid_field = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        screen.fill(color="black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
