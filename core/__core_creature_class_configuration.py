'''
	  Name: __core_creature_class_configuration.py
	Author: Benjamin A
   Purpose: This is a core file for the engine that defines the boundaries of the classes in the game.
            THIS... is going to be mad cray.

'''
from core.__core_constants import core_constants  

class core_creature_class_configuration():
	def __init__(self):
            self.ccs = core_constants()
            self.__creature_settings_dict={i:0 for i in self.ccs.CREATURECLASS.get_index()}
