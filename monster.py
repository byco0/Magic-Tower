from constants import *


class Monster(GeneralSquare):
    ATK2 = 0
    ATK3 = 0

    def add_to_group(self):
        COLLISION_TYPE.add(self)
        MONSTER_TYPE.add(self)


class GreenSlime(Monster):
    ID = 0
    HP = 50
    ATK = 20
    DEF = 1
    GOLD = 1
    EXP = 1


class RedSlime(Monster):
    ID = 1
    HP = 70
    ATK = 15
    DEF = 2
    GOLD = 2
    EXP = 2


class SmallBat(Monster):
    ID = 2
    HP = 100
    ATK = 20
    DEF = 5
    GOLD = 3
    EXP = 3


class Skeleton(Monster):
    ID = 3
    HP = 110
    ATK = 25
    DEF = 5
    GOLD = 5
    EXP = 4


class BlackSlime(Monster):
    ID = 4
    HP = 200
    ATK = 35
    DEF = 10
    GOLD = 5
    EXP = 5


class SkeletonSoldier(Monster):
    ID = 5
    HP = 150
    ATK = 40
    DEF = 20
    GOLD = 8
    EXP = 6


class JuniorWizard(Monster):
    ID = 6
    HP = 125
    ATK = 50
    DEF = 25
    GOLD = 10
    EXP = 7


class BigBat(Monster):
    ID = 7					
    HP = 150
    ATK = 65
    DEF = 30
    GOLD = 10
    EXP = 8


class Ogre(Monster):
    ID = 8				
    HP = 300
    ATK = 75
    DEF = 45
    GOLD = 13
    EXP = 10


class SkeletonCaptain(Monster):
    ID = 9					
    HP = 400
    ATK = 90
    DEF = 50
    GOLD = 15
    EXP = 12


class RockMonster(Monster):
    ID = 10					
    HP = 500
    ATK = 115
    DEF = 65
    GOLD = 15
    EXP = 15


class Magician(Monster):
    ID = 11					
    HP = 250
    ATK = 120
    ATK2 = 100
    DEF = 70
    GOLD = 20
    EXP = 17


class JuniorGuard(Monster):
    ID = 12					
    HP = 450
    ATK = 150
    DEF = 90
    GOLD = 22
    EXP = 19


class RedBat(Monster):
    ID = 13					
    HP = 550
    ATK = 160
    DEF = 90
    GOLD = 25
    EXP = 20


class SeniorWizard(Monster):
    ID = 14					
    HP = 100
    ATK = 200
    DEF = 110
    GOLD = 30
    EXP = 25


class SlimeKing(Monster):
    ID = 15					
    HP = 700
    ATK = 250
    DEF = 125
    GOLD = 32
    EXP = 30


class WhiteWarrior(Monster):
    ID = 16					
    HP = 1300
    ATK = 150
    ATK3 = 1/4
    DEF = 150
    GOLD = 40
    EXP = 35


class GOLDKnight(Monster):
    ID = 17					
    HP = 850
    ATK = 350
    DEF = 200
    GOLD = 45
    EXP = 40


class RedMagician(Monster):
    ID = 18					
    HP = 500
    ATK = 400
    ATK2 = 300
    DEF = 260
    GOLD = 47
    EXP = 45


class OgreSoldier(Monster):
    ID = 19					
    HP = 900
    ATK = 450
    DEF = 330
    GOLD = 50
    EXP = 50


class GhostGuard(Monster):
    ID = 20					
    HP = 1250
    ATK = 500
    DEF = 400
    GOLD = 55
    EXP = 55


class SeniorGuard(Monster):
    ID = 21					
    HP = 1500
    ATK = 560
    DEF = 460
    GOLD = 60
    EXP = 60


class Swordsman(Monster):
    ID = 22					
    HP = 1200
    ATK = 620
    DEF = 520
    GOLD = 65
    EXP = 75


class GhostWarrior(Monster):
    ID = 23					
    HP = 2000
    ATK = 680
    DEF = 590
    GOLD = 70
    EXP = 65


class RedKnight(Monster):
    ID = 24
    HP = 900
    ATK = 750
    DEF = 650
    GOLD = 77
    EXP = 70


class GhostMagician(Monster):
    ID = 25
    HP = 1500
    ATK = 830
    ATK3 = 1/3
    DEF = 730
    GOLD = 80
    EXP = 70


class GhostMagician2(Monster):
    ID = 25
    HP = 2000
    ATK = 1106
    ATK3 = 1/3
    DEF = 973
    GOLD = 106
    EXP = 93


class GhostMagician3(Monster):
    ID = 25
    HP = 3000
    ATK = 2212
    ATK3 = 1/3
    DEF = 1946
    GOLD = 132
    EXP = 116


class GhostKnight(Monster):
    ID = 26
    HP = 2500
    ATK = 900
    DEF = 800
    GOLD = 84
    EXP = 75


class GhostKnight2(Monster):
    ID = 26
    HP = 3333
    ATK = 1200
    DEF = 1133
    GOLD = 112
    EXP = 100


class ShadowWarrior(Monster):
    ID = 27
    HP = 3100
    ATK = 1150
    DEF = 1050
    GOLD = 92
    EXP = 80   


class BlackWarrior(Monster):
    ID = 28					
    HP = 1200
    ATK = 980
    DEF = 900
    GOLD = 88
    EXP = 75


class BlackWarrior2(Monster):
    ID = 28					
    HP = 1600
    ATK = 1306
    DEF = 1200
    GOLD = 117
    EXP = 100


class BlackWarrior3(Monster):
    ID = 28
    HP = 2400
    ATK = 2612
    DEF = 2400
    GOLD = 146
    EXP = 125 


class RedDevil(Monster):
    ID = 29
    HP = 15000
    ATK = 1000
    DEF = 1000
    GOLD = 100
    EXP = 100


class RedDevil2(Monster):
    ID = 29
    HP = 20000
    ATK = 1333
    DEF = 1333
    GOLD = 133
    EXP = 133


class RedDevil3(Monster):
    ID = 29
    HP = 30000
    ATK = 2666
    DEF = 2666
    GOLD = 166
    EXP = 166  


class Vampire(Monster):
    ID = 30
    HP = 30000
    ATK = 1700
    DEF = 1500
    GOLD = 150
    EXP = 120


class Vampire2(Monster):
    ID = 30
    HP = 45000
    ATK = 2550
    DEF = 2250
    GOLD = 312
    EXP = 275


class Vampire3(Monster):
    ID = 30
    HP = 60000
    ATK = 3400
    DEF = 3000
    GOLD = 390
    EXP = 343  


class Boss1(Monster):
    ID = 31
    HP = 99999
    ATK = 5000
    DEF = 4000
    GOLD = 0
    EXP = 0


class Boss2(Monster):
    ID = 32
    HP = 99999
    ATK = 9999
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
