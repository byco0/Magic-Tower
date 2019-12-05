from constants import *
from all_sprites import *

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

        column += 1

    return struct

def init_player(player, level, surf):
    row = 0
    column = 0
    for i in range(1, 111):
        if column == 11:
            column = 0
            row += 1
        if level[row][column] == 'init':
            player.set_position(SCREEN_X/13+SCREEN_X/13*column, SCREEN_Y/13+SCREEN_Y/13*row)
            player.draw(surf)
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

def draw_outside(struct, surf):
    row = 0
    column = 0
    wall = pygame.image.load(MAP_IMGS[10])
    wall = pygame.transform.scale(wall, (int(SCREEN_X/13)+1, int(SCREEN_Y/13)+1))

    for i in range(169):
        if column == 13:
            column = 0
            row += 1

        if struct[row][column] == 1:
            surf.blit(wall, (SCREEN_X/13*column, SCREEN_Y/13*row))

        column += 1

def draw_floor(struct, surf):
    
    for key in struct:
        struct[key].draw(surf)

def draw_overlay(struct, surf):
    
    for key in struct:
        try:
            struct[key].draw(surf)
        except:
            pass

def add_all_to_group(objects):
    for key in objects:
        objects[key].add_to_group()

def remove_all_from_group(objects):
    for key in objects:
        objects[key].kill()

def draw_stats(stats, surf):
    pass
