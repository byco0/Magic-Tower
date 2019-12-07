import pygame
from constants import *


class Monster(GeneralSquare):
    ATT2 = 0
    ATT3 = 0

    def add_to_group(self):
        COLLISION_TYPE.add(self)
        MONSTER_TYPE.add(self)

    def draw_popup(self,player):
        surf = pygame.Surface((POPUP_X,POPUP_Y))
        surf.fill(GREY)
        pygame.draw.rect(surf, [179, 89, 0], [0, 0, POPUP_X, POPUP_Y], 4)
        font = pygame.font.Font(None, 35)

        # Draw monster
        monsterimg = pygame.image.load(os.path.join(MONSTER_DIR, '{}.png'.format(self.ID)))
        monsterimg = pygame.transform.scale(self.image, (AVATAR, AVATAR))
        mimg_X = POPUP_X/14
        mimg_Y = (POPUP_Y-AVATAR)/3
        surf.blit(monsterimg,(mimg_X,mimg_Y))
        pygame.draw.rect(surf, [179, 89, 0], [mimg_X-10, mimg_Y-10, AVATAR+20, AVATAR+20], 2)
        monstername = font.render(self.NAME, True, WHITE)
        surf.blit(monstername, (mimg_X+AVATAR/2-monstername.get_width()/2, mimg_Y+AVATAR+40))


        # Draw player
        playerimg = pygame.transform.scale(player.image, (AVATAR, AVATAR))
        pimg_X = POPUP_X*11/14
        pimg_Y = (POPUP_Y-AVATAR)/3
        surf.blit(playerimg,(pimg_X,pimg_Y))
        pygame.draw.rect(surf, [179, 89, 0], [pimg_X-10, pimg_Y-10, AVATAR+20, AVATAR+20], 2)
        playername = font.render('Player', True, WHITE)
        surf.blit(playername, (pimg_X+AVATAR/2-playername.get_width()/2,pimg_Y+AVATAR+40))

        while self.HP > 0:
            pygame.draw.rect(surf,GREY,pygame.Rect(POPUP_X*4/14,20,pimg_X-POPUP_X*4/14-10,POPUP_Y-40))
            # Draw VS
            fontbig = pygame.font.Font(None, 60)
            VS_text = fontbig.render('VS', True, WHITE)
            surf.blit(VS_text, (POPUP_X/2-35, POPUP_Y/2-35))
            
            # Monster state
            monsterdict = {'HP': self.HP, 'ATT': self.ATT, 'DEF': self.DEF}
            y = POPUP_Y/5
            for key in monsterdict:
                state_text = font.render('{}:   {}'.format(key, monsterdict[key]), True, WHITE)
                surf.blit(state_text, (POPUP_X*4/14, y))
                y += POPUP_Y/5

            # Player state
            y = POPUP_Y/5
            for key in ['HP','ATT','DEF']:
                state_text = font.render('{}:   {}'.format(key, player.STATE[key]), True, WHITE)
                surf.blit(state_text, (POPUP_X*8/14, y))
                y += POPUP_Y/5

            self.HP_update(player)

            # Display on screen
            screen.blit(surf, ((SCREEN_X*5/4-POPUP_X)/2,SCREEN_Y/6))
            pygame.display.flip()
            pygame.time.wait(600)


    def HP_update(self, player):
        monster_minus = player.STATE['ATT'] - self.DEF
        if monster_minus < 0 :
            monster_minus = 0
        self.HP -= monster_minus

        player_minus = self.ATT - player.STATE['DEF']
        if player_minus < 0:
            player_minus = 0
        player.STATE['HP'] -= player_minus

class GreenSlime(Monster):
    NAME = 'Green Slime'
    ID = 0
    HP = 50
    ATT = 20
    DEF = 1
    GOLD = 1
    EXP = 1


class RedSlime(Monster):
    NAME = 'Red Slime'
    ID = 1
    HP = 70
    ATT = 15
    DEF = 2
    GOLD = 2
    EXP = 2


class SmallBat(Monster):
    NAME = 'Small Bat'
    ID = 2
    HP = 100
    ATT = 20
    DEF = 5
    GOLD = 3
    EXP = 3


