import pygame
import sys
import Spritesheet

pygame.init()

TITEL = "Empty Title"
FPS = 30
SCREEN_SIZE = [1200, 800]
BACKGROUND_COLOR_BLACK = (0,0,0)
BACKGROUND_COLOR_GREY = (100,100,100)

#Screen Settings
pygame.display.set_caption(TITEL)
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()


#Sound
pygame.mixer.music.load("themes/Overworld.mp3")
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(.05)


#Player Spritesheet
player_sprite = "sprites/noah.png"
sprite_sheet_image = pygame.image.load(player_sprite).convert_alpha()
spritesheet = Spritesheet.Spritesheet(sprite_sheet_image)   #Spritesheet


#Create Animationlist
action = 0
animation_list = []
last_update = pygame.time.get_ticks()
animation_cooldown = 50 #times between each frame
frame = 0               #start frame
animation_steps = 3    #max of 3 frames
animation = 4



#Split array into animations
for row in range(animation):
    temp_list_img = []
    for column in range(animation_steps):
        temp_list_img.append(spritesheet.get_image(column, row, 16, 20, 2))# frame,column, row,width, height, scale, size
    animation_list.append(temp_list_img)

#Player Settings
velocity = 0.25
pos_y= 400
pos_x= 600
go = True

#Gameloop
while go:
    fps = clock.tick(FPS)

    #update background
    screen.fill(BACKGROUND_COLOR_BLACK)

    #update animation
    current_time = pygame.time.get_ticks()
    if current_time -last_update >= animation_cooldown:
        frame+=1
        last_update = current_time
    #run through specific animation
    if frame >= len(animation_list[action]):
        frame = 0




    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                sys.exit()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_DOWN]:
        pos_y += velocity*fps
        action = 0
        screen.blit(animation_list[action][frame], (pos_x, pos_y))  #geh die frames durch in der liste(x,y)

    elif pressed[pygame.K_UP]:
        pos_y -= velocity*fps
        action = 1
        screen.blit(animation_list[action][frame], (pos_x, pos_y))  #geh die frames durch in der liste(x,y)

    elif pressed[pygame.K_LEFT]:
        pos_x -= velocity*fps
        action = 2
        screen.blit(animation_list[action][frame], (pos_x, pos_y))  #geh die frames durch in der liste(x,y)

    elif pressed[pygame.K_RIGHT]:
        pos_x+= velocity*fps
        action = 3
        screen.blit(animation_list[action][frame], (pos_x, pos_y))  #geh die frames durch in der liste(x,y)

    else:
        screen.blit(animation_list[action][0], (pos_x, pos_y))  #geh die frames durch in der liste(x,y)
        print (pos_x, pos_y)

#show frame image

    pygame.display.update()
pygame.quit()


