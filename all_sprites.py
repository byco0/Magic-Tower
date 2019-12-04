import pygame
from constants import *

class GeneralSquare(pygame.sprite.Sprite):

    def __init__(self, image, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (int(width), int(height)))

        self.rect = self.image.get_rect()
        self.rect[2:] = (self.rect[2]-1, self.rect[3]-1)

    def set_position(self, x, y):
        self.rect = self.rect.move(int(x), int(y))

    def draw(self, surface):
        screen.blit(self.image, self.rect[0:2])

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
        self.rect[2:] = (self.rect[2]-1, self.rect[3]-1)

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
            if pygame.sprite.spritecollideany(self, DOOR_TYPE):
                #print('stage1')
                for key in overlay:
                    try:
                        if overlay[key].door_type in DOORS:
                            #print('stage2')
                            if pygame.sprite.collide_rect(self, overlay[key]):
                                if self.stats[DOOR_KEY[overlay[key].door_type]] > 0:
                                    #print('stage3')
                                    self.stats[DOOR_KEY[overlay[key].door_type]] = self.stats[DOOR_KEY[overlay[key].door_type]] - 1
                                    overlay[key].kill()
                                    overlay[key] = ''
                    except:
                        pass
                        
            self.rect[0:2] = old_position
        

def init_floor(level, struct):
    row = 0
    column = 0

    for key in struct:
        if column == 11:
            column = 0
            row += 1

        if level[row][column] in IMPASSABLE_OBJECTS:
            struct[key] = ImpassableSquare(TILES[level[row][column]], SCREEN_X/13, SCREEN_Y/13)
        else:    
            struct[key] = GeneralSquare(TILES[level[row][column]], SCREEN_X/13, SCREEN_Y/13)
            
        struct[key].set_position(SCREEN_X/13+SCREEN_X/13*column, SCREEN_Y/13+SCREEN_Y/13*row)
        struct[key].add_to_group()

        column += 1

    return struct

def draw_player(level):
    row = 0
    column = 0
    for i in range(1, 111):
        if column == 11:
            column = 0
            row += 1
        if level[row][column] == 'init':
            player.set_position(SCREEN_X/13+SCREEN_X/13*column, SCREEN_Y/13+SCREEN_Y/13*row)
            player.draw(screen)
        column += 1

def init_overlay(overlay, struct):
    row = 0
    column = 0

    for key in struct:
        if column == 11:
            column = 0
            row += 1

        try:
            struct[key] = Door(DOORS[overlay[row][column]], SCREEN_X/13, SCREEN_Y/13, overlay[row][column])
            struct[key].set_position(SCREEN_X/13+SCREEN_X/13*column, SCREEN_Y/13+SCREEN_Y/13*row)
            struct[key].add_to_group()
        except:    
            pass

        column += 1

    return struct

def draw_floor(struct):
    
    for key in struct:
        struct[key].draw(screen)

def draw_overlay(struct):
    
    for key in struct:
        try:
            struct[key].draw(screen)
        except:
            pass
    
#test code
pygame.init()
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
player = Player(PLAYER_IMGS[0], SCREEN_X/13, SCREEN_Y/13)
first_floor = init_floor(FLOOR1, block_objects.copy())
first_overlay = init_overlay(floor1_overlay, overlay_objects.copy())
draw_player(floor1_overlay)
pygame.display.flip()


running = True

while running:
    draw_floor(first_floor)
    draw_overlay(first_overlay)
    player.draw(screen)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            else:
                player.update(event.key, first_overlay)
    pygame.display.flip()

pygame.quit()
