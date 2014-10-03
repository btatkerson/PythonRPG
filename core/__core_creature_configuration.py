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
		self.__MAX_BASE_LEVEL = 40    # See the creature.py "set_base_level" function
		self.__DEFAULT_BASE_ABILITY_SCORE = 1
		self.__MIN_BASE_ABILITY_SCORE = 1
		self.__MAX_BASE_ABILITY_SCORE = 255
		self.__DEFAULT_ABILITY = 0 # strength
		self.__ABILITY_LIST_SHORT = ['str', 'int', 'con', 'wis', 'dex', 'chr']
		self.__ABILITY_LIST = ['strength', 'intelligence', 'constitution', 'wisdom', 'dexterity', 'charisma']
		self.__DEFAULT_SAVING_THROW = 0 # fortitude
		self.__SAVING_THROW_LIST = ['fortitude','reflex','will']
		self.__SAVING_THROW_LIST_SHORT = ['for','ref','wil']
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
		self.__BASE_ATTACK_BONUS = ['poor','average','good','monk']
		self.__DEFAULT_BASE_ATTACK_BONUS = 0


		self.__EQUIPMENT_SLOTS = {"helmet":None,"armor":None,"main_hand":None,"off_hand":None,"amulet":None,
		                           "ring_1":None,"ring_2":None,"gloves":None,"cloak":None,"boots":None,"belt":None}

	# This method converts ability scores to their modifiers
	# score:modifier =>
	#    1: -5,
	#  2-3: -4,
	#  4-5: -3
	# ~~~~~~~~
	#10-11:  0,
	#16-17: +3, so on and so forth
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

	def get_ability_list(self):
		return self.__ABILITY_LIST

	def get_ability_list_short(self):
		return self.__ABILITY_LIST_SHORT

	def get_saving_throw_list(self):
		return self.__SAVING_THROW_LIST

	def get_saving_throw_list_short(self):
		return self.__SAVING_THROW_LIST_SHORT

	def is_saving_throw(self,saving_throw=None):
		if 0 <= saving_throw < len(self.__SAVING_THROW_LIST) or saving_throw in self.__SAVING_THROW_LIST or \
				saving_throw in self.__SAVING_THROW_LIST_SHORT:
			return True
		return False

	# Returns the short name of the saving throw. This is based on input. Defaults to fortitude
	def validate_saving_throw(self,saving_throw=None):
		if is_saving_throw(saving_throw):
			if 0 <= saving_throw < len(self.__SAVING_THROW_LIST):
				return self.__SAVING_THROW_LIST_SHORT[saving_throw]
			elif saving_throw.lower() in self.__SAVING_THROW_LIST_SHORT:
				return saving_throw.lower()
			else:
				return self.__SAVING_THROW_LIST_SHORT[self.__SAVING_THROW_LIST.index(saving_throw.lower())]
		return self.__SAVING_THROW_LIST_SHORT[self.__DEFAULT_SAVING_THROW]

	def get_default_ability(self):
		return self.__DEFAULT_ABILITY

	def is_ability(self,ability=None):
		if ability == None:
			return False
		if 0<= ability < len(self.__ABILITY_LIST) or ability.lower() in self.__ABILITY_LIST_SHORT or ability.lower() \
				in self.__ABILITY_LIST:
			return True
		return False

	# Returns the short name for the input 'ability'. Used for consistency purposes. This way, typing 'strength'
	# where the creature ability keys are shorthand ('strength' == 'str'), validate_ability is placed to assure
	# everything is called properly. Defaults to strength
	def validate_ability(self,ability=None):
		if self.is_ability(ability):
			if 0 <= ability < len(self.__ABILITY_LIST):
				return self.get_ability_list_short()[ability]
			elif ability.lower() in self.__ABILITY_LIST_SHORT:
				return ability.lower()
			else:
				return self.__ABILITY_LIST_SHORT[self.__ABILITY_LIST.index(ability.lower())]
		return self.get_ability_list_short()[self.get_default_ability()]

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

		if type(id) == str: # Turns a string-type 'id' into its numeric index
			if id.lower() in self.__BASE_SAVE_BONUS:
				id = list.index(self.__BASE_SAVE_BONUS,id.lower())

		if 0 <= id < len(self.__BASE_SAVE_BONUS):
			epic_bonus = max(0,round((creature_level-21)/2.0)) # All negative bonuses become zero.

			creature_level = max(min(20,creature_level),self.__MIN_BASE_LEVEL) # 20 is the maximum level of bonus
			# growth excluding epic bonuses. This also keeps the level from being no lower than whatever the minimum
			# base level

			if id == 0: # The base save bonus for a 'poor' level bonuses
				return int(creature_level/3 + epic_bonus)
			else: # The base save bonus for a 'good' level bonus
				return int(2 + creature_level/2 + epic_bonus)

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

			epic_bonus = max(0,round((creature_level-20)/2.0)) # All negative bonuses become zero.

			# This keeps the creature level between the minimum base level stat and no greater than 20,
			# for calculation purposes to add the epic bonuses in appropriately.
			creature_level = max(min(20,int(creature_level)),self.__MIN_BASE_LEVEL) # Attack bonuses do not grow after
			#  20.

			if id == 0: # The base attack bonus for a 'poor' level bonuses
				temp_stack = [i for i in range(1,creature_level/2+1)][::-5] or [0]


			elif id == 1: # base attack bonus for 'average' level
				#temp_stack=sorted(list(set(list(set(sorted([3,6,9,12]+(range(0,16)))[0:creature_level]))[::-5])-set(
				# [i for i in range(0,int(creature_level>1))])))[::-1]
				# ^ This is too insane be more efficient than:
				for i in range(0,int((creature_level-1)/7.0+1)):
					temp_stack.append(creature_level-(creature_level-1)/4-1-i*5)


			elif id == 3: # base attack bonus for the special case of an unarmed monk
				temp_stack=sorted(list(set(list(set(sorted([3,6,9,12]+(range(0,16)))[0:creature_level]))[::-3])-set(
					[i for i in range(0,int(creature_level>1))])))[::-1]
				# ^ This is insane, but it works.

				# for i in range(0,max(1,int((creature_level+4)/4))):
				# 	temp_stack.append(creature_level-(creature_level-1)/4-1-i*3)



			else: # The base save bonus for a 'good' level bonus
				temp_stack = range(1,creature_level+1)[::-5]
				# range(1,creature_level+1) is a list of all numbers 1 to creature_level, [::-5] starts at the
				# end of the list (creature_level) and returns a number every five it can move backward in the list.
				# creature_level : 7
				# range(1,7+1) => range(1,8) = [1,2,3,4,5,6,7]
				# range(1,8)[::-1] = [7,6,5,4,3,2,1] it starts at the end and moves back one listing; everything in reverse
				# range(1,8)[::-2] = [7,  5,  3,  1]
				# range(1,8)[::-3] = [7,    4,    1]
				# range(1,8)[::-4] = [7,      3    ]
				# range(1,8)[::-5] = [7,        2  ]
				# range(1,8)[::-6] = [7,          1]
				# So...
				# # range(1,20+1)[::-5] = [20,15,10,5]
				
				# for i in range(0,int((creature_level-1)/5.0+1)):
				# 	temp_stack.append(creature_level-i*5)
			return [int(i+epic_bonus) for i in temp_stack] # Returns the attacks with appropriate epic bonuses added in.

		return [0]


# a = core_creature_configuration()
#
# for i in range(1,61):
# 	print i,a.get_base_attack_bonus(3,i)#,a.get_base_attack_bonus(1,i),a.get_base_attack_bonus(0,i)