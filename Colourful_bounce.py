import pygame
import random

pygame.init()

Sprite_color_change_event = pygame.USEREVENT + 1
Background_color_change_event = pygame.USEREVENT + 2

Blue= pygame.Color('blue')
Red= pygame.Color('red')
Green= pygame.Color('green')
Yellow= pygame.Color('yellow') 
Purple= pygame.Color('purple')
Cyan= pygame.Color('cyan')
White= pygame.Color('white')
Black= pygame.Color('black')

class Sprite(pygame.sprite.Sprite):
    def __init__(self,colour,  width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.velocity = [random.randint(-1, 1), random.randint(-1, 1)]

    def update(self):
        self.rect.move_ip(self.velocity)
        boundry_hit = False
        if self.rect.left < 0 or self.rect.right > 800:
            self.velocity[0] = -self.velocity[0]
            boundry_hit = True
        if boundry_hit:
            pygame.event.post(pygame.event.Event(Sprite_color_change_event))
            pygame.event.post(pygame.event.Event(Background_color_change_event))
    def change_color(self):
        self.image.fill(random.choice([Blue, Red, Green, Yellow, Purple, Cyan, White, Black]))
def change_background_color():
    global bg_color
    bg_color = random.choice([Blue, Red, Green, Yellow, Purple, Cyan, White, Black])
all_sprites = pygame.sprite.Group()
sp1 = Sprite(White, 20, 30)
sp1.rect.x = random.randint(0,480)
sp1.rect.y = random.randint(0,370)
all_sprites.add(sp1)

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Welcome to colourful bounce!!'_'")
bg_color = Blue
screen.fill(bg_color)
exit= False
clock = pygame.time.Clock()

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == Sprite_color_change_event:
            sp1.change_color()
        elif event.type == Background_color_change_event:
            change_background_color()
    all_sprites.update()
    screen.fill(bg_color)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(240)
pygame.quit()