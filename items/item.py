import pygame
from enum import Enum

# Definiere ITEM_TYPE als Enum
ITEM_TYPE = Enum('ITEM_TYPE', 'HEALTH INVENTORY WEAPON')

class Item:
    def __init__(self, image,name, x, y):
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.name = name  # Du kannst den Namen nach Bedarf festlegen
        self.obstacle = False
        self.type = ITEM_TYPE.INVENTORY
        self.x = x
        self.y = y

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
