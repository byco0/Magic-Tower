from constants import *
from map import *


class Item(GeneralSquare):
    def add_to_group(self):
        COLLISION_TYPE.add(self)
        ITEM_TYPE.add(self)


class RedGem(Item):
    ID = 0

    def effect(self, player):
        player.STATE['ATK'] += 3
        return True


class BlueGem(Item):
    ID = 1

    def effect(self, player):
        player.STATE['DEF'] += 3
        return True


class RedPotion(Item):
    ID = 2

    def effect(self, player):
        player.STATE['HP'] += 200
        return True


class BluePotion(Item):
    ID = 3

    def effect(self, player):
        player.STATE['HP'] += 500
        return True


class HolyWater(Item):
    ID = 4

    def effect(self, player):
        player.STATE['HP'] += (player.STATE['ATK'] + player.STATE['DEF']) // 2
        return True


class YellowKey(Item):
    ID = 5

    def effect(self, player):
        player.KEY_COLLECTION['YK'] += 1
        return True


class BlueKey(Item):
    ID = 6

    def effect(self, player):
        player.KEY_COLLECTION['BK'] += 1
        return True


class RedKey(Item):
    ID = 7

    def effect(self, player):
        player.KEY_COLLECTION['RK'] += 1
        return True


class AllKeys(Item):
    ID = 8

    def effect(self, player):
        player.KEY_COLLECTION['YK'] += 1
        player.KEY_COLLECTION['BK'] += 1
        player.KEY_COLLECTION['RK'] += 1
        return True


class Coin(Item):
    ID = 9

    def effect(self, player):
        player.STATE['GOLD'] += 300
        return True


class Pickaxe(Item):
    ID = 10

    def effect(self, player):
        return True


class Compass(Item):
    ID = 11

    def effect(self, player):
        return True


class Cross(Item):
    ID = 12

    def effect(self, player):
        player.STATE['HP'] += player.STATE['HP'] // 3
        player.STATE['ATK'] += player.STATE['ATK'] // 3
        player.STATE['DEF'] += player.STATE['DEF'] // 3
        return True


class Illustration(Item):
    ID = 13

    def effect(self, player):
        return True


class SmallFeather(Item):
    ID = 14

    def effect(self, player):
        player.STATE['LEVEL'] += 1
        player.STATE['HP'] += 1000
        player.STATE['ATK'] += 10
        player.STATE['DEF'] += 10
        return True


class BigFeather(Item):
    ID = 15

    def effect(self, player):
        player.STATE['LEVEL'] += 3
        player.STATE['HP'] += 3000
        player.STATE['ATK'] += 30
        player.STATE['DEF'] += 30
        return True


class Sword(Item):
    ID = 16

    def effect(self, player):
        player.STATE['ATK'] += 10
        return True


class Sword2(Item):
    ID = 17

    def effect(self, player):
        player.STATE['ATK'] += 30
        return True


class Sword3(Item):
    ID = 18

    def effect(self, player):
        player.STATE['ATK'] += 70
        return True


class Sword4(Item):
    ID = 19

    def effect(self, player):
        if player.STATE['EXP'] >= 500:
            player.STATE['ATK'] += 120
            player.STATE['EXP'] -= 500
            return True
        return False


class Sword5(Item):
    ID = 20

    def effect(self, player):
        player.STATE['ATK'] += 150
        return True


class Shield(Item):
    ID = 21

    def effect(self, player):
        player.STATE['DEF'] += 10
        return True


class Shield2(Item):
    ID = 22

    def effect(self, player):
        player.STATE['DEF'] += 30
        return True


class Shield3(Item):
    ID = 23

    def effect(self, player):
        player.STATE['DEF'] += 85
        return True


class Shield4(Item):
    ID = 24

    def effect(self, player):
        if player.STATE['GOLD'] >= 500:
            player.STATE['DEF'] += 120
            player.STATE['GOLD'] -= 500
            return True
        return False


class Shield5(Item):
    ID = 25

    def effect(self, player):
        player.STATE['DEF'] += 190
        return True


class Staff(Item):
    ID = 26

    def effect(self, player):
        player.STATE['ATK'] += 500
        player.STATE['DEF'] += 500
        return True


def get_item(obj):
    # set monsters list
    ITEM_LIST = [RedGem('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 BlueGem('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 RedPotion('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 BluePotion('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 HolyWater('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 YellowKey('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 BlueKey('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 RedKey('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 AllKeys('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 Coin('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 Pickaxe('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 Compass('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 Cross('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 Illustration('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 SmallFeather('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 BigFeather('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 Sword('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 Sword2('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 Sword3('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 Sword4('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 Sword5('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 Shield('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 Shield2('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 Shield3('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 Shield4('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 Shield5('Item', SCREEN_X / 13, SCREEN_Y / 13),
                 Staff('Item', SCREEN_X / 13, SCREEN_Y / 13)]

    return ITEM_LIST[obj]
