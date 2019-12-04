import pygame
import os

# global variables
WIDTH = 800
HEIGHT = 400
BORDER = 20
VELOCITY = 10
FRAMERATE = 50

class Monster(pygame.sprite.Sprite):
    def __init__(self,x,y):
        # call the parent class (Sprite) constructor
        super().__init__()      
        
        # load monster's image
        self.image = pygame.image.load(os.path.join('Monster','{}.png'.format(self.picture)))
        
        # assign monster's position
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
class GreenSlime(Monster):
    picture = 0
    hp = 50
    atk = 20
    def_ = 1
    gold = 1
    exp = 1

class RedSlime(Monster):
    picture = 1
    hp = 70
    atk = 15
    def_ = 2
    gold = 2
    exp = 2

class SmallBat(Monster):
    picture = 2
    hp = 100
    atk = 20
    def_ = 5
    gold = 3
    exp = 3

class Skeleton(Monster):
    picture = 3
    hp = 110
    atk = 25
    def_ = 5
    gold = 5
    exp = 4
    
class BlackSlime(Monster):
    picture = 4
    hp = 200
    atk = 35
    def_ = 10
    gold = 5
    exp = 5

class SkeletonSoldier(Monster):
    picture = 5
    hp = 150
    atk = 40
    def_ = 20
    gold = 8
    exp = 6

class JuniorWizard(Monster):
    picture = 6
    hp = 125
    atk = 50
    def_ = 25
    gold = 10
    exp = 7
    
class BigBat(Monster):
    picture = 7					
    hp = 150
    atk = 65
    def_ = 30
    gold = 10
    exp = 8
    
class Ogre(Monster):
    picture = 8				
    hp = 300
    atk = 75
    def_ = 45
    gold = 13
    exp = 10

class SkeletonCaptain(Monster):
    picture = 9					
    hp = 400
    atk = 90
    def_ = 50
    gold = 15
    exp = 12
    
class RockMonster(Monster):
    picture = 10					
    hp = 500
    atk = 115
    def_ = 65
    gold = 15
    exp = 15
    
class Magician(Monster):
    picture = 11					
    hp = 250
    atk = 120+100
    def_ = 70
    gold = 20
    exp = 17
    
class JuniorGuard(Monster):
    picture = 12					
    hp = 450
    atk = 150
    def_ = 90
    gold = 22
    exp = 19

class RedBat(Monster):
    picture = 13					
    hp = 550
    atk = 160
    def_ = 90
    gold = 25
    exp = 20

class SeniorWizard(Monster):
    picture = 14					
    hp = 100
    atk = 200
    def_ = 110
    gold = 30
    exp = 25

class SlimeKing(Monster):
    picture = 15					
    hp = 700
    atk = 250
    def_ = 125
    gold = 32
    exp = 30

class WhiteWarrior(Monster):
    picture = 16					
    hp = 1300
    atk = 150+hp/4
    def_ = 150
    gold = 40
    exp = 35

class GoldKnight(Monster):
    picture = 17					
    hp = 850
    atk = 350
    def_ = 200
    gold = 45
    exp = 40

class RedMagician(Monster):
    picture = 18					
    hp = 500
    atk = 400+300
    def_ = 260
    gold = 47
    exp = 45

class OgreSoldier(Monster):
    picture = 19					
    hp = 900
    atk = 450
    def_ = 330
    gold = 50
    exp = 50

class GhostGuard(Monster):
    picture = 20					
    hp = 1250
    atk = 500
    def_ = 400
    gold = 55
    exp = 55

class SeniorGuard(Monster):
    picture = 21					
    hp = 1500
    atk = 560
    def_ = 460
    gold = 60
    exp = 60

class Swordsman(Monster):
    picture = 22					
    hp = 1200
    atk = 620
    def_ = 520
    gold = 65
    exp = 75

class GhostWarrior(Monster):
    picture = 23					
    hp = 2000
    atk = 680
    def_ = 590
    gold = 70
    exp = 65

class RedKnight(Monster):
    picture = 24					
    hp = 900
    atk = 750
    def_ = 650
    gold = 77
    exp = 70

class GhostMagician(Monster):
    picture = 25					
    hp = 1500
    atk = 830+hp/3
    def_ = 730
    gold = 80
    exp = 70
    
class GhostMagicianPlus(Monster):
    picture = 25				
    hp = 2000
    atk = 1106+hp/3
    def_ = 973
    gold = 106
    exp = 93

class GhostMagicianPlusPlus(Monster):
    picture = 25					
    hp = 3000
    atk = 2212+hp/3
    def_ = 1946
    gold = 132
    exp = 116   

class GhostKnight(Monster):
    picture = 26					
    hp = 2500
    atk = 900
    def_ = 800
    gold = 84
    exp = 75
    
class GhostKnightPlus(Monster):
    picture = 26					
    hp = 3333
    atk = 1200
    def_ = 1133
    gold = 112
    exp = 100

class ShadowWarrior(Monster):
    picture = 27					
    hp = 3100
    atk = 1150
    def_ = 1050
    gold = 92
    exp = 80   
    
class BlackWarrior(Monster):
    picture = 28					
    hp = 1200
    atk = 980
    def_ = 900
    gold = 88
    exp = 75
    
class BlackWarriorPlus(Monster):
    picture = 28					
    hp = 1600
    atk = 1306
    def_ = 1200
    gold = 117
    exp = 100

class BlackWarriorPlusPlus(Monster):
    picture = 28					
    hp = 2400
    atk = 2612
    def_ = 2400
    gold = 146
    exp = 125 
    
class RedDevil(Monster):
    picture = 29					
    hp = 15000
    atk = 1000
    def_ = 1000
    gold = 100
    exp = 100
    
class RedDevilPlus(Monster):
    picture = 29					
    hp = 20000
    atk = 1333
    def_ = 1333
    gold = 133
    exp = 133

class RedDevilPlusPlus(Monster):
    picture = 29					
    hp = 30000
    atk = 2666
    def_ = 2666
    gold = 166
    exp = 166  
    
class Vampire(Monster):
    picture = 30					
    hp = 30000
    atk = 1700
    def_ = 1500
    gold = 150
    exp = 120
    
class VampirePlus(Monster):
    picture = 30					
    hp = 45000
    atk = 2550
    def_ = 2250
    gold = 312
    exp = 275

class VampirePlusPlus(Monster):
    picture = 30					
    hp = 60000
    atk = 3400
    def_ = 3000
    gold = 390
    exp = 343  
    
class Boss1(Monster):
    picture = 31					
    hp = 99999
    atk = 5000
    def_ = 4000
    gold = 0
    exp = 0
    
class Boss2(Monster):
    picture = 32					
    hp = 99999
    atk = 9999
    def_ = 5000
    gold = 0
    exp = 0
    
# start drawing our scenario:
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
bgColor = pygame.Color("white")
# filling the background
screen.fill(bgColor)

# initialize monsters 
b1=Boss1(0,0)
b2=Boss2(0,100)

# this will be a list that will contain all the monsters we intend to use in our game.
all_monster = pygame.sprite.Group()
all_monster.add(b1)
all_monster.add(b2)

# draw all monsters
all_monster.draw(screen)

while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break
    pygame.display.flip()
pygame.quit() 
