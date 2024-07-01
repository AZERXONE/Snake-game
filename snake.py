import random
import pygame
from screen import Screen

class Snake:

    x = 0
    y = 0
    width = 40
    height = 40

    color = (0,255,0)

    def __init__(self):
        
        self.x = random.randrange(5,Screen.screen_x,50)
        self.y = random.randrange(5,Screen.screen_y,50)

    def create(self):

        return pygame.Rect(self.x, self.y, self.height, self.width)

    def draw(self, screen):

        pygame.draw.rect(screen, self.color, self.create())

    def checkOutliing(self):

        if self.x > Screen.screen_x - 10:
            self.x = 5
        
        if self.x < 5:
            self.x = Screen.screen_x - 45

        if self.y > Screen.screen_y - 10:
            self.y = 5

        if self.y < 5:
            self.y = Screen.screen_y - 45


    def datas(self):

        print(self.x)
        print(self.y)

    def getPrev(self):

        return self
    