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

class Player(generalsquare):

    def update(self, pressed_key):
        if pressed_key



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
    
#test code
pygame.init()
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
draw_floor(Floor1)      
pygame.display.flip()

running = True

while running:
    for event in pygame.event.get()
    if event.type == QUIT:
        running = False
    elif event.type == KEYDOWN:
        if event.key == K_ESCAPE:
            running = False
    pygame.display.flip()

pygame.quit()
