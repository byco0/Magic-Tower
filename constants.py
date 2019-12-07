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
        self.rect[2:] = (self.rect[2] - self.rect[2]/4, self.rect[3] - self.rect[3]/4)

    def set_position(self, x, y):
        self.rect[0:2] = [x, y]

    def draw(self, surf):
        surf.blit(self.image, self.rect[0:2])

    def add_to_group(self):
        pass


# set some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (64, 64, 64)
YELLOW = (255, 255, 0)

# set the screen constants
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
DISPLAY_SIZE_X = screen.get_width()
DISPLAY_SIZE_Y = screen.get_height()

SCREEN_X = int(DISPLAY_SIZE_X/5*4)
SCREEN_Y = DISPLAY_SIZE_Y

# set the monster popup screen size
POPUP_X = SCREEN_X
POPUP_Y = SCREEN_Y//2
AVATAR = SCREEN_Y//6

# set the jump screen size
JUMP_X = 750
JUMP_Y = 450

# create sprite groups
COLLISION_TYPE = pygame.sprite.Group()
DOOR_TYPE = pygame.sprite.Group()
STAIR_TYPE = pygame.sprite.Group()
MONSTER_TYPE = pygame.sprite.Group()
ITEM_TYPE = pygame.sprite.Group()
NPC_TYPE = pygame.sprite.Group()
PLAYER = pygame.sprite.Group()
KEY_TYPE = pygame.sprite.Group()

#get images
DIR = os.path.dirname(__file__)
ITEM_DIR = os.path.join(DIR,'Item')
NPC_DIR = os.path.join(DIR,'NPC')
MONSTER_DIR = os.path.join(DIR,'Monster')

ITEM_IMGS = []

for x in os.listdir(ITEM_DIR):
    ITEM_IMGS.append(os.path.join(ITEM_DIR, x))

NPC_IMGS = []

for x in os.listdir(NPC_DIR):
    NPC_IMGS.append(os.path.join(NPC_DIR, x))

KEY_IMGS = {'YK': os.path.join(ITEM_DIR, '16.png'), 'BK': os.path.join(ITEM_DIR, '17.png'), 'RK': os.path.join(ITEM_DIR, '18.png')}

#dictionary of key to file locations
KEYS = {'YK': ITEM_IMGS[3], 'BK': ITEM_IMGS[4], 'RK': ITEM_IMGS[5]}
ITEMS = {'i0': ITEM_IMGS[0], 'i1': ITEM_IMGS[1], 'i4': ITEM_IMGS[18], 'i5': ITEM_IMGS[25], 'i42': ITEM_IMGS[20]  }
NPCS = {'fairy': NPC_IMGS[1]}
