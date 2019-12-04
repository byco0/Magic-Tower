import pygame
from constants import *
from all_sprites import *


#failed code due to all sprite positions for all levels being registered in collison detection


class GameState():
    floor = 0
        
world_floors = {}

def fetch_floors():
    for key in FLOORS:
        if key > 1:
            break
        world_floors[key] = init_floor(FLOORS[key], block_objects.copy())

state = GameState()
fetch_floors()

pygame.init()
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
player = Player(PLAYER_IMGS[0], SCREEN_X/13, SCREEN_Y/13)
#first_floor = init_floor(FLOOR1, block_objects.copy())
#first_floor = init_floor(FLOORS[0], block_objects.copy())
first_overlay = init_overlay(floor1_overlay, overlay_objects.copy())
init_player(player, floor1_overlay, screen)
pygame.display.flip()


def play_level(floor):   
    running = True
    add_all_to_group(world_floors[floor])

    while running:
        #draw_floor(first_floor, screen)
        draw_floor(world_floors[floor], screen)
        draw_overlay(first_overlay, screen)
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

    remove_all_from_group(world_floors[floor])

running = True

while running:
    play_level(state.floor)
    running = False

pygame.quit()
