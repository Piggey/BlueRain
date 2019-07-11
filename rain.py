import pygame, sys, random
from drop import Drop
pygame.init()

size = width, height = 1024, 360
background = 0, 0, 0
screen = pygame.display.set_mode(size)

droplets = []
for i in range(250):
    x = random.randint(0,width)
    y = random.randint(100,400) * -1
    grav = random.randint(1,5)

    droplets.append(Drop(i, x, y, grav, screen))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(background)
    for obj in droplets:
        obj.fall()

    pygame.display.update()