class Skeleton(Monster):
    NAME = 'Skeleton'
    ID = 3
    HP = 110
    ATT = 25
    DEF = 5
    GOLD = 5
    EXP = 4


class BlackSlime(Monster):
    NAME = 'Black Slime'
    ID = 4
    HP = 200
    ATT = 35
    DEF = 10
    GOLD = 5
    EXP = 5


class SkeletonSoldier(Monster):
    NAME = 'Skeleton Soldier'
    ID = 5
    HP = 150
    ATT = 40
    DEF = 20
    GOLD = 8
    EXP = 6


class JuniorWizard(Monster):
    NAME = 'Junior Wizard'
    ID = 6
    HP = 125
    ATT = 50
    DEF = 25
    GOLD = 10
    EXP = 7


class BigBat(Monster):
    NAME = 'Big Bat'
    ID = 7
    HP = 150
    ATT = 65
    DEF = 30
    GOLD = 10
    EXP = 8


class Ogre(Monster):
    NAME = 'Orge'
    ID = 8
    HP = 300
    ATT = 75
    DEF = 45
    GOLD = 13
    EXP = 10


class SkeletonCaptain(Monster):
    NAME = 'Skeleton Captain'
    ID = 9
    HP = 400
    ATT = 90
    DEF = 50
    GOLD = 15
    EXP = 12


class RockMonster(Monster):
    NAME = 'Rock Monster'
    ID = 10
    HP = 500
    ATT = 115
    DEF = 65
    GOLD = 15
    EXP = 15


class Magician(Monster):
    NAME = 'Magician'
    ID = 11
    HP = 250
    ATT = 120
    ATT2 = 100
    DEF = 70
    GOLD = 20
    EXP = 17


class JuniorGuard(Monster):
    NAME = 'Junior Guard'
    ID = 12
    HP = 450
    ATT = 150
    DEF = 90
    GOLD = 22
    EXP = 19


class RedBat(Monster):
    NAME = 'Red Bat'
    ID = 13
    HP = 550
    ATT = 160
    DEF = 90
    GOLD = 25
    EXP = 20


class SeniorWizard(Monster):
    NAME = 'Senior Wizard'
    ID = 14
    HP = 100
    ATT = 200
    DEF = 110
    GOLD = 30
    EXP = 25


class SlimeKing(Monster):
    NAME = 'Slime King'
    ID = 15
    HP = 700
    ATT = 250
    DEF = 125
    GOLD = 32
    EXP = 30


class WhiteWarrior(Monster):
    NAME = 'White Warrior'
    ID = 16
    HP = 1300
    ATT = 150
    ATT3 = 1/4
    DEF = 150
    GOLD = 40
    EXP = 35


class GOLDKnight(Monster):
    NAME = 'Gold Knight'
    ID = 17
    HP = 850
    ATT = 350
    DEF = 200
    GOLD = 45
    EXP = 40


class RedMagician(Monster):
    NAME = 'Red Magician'
    ID = 18
    HP = 500
    ATT = 400
    ATT2 = 300
    DEF = 260
    GOLD = 47
    EXP = 45


class OgreSoldier(Monster):
    NAME = 'Orge Soldier'
    ID = 19
    HP = 900
    ATT = 450
    DEF = 330
    GOLD = 50
    EXP = 50


class GhostGuard(Monster):
    NAME = 'Ghost Guard'
    ID = 20
    HP = 1250
    ATT = 500
    DEF = 400
    GOLD = 55
    EXP = 55


class SeniorGuard(Monster):
    NAME = 'Senior Guard'
    ID = 21
    HP = 1500
    ATT = 560
    DEF = 460
    GOLD = 60
    EXP = 60


class Swordsman(Monster):
    NAME = 'Swordsman'
    ID = 22
    HP = 1200
    ATT = 620
    DEF = 520
    GOLD = 65
    EXP = 75


class GhostWarrior(Monster):
    NAME = 'Ghost Warrior'
    ID = 23
    HP = 2000
    ATT = 680
    DEF = 590
    GOLD = 70
    EXP = 65


