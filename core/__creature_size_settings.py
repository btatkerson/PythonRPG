'''
      Name: __creature_size_settings.py
    Author: Benjamin A
      Date: Jul 7, 2015
    
   Purpose: Holds the information that is affected by the size of creature including reach distance and size modifiers
       
       
'''
import core.__core_constants_mod as ccs
from core.__core_creature_size_class_configuration import core_creature_size_configuration as size_config

class creature_size_settings():
    def __init__(self,size_class=None,space_in_feet=None,reach_distance=None,size_modifier=None):
        self.size_class = None
        self.space_in_feet = None
        self.reach_distance = None
        self.size_modifier = None

        self.set_size_class(size_class)
        self.set_space_in_feet(space_in_feet)
        self.set_reach_distance(reach_distance)
        self.set_size_modifier(size_modifier)

    def set_size_class(self,size_class=None):
        if ccs.SIZECLASS.verify(size_class):
            self.size_class = ccs.SIZECLASS.verify(size_class)
        else:
            self.size_class = size_config().get_default_size_class()
        
    def get_size_class(self):
        return self.size_class


    def set_space_in_feet(self,space_in_feet):
        if space_in_feet is not None:
            self.space_in_feet = min(max(size_config().get_min_space_in_feet(),space_in_feet),size_config().get_max_space_in_feet())
        else:
            self.space_in_feet = size_config().get_default_space_in_feet()

    def get_space_in_feet(self):
        return self.space_in_feet

    def set_reach_distance(self,reach_distance):
        if reach_distance is not None:
            self.reach_distance = min(max(size_config().get_min_reach_distance(),reach_distance),size_config().get_max_reach_distance())
        else:
            self.reach_distance = size_config().get_default_reach_distance()

    def get_reach_distance(self):
        return self.reach_distance

    def set_size_modifier(self,size_modifier):
        if size_modifier is not None:
            self.size_modifier = min(max(size_config().get_min_size_modifier(),size_modifier),size_config().get_max_size_modifier())
        else:
            self.size_modifier = size_config().get_default_size_modifier()

    def get_size_modifier(self):
        return self.size_modifier
