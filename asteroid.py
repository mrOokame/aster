import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y,radius):
        super().__init__(x,y, radius)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20.0, 50.0)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = self.velocity.rotate(random_angle) * 1.2

        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = self.velocity.rotate(-random_angle) * 1.2

    def update(self, dt):
        self.position += self.velocity * dt
  
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
