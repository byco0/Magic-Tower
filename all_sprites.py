import pygame
from constants import *

class GeneralSquare(pygame.sprite.Sprite):

    def __init__(self, image, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (int(width), int(height)))

        self.rect = self.image.get_rect()

    def set_position(self, x, y):
        self.rect = self.rect.move(x, y)

    def draw(self, surface):
        screen.blit(self.image, self.rect[0:2])

    def add_to_group(self):
        pass

class Player(GeneralSquare):

    def update(self, pressed_key):
        if pressed_key == K_UP:
            self.rect.move_ip(0, -SCREEN_Y/13)
        if pressed_key == K_DOWN:
            self.rect.move_ip(0, SCREEN_Y/13)
        if pressed_key == K_RIGHT:
            self.rect.move_ip(SCREEN_X/13, 0)
        if pressed_key == K_LEFT:
            self.rect.move_ip(-SCREEN_X/13, 0)



class ImpassableSquare(GeneralSquare):

    def add_to_group(self):
        COLLISON_TYPE.add(self)
        

def draw_floor(level):
    row = 0
    column = 0

    for key in block_objects:
        if column == 11:
            column = 0
            row += 1

        if level[row][column] in IMPASSABLE_OBJECTS:
            block_objects[key] = ImpassableSquare(TILES[level[row][column]], SCREEN_X/13, SCREEN_Y/13)
        else:    
            block_objects[key] = GeneralSquare(TILES[level[row][column]], SCREEN_X/13, SCREEN_Y/13)
            
        block_objects[key].set_position(SCREEN_X/13+SCREEN_X/13*column, SCREEN_Y/13+SCREEN_Y/13*row)
        block_objects[key].add_to_group()
        block_objects[key].draw(screen)

        column += 1

def draw_player(level):
    row = 0
    column = 0
    for i in range(1, 111):
        if column == 11:
            column = 0
            row += 1
        if level[row][column] == 'init':
            print('found')
            print((SCREEN_X/13+SCREEN_X/13*column, SCREEN_Y/13+SCREEN_Y/13*row))
            player.set_position(SCREEN_X/13+SCREEN_X/13*column, SCREEN_Y/13+SCREEN_Y/13*row)
            player.draw(screen)
        column += 1
    
#test code
pygame.init()
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
player = Player(PLAYER_IMGS[0], SCREEN_X/13, SCREEN_Y/13)
draw_floor(FLOOR1)
draw_player(floor1_overlay)
pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            else:
                draw_floor(FLOOR1)
                player.update(event.key)
                player.draw(screen)
    pygame.display.flip()

pygame.quit()
