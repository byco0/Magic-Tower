import pygame
from constants import *
import os

#surf = pygame.Surface((SCREEN_X, SCREEN_Y))

class floor_square():

    def __init__(self, image, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image)

        self.rect = self.image.get_rect()

    def set_position(self, x, y):
        self.rect = self.rect.move(x, y)

    def draw(self, surface):
        screen.blit(self.image, self.rect[0:2])

    
#test code
pygame.init()
screen = pygame.display.set_mode((800,600))
test = floor_square(IMAGES[0], SCREEN_X/12, SCREEN_Y/12)
test.set_position(60,70)
test.draw(screen)
pygame.display.flip()
