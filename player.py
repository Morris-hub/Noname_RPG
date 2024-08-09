import pygame
from Spritesheet import Spritesheet
from collider import Collider

class Player:
    def __init__(self, spritesheet, pos_x, pos_y, velocity=0.25):
        self.spritesheet = spritesheet
        self.velocity = velocity
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.action = 0
        self.frame = 0
        self.animation_cooldown = 100
        self.inventory = []
        self.last_update = pygame.time.get_ticks()

        self.animation_list = self.create_animation_list()
        self.rect = self.animation_list[0][0].get_rect(topleft=(self.pos_x, self.pos_y))
        self.collider = Collider(self)

    def create_animation_list(self):
        animation_list = []
        animation_steps = 4
        animation = 4

        for row in range(animation):
            temp_list_img = []
            for column in range(animation_steps):
                temp_list_img.append(self.spritesheet.get_image(column, row, 16, 20, 2))
            animation_list.append(temp_list_img)

        return animation_list

    def update(self, fps):
        moved = self.handle_input(fps)
        if moved:  # Update animation only if moved
            self.update_animation()

    def handle_input(self, fps):
        moved = False
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_DOWN]:
            self.pos_y += self.velocity * fps
            self.action = 0
            moved = True
        elif pressed[pygame.K_UP]:
            self.pos_y -= self.velocity * fps
            self.action = 1
            moved = True
        elif pressed[pygame.K_LEFT]:
            self.pos_x -= self.velocity * fps
            self.action = 2
            moved = True
        elif pressed[pygame.K_RIGHT]:
            self.pos_x += self.velocity * fps
            self.action = 3
            moved = True
        else:
            self.frame = 0  # Reset to the first frame when not moving

        self.rect.topleft = (self.pos_x, self.pos_y)
        return moved  # Return whether the player has moved

    def update_animation(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.animation_cooldown:
            self.frame += 1
            self.last_update = current_time
        if self.frame >= len(self.animation_list[self.action]):
            self.frame = 0

    def draw(self, screen):
        screen.blit(self.animation_list[self.action][self.frame], self.rect.topleft)

    def check_collision(self, item):
        return self.collider.check_collision(item)
