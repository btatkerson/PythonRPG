'''
      Name: __core_race_configuration.py
    Author: Benjamin A
      Date: Jul 7, 2015

   Purpose: This is a core file for the engine that defines the boundaries of the races in the game.
            It limits race types and offers methods that provides information on the core components of races

'''

from core.__core_constants import core_constants
from core.__creature_size_settings import creature_size_settings
from core.__race_settings import race_settings



class core_race_configuration():
    def __init__(self):
        self.__DEFAULT_RACE_TYPE = core_constants().CREATURERACE.HUMAN
        self.__DEFAULT_FAVORED_CLASSES = core_constants().CREATURECLASS.get_index() # All classes
        self.__DEFAULT_FAVORED_DEITIES = []
        self.__DEFAULT_SIZE_CLASS = core_constants().SIZECLASS.MEDIUM
        self.__DEFAULT_BASE_LAND_SPEED = 0

        self.__MIN_ABILITY_BONUS = -2
        self.__MAX_ABILITY_BONUS = 2
        self.__DEFAULT_ABILITY_BONUS = 0

        self.__SIZE_CLASSES = {core_constants().SIZECLASS.FINE:creature_size_settings(core_constants().SIZECLASS.FINE, .5, 0, 8),
                               core_constants().SIZECLASS.DIMINUTIVE:creature_size_settings(core_constants().SIZECLASS.DIMINUTIVE, 1, 0, 4),
                               core_constants().SIZECLASS.TINY:creature_size_settings(core_constants().SIZECLASS.TINY, 2.5, 0, 2),
                               core_constants().SIZECLASS.SMALL:creature_size_settings(core_constants().SIZECLASS.SMALL, 5, 5, 1),
                               core_constants().SIZECLASS.MEDIUM:creature_size_settings(core_constants().SIZECLASS.MEDIUM, 5, 5, 0),
                               core_constants().SIZECLASS.LARGE_TALL:creature_size_settings(core_constants().SIZECLASS.LARGE_TALL, 10, 10, -1),
                               core_constants().SIZECLASS.LARGE_LONG:creature_size_settings(core_constants().SIZECLASS.LARGE_LONG, 10, 5, -1),
                               core_constants().SIZECLASS.HUGE_TALL:creature_size_settings(core_constants().SIZECLASS.HUGE_TALL, 15, 15, -2),
                               core_constants().SIZECLASS.HUGE_LONG:creature_size_settings(core_constants().SIZECLASS.HUGE_LONG, 15, 10, -2),
                               core_constants().SIZECLASS.GARGANTUAN_TALL:creature_size_settings(core_constants().SIZECLASS.GARGANTUAN_TALL, 20, 20, -4),
                               core_constants().SIZECLASS.GARGANTUAN_LONG:creature_size_settings(core_constants().SIZECLASS.GARGANTUAN_LONG, 20, 15, -4),
                               core_constants().SIZECLASS.COLOSSAL_TALL:creature_size_settings(core_constants().SIZECLASS.COLOSSAL_TALL, 30, 30, -8),
                               core_constants().SIZECLASS.COLOSSAL_LONG:creature_size_settings(core_constants().SIZECLASS.COLOSSAL_LONG, 30, 20, -8)}


        self.__PLAYABLE_RACES = {
            core_constants().CREATURERACE.HUMAN:race_settings(True,core_constants().CREATURECLASS.get_index(),None,core_constants().SIZECLASS.MED,None),
            core_constants().CREATURERACE.DWARF:race_settings(True,core_constants().CREATURECLASS.FTR,None,core_constants().SIZECLASS.MED,{'con':2,'chr':-2}),
            core_constants().CREATURERACE.ELF:race_settings(True,core_constants().CREATURECLASS.WIZ,None,core_constants().SIZECLASS.MED,{'dex':2,'con':-2}),
            core_constants().CREATURERACE.GNOME:race_settings(True,core_constants().CREATURECLASS.WIZ,None,core_constants().SIZECLASS.SML,{'con':2,'str':-2}),
            core_constants().CREATURERACE.HALFELF:race_settings(True,core_constants().CREATURECLASS.get_index(),None,core_constants().SIZECLASS.MED,None),
            core_constants().CREATURERACE.HALFORC:race_settings(True,core_constants().CREATURECLASS.BBN,None,core_constants().SIZECLASS.MED,{'str':2,'int':-2,'chr':-2}),
            core_constants().CREATURERACE.HALFLING:race_settings(True,core_constants().CREATURECLASS.ROG,None,core_constants().SIZECLASS.SML,{'dex':2,'str':-2})}

        
    def get_size_class_information(self, size_class=None):
        if core_constants().SIZECLASS.verify(size_class):
            return self.__SIZE_CLASSES[core_constants().SIZECLASS.verify(size_class)]
        return self.__SIZE_CLASSES[core_constants().SIZECLASS.verify(self.__DEFAULT_SIZE_CLASS)]
    
    def get_size_class_information_by_race(self, race=None):
        return self.get_size_class_information(self.get_race_information(race).get_size_class())
 
    def get_race_information(self,race=None):
        if race != None:
            if self.is_playable_race(race):
                return self.__PLAYABLE_RACES[core_constants().CREATURERACE.verify(race)]
        return race_settings(False,self.__DEFAULT_FAVORED_CLASSES,None,self.__DEFAULT_SIZE_CLASS)

    def is_playable_race(self,race=None):
        if core_constants().CREATURERACE.verify(race) in self.__PLAYABLE_RACES:
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
