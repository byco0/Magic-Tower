import pygame
from constants import *
from map import *


class Player(GeneralSquare):
    # define collection
    KEY_COLLECTION = {'YK': 1, 'BK': 1, 'RK': 1}
    STATE = {'LEVEL': 1, 'HP': 1000, 'ATK': 10, 'DEF': 10, 'GOLD': 0, 'EXP': 0}
    FLOOR = 1
    FLOOR_SET = {FLOOR}
    ID = 'default'

    def update(self, pressed_key, overlay, floor):
        old_position = self.rect[0:2]
        if pressed_key == K_UP:
            self.rect.move_ip(0, int(-SCREEN_Y / 13))
        elif pressed_key == K_DOWN:
            self.rect.move_ip(0, int(SCREEN_Y / 13))
        elif pressed_key == K_RIGHT:
            self.rect.move_ip(int(SCREEN_X / 13), 0)
        elif pressed_key == K_LEFT:
            self.rect.move_ip(int(-SCREEN_X / 13), 0)

        if pygame.sprite.spritecollideany(self, COLLISION_TYPE):
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
                            self.FLOOR_SET = self.FLOOR_SET | {self.FLOOR}
                    elif type(overlay[key]) == StairDown:
                        if pygame.sprite.collide_rect(self, overlay[key]):
                            self.FLOOR -= 1
                            self.FLOOR_SET = self.FLOOR_SET | {self.FLOOR}
                    i += 1

            if pygame.sprite.spritecollideany(self, MONSTER_TYPE):
                i = 0
                for key in overlay:
                    try:
                        if pygame.sprite.collide_rect(self, overlay[key]):
                            # condition for ability to fight
                            monster_ability = {'HP': overlay[key].HP, 'ATK': overlay[key].ATK, 'ATK2': overlay[key].ATK2, 'ATK3': overlay[key].ATK3, 'DEF': overlay[key].DEF}
                            player_ability = {'HP': self.STATE['HP'], 'ATK': self.STATE['ATK'], 'DEF': self.STATE['DEF']}

                            if monster_ability['ATK'] > player_ability['DEF']:
                                player_minus = monster_ability['ATK'] - player_ability['DEF']
                            else:
                                player_minus = 0

                            if player_ability['ATK'] > monster_ability['DEF']:
                                monster_minus = player_ability['ATK'] - monster_ability['DEF']
                            else:
                                break

                            if monster_ability['ATK2'] != 0:
                                player_ability['HP'] -= monster_ability['ATK2']

                            if monster_ability['ATK3'] != 0:
                                player_ability['HP'] -= player_ability['HP'] // monster_ability['ATK3']

                            while monster_ability['HP'] > 0 and player_ability['HP'] > 0:
                                monster_ability['HP'] -= monster_minus
                                player_ability['HP'] -= player_minus

                            if monster_ability['HP'] <= 0:
                                if monster_ability['ATK2'] != 0:
                                    self.STATE['HP'] -= monster_ability['ATK2']
                                if monster_ability['ATK3'] != 0:
                                    self.STATE['HP'] -= self.STATE['HP'] // monster_ability['ATK3']
                                overlay[key].draw_popup(self, 'fight.wav')
                                self.STATE['GOLD'] += overlay[key].GOLD
                                self.STATE['EXP'] += overlay[key].EXP
                                floor[int(i / 11)][int(i % 11)] = 0
                                overlay[key].kill()
                                overlay[key] = 0
                    except:
                        pass

                i += 1

            if pygame.sprite.spritecollideany(self, ITEM_TYPE):
                i = 0
                for key in overlay:
                    try:
                        if pygame.sprite.collide_rect(self, overlay[key]):
                            self.sound('pickup.wav')
                            if overlay[key].effect(self):
                                floor[int(i / 11)][int(i % 11)] = 0
                                overlay[key].kill()
                                overlay[key] = 0
                    except:
                        pass
                i += 1

            self.rect[0:2] = old_position
        elif self.rect[0] < int(SCREEN_X / 13) or self.rect.right > int(SCREEN_X / 13 * 12) or self.rect[1] < int(SCREEN_Y / 13) or self.rect.bottom > int(SCREEN_Y / 13 * 12):
            self.rect[0:2] = old_position


    def sound(self,file):
        effect = pygame.mixer.Sound(os.path.join(SOUND_DIR, file))
        effect.set_volume(0.3)
        effect.play()
