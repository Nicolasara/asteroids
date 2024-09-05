import pygame
from random import uniform
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
        
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        if (new_radius < ASTEROID_MIN_RADIUS):
            return
        
        angle = uniform(20, 50)
        asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
        new_velocity = self.velocity * 1.2
        asteroid_a.velocity = new_velocity.rotate(angle)
        asteroid_b.velocity = new_velocity.rotate(-angle)