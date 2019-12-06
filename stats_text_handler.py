import pygame

pygame.init()
pygame.font.init()

def draw_stats(player, width, height):
    surf = pygame.Surface((width, height))
    font = pygame.font.Font(None, 26)
    new_x = width/4
    new_y = height/14*2
    for key in player.stats:
        stat_text = font.render('{}: {}'.format(key, player.stats[key]), True, WHITE)
        surf.blit(stat_text, (x, y-stat_text.get_height()))
        new_y += height/14
        
    return surf
