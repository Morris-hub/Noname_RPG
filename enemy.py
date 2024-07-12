import pygame
import random

class Enemy:
    def __init__(self, spritesheet, screen_size):
        self.spritesheet = spritesheet
        self.screen_size = screen_size
        self.animation_list = []
        self.load_animations()
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.direction = self.get_random_direction()
        self.speed = 5
        self.step_counter = 0
        self.image = self.get_current_frame()
        self.rect = self.image.get_rect()
        self.rect.center = (self.screen_size[0] // 2, self.screen_size[1] // 2)

    def load_animations(self):
        animation_steps = 4
        animation_rows = 4
        sprite_width = 16
        sprite_height = 20
        scale = 2

        for row in range(animation_rows):
            temp_list = []
            for frame in range(animation_steps):
                temp_list.append(self.spritesheet.get_image(frame, row, sprite_width, sprite_height, scale))
            self.animation_list.append(temp_list)

    def get_random_direction(self):
        if random.choice([True, False]):
            return pygame.Vector2(random.choice([-1, 1]), 0)  # Horizontal
        else:
            return pygame.Vector2(0, random.choice([-1, 1]))  # Vertical

    def get_current_frame(self):
        if self.direction.x < 0:
            return self.animation_list[2][self.frame_index]  # Left
        elif self.direction.x > 0:
            return self.animation_list[3][self.frame_index]  # Right
        elif self.direction.y < 0:
            return self.animation_list[1][self.frame_index]  # Up
        else:
            return self.animation_list[0][self.frame_index]  # Down

    def update(self, fps):
        ANIMATION_COOLDOWN = 100
        current_time = pygame.time.get_ticks()

        if current_time - self.update_time > ANIMATION_COOLDOWN:
            self.frame_index += 1
            self.update_time = current_time
            if self.frame_index >= len(self.animation_list[0]):
                self.frame_index = 0

        # Update position
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed

        # Increment step counter
        self.step_counter += 1

        # Change direction every 15 steps
        if self.step_counter >= 15:
            self.direction = self.get_random_direction()
            self.step_counter = 0

        # Ensure enemy stays within screen bounds
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.screen_size[0]:
            self.rect.right = self.screen_size[0]
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.screen_size[1]:
            self.rect.bottom = self.screen_size[1]

        self.image = self.get_current_frame()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
