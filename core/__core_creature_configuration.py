'''
	  Name: __core_creature_configuration.py
	Author: Benjamin A
   Purpose: This is a core file for the engine that defines the boundaries of the creatures in the game.
            It limits levels, defines EQUIPMENT slots available, etc.

'''
from __core_race_configuration import core_race_configuration

class core_creature_configuration(core_race_configuration):
	def __init__(self):
		core_race_configuration.__init__(self) # Inherits the core race configurations of the game, the creature configuration is highly involved with races
		self.__DEFAULT_BASE_LEVEL = 0 # This is technically fixed to go to 1 because of |
		self.__MIN_BASE_LEVEL = 1     # THIS <------------------------------------------'
		self.__MAX_BASE_LEVEL = 60    # See the creature.py "set_base_level" function
		self.__DEFAULT_BASE_ABILITY_SCORE = 1
		self.__MIN_BASE_ABILITY_SCORE = 1
		self.__MAX_BASE_ABILITY_SCORE = 255
		self.__DEFAULT_EXPERIENCE_GROW_RATE = 1000 # Smaller is faster
		self.__DEFAULT_GOOD_VS_EVIL = 50 # Neutral
		self.__MIN_GOOD_VS_EVIL = 0
		self.__MAX_GOOD_VS_EVIL = 100
		self.__DEFAULT_LAW_VS_CHAOS = 50 # Neutral
		self.__MIN_LAW_VS_CHAOS = 0
		self.__MAX_LAW_VS_CHAOS = 100
		self.__DEFAULT_BASE_HIT_POINTS = 5
		self.__MIN_BASE_HIT_POINTS = 1
		self.__MIN_ABILITY_SCORE = 1

		self.__EQUIPMENT_SLOTS = {"HELMET":None,"ARMOR":None,"MAIN_HAND":None,"OFF_HAND":None,"AMULET":None,
		                           "RING_1":None,"RING_2":None,"GLOVES":None,"CLOAK":None,"BOOTS":None,"BELT":None}

	# This method converts ability scores to their modifiers
	# score:modifier => 1: -5, 2-3: -4, 4-5: -3 ... 10-11: 0, 16-17: +3
	# This is a critical calculation to the core gameplay.
	def ability_modifier_from_score(self,score):
		if score < self.get_min_ability_score():
			score = self.get_min_ability_score()

		return int(score/2)-5

	def get_default_base_level(self):
		return self.__DEFAULT_BASE_LEVEL

	def get_min_base_level(self):
		return self.__MIN_BASE_LEVEL

	def get_max_base_level(self):
		return self.__MAX_BASE_LEVEL

	def get_min_base_ability_score(self):
		return self.__MIN_BASE_ABILITY_SCORE

	def get_max_base_ability_score(self):
		return self.__MAX_BASE_ABILITY_SCORE

	def get_default_experience_grow_rate(self):
		return self.__DEFAULT_EXPERIENCE_GROW_RATE

	def get_default_good_vs_evil(self):
		return self.__DEFAULT_GOOD_VS_EVIL

	def get_min_good_vs_evil(self):
		return self.__MIN_GOOD_VS_EVIL

	def get_max_good_vs_evil(self):
		return self.__MAX_GOOD_VS_EVIL

	def get_default_law_vs_chaos(self):
		return self.__DEFAULT_LAW_VS_CHAOS

	def get_min_law_vs_chaos(self):
		return self.__MIN_LAW_VS_CHAOS

	def get_max_law_vs_chaos(self):
		return self.__MAX_LAW_VS_CHAOS

	def get_default_base_hit_points(self):
		return self.__DEFAULT_BASE_HIT_POINTS

	def get_min_base_hit_points(self):
		return self.__MIN_BASE_HIT_POINTS

	def get_min_ability_score(self):
		return self.__MIN_ABILITY_SCORE