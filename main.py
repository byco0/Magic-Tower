import os
import pygame
from map import *
from monster import *
from player import *


def init_floor(level, struct):
    row = 0
    column = 0

    for key in struct:
        if column == 11:
            column = 0
            row += 1
        if level[row][column] == 0:
            struct[key] = Wall('Map', SCREEN_X / 13, SCREEN_Y / 13)
        elif level[row][column] == 1:
            struct[key] = Ground('Map', SCREEN_X / 13, SCREEN_Y / 13)
        elif level[row][column] == 2:
            struct[key] = Star('Map', SCREEN_X / 13, SCREEN_Y / 13)
        elif level[row][column] == 3:
            struct[key] = Lava('Map', SCREEN_X / 13, SCREEN_Y / 13)

        struct[key].set_position(SCREEN_X / 13 + SCREEN_X / 13 * column, SCREEN_Y / 13 + SCREEN_Y / 13 * row)
        column += 1

    return struct


def init_overlay(level, struct, floorNum):
    row = 0
    column = 0

    for key in struct:
        if column == 11:
            column = 0
            row += 1

        obj = level[row][column]
        try:
            int(obj)
        except:
            if obj[0] == 'm':
                struct[key] = get_monster(int(obj[1:]))
                struct[key].set_position(SCREEN_X / 13 + SCREEN_X / 13 * column, SCREEN_Y / 13 + SCREEN_Y / 13 * row)
                struct[key].add_to_group()
            elif obj[0] == 's':
                if int(obj[-1]) > floorNum:
                    struct[key] = StairUp('Map', SCREEN_X / 13, SCREEN_Y / 13)
                else:
                    struct[key] = StairDown('Map', SCREEN_X / 13, SCREEN_Y / 13)
                struct[key].set_position(SCREEN_X / 13 + SCREEN_X / 13 * column, SCREEN_Y / 13 + SCREEN_Y / 13 * row)
                struct[key].add_to_group()
            elif obj == 'YD':
                struct[key] = YellowDoor('Map', SCREEN_X / 13, SCREEN_Y / 13)
                struct[key].set_position(SCREEN_X / 13 + SCREEN_X / 13 * column, SCREEN_Y / 13 + SCREEN_Y / 13 * row)
                struct[key].add_to_group()
            elif obj == 'BD':
                struct[key] = BlueDoor('Map', SCREEN_X / 13, SCREEN_Y / 13)
                struct[key].set_position(SCREEN_X / 13 + SCREEN_X / 13 * column, SCREEN_Y / 13 + SCREEN_Y / 13 * row)
                struct[key].add_to_group()
            elif obj == 'RD':
                struct[key] = RedDoor('Map', SCREEN_X / 13, SCREEN_Y / 13)
                struct[key].set_position(SCREEN_X / 13 + SCREEN_X / 13 * column, SCREEN_Y / 13 + SCREEN_Y / 13 * row)
                struct[key].add_to_group()
            elif obj[1] == 'K':
                struct[key] = Key(KEYS[obj], SCREEN_X/13, SCREEN_Y/13,obj)
                struct[key].set_position(SCREEN_X/13+SCREEN_X/13*column, SCREEN_Y/13+SCREEN_Y/13*row)
                struct[key].add_to_group()
            elif obj[0] == 'i' :
                struct[key] = OtherItem(ITEMS[obj], SCREEN_X/13, SCREEN_Y/13,obj)
                struct[key].set_position(SCREEN_X/13+SCREEN_X/13*column, SCREEN_Y/13+SCREEN_Y/13*row)
                struct[key].add_to_group()
            elif obj[0] == 'f':
                struct[key] = NPC(NPCS[obj], SCREEN_X/13, SCREEN_Y/13,obj)
                struct[key].set_position(SCREEN_X/13+SCREEN_X/13*column, SCREEN_Y/13+SCREEN_Y/13*row)
                struct[key].add_to_group()

        column += 1

    return struct


def init_player(player, level, init):
    for row in range(0, 11):
        for column in range(0, 11):
            if level[row][column] == init:
                player.set_position(SCREEN_X / 13 + SCREEN_X / 13 * column, SCREEN_Y / 13 + SCREEN_Y / 13 * row)
                break


def draw_floor(struct, surf):
    for key in struct:
        struct[key].draw(surf)


def draw_overlay(struct, surf):
    for key in struct:
        try:
            struct[key].draw(surf)
        except:
            pass


def draw_outside(struct, surf):
    row = 0
    column = 0
    wall2 = pygame.image.load(os.path.join('Map', 'Wall2.png'))
    wall2 = pygame.transform.scale(wall2, (int(SCREEN_X / 13) + 1, int(SCREEN_Y / 13) + 1))

    for i in range(169):
        if column == 13:
            column = 0
            row += 1
        if struct[row][column] == 1:
            surf.blit(wall2, (SCREEN_X / 13 * column, SCREEN_Y / 13 * row))
        column += 1


def add_all_to_group(objects):
    for key in objects:
        objects[key].add_to_group()


def remove_all_from_group(objects):
    for key in objects:
        objects[key].kill()


def draw_stats(stats, surf):
    pass


def fetch_floors():
    for key in FLOORS:
        if key > 1:
            break
        world_floors[key] = init_floor(FLOORS[key], block_objects.copy())


world_floors = {}
fetch_floors()
pygame.init()
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
player = Player('Player', SCREEN_X / 13, SCREEN_Y / 13)
overlay = init_overlay(floor_overlays[player.FLOOR - 1], overlay_objects.copy(), player.FLOOR - 1)
init_player(player, floor_overlays[player.FLOOR - 1], 1)
add_all_to_group(world_floors[player.FLOOR - 1])
running = True

while running:
    draw_floor(world_floors[player.FLOOR - 1], screen)
    draw_overlay(overlay, screen)
    draw_outside(OUTSIDE, screen)
    player.draw(screen)
    pygame.display.flip()
    temp = player.FLOOR - 1
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            else:
                player.update(event.key, overlay, floor_overlays[player.FLOOR - 1])
    if player.FLOOR - 1 != temp:
        remove_all_from_group(world_floors[temp])
        COLLISION_TYPE.empty()
        overlay = init_overlay(floor_overlays[player.FLOOR - 1], overlay_objects.copy(), player.FLOOR - 1)
        if player.FLOOR - 1 > temp:
            init_player(player, floor_overlays[player.FLOOR - 1], 1)
        else:
            init_player(player, floor_overlays[player.FLOOR - 1], 2)
        add_all_to_group(world_floors[player.FLOOR - 1])

remove_all_from_group(world_floors[player.FLOOR - 1])
pygame.quit()
