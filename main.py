import pygame
import sys
import os
from Spritesheet import Spritesheet  # Importiere die Spritesheet-Klasse
from enemy import Enemy  # Importiere die Enemy-Klasse aus der externen Datei
from items.item import Item  # Importiere die Item-Klasse aus der externen Datei
from player import Player  # Importiere die Player-Klasse aus der externen Datei
from collider import Collider  # Importiere die Collider-Klasse aus der externen Datei
from settings import TITEL, FPS, SCREEN_SIZE, BACKGROUND_COLOR_BLUE  # Importiere die Einstellungen
import random 
pygame.init()



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

# Enemy Spritesheet
enemy_sprite = "sprites/enemy.png"
sprite_sheet_image = pygame.image.load(enemy_sprite).convert_alpha()
enemy_spritesheet = Spritesheet(sprite_sheet_image)  # Spritesheet

# Item Spritesheet
item_sprite = "sprites/key.png"  # Item-Spritesheet
item_image = pygame.image.load(item_sprite).convert_alpha()

weapon_sprite = "sprites/weapon.png"  # Item-Spritesheet
weapon_image = pygame.image.load(weapon_sprite).convert_alpha()

potion_sprite = "sprites/potion.png"  # Item-Spritesheet
potion_image = pygame.image.load(potion_sprite).convert_alpha()


# Player Settings
go = True
info_window = False
menu_window = False

# Initialisiere Player, Enemy und Item
player = Player(spritesheet, 600, 400)
enemy = Enemy(enemy_spritesheet, SCREEN_SIZE)
items = [
    Item(item_image, "Key", random.randint(0, 1000), random.randint(0, 800)),
    Item(weapon_image, "Stick", random.randint(0, 1000), random.randint(0, 800)),
    Item(potion_image, "Unko", random.randint(0, 1000), random.randint(0, 800)),
]

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

# Gameloop
while go:
    fps = clock.tick(FPS)

    # Hintergrund aktualisieren
    screen.fill(BACKGROUND_COLOR_BLUE)

    # Event-Handler
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

    # Spieler-Position und Animation aktualisieren
    player.update(fps)

    # Spieler- und Gegner-Zeichenreihenfolge bestimmen
    if player.rect.top <= enemy.rect.top:
        player.draw(screen)  # Spieler zeichnen
        enemy.draw(screen)   # Gegner zeichnen
    else:
        enemy.draw(screen)   # Gegner zeichnen
        player.draw(screen)  # Spieler zeichnen

    # Gegner aktualisieren
    #enemy.update(fps)

    
    


 # Items anzeigen und Kollision überprüfen
    for item in items[:]:  # Durch Kopie der Liste iterieren, um Items entfernen zu können
        item.draw(screen)
        if player.check_collision(item):
            player.inventory.append(item.name)
            print("Collected:", item.name, "Inventory:", player.inventory)
            items.remove(item)  # Item aus der Liste entfernen

    if info_window:
        lines = [
            "Dev Statistic:",
            "",
            f"music={current_theme}",
            f"volume={'%.2f' % pygame.mixer.music.get_volume()}",
            f"frame={player.frame}",
            f"FPS={fps}",
            f"velocity={player.velocity}",
            f"x_coordinate={player.pos_x}",
            f"y_coordinate={player.pos_y}",
            f"collected={str(player.inventory)}"

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

    # Bildschirm aktualisieren
    pygame.display.update()

pygame.quit()
