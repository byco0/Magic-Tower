import pygame
from constants import *

class GeneralSquare(pygame.sprite.Sprite):

    def __init__(self, image, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (int(width)+1, int(height)+1))

        self.rect = self.image.get_rect()
        self.rect[2:] = (self.rect[2]-5, self.rect[3]-3)

    def set_position(self, x, y):
        self.rect = self.rect.move(int(x), int(y))

    def draw(self, surf):
        surf.blit(self.image, self.rect[0:2])

    def add_to_group(self):
        pass

class ImpassableSquare(GeneralSquare):

    def add_to_group(self):
        COLLISION_TYPE.add(self)

class Door(GeneralSquare):

    def __init__(self, image, width, height, door_type):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (int(width), int(height)))

        self.rect = self.image.get_rect()
        self.rect[2:] = (self.rect[2]-5, self.rect[3]-3)

        self.door_type = door_type

    def add_to_group(self):
        COLLISION_TYPE.add(self)
        DOOR_TYPE.add(self)

class Player(GeneralSquare):

    stats = BASE_STATS.copy()

    def update(self, pressed_key, overlay):
        old_position = self.rect[0:2]
        if pressed_key == K_UP:
            self.rect.move_ip(0, int(-SCREEN_Y/13))
        if pressed_key == K_DOWN:
            self.rect.move_ip(0, int(SCREEN_Y/13))
        if pressed_key == K_RIGHT:
            self.rect.move_ip(int(SCREEN_X/13), 0)
        if pressed_key == K_LEFT:
            self.rect.move_ip(int(-SCREEN_X/13), 0)

        if pygame.sprite.spritecollideany(self, COLLISION_TYPE):
            print('collision')
            if pygame.sprite.spritecollideany(self, DOOR_TYPE):
                for key in overlay:
                    try:
                        if overlay[key].door_type in DOORS:
                            if pygame.sprite.collide_rect(self, overlay[key]):
                                if self.stats[DOOR_KEY[overlay[key].door_type]] > 0:
                                    self.stats[DOOR_KEY[overlay[key].door_type]] = self.stats[DOOR_KEY[overlay[key].door_type]] - 1
                                    overlay[key].kill()
                                    overlay[key] = ''
                    except:
                        pass
                        
            self.rect[0:2] = old_position

        elif self.rect[0] < int(SCREEN_X/13) or self.rect.right > int(SCREEN_X/13*12) or self.rect[1] < int(SCREEN_Y/13) or self.rect.bottom > int(SCREEN_Y/13*12):
            self.rect[0:2] = old_position
