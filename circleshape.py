import pygame
import logger

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.x = x
        self.y = y
        self.position = pygame.Vector2(self.x, self.y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass

    def collides_with(self, other):
        other_circle = CircleShape(other.x, other.y, other.radius)
        d = self.position.distance_to(other_circle.position)
        r1 = self.radius
        r2 = other_circle.radius
        threshold = r1+r2
        if d < threshold:
            return True
        else:
            return False
