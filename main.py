# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroirds = pygame.sprite.Group()
    shots =  pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)
    Asteroid.containers = (asteroirds, updatable, drawable)
    AsteroidField.containers = (updatable)
   
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    game_is_running = True
    while game_is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, color=SCREEN_COLOR)

        for element in updatable:
            element.update(dt)

        for element in drawable:
            element.draw(screen)

        for asteroid in asteroirds:
            colission_detected = asteroid.is_colliding(player)
            
            if colission_detected:
                print("Game over!") 
                return
            
            for bullet in shots:
                if bullet.is_colliding(asteroid):
                    bullet.kill()
                    asteroid.split()

        pygame.display.flip()

        time = clock.tick(60)
        dt = time / 1000

if __name__ == "__main__":
    main()