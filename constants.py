# -*- coding: utf-8 -*-
"""
This is a file to store all base values for the game.
"""
import os
import pygame

DIR = os.path.dirname(__file__)
IMG_DIR = os.path.join(DIR, 'Map')
IMAGES = os.listdir(IMG_DIR)

temp = []

for x in IMAGES:
    temp.append(os.path.join(IMG_DIR, x))

IMAGES = temp

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SCREEN_X = 800
SCREEN_Y = 600

HP = 1000
ATT = 10
DEF = 10
GOLD = 0
EXP = 0
RK = 1
BK = 1
YK = 1

ENEMIES = pygame.sprite.Group()
COLLISON_TYPE = pygame.sprite.Group()

TILES = {1: IMAGES[3], 'lava': IMAGES[4], 'star': IMAGES[7],
         0: IMAGES[11]}

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

Floor1 = [[0,'star','star','star','star',1,'star','star','star','star',0],
          [0,'star','star','star','star',1,'star','star','star','star',0],
          [0,'star','star','star','star',1,'star','star','star','star',0],
          [0,'star','star','star','star',1,'star','star','star','star',0],
          [0,'star','star','star','star',1,'star','star','star','star',0],
          [0,'star','star','star','star',1,'star','star','star','star',0],
          [0,0,'star','star','star',1,'star','star','star',0,0],
          [0,0,0,0,0,1,0,0,0,0,0],
          ['lava',0,'lava',0,1,1,1,0,'lava',0,'lava'],
          ['lava','lava','lava','lava','lava',1,'lava','lava','lava','lava','lava'],
          ['lava','lava','lava','lava','lava',1,'lava','lava','lava','lava','lava']]

Floor1_overlay = [[0,0,0,0,0,'stair2',0,0,0,0,0],
                  [0,0,0,0,0,'init',0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,'YD',0,0,0,0,0],
                  [0,0,0,0,0,'fairy',0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,'init',0,0,0,0,0]]

Floor2 = [[1,1,1,1,1,1,1,1,1,1,1],
          [0,0,0,0,0,0,0,0,0,0,1],
          [1,1,1,1,1,0,1,1,1,0,1],
          [1,1,1,0,1,0,1,1,1,0,1],
          [0,1,0,0,1,0,0,0,1,0,1],
          [1,1,1,0,1,1,1,1,1,0,1],
          [1,1,1,0,1,0,0,0,0,0,1],
          [0,1,0,0,1,1,1,1,1,1,1],
          [1,1,1,0,0,1,0,0,0,1,0],
          [1,1,1,0,1,1,1,0,1,1,1],
          [1,1,1,0,1,1,1,0,1,1,1]]

Floor2_overlay = [['stair3','init','YK',0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0],
                  ['i4',0,'m3',0,0,0,'i4','YK','i4',0,0],
                  ['YK','m3','i0',0,0,0,'i4','YK','i4',0,0],
                  [0,0,0,0,0,0,0,0,'m4',0,0],
                  ['YK','m5',0,0,0,0,'m6','m0','m2',0,0],
                  ['i1',0,'BK',0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0],
                  [0,'m5',0,0,0,0,0,0,0,0,0],
                  ['i4','i5','YK',0,'RK','init',0,0,'YK','m8','BK'],
                  ['i4','i42','YK',0,0,'stair1',0,0,'YK','YK','YK']]

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
