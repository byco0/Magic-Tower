import pygame

pygame.init()
pygame.font.init()

def draw_battle_box(player, monster, width, height):
    surf = pygame.Surface((x, y))
    font = pygame.font.Font(None, 26)
    new_x = width/4
    new_y = height/4
    vital_stats = ['HP', 'ATT', 'DEF']
    for key in vital_stats:
        stat_text = font.render('{}: {}'.format(key, player.stats[key]), True, WHITE)
        surf.blit(stat_text, (new_x, new_y-stat_text.get_height()))
        new_y += height/4
    new_x width/4*3
    new_y height/4
    for key in vital_stats:
        stat_text = font.render('{}: {}'.format(key, monster.stats[key]), True, WHITE)
        surf.blit(stat_text, (new_x, new_y-stat_text.get_height()))
        new_y += height/4

    return surf
