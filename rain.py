import pygame, sys, random
from drop import Drop
pygame.init()

size = width, height = 1024, 360
background = 0, 0, 0
screen = pygame.display.set_mode(size)

droplets = []
for i in range(500):
    x = random.randint(0,width)
    y = random.randint(100,400) * -1
    grav = random.randint(1,5)
    scale = random.randint(2,4)

    droplets.append(Drop(i, x, y, grav, scale, screen))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(background)
    for obj in droplets:
        obj.fall()

    pygame.display.update()