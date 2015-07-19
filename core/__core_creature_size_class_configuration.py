'''
      Name: __core_creature_size_configuration.py
    Author: Benjamin A
      Date: Jul 7, 2015
    
   Purpose: This holds the core data of size classes. This may not be necessary since
            size classes may not need to be extendable
       
'''


from core.__core_constants import core_constants

class core_creature_size_configuration():
    def __init__(self):
        self.__DEFAULT_SIZE_CLASS = core_constants().SIZECLASS.MEDIUM

        self.__MIN_SPACE_IN_FEET = .5 
        self.__MAX_SPACE_IN_FEET = 30
        self.__DEFAULT_SPACE_IN_FEET = 5

        self.__MIN_REACH_DISTANCE = 0
        self.__MAX_REACH_DISTANCE = 30
        self.__DEFAULT_REACH_DISTANCE = 5

        self.__MIN_SIZE_MODIFIER = -8
        self.__MAX_SIZE_MODIFIER = 8
        self.__DEFAULT_SIZE_MODIFIER = 0

    def get_default_size_class(self):
        return self.__DEFAULT_SIZE_CLASS

    def get_min_space_in_feet(self):
        return self.__MIN_SPACE_IN_FEET

    def get_max_space_in_feet(self):
        return self.__MAX_SPACE_IN_FEET

    def get_default_space_in_feet(self):
        return self.__DEFAULT_SPACE_IN_FEET

    def get_min_reach_distance(self):
        return self.__MIN_REACH_DISTANCE

    def get_max_reach_distance(self):
        return self.__MAX_REACH_DISTANCE

    def get_default_reach_distance(self):
        return self.__DEFAULT_REACH_DISTANCE

    def get_min_size_modifier(self):
        return self.__MIN_SIZE_MODIFIER

    def get_max_size_modifier(self):
        return self.__MAX_SIZE_MODIFIER

    def get_default_size_modifier(self):
        return self.__DEFAULT_SIZE_MODIFIER











