import os
import pygame
from map import *
from constants import *


class Player(GeneralSquare):
    ID = 'default'
    NAME = ''
    STATE = {'LEVEL': 1, 'HP': 1000, 'ATK': 10, 'DEF': 10, 'GOLD': 0, 'EXP': 0}
    KEY_COLLECTION = {'Yellow Key': 1, 'Blue Key': 1, 'Red Key': 1}
    FLOOR = 1
    FLOOR_SET = {FLOOR}
    COMPASS = False
    ILLUSTRATION = False
    WIN = False

    def playSound(self, file):
        effect = pygame.mixer.Sound(os.path.join('Sound', file))
        effect.play()

    def showMessage(self, text):
        width = SCREEN_X - 100
        height = SCREEN_Y // 7
        surf = pygame.Surface((width, height))
        pygame.draw.rect(surf, ORANGE, [0, 0, width, height], 5)
        font = pygame.font.Font(None, width // 25)
        text_print = font.render('{}'.format(text), True, WHITE)
        surf.blit(text_print, (width / 2 - text_print.get_width() / 2, height / 2 - 20))
        screen.blit(surf, (SCREEN_X / 4 + (SCREEN_X - width) / 2, (SCREEN_Y - height) / 2))
        pygame.display.flip()
        pygame.time.wait(750)

    def update(self, pressed_key, overlay, world_overlays, world_floors):
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
                for key in overlay:
                    if type(overlay[key]) == YellowDoor:
                        if pygame.sprite.collide_rect(self, overlay[key]):
                            if self.KEY_COLLECTION['Yellow Key'] > 0:
                                self.KEY_COLLECTION['Yellow Key'] -= 1
                                overlay[key].kill()
                                overlay[key] = 0
                    elif type(overlay[key]) == BlueDoor:
                        if pygame.sprite.collide_rect(self, overlay[key]):
                            if self.KEY_COLLECTION['Blue Key'] > 0:
                                self.KEY_COLLECTION['Blue Key'] -= 1
                                overlay[key].kill()
                                overlay[key] = 0
                    elif type(overlay[key]) == RedDoor:
                        if pygame.sprite.collide_rect(self, overlay[key]):
                            if self.KEY_COLLECTION['Red Key'] > 0:
                                self.KEY_COLLECTION['Red Key'] -= 1
                                overlay[key].kill()
                                overlay[key] = 0

            if pygame.sprite.spritecollideany(self, STAIR_TYPE):
                for key in overlay:
                    if type(overlay[key]) == StairUp:
                        if pygame.sprite.collide_rect(self, overlay[key]):
                            self.FLOOR += 1
                            self.FLOOR_SET = self.FLOOR_SET | {self.FLOOR}
                    elif type(overlay[key]) == StairDown:
                        if pygame.sprite.collide_rect(self, overlay[key]):
                            self.FLOOR -= 1
                            self.FLOOR_SET = self.FLOOR_SET | {self.FLOOR}
                    
            if pygame.sprite.spritecollideany(self, MONSTER_TYPE):
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
                                overlay[key].draw_popup(self)
                                self.playSound('fight.wav')
                                self.STATE['GOLD'] += overlay[key].GOLD
                                self.STATE['EXP'] += overlay[key].EXP
                                if overlay[key].NAME == 'Boss':
                                    self.showMessage('You have conquered the magic tower!')
                                    self.WIN = True
                                overlay[key].kill()
                                overlay[key] = 0
                    except:
                        pass

            if pygame.sprite.spritecollideany(self, NPC_TYPE):
                i = 0
                for key in overlay:
                    try:
                        if pygame.sprite.collide_rect(self, overlay[key]):
                            if overlay[key].ID == 'Fairy':
                                overlay[key].action(world_overlays)
                                self.showMessage('Hi {}! Welcome to Magic Tower! Enjoy your game!'.format(self.NAME))
                                if i == 93:
                                    overlay[key].kill()
                                    overlay[key] = 0
                            elif overlay[key].ID == 'Thief':
                                overlay[key].action(world_overlays)
                                self.showMessage('Thanks for saving me, {}! I will open the magic door in floor 3 for you!'.format(self.NAME))
                                overlay[key].kill()
                                overlay[key] = 0
                            elif overlay[key].ID == 'Princess':
                                self.showMessage('You are my hero, {}! I will wait for you here until you defeat final boss!'.format(self.NAME))
                            else:
                                overlay[key].action(self)
                    except:
                        pass
                    i += 1

            if pygame.sprite.spritecollideany(self, ITEM_TYPE):
                for key in overlay:
                    try:
                        if pygame.sprite.collide_rect(self, overlay[key]):
                            if overlay[key].ID == 10:
                                overlay[key].effect(world_overlays, world_floors)
                                self.showMessage(overlay[key].message)
                                overlay[key].kill()
                                overlay[key] = 0
                            elif overlay[key].effect(self):
                                self.showMessage(overlay[key].message)
                                overlay[key].kill()
                                overlay[key] = 0
                            else:
                                self.showMessage(overlay[key].message)
                    except:
                        pass

            self.rect[0:2] = old_position
        elif self.rect[0] < int(SCREEN_X / 13) or self.rect.right > int(SCREEN_X / 13 * 12) or self.rect[1] < int(SCREEN_Y / 13) or self.rect.bottom > int(SCREEN_Y / 13 * 12):
            self.rect[0:2] = old_position
