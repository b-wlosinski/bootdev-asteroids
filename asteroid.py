import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        super().__init__(self.x,self.y,self.radius)
    
    def draw(self, screen):
        self.center = self.position
        self.screen = screen
        pygame.draw.circle(self.screen, "white", self.center, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position = self.position + (self.velocity * dt)
        self.x = self.position[0]
        self.y = self.position[1]

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        rand_angle = random.uniform(20,50)
        new_velocity = self.velocity.rotate(rand_angle)
        new_op_velocity = self.velocity.rotate(-1 * rand_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.x, self.y, new_radius)
        a2 = Asteroid(self.x, self.y, new_radius)
        a1.velocity = new_velocity * 1.2
        a2. velocity = new_op_velocity * 1.2