'''
	  Name: creature.py
	Author: Benjamin A
   Purpose: The creature class creates an object with relevant methods to in-game creatures, npcs, pcs, etc
            This class can be used to create subclasses that inherit all the common traits of creatures,
            but extended to define specific and even custom creatures.

'''

from core.__core_creature_configuration import core_creature_configuration

class creature():
	# A short method in most classes that calls the core settings for that particular class.
	def _core(self):
		return core_creature_configuration()

	def __init__(self, playable_character=False, name='NAME',  race='UNKNOWN', deity=None, law_vs_chaos=_core(None).get_default_law_vs_chaos(),  good_vs_evil=_core(None).get_default_good_vs_evil(),  base_hit_points=_core(None).get_min_base_hit_points(),  base_level=_core(None).get_default_base_level(),  exp=0,  base_ac=0,  base_level_rate=1000, str=_core(None).get_min_base_ability_score(), inte =_core(None).get_min_base_ability_score(),chr =_core(None).get_min_base_ability_score(),dex =_core(None).get_min_base_ability_score(),con =_core(None).get_min_base_ability_score(),wis=_core(None).get_min_base_ability_score()):
		self.playable_character=playable_character
		self.name=name
		self.race=race
		self.deity=deity
		self.law_vs_chaos=law_vs_chaos # Scale 0 - 100. 0-32 = Chaos, 33-67 = Neutral, 68-100 = Law
		self.good_vs_evil=good_vs_evil # Scale 0 - 100. 0-32 = Evil, 33-67 = Neutral, 68-100 = Good

		self.base_hit_points=base_hit_points
		self.current_hit_points = self.base_hit_points

		self.base_level_rate=base_level_rate # 1000 is the standard growth,  the lower the number, the faster a character can base_level
		self.base_level=base_level or self.set_base_level_by_experience(exp)    # If base_level is zero, sets base_level by experience
		self.experience=exp or self.set_experience_by_base_level(base_level)    # If experience is zero, sets experience based on base_level. Defaults to 0 experience
																				# base_level 1 when no parameters entered.
		self.base_attack_bonus=0
		self.base_saving_throw_bonus={"fortitude":0,"will":0,"reflex":0}

		self.base_abilities={'str':str, 'int':inte, 'con':con, 'wis':wis, 'dex':dex, 'chr':chr} # Dictionary for base abilities
		self.base_armor_class=0

		self.skill_set=[] # Holds list of player abilities
		self.inventory=[] # Holds list of items, an inventory system is in the future.

	# Returns the base_level of the creature
	def get_base_level(self):
		return self.base_level

	# Sets all the base abilities at once,  or whichever are provided.
	# absolute == False : Base ability has parameter added to it (str=1 ==> self.base_abilities['str'] += 1)
	# absolute == True : Base ability is set to parameter (str=1 ==> self.base_abilities['str']=1)
	def set_all_base_ability_score(self, str=0, inte=0, con=0, wis=0, dex=0, chr=0, absolute=False):
		# if abilityements necessary. If absolute=true
		if str:
			self.set_base_str(str, absolute)
		if inte:
			self.set_base_int(inte, absolute)
		if con:
			self.set_base_con(con, absolute)
		if wis:
			self.set_base_wis(wis, absolute)
		if dex:
			self.set_base_dex(dex, absolute)
		if chr:
			self.set_base_chr(chr, absolute)

		return self.base_abilities
	
	# Allows one base ability to be modified at a time
	def set_base_ability_score(self, ability='', add=0, absolute=False):
		if ability.lower() in ['str', 'int', 'con', 'wis', 'dex', 'chr']:
			if absolute:
				self.base_abilities[ability.lower()]=add
			else:
				self.base_abilities[ability.lower()] += add
		else:
			return -1

		# Makes sure the base ability is valid and keeps the value within range
		if self.base_abilities[ability] > self._core().get_max_base_ability_score():
			self.base_abilities[ability] = self._core().get_max_base_ability_score()
		elif self.base_abilities[ability] < self._core().get_min_base_ability_score():
			self.base_abilities[ability] = self._core().get_min_base_ability_score()

		return self.base_abilities[ability]

	# Returns base ability value for any valid ability provided
	def get_base_ability_score(self, ability=''):
		if ability.lower() in ['str', 'int', 'con', 'wis', 'dex', 'chr']:
			return self.base_abilities[ability.lower()]
		else:
			return -1

	# Returns the base ability score for the Strength ability
	def get_base_str(self):
		return self.get_base_ability_score('str')

	# Sets the base ability score for the Strength ability
	# Variable 'add' will add any value placed in the parameter to the base ability. If variable 'absolute' is set to True,
	# the base ability will be set to the value provided for variable 'add'
	def set_base_str(self, add, absolute=False):
		return self.set_base_ability_score('str',add,absolute)

	# Returns the base ability score for the Intelligence ability
	def get_base_int(self):
		return self.get_base_ability_score('int')

	# Sets the base ability score for the Intelligence ability
	# Variable 'add' will add any value placed in the parameter to the base ability. If variable 'absolute' is set to True,
	# the base ability will be set to the value provided for variable 'add'
	def set_base_int(self, add, absolute=False):
		return self.set_base_ability_score('int',add,absolute)

	# Returns the base ability score for the Constitution ability
	def get_base_con(self):
		return self.get_base_ability_score('con')

	# Sets the base ability score for the Constitution ability
	# Variable 'add' will add any value placed in the parameter to the base ability. If variable 'absolute' is set to True,
	# the base ability will be set to the value provided for variable 'add'
	def set_base_con(self, add, absolute=False):
		return self.set_base_ability_score('con',add,absolute)

	# Returns the base ability score for the Wisdom ability
	def get_base_wis(self):
		return self.get_base_ability_score('wis')

	# Sets the base ability score for the Wisdom ability
	# Variable 'add' will add any value placed in the parameter to the base ability. If variable 'absolute' is set to True,
	# the base ability will be set to the value provided for variable 'add'
	def set_base_wis(self, add, absolute=False):
		return self.set_base_ability_score('wis',add,absolute)

	# Returns the base ability score for the Dexterity ability
	def get_base_dex(self):
		return self.get_base_ability_score('dex')

	# Sets the base ability score for the Dexterity ability
	# Variable 'add' will add any value placed in the parameter to the base ability. If variable 'absolute' is set to True,
	# the base ability will be set to the value provided for variable 'add'
	def set_base_dex(self, add, absolute=False):
		return self.set_base_ability_score('dex',add,absolute)

	# Returns the base ability score for the Charisma ability
	def get_base_chr(self):
		return self.get_base_ability_score('chr')

	# Sets the base ability score for the Charisma ability
	# Variable 'add' will add any value placed in the parameter to the base ability. If variable 'absolute' is set to True,
	# the base ability will be set to the value provided for variable 'add'
	def set_base_chr(self, add, absolute=False):
		return self.set_base_ability_score('chr',add,absolute)

	# Sets appropriate experience points based on base_level (By default, identical to DnD's base_level)
	def set_experience_by_base_level(self, base_level=1):
		return sum(range(1, base_level)*self.base_level_rate)

	# Returns base_level based on experience, if the experience is greater than what's needed to reach the maximum base_level,
	# then the maximum base_level allowed is returned
	def set_base_level_by_experience(self, exp=0):		# Sets base_level based on experience points
		for i in range(1, self._core().get_max_base_level()+1):
			if sum(range(1, i)*self.base_level_rate) > exp:
				return i - 1
		return self._core().get_max_base_level()
	
	def set_name(self, name):
		self.name = name
		return self.name
		
	def get_name(self):
		return self.name

	# Sets the law_vs_chaos value keeping it within restricted values
	def set_law_vs_chaos(self, add, absolute=False):
		if absolute:
			self.law_vs_chaos = add
			if self.law_vs_chaos < self._core().get_min_law_vs_chaos():
				self.law_vs_chaos = self._core().get_min_law_vs_chaos()
			elif self.law_vs_chaos > self._core().get_max_law_vs_chaos():
				self.law_vs_chaos = self._core().get_max_law_vs_chaos()
		else:
			self.law_vs_chaos += add

		return self.law_vs_chaos

	# Sets the good_vs_evil value keeping it within restricted values
	def set_good_vs_evil(self, add, absolute=False):
		if absolute:
			self.good_vs_evil = add
			if self.good_vs_evil < self._core().get_min_good_vs_evil():
				self.good_vs_evil = self._core().get_min_good_vs_evil()
			elif self.good_vs_evil > self._core().get_max_good_vs_evil():
				self.good_vs_evil = self._core().get_max_good_vs_evil()
		else:
			self.good_vs_evil += add

		return self.good_vs_evil

	# Returns law vs chaos values and or "lawful", "chaotic", and "neutral"
	def get_law_vs_chaos(self, value_word_combo=0): # 0 returns value,  1 returns word,  2 returns both,  -1 returns raw variable
		temp=[0, 0]

		if self.law_vs_chaos < 33:
			temp = [0, "chaotic"]
		elif self.law_vs_chaos > 67:
			temp = [2, "lawful"]
		else:
			temp = [1, "neutral"]
		
		if 0 <= value_word_combo < 2:
			return temp[value_word_combo]
		elif value_word_combo == -1:
			return self.law_vs_chaos
		else:
			return temp

	# Returns "evil", "good", or "neutral" based on good_vs_evil value
	def get_good_vs_evil(self, value_word_combo=0): # 0 returns value,  1 returns word,  2 returns both,  -1 returns raw variable
		temp=[0, 0]

		if self.good_vs_evil < 33:
			temp = [0, "evil"]
		elif self._core().get_max_base_ability_score() >= self.good_vs_evil > 67:
			temp = [2, "good"]
		else:
			temp = [1, "neutral"]

		if 0 <= value_word_combo < 2:
			return temp[value_word_combo]
		elif value_word_combo == -1:
			return self.good_vs_evil
		else:
			return temp

	# Get the alignment in different forms
	def get_alignment(self, value_word_combo=0): # 0 returns list of values (Lawful Evil=[2, 0]),  1 returns words (Lawful Evil=["Lawful",  "Evil"],  2 returns a list holding two lists of values and words,  -1 returns the exact alignment variables
		temp=[self.get_law_vs_chaos(2), self.get_good_vs_evil(2)]
		if value_word_combo == 0:
			return [temp[0][0], temp[1][0]]
		elif value_word_combo == 1:
			if temp[0][0] == 1 and temp[1][0] == 1: #
				return ["true", "neutral"]
			return [temp[0][1], temp[1][1]]
		elif value_word_combo == -1:
			return [self.get_law_vs_chaos(value_word_combo), self.get_good_vs_evil(value_word_combo)]
		else:
			return temp

	# Sets the creature level exactly as long as it's
	def set_absolute_base_level(self, base_level=_core(None).get_default_base_level(),set_experience=False):
		if self._core().get_min_base_level() <= base_level <= self._core().get_max_base_level():
			self.base_level = base_level
		else:
			self.base_level = 1

		if set_experience:
			self.set_experience_by_base_level(self.base_level)

		return self.base_level
	
	# Gets the ability modifier for whatever ability score is given to it
	def get_ability_modifier(self,ability=''):
		if ability.lower() in ['str', 'int', 'con', 'wis', 'dex', 'chr']:
			return self._core().ability_modifier_from_score(self.get_base_ability_score(ability.lower()))
		else:
			return -1

	# Returns the strength modifier
	def mod_str(self):
		return self.get_ability_modifier('str')

	# Returns the intelligence modifier
	def mod_int(self):
		return self.get_ability_modifier('int')

	# Returns the constitution modifier
	def mod_con(self):
		return self.get_ability_modifier('con')

	# Returns the wisdom modifier
	def mod_wis(self):
		return self.get_ability_modifier('wis')

	# Returns the dexterity modifier
	def mod_dex(self):
		return self.get_ability_modifier('dex')

	# Returns the charisma modifier
	def mod_chr(self):
		return self.get_ability_modifier('chr')

####################################################### TEST CODE ######################################################
a = creature(race='DOG', name="Carl", exp=19673, law_vs_chaos=30, good_vs_evil=90, base_level_rate=1000)

print a.name,  a.race,  a.base_level,  a.experience,  a.get_alignment(1), a.set_absolute_base_level(90), a.base_level, a.set_base_str(19), a.get_ability_modifier('str')