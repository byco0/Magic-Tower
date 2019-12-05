def draw_stats(player, surf):
    x = 100
    y = 75
    for key in player.stats:
        stat_text = font.render('{}: {}'.format(key, player.stats[key]), True, WHITE)
        surf.blit(stat_text, (x, y-stat_text.get_height()))
        y += 60
        
    return surf

