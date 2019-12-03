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
        surface.blit(self.image, self.rect)

    

