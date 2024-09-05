# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidField import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")
    
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Check for player inputs
        
        # Update the game world
        for updatableObject in updatable:
            updatableObject.update(dt)
            
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collided(shot):
                    asteroid.split()
                    shot.kill()
            if asteroid.collided(player):
                print("Game over!")
                sys.exit()
        
        # Draw the game to the screen
        screen.fill(color=(0, 0, 0))
        for drawableObject in drawable:
            drawableObject.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
