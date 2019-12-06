import pygame

pygame.init()
pygame.font.init()

def draw_stats(player, x, y):
    surf = pygame.Surface((x, y))
    font = pygame.font.Font(None, 26)
    new_x = x/4
    new_y = y/10
    for key in player.stats:
        stat_text = font.render('{}: {}'.format(key, player.stats[key]), True, WHITE)
        surf.blit(stat_text, (x, y-stat_text.get_height()))
        new_y += y/10
        
    return surf
