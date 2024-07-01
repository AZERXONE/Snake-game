import random
import pygame
from screen import Screen

class Apple:

    x = 0
    y = 0
    width = 40
    height = 40

    color = (255,0,0)

    def __init__(self):
        
        self.x = random.randrange(5,Screen.screen_x,50)
        self.y = random.randrange(5,Screen.screen_y,50)

    def create(self):

        return pygame.Rect(self.x, self.y, self.height, self.width)

    def draw(self, screen):

        pygame.draw.rect(screen, self.color, self.create())