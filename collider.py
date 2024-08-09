import pygame

class Collider:
    def __init__(self, player):
        self.player = player

    def check_collision(self, item):
        return self.player.rect.colliderect(item.rect)
