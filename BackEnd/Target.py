import pygame

class Target:
    def __init__(self, x, y, image, speed_multiplier=1):
        self.x = x
        self.y = y
        self.image = image
        self.speed_multiplier = speed_multiplier
        self.rect = pygame.Rect(x + 20, y, 60, 60)

