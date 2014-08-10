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
		self.__MIN_CURRENT_HIT_POINTS = -10
		self.__MIN_ABILITY_SCORE = 1
		self.__BASE_SAVE_BONUS = ['poor','good']
		self.__DEFAULT_BASE_SAVE_BONUS = 0
		self.__BASE_ATTACK_BONUS = ['poor','average','good']
		self.__DEFAULT_BASE_ATTACK_BONUS = 0

		self.__EQUIPMENT_SLOTS = {"helmet":None,"armor":None,"main_hand":None,"off_hand":None,"amulet":None,
		                           "ring_1":None,"ring_2":None,"gloves":None,"cloak":None,"boots":None,"belt":None}

	# This method converts ability scores to their modifiers
	# score:modifier => 1: -5, 2-3: -4, 4-5: -3 ... 10-11: 0, 16-17: +3
	# This is a critical calculation to the core gameplay.
	def ability_modifier_from_score(self,score):
		if score < self.get_min_ability_score():
			score = self.get_min_ability_score()

		return int(score-10)/2

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

	def get_min_current_hit_points(self):
		return self.__MIN_CURRENT_HIT_POINTS

	def get_min_base_hit_points(self):
		return self.__MIN_BASE_HIT_POINTS

	def get_min_ability_score(self):
		return self.__MIN_ABILITY_SCORE


	def get_base_save_bonus_name_by_id(self,id=None):
		if id is None:
			id = self.__BASE_SAVE_BONUS

		if 0 <= id < len(self.__BASE_SAVE_BONUS):
			return self.__BASE_SAVE_BONUS[id]
		return self.__BASE_SAVE_BONUS[self.__DEFAULT_BASE_SAVE_BONUS]

	def get_base_save_bonus_id_by_name(self,name=None):
		if name is None:
			name = self.get_base_save_bonus_name_by_id(self.__DEFAULT_BASE_SAVE_BONUS)

		if name.lower() in self.__BASE_SAVE_BONUS:
			return list.index(self.__BASE_SAVE_BONUS,name.lower())
		return self.__DEFAULT_BASE_SAVE_BONUS

	# Returns a list of save bonuses for the 'poor', and 'good', id can be given as a value or the name value,
	# creature_level is fairly self-explanatory
	# 0 : 'poor',
	# 1 : 'good'
	def get_base_save_bonus(self,id=None,creature_level=1):
		if id is None:
			id = self.__DEFAULT_BASE_SAVE_BONUS

		if type(id) == str:
			if id.lower() in self.__BASE_SAVE_BONUS:
				id = list.index(self.__BASE_SAVE_BONUS,id.lower())

		if 0 <= id < len(self.__BASE_SAVE_BONUS):
			if id == 0: # The base save bonus for a 'poor' level bonuses
				return creature_level/3
			else: # The base save bonus for a 'good' level bonus
				return 2 + creature_level/2

		return 0

	def get_base_attack_bonus_name_by_id(self,id=None):
		if id is None:
			id = self.__BASE_ATTACK_BONUS

		if 0 <= id < len(self.__BASE_ATTACK_BONUS):
			return self.__BASE_ATTACK_BONUS[id]
		return self.__BASE_ATTACK_BONUS[self.__DEFAULT_BASE_ATTACK_BONUS]

	def get_base_attack_bonus_id_by_name(self,name=None):
		if name is None:
			name = self.get_base_attack_bonus_name_by_id(self.__DEFAULT_BASE_ATTACK_BONUS)

		if name in self.__BASE_ATTACK_BONUS:
			return list.index(self.__BASE_ATTACK_BONUS,name)
		return self.__DEFAULT_BASE_ATTACK_BONUS

	# Returns a list of attack bonuses for the 'poor', 'average', and 'good', if there are multiple attacks,
	# the sequential bonuses are provided. id can be given as a value or the name value
	# 0 : 'poor',
	# 1 : 'average',
	# 2 : 'good'
	def get_base_attack_bonus(self,id=None,creature_level = 1):
		if id is None:
			id = self.__DEFAULT_BASE_ATTACK_BONUS

		if type(id) == str:
			if id.lower() in self.__BASE_ATTACK_BONUS:
				id = list.index(self.__BASE_ATTACK_BONUS,id.lower())

		if 0 <= id < len(self.__BASE_ATTACK_BONUS):
			temp_stack = []
			if id == 0: # The base attack bonus for a 'poor' level bonuses
				for i in range(0,int((creature_level-1)/12.0+1)):
					temp_stack.append(creature_level/2-i*5)

			elif id == 1: # base attack bonus for 'average' level
				for i in range(0,int((creature_level-1)/7.0+1)):
					temp_stack.append(creature_level-(creature_level-1)/4-1-i*5)

			else: # The base save bonus for a 'good' level bonus
				for i in range(0,int((creature_level-1)/5.0+1)):
					temp_stack.append(creature_level-i*5)

			return temp_stack

		return [0]

