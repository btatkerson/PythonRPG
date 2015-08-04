'''
      Name: __core_race_configuration.py
    Author: Benjamin A
      Date: Jul 7, 2015

   Purpose: This is a core file for the engine that defines the boundaries of the races in the game.
            It limits race types and offers methods that provides information on the core components of races

'''

import core.__core_constants_mod as ccs
from core.__creature_size_settings import creature_size_settings
from core.__race_settings import race_settings



class core_race_configuration():
    def __init__(self):
        self.__DEFAULT_RACE_TYPE = ccs.CREATURERACE.HUMAN
        self.__DEFAULT_FAVORED_CLASSES = ccs.CREATURECLASS.get_index() # All classes
        self.__DEFAULT_FAVORED_DEITIES = []
        self.__DEFAULT_SIZE_CLASS = ccs.SIZECLASS.MEDIUM
        self.__DEFAULT_BASE_LAND_SPEED = 0

        self.__MIN_ABILITY_BONUS = -2
        self.__MAX_ABILITY_BONUS = 2
        self.__DEFAULT_ABILITY_BONUS = 0

        self.__SIZE_CLASSES = {ccs.SIZECLASS.FINE:creature_size_settings(ccs.SIZECLASS.FINE, .5, 0, 8),
                               ccs.SIZECLASS.DIMINUTIVE:creature_size_settings(ccs.SIZECLASS.DIMINUTIVE, 1, 0, 4),
                               ccs.SIZECLASS.TINY:creature_size_settings(ccs.SIZECLASS.TINY, 2.5, 0, 2),
                               ccs.SIZECLASS.SMALL:creature_size_settings(ccs.SIZECLASS.SMALL, 5, 5, 1),
                               ccs.SIZECLASS.MEDIUM:creature_size_settings(ccs.SIZECLASS.MEDIUM, 5, 5, 0),
                               ccs.SIZECLASS.LARGE_TALL:creature_size_settings(ccs.SIZECLASS.LARGE_TALL, 10, 10, -1),
                               ccs.SIZECLASS.LARGE_LONG:creature_size_settings(ccs.SIZECLASS.LARGE_LONG, 10, 5, -1),
                               ccs.SIZECLASS.HUGE_TALL:creature_size_settings(ccs.SIZECLASS.HUGE_TALL, 15, 15, -2),
                               ccs.SIZECLASS.HUGE_LONG:creature_size_settings(ccs.SIZECLASS.HUGE_LONG, 15, 10, -2),
                               ccs.SIZECLASS.GARGANTUAN_TALL:creature_size_settings(ccs.SIZECLASS.GARGANTUAN_TALL, 20, 20, -4),
                               ccs.SIZECLASS.GARGANTUAN_LONG:creature_size_settings(ccs.SIZECLASS.GARGANTUAN_LONG, 20, 15, -4),
                               ccs.SIZECLASS.COLOSSAL_TALL:creature_size_settings(ccs.SIZECLASS.COLOSSAL_TALL, 30, 30, -8),
                               ccs.SIZECLASS.COLOSSAL_LONG:creature_size_settings(ccs.SIZECLASS.COLOSSAL_LONG, 30, 20, -8)}


        self.__PLAYABLE_RACES = {
            ccs.CREATURERACE.HUMAN:race_settings(True,ccs.CREATURECLASS.get_index(),None,ccs.SIZECLASS.MED,None),
            ccs.CREATURERACE.DWARF:race_settings(True,ccs.CREATURECLASS.FTR,None,ccs.SIZECLASS.MED,{'con':2,'chr':-2}),
            ccs.CREATURERACE.ELF:race_settings(True,ccs.CREATURECLASS.WIZ,None,ccs.SIZECLASS.MED,{'dex':2,'con':-2}),
            ccs.CREATURERACE.GNOME:race_settings(True,ccs.CREATURECLASS.WIZ,None,ccs.SIZECLASS.SML,{'con':2,'str':-2}),
            ccs.CREATURERACE.HALFELF:race_settings(True,ccs.CREATURECLASS.get_index(),None,ccs.SIZECLASS.MED,None),
            ccs.CREATURERACE.HALFORC:race_settings(True,ccs.CREATURECLASS.BBN,None,ccs.SIZECLASS.MED,{'str':2,'int':-2,'chr':-2}),
            ccs.CREATURERACE.HALFLING:race_settings(True,ccs.CREATURECLASS.ROG,None,ccs.SIZECLASS.SML,{'dex':2,'str':-2})}

        
    def get_size_class_information(self, size_class=None):
        size_class = ccs.SIZECLASS.verify(size_class)
        if size_class:
            return self.__SIZE_CLASSES[size_class]
        return self.__SIZE_CLASSES[ccs.SIZECLASS.verify(self.__DEFAULT_SIZE_CLASS)] or creature_size_settings()
    
    def get_size_class_information_by_race(self, race=None):
        return self.get_size_class_information(self.get_race_information(race).get_size_class()) or creature_size_settings()
 
    def get_race_information(self,race=None):
        race = ccs.CREATURERACE.verify(race)
        if race:
            if self.is_playable_race(race):
                return self.__PLAYABLE_RACES[race]
        return race_settings(False,self.__DEFAULT_FAVORED_CLASSES,None,self.__DEFAULT_SIZE_CLASS)

    def is_playable_race(self,race=None):
        if ccs.CREATURERACE.verify(race) in self.__PLAYABLE_RACES:
            return True
        return False

    def get_default_race_type(self):
        return self.__DEFAULT_RACE_TYPE

    def get_default_favored_classes(self):
        return self.__DEFAULT_FAVORED_CLASSES

    def get_default_favored_deities(self):
        return self.__DEFAULT_FAVORED_DEITIES

    def get_default_size_class(self):
        return self.__DEFAULT_SIZE_CLASS

    def get_default_base_land_speed(self):
        return self.__DEFAULT_BASE_LAND_SPEED

    def get_min_ability_bonus(self):
        return self.__MIN_ABILITY_BONUS

    def get_max_ability_bonus(self):
        return self.__MAX_ABILITY_BONUS

    def get_default_ability_bonus(self):
        return self.__DEFAULT_ABILITY_BONUS
