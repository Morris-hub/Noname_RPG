import pygame
import sys
import os
from Spritesheet import Spritesheet  # Importiere die Spritesheet-Klasse
from enemy import Enemy  # Importiere die Enemy-Klasse aus der externen Datei

pygame.init()

TITEL = "Hello World!"
FPS = 30
SCREEN_SIZE = [1200, 800]
BACKGROUND_COLOR_BLUE = (202, 228, 241)

# Screen Settings
pygame.display.set_caption(TITEL)
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

# Sound
os.chdir(os.path.dirname(__file__))
themes_path = os.path.join(os.getcwd(), "themes/")
sprites_path = os.path.join(os.getcwd(), "sprites/")
fonts_path = os.path.join(os.getcwd(), "fonts/")
current_theme = "Overworld.mp3"

pygame.mixer.music.load(themes_path + current_theme)
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(.05)

fireball_sound = pygame.mixer.Sound(os.path.join(themes_path, "Fireball.mp3"))
fireball_sound.set_volume(.05)

# Player Spritesheet
player_sprite = "sprites/noah.png"
sprite_sheet_image = pygame.image.load(player_sprite).convert_alpha()
spritesheet = Spritesheet(sprite_sheet_image)  # Spritesheet


enemy_sprite = "sprites/enemy.png"
sprite_sheet_image = pygame.image.load(enemy_sprite).convert_alpha()
enemy_spritesheet = Spritesheet(sprite_sheet_image)  # Spritesheet
# Create Animationlist
action = 0
animation_list = []
last_update = pygame.time.get_ticks()
animation_cooldown = 100  # times between each frame
frame = 0  # start frame
animation_steps = 4  # max of 4 frames per animation
animation = 4  # number of animations

# Split array into animations
for row in range(animation):
    temp_list_img = []
    for column in range(animation_steps):
        temp_list_img.append(spritesheet.get_image(column, row, 16, 20, 2))  # frame, column, row, width, height, scale
    animation_list.append(temp_list_img)

# Player Settings
velocity = 0.25
pos_y = 400
pos_x = 600
player_rect = animation_list[0][0].get_rect(topleft=(pos_x, pos_y))
go = True
info_window = False
menu_window = False

def draw_text_window(screen, lines, x, y, width, height):
    font = pygame.font.Font(fonts_path + "VCR_OSD_MONO.ttf", 18)
    window_rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, (255, 255, 255), window_rect)  # Weißer Hintergrund
    pygame.draw.rect(screen, (0, 0, 0), window_rect, 2)  # Schwarzer Rand

    text_y = y + 10  # Startposition für den Text, etwas unterhalb des oberen Rands
    line_spacing = 5  # Abstand zwischen den Zeilen

    for line in lines:
        text_surface = font.render(line, True, (0, 0, 0))
        screen.blit(text_surface, (x + 10, text_y))
        text_y += text_surface.get_height() + line_spacing

enemy = Enemy(enemy_spritesheet, SCREEN_SIZE)

# Gameloop
while go:
    fps = clock.tick(FPS)

    # Update background
    screen.fill(BACKGROUND_COLOR_BLUE)

    # Update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
    if frame >= len(animation_list[action]):
        frame = 0

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.key == pygame.K_i:
                info_window = not info_window
            if event.key == pygame.K_SPACE:
                menu_window = not menu_window
            if event.key == pygame.K_f:
                fireball_sound.play()
            if event.key == pygame.K_m:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1, 0.0)

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_DOWN]:
        pos_y += velocity * fps
        action = 0
    elif pressed[pygame.K_UP]:
        pos_y -= velocity * fps
        action = 1
    elif pressed[pygame.K_LEFT]:
        pos_x -= velocity * fps
        action = 2
    elif pressed[pygame.K_RIGHT]:
        pos_x += velocity * fps
        action = 3
    else:
        frame = 0

    player_rect.topleft = (pos_x, pos_y)

    # Draw based on y position to determine layer
    if player_rect.top <= enemy.rect.top:
        screen.blit(animation_list[action][frame], player_rect.topleft)  # Player
        enemy.draw(screen)  # Enemy
    else:
        enemy.draw(screen)  # Enemy
        screen.blit(animation_list[action][frame], player_rect.topleft)  # Player

    # Update Enemy
    enemy.update(fps)

    if info_window:
        lines = [
            "Dev Statistic:",
            "",
            f"music={current_theme}",
            f"volume={'%.2f' % pygame.mixer.music.get_volume()}",
            f"frame={frame}",
            f"FPS={fps}",
            f"velocity={velocity}",
            f"x_coordinate={pos_x}",
            f"y_coordinate={pos_y}"
        ]
        draw_text_window(screen, lines, 930, 25, 250, 200)

    if menu_window:
        lines = [
            "1. New Game",
            "2. Load Game",
            "3. Save Game",
            "4. Exit Game",
            "5. Options",
            "6. Credits",
            "7. Quit"
        ]
        draw_text_window(screen, lines, 925, 25, 250, 200)

    # Show frame image
    pygame.display.update()

pygame.quit()
