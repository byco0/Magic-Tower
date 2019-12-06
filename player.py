import pygame
from constants import *
from map import *


class Player(GeneralSquare):
    # define collection
    KEY_COLLECTION = {'YK': 1, 'BK': 1, 'RK': 1}
    STATE = {'HP' : 1000, 'ATT' : 10, 'DEF' : 10, 'GOLD' : 0, 'EXP' : 0, 'LEVEL' : 1}    
    
    FLOOR = 1
    ID = 'default'

    def update(self, pressed_key, overlay, floor):
        old_position = self.rect[0:2]
        if pressed_key == K_UP:
            self.rect.move_ip(0, int(-SCREEN_Y / 13))
        if pressed_key == K_DOWN:
            self.rect.move_ip(0, int(SCREEN_Y / 13))
        if pressed_key == K_RIGHT:
            self.rect.move_ip(int(SCREEN_X / 13), 0)
        if pressed_key == K_LEFT:
            self.rect.move_ip(int(-SCREEN_X / 13), 0)
        if pygame.sprite.spritecollideany(self, KEY_TYPE):
            i = 0
            for key in overlay:
                try:
                    if overlay[key].type in KEYS:
                        if pygame.sprite.collide_rect(self, overlay[key]):
                            self.KEY_COLLECTION[overlay[key].type] += 1
                            floor[int(i / 11)][int(i % 11)] = 0
                            overlay[key].kill()
                            overlay[key] = 0
                            print(self.KEY_COLLECTION)
                except:
                    pass
            i += 1
        if pygame.sprite.spritecollideany(self, ITEM_TYPE):
            i = 0
            for key in overlay:
                try:
                    if overlay[key].type in ITEMS:
                        if pygame.sprite.collide_rect(self, overlay[key]):
                            floor[int(i / 11)][int(i % 11)] = 0
                            overlay[key].kill()
                            overlay[key] = 0
                except:
                    pass
            i += 1
        if pygame.sprite.spritecollideany(self, NPC_TYPE):
            i = 0
            for key in overlay:
                try:
                    if overlay[key].type in NPCS:
                        if pygame.sprite.collide_rect(self, overlay[key]):
                            floor[int(i / 11)][int(i % 11)] = 0
                            overlay[key].kill()
                            overlay[key] = 0
                except:
                    pass
                        
            i += 1
        if pygame.sprite.spritecollideany(self, COLLISION_TYPE):
            print('collision')

            if pygame.sprite.spritecollideany(self, DOOR_TYPE):
                i = 0
                for key in overlay:
                    if type(overlay[key]) == YellowDoor:
                        if pygame.sprite.collide_rect(self, overlay[key]):
                            if self.KEY_COLLECTION['YK'] > 0:
                                self.KEY_COLLECTION['YK'] -= 1
                                floor[int(i / 11)][int(i % 11)] = 0
                                overlay[key].kill()
                                overlay[key] = 0
                    elif type(overlay[key]) == BlueDoor:
                        if pygame.sprite.collide_rect(self, overlay[key]):
                            if self.KEY_COLLECTION['BK'] > 0:
                                self.KEY_COLLECTION['BK'] -= 1
                                floor[int(i / 11)][int(i % 11)] = 0
                                overlay[key].kill()
                                overlay[key] = 0
                    elif type(overlay[key]) == RedDoor:
                        if pygame.sprite.collide_rect(self, overlay[key]):
                            if self.KEY_COLLECTION['RK'] > 0:
                                self.KEY_COLLECTION['RK'] -= 1
                                floor[int(i / 11)][int(i % 11)] = 0
                                overlay[key].kill()
                                overlay[key] = 0
                    i += 1

            if pygame.sprite.spritecollideany(self, STAIR_TYPE):
                i = 0
                for key in overlay:
                    if type(overlay[key]) == StairUp:
                        if pygame.sprite.collide_rect(self, overlay[key]):
                            self.FLOOR += 1
                    elif type(overlay[key]) == StairDown:
                        if pygame.sprite.collide_rect(self, overlay[key]):
                            self.FLOOR -= 1
                    i += 1
                    
            self.rect[0:2] = old_position
        elif self.rect[0] < int(SCREEN_X / 13) or self.rect.right > int(SCREEN_X / 13 * 12) or self.rect[1] < int(SCREEN_Y / 13) or self.rect.bottom > int(SCREEN_Y / 13 * 12):
            self.rect[0:2] = old_position