class RedKnight(Monster):
    NAME = 'Red Knight'
    ID = 24
    HP = 900
    ATT = 750
    DEF = 650
    GOLD = 77
    EXP = 70


class GhostMagician(Monster):
    NAME = 'Ghost Magician'
    ID = 25
    HP = 1500
    ATT = 830
    ATT3 = 1/3
    DEF = 730
    GOLD = 80
    EXP = 70


class GhostMagician2(Monster):
    NAME = 'Ghost Magician 2'
    ID = 25
    HP = 2000
    ATT = 1106
    ATT3 = 1/3
    DEF = 973
    GOLD = 106
    EXP = 93


class GhostMagician3(Monster):
    NAME = 'Ghost Magician 3'
    ID = 25
    HP = 3000
    ATT = 2212
    ATT3 = 1/3
    DEF = 1946
    GOLD = 132
    EXP = 116


class GhostKnight(Monster):
    NAME = 'Ghost Knight'
    ID = 26
    HP = 2500
    ATT = 900
    DEF = 800
    GOLD = 84
    EXP = 75


class GhostKnight2(Monster):
    NAME = 'Ghost Knight 2'
    ID = 26
    HP = 3333
    ATT = 1200
    DEF = 1133
    GOLD = 112
    EXP = 100


class ShadowWarrior(Monster):
    NAME = 'Shadow Warrior'
    ID = 27
    HP = 3100
    ATT = 1150
    DEF = 1050
    GOLD = 92
    EXP = 80


class BlackWarrior(Monster):
    NAME = 'Black Warrior'
    ID = 28
    HP = 1200
    ATT = 980
    DEF = 900
    GOLD = 88
    EXP = 75


class BlackWarrior2(Monster):
    NAME = 'Black Warrior 2'
    ID = 28
    HP = 1600
    ATT = 1306
    DEF = 1200
    GOLD = 117
    EXP = 100


class BlackWarrior3(Monster):
    NAME = 'Black Warrior 3'
    ID = 28
    HP = 2400
    ATT = 2612
    DEF = 2400
    GOLD = 146
    EXP = 125


class RedDevil(Monster):
    NAME = 'Red Devil'
    ID = 29
    HP = 15000
    ATT = 1000
    DEF = 1000
    GOLD = 100
    EXP = 100


class RedDevil2(Monster):
    NAME = 'Red Devil 2'
    ID = 29
    HP = 20000
    ATT = 1333
    DEF = 1333
    GOLD = 133
    EXP = 133


class RedDevil3(Monster):
    NAME = 'Red Devil 3'
    ID = 29
    HP = 30000
    ATT = 2666
    DEF = 2666
    GOLD = 166
    EXP = 166


class Vampire(Monster):
    NAME = 'Vampire'
    ID = 30
    HP = 30000
    ATT = 1700
    DEF = 1500
    GOLD = 150
    EXP = 120


class Vampire2(Monster):
    NAME = 'Vampire 2'
    ID = 30
    HP = 45000
    ATT = 2550
    DEF = 2250
    GOLD = 312
    EXP = 275


class Vampire3(Monster):
    NAME = 'Vampire 3'
    ID = 30
    HP = 60000
    ATT = 3400
    DEF = 3000
    GOLD = 390
    EXP = 343


class Boss1(Monster):
    NAME = 'Boss 1'
    ID = 31
    HP = 99999
    ATT = 5000
    DEF = 4000
    GOLD = 0
    EXP = 0


class Boss2(Monster):
    NAME = 'Boss 2'
    ID = 32
    HP = 99999
    ATT = 9999
    DEF = 5000
    GOLD = 0
    EXP = 0


def get_monster(obj):
    # set monsters list
    MONSTER_LIST = [GreenSlime('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                RedSlime('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                SmallBat('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                Skeleton('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                BlackSlime('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                SkeletonSoldier('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                JuniorWizard('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                BigBat('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                Ogre('Monster', SCREEN_X / 13, SCREEN_Y / 13),
                SkeletonCaptain('Monster', SCREEN_X / 13, SCREEN_Y / 13)]

    return MONSTER_LIST[obj]
