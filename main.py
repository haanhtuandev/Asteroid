import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import sys
def main():
    pygame.init
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    asteroid_field = AsteroidField()

# Change the game loop to use the new groups instead of the Player object directly.
# Call the .update() method on the "updatables" group.
# Loop over all "drawables" and .draw() them individually.

    while True:
        pygame.Surface.fill(screen, (0,0,0))
        updatable.update(dt)

        # Draw all objects in the `drawables` group
        for sprite in drawable:
            sprite.draw(screen)  # Calls .draw(screen) on each sprite
        
        for asteroid in asteroids:
            if asteroid.is_collided(player):
                print("Game over!")
                sys.exit()
            for bullet in shots:
                if asteroid.is_collided(bullet):
                    bullet.kill()
                    asteroid.split()
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()