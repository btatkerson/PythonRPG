'''
	 Name: creature.py
	Author: Benjamin A
 Purpose: The creature class creates an object with relevant methods to in-game creatures, npcs, pcs, etc
 This class can be used to create subclasses that inherit all the common traits of creatures, 
 but extended to define specific and even custom creatures.
 
'''

from core.__core_creature_configuration import core_creature_configuration
from core.verbose import verbose
from skill_set import skill_set
from dice import dice


class creature(verbose, dice): 
	# A short method in most classes that calls the core settings for that particular class.
	def _core(self): 
		return core_creature_configuration()

	def __init__(self, playable_character=False, name='NAME', race='UNKNOWN', deity=None, 
	 law_vs_chaos=_core(None).get_default_law_vs_chaos(), good_vs_evil=_core(None).get_default_good_vs_evil(), 
	 base_hit_points=_core(None).get_min_base_hit_points(), base_level=_core(None).get_default_base_level(), 
	 exp=0, base_ac=0, base_level_rate=1000, str=_core(None).get_min_base_ability_score(), 
	 inte=_core(None).get_min_base_ability_score(), chr=_core(None).get_min_base_ability_score(), 
	 dex=_core(None).get_min_base_ability_score(), con=_core(None).get_min_base_ability_score(), 
	 wis=_core(None).get_min_base_ability_score(), verbose=False): 
		verbose.__init__(self)
		dice.__init__(self)
		self.playable_character=playable_character
		self.name=name
		self.race=race
		self.deity=deity
		self.law_vs_chaos=law_vs_chaos # Scale 0 - 100. 0-32= Chaos, 33-67= Neutral, 68-100= Law
		self.good_vs_evil=good_vs_evil # Scale 0 - 100. 0-32= Evil, 33-67= Neutral, 68-100= Good

		self.base_hit_points=base_hit_points
		self.current_hit_points= self.base_hit_points

		self.base_level_rate=base_level_rate # 1000 is the standard growth, the lower the number, the faster a character can base_level
		self.base_level=base_level or self.set_base_level_by_experience(exp) # If base_level is zero, sets base_level by experience
		self.experience=exp or self.set_experience_by_base_level(base_level) # If experience is zero, sets experience based on base_level. Defaults to 0 experience
	# base_level 1 when no parameters entered.
		self.skill_set= skill_set()

		self.base_saving_throw_bonus={i: 0 for i in self._core().get_saving_throw_list()}

		self.base_abilities={'str': str, 'int': inte, 'con': con, 'wis': wis, 'dex': dex, 'chr': chr} # Dictionary for base abilities
		self.base_armor_class=0

		self.inventory=[] # Holds list of items, an inventory system is in the future.

	# Returns the base_level of the creature
	def get_base_level(self): 
		return self.base_level

	def get_experience(self):
		'''
		Returns the creature experience
		'''
		return self.experience
	
	def get_experience_needed_to_level(self):
		'''
		Returns the experience needed in order to level up
		'''
		temp = sum([i * self.base_level_rate for i in range(1, self.base_level+1)]) - self.experience
		if temp > 0:
			return temp
		return 0

	def get_experience_toward_next_level(self):
		'''
		Returns the current experience earned toward the next level
		
		This is used for tracking progress.
		'''
		return self.experience - sum([i*self.base_level_rate for i in range(1,self.base_level)])

	def base_attack_bonus(self): 
		'''
		Returns the attack bonuses based on level and attack-ability
		'''
		return self._core().get_base_attack_bonus(2, self.base_level) # <---------------------------------------- Not always two, fix it!


	def attack_roll(self): 
		attack_list = []
		for i in self.base_attack_bonus(): 
			roll=sum(self.d20())
			if roll== 20: 
				self.verbo("Critical Hit!", True)
				roll=sum(self.d20())
			attack_list.append(roll + self.mod_str())
			print(roll + self.mod_str())
		return attack_list

	def get_skill_set(self): 
		return self.skill_set

	def get_skill(self, id=None): 
		return self.skill_set.get_skill(id)

	# Sets all the base abilities at once, or whichever are provided.
	# absolute== False : Base ability has parameter added to it (str=1==> self.base_abilities['str'] += 1)
	# absolute== True : Base ability is set to parameter (str=1==> self.base_abilities['str']=1)
	def set_all_base_ability_score(self, str=0, inte=0, con=0, wis=0, dex=0, chr=0, absolute=False): 
		# if statements necessary. If absolute=true
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
		if self._core().is_ability(ability): 
			ability= self._core().validate_ability(ability)
			if absolute: 
				self.base_abilities[ability.lower()]=add
			else: 
				self.base_abilities[ability.lower()] += add
		else: 
			return -1
		# Makes sure the base ability is valid and keeps the value within range
		if self.base_abilities[ability] > self._core().get_max_base_ability_score(): 
			self.base_abilities[ability]= self._core().get_max_base_ability_score()
		elif self.base_abilities[ability] < self._core().get_min_base_ability_score(): 
			self.base_abilities[ability]= self._core().get_min_base_ability_score()

		return self.base_abilities[ability]

	# Returns base ability value for any valid ability provided
	def get_base_ability_score(self, ability=''): 
		if self._core().is_ability(ability): 
			ability= self._core().validate_ability(ability)
			return self.base_abilities[ability]
		else: 
			return -1

	# Returns the base ability score for the Strength ability
	def get_base_str(self): 
		return self.get_base_ability_score('str')

	# Sets the base ability score for the Strength ability
	# Variable 'add' will add any value placed in the parameter to the base ability. If variable 'absolute' is set to True, 
	# the base ability will be set to the value provided for variable 'add'
	def set_base_str(self, add, absolute=False): 
		return self.set_base_ability_score('str', add, absolute)

	# Returns the base ability score for the Intelligence ability
	def get_base_int(self): 
		return self.get_base_ability_score('int')

	# Sets the base ability score for the Intelligence ability
	# Variable 'add' will add any value placed in the parameter to the base ability. If variable 'absolute' is set to True, 
	# the base ability will be set to the value provided for variable 'add'
	def set_base_int(self, add, absolute=False): 
		return self.set_base_ability_score('int', add, absolute)

	# Returns the base ability score for the Constitution ability
	def get_base_con(self): 
		return self.get_base_ability_score('con')

	# Sets the base ability score for the Constitution ability
	# Variable 'add' will add any value placed in the parameter to the base ability. If variable 'absolute' is set to True, 
	# the base ability will be set to the value provided for variable 'add'
	def set_base_con(self, add, absolute=False): 
		return self.set_base_ability_score('con', add, absolute)

	# Returns the base ability score for the Wisdom ability
	def get_base_wis(self): 
		return self.get_base_ability_score('wis')

	# Sets the base ability score for the Wisdom ability
	# Variable 'add' will add any value placed in the parameter to the base ability. If variable 'absolute' is set to True, 
	# the base ability will be set to the value provided for variable 'add'
	def set_base_wis(self, add, absolute=False): 
		return self.set_base_ability_score('wis', add, absolute)

	# Returns the base ability score for the Dexterity ability
	def get_base_dex(self): 
		return self.get_base_ability_score('dex')

	# Sets the base ability score for the Dexterity ability
	# Variable 'add' will add any value placed in the parameter to the base ability. If variable 'absolute' is set to True, 
	# the base ability will be set to the value provided for variable 'add'
	def set_base_dex(self, add, absolute=False): 
		return self.set_base_ability_score('dex', add, absolute)

	# Returns the base ability score for the Charisma ability
	def get_base_chr(self): 
		return self.get_base_ability_score('chr')

	# Sets the base ability score for the Charisma ability
	# Variable 'add' will add any value placed in the parameter to the base ability. If variable 'absolute' is set to True, 
	# the base ability will be set to the value provided for variable 'add'
	def set_base_chr(self, add, absolute=False): 
		return self.set_base_ability_score('chr', add, absolute)

	# Sets appropriate experience points based on base_level (By default, identical to DnD's base_level)
	def set_experience_by_base_level(self, base_level=1): 
		return sum([i * self.base_level_rate for i in range(1, base_level)])

	# Returns base_level based on experience, if the experience is greater than what's needed to reach the maximum base_level, 
	# then the maximum base_level allowed is returned
	def set_base_level_by_experience(self, exp=0): 		# Sets base_level based on experience points
		for i in range(1, self._core().get_max_base_level() + 1): 
			if sum([i * self.base_level_rate for i in range(1, i)]) > exp: 
				return i - 1
		return self._core().get_max_base_level()
	
	def set_name(self, name): 
		self.name= name
		return self.name
		
	def get_name(self): 
		return self.name

	# Sets the law_vs_chaos value keeping it within restricted values
	def set_law_vs_chaos(self, add, absolute=False): 
		if absolute: 
			self.law_vs_chaos= add
			if self.law_vs_chaos < self._core().get_min_law_vs_chaos(): 
				self.law_vs_chaos= self._core().get_min_law_vs_chaos()
			elif self.law_vs_chaos > self._core().get_max_law_vs_chaos(): 
				self.law_vs_chaos= self._core().get_max_law_vs_chaos()
		else: 
			self.law_vs_chaos += add

		return self.law_vs_chaos

	# Sets the good_vs_evil value keeping it within restricted values
	def set_good_vs_evil(self, add, absolute=False): 
		if absolute: 
			self.good_vs_evil= add
			if self.good_vs_evil < self._core().get_min_good_vs_evil(): 
				self.good_vs_evil= self._core().get_min_good_vs_evil()
			elif self.good_vs_evil > self._core().get_max_good_vs_evil(): 
				self.good_vs_evil= self._core().get_max_good_vs_evil()
		else: 
			self.good_vs_evil += add

		return self.good_vs_evil

	# Returns law vs chaos values and or "lawful", "chaotic", and "neutral"
	def get_law_vs_chaos(self, value_word_combo=0): # 0 returns value, 1 returns word, 2 returns both, -1 returns raw variable
		temp=[0, 0]

		if self.law_vs_chaos < 33: 
			temp= [0, "chaotic"]
		elif self.law_vs_chaos > 67: 
			temp= [2, "lawful"]
		else: 
			temp= [1, "neutral"]
		
		if 0 <= value_word_combo < 2: 
			return temp[value_word_combo]
		elif value_word_combo== -1: 
			return self.law_vs_chaos
		else: 
			return temp

	def isChaotic(self): 
		if self.get_law_vs_chaos()== 0: 
			return True
		return False

	# Returns true if creature is neutral in respect to "Law Vs Chaos" (as opposed to "Good Vs Evil")
	def isNeutralLvC(self): 
		if self.get_law_vs_chaos()== 1: 
			return True
		return False

	def isLawful(self): 
		if self.get_law_vs_chaos()== 2: 
			return True
		return False

	# Returns "evil", "good", or "neutral" based on good_vs_evil value
	def get_good_vs_evil(self, value_word_combo=0): # 0 returns value, 1 returns word, 2 returns both, -1 returns raw variable
		temp=[0, 0]

		if self.good_vs_evil < 33: 
			temp= [0, "evil"]
		elif self._core().get_max_base_ability_score() >= self.good_vs_evil > 67: 
			temp= [2, "good"]
		else: 
			temp= [1, "neutral"]

		if 0 <= value_word_combo < 2: 
			return temp[value_word_combo]
		elif value_word_combo== -1: 
			return self.good_vs_evil
		else: 
			return temp

	# Return quick checks for creature alignments
	def isGood(self): 
		if self.get_good_vs_evil()== 2: 
			return True
		return False

	# Returns true if creature is neutral in respect to "Good Vs Evil" (as opposed to "Law Vs Chaos")
	def isNeutralGvE(self): 
		if self.get_good_vs_evil()== 1: 
			return True
		return False

	def isEvil(self): 
		if self.get_good_vs_evil()== 0: 
			return True
		return False

	# Get the alignment in different forms
	def get_alignment(self, value_word_combo=0): # 0 returns list of values (Lawful Evil=[2, 0]), 1 returns words (Lawful Evil=["Lawful", "Evil"], 2 returns a list holding two lists of values and words, -1 returns the exact alignment variables
		temp=[self.get_law_vs_chaos(2), self.get_good_vs_evil(2)]
		if value_word_combo== 0: 
			return [temp[0][0], temp[1][0]]
		elif value_word_combo== 1: 
			if temp[0][0]== 1 and temp[1][0]== 1: #
				return ["true", "neutral"]
			return [temp[0][1], temp[1][1]]
		elif value_word_combo== -1: 
			return [self.get_law_vs_chaos(value_word_combo), self.get_good_vs_evil(value_word_combo)]
		else: 
			return temp

	def isChaoticEvil(self): 
		if self.isChaotic() and self.isEvil(): 
			return True
		return False

	def isChaoticNeutral(self): 
		if self.isChaotic() and self.isNeutralGvE(): 
			return True
		return False

	def isChaoticGood(self): 
		if self.isChaotic() and self.isGood(): 
			return True
		return False

	def isNeutralEvil(self): 
		if self.isNeutralLvC() and self.isEvil(): 
			return True
		return False

	def isTrueNeutral(self): 
		if self.isNeutralLvC() and self.isNeutralGvE(): 
			return True
		return False

	def isNeutralGood(self): 
		if self.isNeutralLvC() and self.isGood(): 
			return True
		return False

	def isLawfulEvil(self): 
		if self.isLawful() and self.isEvil(): 
			return True
		return False

	def isLawfulNeutral(self): 
		if self.isLawful() and self.isNeutralGvE(): 
			return True
		return False

	def isLawfulGood(self): 
		if self.isLawful() and self.isGood(): 
			return True
		return False

	# Sets the creature level exactly and gives the
	def set_absolute_base_level(self, base_level=None, set_experience=True): 
		if base_level == None: 
			return self._core().get_default_base_level()
		if self._core().get_min_base_level() <= base_level <= self._core().get_max_base_level(): 
			self.base_level= base_level
		elif base_level < self._core().get_min_base_level(): 
			self.base_level= self._core().get_min_base_level()
		elif base_level > self._core().get_max_base_level(): 
			self.base_level= self._core().get_max_base_level()
		else: 
			self.base_level= self._core().get_default_base_level()

		if set_experience: 
			self.set_experience_by_base_level(self.base_level)

		return self.base_level
	
	# Gets the ability modifier for whatever ability score is given to it
	def get_ability_modifier(self, ability=''): 
		if self._core().is_ability(ability): 
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
a= creature(race='DOG', name="Carl", exp=19673, law_vs_chaos=30, good_vs_evil=90, base_level_rate=1000, verbose=True)

print(a.name, a.race, a.base_level, a.experience, a.get_experience_needed_to_level(),a.get_experience_toward_next_level(),a.get_alignment(1), \
	a.set_base_str(24), a.get_ability_modifier('str'))
print(a.base_saving_throw_bonus)
print('Attack!: ', a.attack_roll())
print(a.get_skill_set().get_skill(10).get_class_skills())
a.get_skill(10).set_base_skill_points(5)
print(a.get_skill(10).get_base_skill_points())
a.get_skill(10).set_base_skill_points(7)
print(a.get_skill(10).get_base_skill_points())
a.get_skill(10).set_base_skill_points(21, True)
print(a.get_skill(10).get_base_skill_points())
print(a.get_skill(11).get_skill_name())
