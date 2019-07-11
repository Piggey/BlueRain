import pygame, random, time

class Drop(object):
    window_width = 1024
    window_height = 360
    width = 10
    height = 25
    color = 70,130,180

    def __init__(self, number, x, y, gravity, surface):
        self.number = number
        self.x = x
        self.y = y
        self.gravity = gravity
        self.surface = surface

    def fall(self):
        mouse_x = pygame.mouse.get_pos()[0]
        delta = mouse_x - self.x
        self.x += 0.001 * delta
        self.y = self.y + self.gravity

        if(self.y > self.window_height):
            self.y = random.randint(100,400) * -1
            self.x = random.randint(0,self.window_width)
    
        pygame.draw.rect(self.surface, self.color, [self.x, self.y, self.width, self.height])

        