from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(color="white", surface=screen, radius=self.radius, center=self.position, width=2)
    
    def update(self, dt):
        for i in range(0, 2):
            self.position[i] += (self.velocity[i] * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        positive_velocity = self.velocity.rotate(angle)
        negative_velocity = self.velocity.rotate(float(f"-{angle}"))
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_1 = Asteroid(self.position[0], self.position[1], new_radius)
        new_asteroid_1.velocity = (positive_velocity * 1.2)
        new_asteroid_2 = Asteroid(self.position[0], self.position[1], new_radius)
        new_asteroid_2.velocity = (negative_velocity * 1.2)