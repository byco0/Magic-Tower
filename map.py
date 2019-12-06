from constants import *


class Map(GeneralSquare):
    pass


class Ground(Map):
    ID = 'Ground'


class Impassable(Map):
    def add_to_group(self):
        COLLISION_TYPE.add(self)


class Wall(Impassable):
    ID = 'Wall'


class Star(Impassable):
    ID = 'Star'


class Lava(Impassable):
    ID = 'Lava'


class Stair(Map):
    def add_to_group(self):
        COLLISION_TYPE.add(self)
        STAIR_TYPE.add(self)


class StairUp(Stair):
    ID = 'Up Stair'


class StairDown(Stair):
    ID = 'Down Stair'


class Door(Map):
    def add_to_group(self):
        COLLISION_TYPE.add(self)
        DOOR_TYPE.add(self)


class YellowDoor(Door):
    ID = 'Yellow Door'


class BlueDoor(Door):
    ID = 'Blue Door'


class RedDoor(Door):
    ID = 'Red Door'


class MagicDoor(Door):
    ID = 'Magic Door'


# data structure for map
block_objects = {'block_1': '', 'block_2': '', 'block_3': '', 'block_4': '',
                 'block_5': '', 'block_6': '', 'block_7': '', 'block_8': '',
                 'block_9': '', 'block_10': '', 'block_11': '', 'block_12': '',
                 'block_13': '', 'block_14': '', 'block_15': '', 'block_16': '',
                 'block_17': '', 'block_18': '', 'block_19': '', 'block_20': '',
                 'block_21': '', 'block_22': '', 'block_23': '', 'block_24': '',
                 'block_25': '', 'block_26': '', 'block_27': '', 'block_28': '',
                 'block_29': '', 'block_30': '', 'block_31': '', 'block_32': '',
                 'block_33': '', 'block_34': '', 'block_35': '', 'block_36': '',
                 'block_37': '', 'block_38': '', 'block_39': '', 'block_40': '',
                 'block_41': '', 'block_42': '', 'block_43': '', 'block_44': '',
                 'block_45': '', 'block_46': '', 'block_47': '', 'block_48': '',
                 'block_49': '', 'block_50': '', 'block_51': '', 'block_52': '',
                 'block_53': '', 'block_54': '', 'block_55': '', 'block_56': '',
                 'block_57': '', 'block_58': '', 'block_59': '', 'block_60': '',
                 'block_61': '', 'block_62': '', 'block_63': '', 'block_64': '',
                 'block_65': '', 'block_66': '', 'block_67': '', 'block_68': '',
                 'block_69': '', 'block_70': '', 'block_71': '', 'block_72': '',
                 'block_73': '', 'block_74': '', 'block_75': '', 'block_76': '',
                 'block_77': '', 'block_78': '', 'block_79': '', 'block_80': '',
                 'block_81': '', 'block_82': '', 'block_83': '', 'block_84': '',
                 'block_85': '', 'block_86': '', 'block_87': '', 'block_88': '',
                 'block_89': '', 'block_90': '', 'block_91': '', 'block_92': '',
                 'block_93': '', 'block_94': '', 'block_95': '', 'block_96': '',
                 'block_97': '', 'block_98': '', 'block_99': '', 'block_100': '',
                 'block_101': '', 'block_102': '', 'block_103': '', 'block_104': '',
                 'block_105': '', 'block_106': '', 'block_107': '', 'block_108': '',
                 'block_109': '', 'block_110': '', 'block_111': '', 'block_112': '',
                 'block_113': '', 'block_114': '', 'block_115': '', 'block_116': '',
                 'block_117': '', 'block_118': '', 'block_119': '', 'block_120': '',
                 'block_121': ''}

overlay_objects = {'block_1': '', 'block_2': '', 'block_3': '', 'block_4': '',
                 'block_5': '', 'block_6': '', 'block_7': '', 'block_8': '',
                 'block_9': '', 'block_10': '', 'block_11': '', 'block_12': '',
                 'block_13': '', 'block_14': '', 'block_15': '', 'block_16': '',
                 'block_17': '', 'block_18': '', 'block_19': '', 'block_20': '',
                 'block_21': '', 'block_22': '', 'block_23': '', 'block_24': '',
                 'block_25': '', 'block_26': '', 'block_27': '', 'block_28': '',
                 'block_29': '', 'block_30': '', 'block_31': '', 'block_32': '',
                 'block_33': '', 'block_34': '', 'block_35': '', 'block_36': '',
                 'block_37': '', 'block_38': '', 'block_39': '', 'block_40': '',
                 'block_41': '', 'block_42': '', 'block_43': '', 'block_44': '',
                 'block_45': '', 'block_46': '', 'block_47': '', 'block_48': '',
                 'block_49': '', 'block_50': '', 'block_51': '', 'block_52': '',
                 'block_53': '', 'block_54': '', 'block_55': '', 'block_56': '',
                 'block_57': '', 'block_58': '', 'block_59': '', 'block_60': '',
                 'block_61': '', 'block_62': '', 'block_63': '', 'block_64': '',
                 'block_65': '', 'block_66': '', 'block_67': '', 'block_68': '',
                 'block_69': '', 'block_70': '', 'block_71': '', 'block_72': '',
                 'block_73': '', 'block_74': '', 'block_75': '', 'block_76': '',
                 'block_77': '', 'block_78': '', 'block_79': '', 'block_80': '',
                 'block_81': '', 'block_82': '', 'block_83': '', 'block_84': '',
                 'block_85': '', 'block_86': '', 'block_87': '', 'block_88': '',
                 'block_89': '', 'block_90': '', 'block_91': '', 'block_92': '',
                 'block_93': '', 'block_94': '', 'block_95': '', 'block_96': '',
                 'block_97': '', 'block_98': '', 'block_99': '', 'block_100': '',
                 'block_101': '', 'block_102': '', 'block_103': '', 'block_104': '',
                 'block_105': '', 'block_106': '', 'block_107': '', 'block_108': '',
                 'block_109': '', 'block_110': '', 'block_111': '', 'block_112': '',
                 'block_113': '', 'block_114': '', 'block_115': '', 'block_116': '',
                 'block_117': '', 'block_118': '', 'block_119': '', 'block_120': '',
                 'block_121': ''}


