import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        return pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        if self.timer > 0:
            return
        shot_velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED
        shot = Shot(self.position[0], self.position[1], SHOT_RADIUS)
        shot.velocity = shot_velocity
        self.timer = PLAYER_SHOOT_COOLDOWN

    def update(self, dt):
        self.timer -= dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            return self.shoot()
        if keys[pygame.K_w]:
            return self.move(dt)
        if keys[pygame.K_d]:
            return self.rotate(dt)
        # Calculate invert of dt now that it's needed
        inverted_dt = float(f"-{dt}")
        if keys[pygame.K_a]:
            return self.rotate(inverted_dt)
        if keys[pygame.K_s]:
            return self.move(inverted_dt)
    
