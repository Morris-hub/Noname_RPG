import pygame

class Spritesheet:
    def __init__(self, image): # constructor
        self.sheet = image

    def get_image(self, frame, row, width, height, scale):
        # Empty image with width and height
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        # Split given image to a specific frame
        image.blit(self.sheet, (0, 0), ((frame*width), (row*height), width, height))
        # Scale image
        image = pygame.transform.scale(image, (width*scale, height*scale))
        return image
