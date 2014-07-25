'''
	  Name: __core_creature_configuration.py
	Author: Benjamin A
   Purpose: This is a core file for the engine that defines the boundaries of the creatures in the game.
            It limits levels, defines equiptable slots available, etc.

'''

class core_creature_configuration():
	def __init__(self):
		self.__DEFAULT_CREATURE_LEVEL = 0 # This is technically fixed to go to 1 because of |
		self.__MIN_CREATURE_LEVEL = 1     # THIS <------------------------------------------'
		self.__MAX_CREATURE_LEVEL = 61    # See the creature.py "set_creature_level" function
		self.__DEFAULT_BASE_STAT_LEVEL = 1
		self.__MIN_BASE_STAT_LEVEL = 1
		self.__MAX_BASE_STAT_LEVEL = 255
		self.__DEFAULT_EXPERIENCE_GROW_RATE = 1000 # Smaller is faster
		self.__MIN_GOOD_VS_EVIL = 0
		self.__MAX_GOOD_VS_EVIL = 100
		self.__MIN_LAW_VS_CHAOS = 0
		self.__MAX_LAW_VS_CHAOS = 100
		self.__EQUIPTABLE_SLOTS = {"HELMET":None,"ARMOR":None,"MAIN_HAND":None,"OFF_HAND":None,"AMULET":None,
		                           "RING_1":None,"RING_2":None,"GLOVES":None,"CLOAK":None,"BOOTS":None,"BELT":None}

	def get_default_creature_level(self):
		return self.__DEFAULT_CREATURE_LEVEL

	def get_min_creature_level(self):
		return self.__MIN_CREATURE_LEVEL

	def get_max_creature_level(self):
		return self.__MAX_CREATURE_LEVEL

	def get_min_base_stat_level(self):
		return self.__MIN_BASE_STAT_LEVEL

	def get_max_base_stat_level(self):
		return self.__MAX_BASE_STAT_LEVEL

	def get_default_experience_grow_rate(self):
		return self.__DEFAULT_EXPERIENCE_GROW_RATE

	def get_min_good_vs_evil(self):
		return self.__MIN_GOOD_VS_EVIL

	def get_max_good_vs_evil(self):
		return self.__MAX_GOOD_VS_EVIL

	def get_min_law_vs_chaos(self):
		return self.__MIN_LAW_VS_CHAOS

	def get_max_law_vs_chaos(self):
		return self.__MAX_LAW_VS_CHAOS