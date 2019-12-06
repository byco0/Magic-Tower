# This is a file to store all base values for the game.
import os
import pygame
# import some keys from pygame.locals for easier access
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)


class GeneralSquare(pygame.sprite.Sprite):
    def __init__(self, DIR, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(DIR, '{}.png'.format(self.ID)))
        self.image = pygame.transform.scale(self.image, (int(width)+1, int(height)+1))
        self.rect = self.image.get_rect()
        self.rect[2:] = (self.rect[2] - 5, self.rect[3] - 3)

    def set_position(self, x, y):
        self.rect[0:2] = [x, y]

    def draw(self, surf):
        surf.blit(self.image, self.rect[0:2])

    def add_to_group(self):
        pass


# set some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# set the screen size
SCREEN_X = 800
SCREEN_Y = 600

# create sprite groups
COLLISION_TYPE = pygame.sprite.Group()
DOOR_TYPE = pygame.sprite.Group()
STAIR_TYPE = pygame.sprite.Group()
MONSTER_TYPE = pygame.sprite.Group()
ITEM_TYPE = pygame.sprite.Group()
NPC_TYPE = pygame.sprite.Group()
PLAYER = pygame.sprite.Group()
