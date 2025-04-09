from circleshape import *
import random 
from constants import *
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,(255,255,255),(self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return 
        else:
            random_angle = self.velocity.rotate(random.uniform(20, 50))
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            partical1 = Asteroid(self.position.x, self.position.y, new_radius)
            partical2 = Asteroid(self.position.x, self.position.y, new_radius)

            partical1.velocity = random_angle * 1.2
            partical2.velocity = -random_angle * 1.2