import pygame

class Obstacle:
    def __init__(self, image, x, y):
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.x = x
        self.y = y
        self.obstacle = True