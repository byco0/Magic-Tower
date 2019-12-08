import os
import pygame
from item import *
from map import *
from monster import *
from player import *
from constants import *


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

        obj = str(level[row][column])
        if obj[0] == 'm':
            struct[key] = get_monster(int(obj[1:]))
            struct[key].set_position(SCREEN_X / 13 + SCREEN_X / 13 * column, SCREEN_Y / 13 + SCREEN_Y / 13 * row)
        elif obj[0] == 'i':
            struct[key] = get_item(int(obj[1:]))
            struct[key].set_position(SCREEN_X / 13 + SCREEN_X / 13 * column, SCREEN_Y / 13 + SCREEN_Y / 13 * row)
        elif obj[0] == 's':
            if int(obj[1:]) > floorNum:
                struct[key] = StairUp('Map', SCREEN_X / 13, SCREEN_Y / 13)
            else:
                struct[key] = StairDown('Map', SCREEN_X / 13, SCREEN_Y / 13)
            struct[key].set_position(SCREEN_X / 13 + SCREEN_X / 13 * column, SCREEN_Y / 13 + SCREEN_Y / 13 * row)
        elif obj == 'YD':
            struct[key] = YellowDoor('Map', SCREEN_X / 13, SCREEN_Y / 13)
            struct[key].set_position(SCREEN_X / 13 + SCREEN_X / 13 * column, SCREEN_Y / 13 + SCREEN_Y / 13 * row)
        elif obj == 'BD':
            struct[key] = BlueDoor('Map', SCREEN_X / 13, SCREEN_Y / 13)
            struct[key].set_position(SCREEN_X / 13 + SCREEN_X / 13 * column, SCREEN_Y / 13 + SCREEN_Y / 13 * row)
        elif obj == 'RD':
            struct[key] = RedDoor('Map', SCREEN_X / 13, SCREEN_Y / 13)
            struct[key].set_position(SCREEN_X / 13 + SCREEN_X / 13 * column, SCREEN_Y / 13 + SCREEN_Y / 13 * row)
        elif obj == 'MD':
            struct[key] = MagicDoor('Map', SCREEN_X / 13, SCREEN_Y / 13)
            struct[key].set_position(SCREEN_X / 13 + SCREEN_X / 13 * column, SCREEN_Y / 13 + SCREEN_Y / 13 * row)

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
        try:
            objects[key].add_to_group()
        except:
            pass


def remove_all_from_group(objects):
    for key in objects:
        try:
            objects[key].kill()
        except:
            pass


def fetch_floors():
    floors = {}
    for key in FLOORS:
        floors[key] = init_floor(FLOORS[key], block_objects.copy())
    return floors


def fetch_overlays():
    overlays = {}
    i = 1
    for key in floor_overlays:
        overlays[key] = init_overlay(floor_overlays[key], overlay_objects.copy(), i)
        i += 1
    return overlays


def draw_stats(player, width, height):
    surf = pygame.Surface((width, height))
    font = pygame.font.Font(None, 40)
    new_x = width / 2
    new_y = height / 7
    state_text = font.render('FLOOR: {}'.format(player.FLOOR), True, WHITE)
    surf.blit(state_text, (new_x, new_y - state_text.get_height()))
    new_y += height / 14
    for key in player.STATE:
        state_text = font.render('{}: {}'.format(key, player.STATE[key]), True, WHITE)
        surf.blit(state_text, (new_x, new_y - state_text.get_height()))
        new_y += height / 14
    for key in player.KEY_COLLECTION:
        state_text = font.render(': {}'.format(player.KEY_COLLECTION[key]), True, WHITE)
        surf.blit(state_text, (new_x + width / 4, new_y - state_text.get_height() / 2))
        img = pygame.image.load(KEY_IMGS[key])
        img = pygame.transform.scale(img, (int(SCREEN_X / 13 + 1), int(SCREEN_Y / 13 + 1)))
        surf.blit(img, (new_x - width / 8, new_y - img.get_height() / 2))
        new_y += height / 14

    wall2 = pygame.image.load(os.path.join('Map', 'Wall2.png'))
    wall2 = pygame.transform.scale(wall2, (int(SCREEN_X / 13) + 1, int(SCREEN_Y / 13) + 1))
    y1 = 0
    y2 = int(SCREEN_Y / 13 * 12)
    for x in range(4):
        surf.blit(wall2, (SCREEN_X / 13 * x, y1))
        surf.blit(wall2, (SCREEN_X / 13 * x, y2))
    x = 0
    for y in range(1, 12):
        surf.blit(wall2, (x, SCREEN_Y / 13 * y))
    return surf

