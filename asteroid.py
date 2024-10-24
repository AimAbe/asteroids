import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
         super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self,):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            vector_one = self.velocity.rotate(random_angle)
            vector_two = self.velocity.rotate(-random_angle)
            
            radius_change = self.radius - ASTEROID_MIN_RADIUS 
            
            split_asteroid = Asteroid(self.position.x, self.position.y, radius_change)
            split_asteroid.velocity = vector_one * 1.2
            
            split_asteroid = Asteroid(self.position.x, self.position.y, radius_change)
            split_asteroid.velocity = vector_two * 1.2