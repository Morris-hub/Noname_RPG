import pygame


class Spritesheet:
    def __init__(self, image): # constructor
        self.sheet = image


    def get_image(self, frame,row,  width, height, scale):
        #empty image with width and height
        image = pygame.Surface((width, height)).convert_alpha()
        #split given image to a specific frame
        image.blit(self.sheet, (0, 0), ((frame * width), (row * height), width, height))
        #scale image
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.get_colorkey()
        return image