def draw_jump(player, width, height, selected):
    surf = pygame.Surface((width, height))
    pygame.draw.rect(surf, [179, 89, 0], [0, 0, width, height], 5)
    font = pygame.font.Font(None, width//18)
    title = font.render('FLOOR JUMP', True, WHITE)
    surf.blit(title, (width/2-title.get_width()/2, height/10))
    x = width/9
    y = height/4
    font = pygame.font.Font(None, width//23)
    for i in FLOORS:
        if i == selected:
            floor_text = font.render('Floor {}'.format(i+1), True, YELLOW)
        elif i+1 > len(player.FLOOR_SET):
            floor_text = font.render('Floor {}'.format(i+1), True, GREY)
        else:
            floor_text = font.render('Floor {}'.format(i+1), True, WHITE)
        surf.blit(floor_text, (x, y))
        y += height/11
        if i % 7 == 6:
            x += width/3
            y = height/4
    return surf

pygame.init()
pygame.font.init()
pygame.mixer.init()
player = Player('Player', SCREEN_X / 13, SCREEN_Y / 13)
init_player(player, floor_overlays[player.FLOOR - 1], 1)
world_floors = fetch_floors()
world_overlays = fetch_overlays()
surf1 = pygame.Surface((SCREEN_X, SCREEN_Y))
add_all_to_group(world_floors[player.FLOOR - 1])
add_all_to_group(world_overlays[player.FLOOR - 1])
running = True

# Add background music
pygame.mixer.music.load(os.path.join(SOUND_DIR, 'background.mp3'))
pygame.mixer.music.play(-1)

while running:
    draw_floor(world_floors[player.FLOOR - 1], surf1)
    draw_overlay(world_overlays[player.FLOOR - 1], surf1)
    draw_outside(OUTSIDE, surf1)
    player.draw(surf1)
    screen.blit(surf1, (SCREEN_X / 4, 0))
    screen.blit(draw_stats(player, SCREEN_X / 4, SCREEN_Y), (0, 0))
    pygame.display.flip()
    temp = player.FLOOR - 1
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == pygame.K_j:
                screen.blit(draw_jump(player, JUMP_X, JUMP_Y, player.FLOOR-1),(SCREEN_X/4+(SCREEN_X-JUMP_X)/2,(SCREEN_Y-JUMP_Y)/2))
                pygame.display.flip()
                choosing = True
                while choosing:
                    for event in pygame.event.get():
                        if event.type == KEYDOWN:
                            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                                if event.key == pygame.K_UP:
                                    if  player.FLOOR > 1:
                                        player.FLOOR -= 1
                                elif event.key == pygame.K_DOWN:
                                    if  player.FLOOR < len(FLOORS) and player.FLOOR < len(player.FLOOR_SET):
                                        player.FLOOR += 1
                                screen.blit(draw_jump(player, JUMP_X, JUMP_Y,  player.FLOOR-1),(SCREEN_X/4+(SCREEN_X-JUMP_X)/2,(SCREEN_Y-JUMP_Y)/2))
                                pygame.display.flip()
                            elif event.key == pygame.K_RETURN:
                                choosing = False
            else:
                player.update(event.key, world_overlays[player.FLOOR - 1], floor_overlays[player.FLOOR - 1])
    if player.FLOOR - 1 != temp:
        remove_all_from_group(world_floors[temp])
        remove_all_from_group(world_overlays[temp])
        COLLISION_TYPE.empty()
        if player.FLOOR - 1 > temp:
            init_player(player, floor_overlays[player.FLOOR - 1], 1)
        else:
            init_player(player, floor_overlays[player.FLOOR - 1], 2)
        add_all_to_group(world_floors[player.FLOOR - 1])
        add_all_to_group(world_overlays[player.FLOOR - 1])

pygame.mixer.music.stop()
remove_all_from_group(world_floors[player.FLOOR - 1])
remove_all_from_group(world_overlays[player.FLOOR - 1])
pygame.quit()
