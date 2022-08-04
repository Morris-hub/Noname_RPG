import Pygame
import Spritesheet

class Player(Spritesheet.Spritesheet):       #vererbt von Spritesheet

    def __init__(self, image):
        super(Player, self).__init__(image)  # Konstruktoe von Elternklasse
        self.velocity = 5
        self.pos_x = 100
        self.pos_y = 100

    def update_animation(self):
        animation_list = []
        action = 0
        last_update = Pygame.time.get_ticks()

        animation_cooldown = 100
        frame = 0

        #update animation
        current_time = Pygame.time.get_ticks()
        if current_time -last_update >= animation_cooldown:
            frame += 1
            last_update = current_time

        if frame >= len(animation_list[action]):
            frame = 0
    #erstellt image


    def player_movement(self):
        frame = 0

        pressed = Pygame.key.get_pressed()
        if pressed[Pygame.K_DOWN]:
            self.pos_y += self.velocity
           # pygame.display.blit(animation_list[action][frame], (self.pos_x, self.pos_y))  #geh die frames durch in der liste(x,y)

        Pygame.Surface.blit()
        return self.pos_y

      #  elif pressed[pygame.K_UP]:
       # self.pos_y -= self.velocity
        ##return self.pos_y

      #  elif pressed[pygame.K_LEFT]:
       #     self.pos_x -= self.velocity
          #  return self.pos_x

        #elif pressed[pygame.K_RIGHT]:

        #    self.pos_x += self.velocity
        #  return self.pos_x






