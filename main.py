import pygame
import random
import copy

from snake import Snake
from apple import Apple
from screen import Screen

pygame.init()

size_x = Screen.screen_x
size_y = Screen.screen_y
screen = pygame.display.set_mode((size_x, size_y))
clock = pygame.time.Clock()

snakes = []

s = Snake()

snakes.append(s)
snakes.append(s)

apple_alive = False

speed = 50
x_speed = 0
y_speed = 0

l = True
r = True
u = True
d = True

score = 0
fps = 10
run = True

while run:

    screen.fill((0,0,0))

    if not apple_alive:
        apple = Apple()
        apple_alive = True
    else:
        apple.draw(screen)

    for snake in snakes:
        snake.draw(screen)

    key = pygame.key.get_pressed()

    if key[pygame.K_a] == True and l:
        new_snake = copy.deepcopy(snakes[-1])
        x_speed = speed * -1
        y_speed = 0
        r = False
        d = True
        u = True

    elif key[pygame.K_d] == True and r:
        new_snake = copy.deepcopy(snakes[-1])
        x_speed = speed
        y_speed = 0
        l = False
        d = True
        u = True

    elif key[pygame.K_w] == True and u:
        new_snake = copy.deepcopy(snakes[-1])
        x_speed = 0
        y_speed = speed * -1
        d = False
        r = True
        l = True

    elif key[pygame.K_s] == True and d:
        new_snake = copy.deepcopy(snakes[-1])
        x_speed = 0
        y_speed = speed
        u = False
        r = True
        l = True

    snakes[0].x += x_speed
    snakes[0].y += y_speed

    for snake in snakes:
        snake.checkOutliing()

    collide = apple.create().colliderect(snakes[0].create())

    if collide:
        apple_alive = False
        snakes.append(new_snake)
        score += 1
        print(score)

    for i in range(len(snakes) - 1, 0, -1):
        snakes[i] = copy.deepcopy(snakes[i - 1])

    if len(snakes) > 3:
        for snake in snakes[3:]:
            if snakes[0].create().colliderect(snake.create()) == True:
                run = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

    clock.tick(fps)

pygame.quit()