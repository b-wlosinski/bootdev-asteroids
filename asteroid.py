import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH

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