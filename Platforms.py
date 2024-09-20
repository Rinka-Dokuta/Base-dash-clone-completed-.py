import pygame
import random

GREEN = (0, 100, 0)
BLUE = (0, 50, 150)

class Platform:
    def __init__(self):
        self.width = random.randint(60,100) #random platform width
        self.height = 30
        self.x = 800 #start at the right side of the screen
        self.y = random.randint(10, 550) #random y postion
        self.speed = random.uniform(3 , 4) #random platform speed
        self.type = random.randint(0, 2) #two types of platforms to start
    
        
    def update(self):
        self.x -= self.speed #move platforms to the left
    
    def draw(self, screen):
        if self.type == 1:
            pygame.draw.rect(screen, GREEN, (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(screen, BLUE, (self.x, self.y, self.width, self.height))
