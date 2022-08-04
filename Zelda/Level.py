import pygame




import pygame

import sys

import Spritesheet
#General Setup

pygame.init()
titel = "Empty Title"
pygame.display.set_caption(titel)
screen = pygame.display.set_mode([1200, 800])
clock = pygame.time.Clock()
FPS = 60


#Sound
pygame.mixer.music.load('/Users/morrisschacht/Downloads/Zelda Links Awakening Music - Overworld  Main Theme.mp3')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(.05)


#Player Spritesheet
player_sprite = "/Users/morrisschacht/Downloads/isaiah658's-Pixel-Pack 2/Characters/noah.png"
sprite_sheet_image = pygame.image.load(player_sprite).convert_alpha()
spritesheet = Spritesheet.Spritesheet(sprite_sheet_image)   #clSpritesheet


#player_sprite = "/Users/morrisschacht/Downloads/isaiah658's-Pixel-Pack 2/Characters/noah.png"
#sprite_sheet_image = pygame.image.load(player_sprite).convert_alpha()
#player_spritesheet = Player(sprite_sheet_image)






BLACK = (0,0,0)

#create animation list
action = 0
animation_cooldown = 50 #times between each frame
last_update = pygame.time.get_ticks()
frame = 0



def split_actions():
    animation_list = []
    animation = 4
    animation_steps = 3    #max of 3 frames


    #split array into animations
    for row in range(animation):
        temp_list_img = []
        for column in range(animation_steps):
            temp_list_img.append(spritesheet.get_image(column, row, 16, 18, 3))# frame,column, row,width, height, scale, size
        animation_list.append(temp_list_img)
    return animation_list





velocity = 1
go = True
pos_y= 400
pos_x= 600

#Gameloop
while go:
    fps = clock.tick(FPS)

    animation_list = split_actions()


    #update background
    screen.fill((50, 50, 50))

    #update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame+=1 
        last_update = current_time #go back to first frame
    #run through specific animation
    if frame >= len(animation_list[action]):
        frame = 0 #go back to first frame when at the end of the array




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