# floor and overlay data
OUTSIDE = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# 0 means wall, 1 means ground, 2 means star, 3 means lava
FLOOR1 = [[0, 2, 2, 2, 2, 1, 2, 2, 2, 2, 0],
          [0, 2, 2, 2, 2, 1, 2, 2, 2, 2, 0],
          [0, 2, 2, 2, 2, 1, 2, 2, 2, 2, 0],
          [0, 2, 2, 2, 2, 1, 2, 2, 2, 2, 0],
          [0, 2, 2, 2, 2, 1, 2, 2, 2, 2, 0],
          [0, 2, 2, 2, 2, 1, 2, 2, 2, 2, 0],
          [0, 0, 2, 2, 2, 1, 2, 2, 2, 0, 0],
          [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
          [3, 0, 3, 0, 1, 1, 1, 0, 3, 0, 3],
          [3, 3, 3, 3, 3, 1, 3, 3, 3, 3, 3],
          [3, 3, 3, 3, 3, 1, 3, 3, 3, 3, 3]]

FLOOR2 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
          [1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
          [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
          [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
          [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
          [0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0],
          [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
          [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1]]

FLOOR3 = ''
FLOOR4 = ''
FLOOR5 = ''
FLOOR6 = ''
FLOOR7 = ''
FLOOR8 = ''
FLOOR9 = ''
FLOOR10 = ''
FLOOR11 = ''
FLOOR12 = ''
FLOOR13 = ''
FLOOR14 = ''
FLOOR15 = ''
FLOOR16 = ''
FLOOR17 = ''
FLOOR18 = ''
FLOOR19 = ''
FLOOR20 = ''

# floors
FLOORS = {0: FLOOR1, 1: FLOOR2, 2: FLOOR3, 3: FLOOR4, 4: FLOOR5, 5: FLOOR6, 6: FLOOR7, 7: FLOOR8, 8: FLOOR9,
          9: FLOOR10, 10: FLOOR11, 11: FLOOR12, 12: FLOOR13, 13: FLOOR14, 14: FLOOR15, 15: FLOOR16, 16: FLOOR17,
          17: FLOOR18, 18: FLOOR19, 19: FLOOR20}

floor1_overlay = [[0,0,0,0,0,'stair2',0,0,0,0,0],
                  [0,0,0,0,0,2,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,'YD',0,0,0,0,0],
                  [0,0,0,0,0,'fairy',0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,1,0,0,0,0,0]]

floor2_overlay = [['stair3',2,'YK','m0','m1','m0',0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0],
                  ['i4',0,'m3','YD',0,0,'i4','YK','i4',0,0],
                  ['YK','m3','i0',0,0,0,'i4','YK','i4',0,0],
                  [0,0,0,0,0,0,0,0,'m4',0,0],
                  ['YK','m5',0,0,0,'YD','m6','m0','m2',0,0],
                  ['i1',0,'BK',0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0],
                  [0,'m5',0,0,0,'RD',0,0,0,'YD',0],
                  ['i4','i5','YK',0,'RK',1,0,0,'YK','m8','BK'],
                  ['i4','i42','YK',0,0,'stair1',0,0,'YK','YK','YK']]

floor3_overlay = []

floor4_overlay = []

floor5_overlay = []

floor6_overlay = []

floor7_overlay = []

floor8_overlay = []

floor9_overlay = []

floor10_overlay = []

floor11_overlay = []

floor12_overlay = []

floor13_overlay = []

floor14_overlay = []

floor15_overlay = []

floor16_overlay = []

floor17_overlay = []

floor18_overlay = []

floor19_overlay = []

floor20_overlay = []

floor_overlays = {0: floor1_overlay, 1: floor2_overlay, 2: floor3_overlay, 3: floor4_overlay, 4: floor5_overlay,
                  5: floor6_overlay, 6: floor7_overlay, 7: floor8_overlay, 8: floor9_overlay, 9: floor10_overlay,
                  10: floor11_overlay, 11: floor12_overlay, 12: floor13_overlay, 13: floor14_overlay, 14: floor15_overlay,
                  15: floor16_overlay, 16: floor17_overlay, 17: floor18_overlay, 18: floor19_overlay, 19: floor20_overlay}

empty_overlay = [[0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0]]