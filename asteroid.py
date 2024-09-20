from circleshape import CircleShape
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(color="white", surface=screen, radius=self.radius, center=self.position, width=2)
    
    def update(self, dt):
        for i in range(0, 2):
            self.position[i] += (self.velocity[i] * dt)
    
