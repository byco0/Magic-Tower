import pygame

pygame.init()
pygame.font.init()

def draw_stats(player):
    pygame
    font = pygame.font.Font(None, 26)
    x = 100
    y = 75
    for key in player.stats:
        stat_text = font.render('{}: {}'.format(key, player.stats[key]), True, WHITE)
        surf.blit(stat_text, (x, y-stat_text.get_height()))
        y += 60
        
    return surf
