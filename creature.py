from core.__core_creature_configuration import core_creature_configuration

class creature():
	# A short method in most classes that calls the core settings for that particular class
	def _core(self):
		return core_creature_configuration()

	def __init__(self,  name = 'NAME',  race = 'UNKNOWN',  law_vs_chaos = 50,  good_vs_evil = 50,  hit_points = 5,  level = _core(None).get_default_creature_level(),  exp = 0,  base_ac = 0,  leveling_rate = 1000):
		self.name = name
		self.race = race
		self.law_vs_chaos = law_vs_chaos
		self.good_vs_evil = good_vs_evil
		
		self.hit_points = hit_points

		
		self.leveling_rate = leveling_rate # 1000 is the standard growth,  the lower the number,  the faster a character can level
		self.level = level or self.level_by_experience(exp)      # If level is zero,  sets level by experience
		self.experience = exp or self.experience_by_level(level) # If experience is zero,  sets experience based on level	
		
		self.base_stats={'str':0, 'int':0, 'con':0, 'wis':0, 'dex':0, 'chr':0} # Dictionary for base stats
		self.base_armor_class = 0
		
		self.skill_set = []				
		self.inventory = []

	def get_base_attack(self):
		return self.level

	# Sets all the base stats at once,  or whichever are provided.
	# absolute == False : Base stat has parameter added to it (str = 1 ==> self.base_stats['str'] += 1)
	# absolute == True : Base stat is set to parameter (str = 1 ==> self.base_stats['str'] = 1)
	def set_all_base_stat(self, str=0, inte=0, con=0, wis=0, dex=0, chr=0, absolute=False):
		# if statements necessary. If absolute = true
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


	def set_base_stat(self, stat = '', add=0, absolute=False):
		if stat.lower() in ['str', 'int', 'con', 'wis', 'dex', 'chr']:
			if absolute:
				self.base_stats[stat.lower()] = add
			else:
				self.base_stats[stat.lower()] += add
		else:
			return -1

	def get_base_stat(self, stat = ''):
		if stat.lower() in ['str', 'int', 'con', 'wis', 'dex', 'chr']:
			return self.base_stats[stat.lower()]
		else:
			return -1
			
	def get_base_str(self):
		return self.get_base_stat('str')
	
	def set_base_str(self, add, absolute=False):
		if absolute:
			self.base_stats['str'] = add
		else:
			self.base_stats['str'] += add
		return self.get_base_stat('str')

	def get_base_int(self):
		return self.get_base_stat('int')

	def set_base_int(self, add, absolute=False):
		if absolute:
			self.base_stats['int'] = add
		else:
			self.base_stats['int'] += add
		return self.get_base_stat('int')

	def get_base_con(self):
		return self.get_base_stat('con')
	
	def set_base_con(self, add, absolute=False):
		if absolute:
			self.base_stats['con'] = add
		else:
			self.base_stats['con'] += add
		return self.get_base_stat('con')

	def get_base_wis(self):
		return self.get_base_stat('wis')

	def set_base_wis(self, add, absolute=False):
		if absolute:
			self.base_stats['wis'] = add
		else:
			self.base_stats['wis'] += add
		return self.get_base_stat('wis')

	def get_base_dex(self):
		return self.get_base_stat('dex')
	
	def set_base_dex(self, add, absolute=False):
		if absolute:
			self.base_stats['dex'] = add
		else:
			self.base_stats['dex'] += add
		return self.get_base_stat('dex')

	def get_base_chr(self):
		return self.get_base_stat('chr')
		
	def set_base_chr(self, add, absolute=False):
		if absolute:
			self.base_stats['chr'] = add
		else:
			self.base_stats['chr'] += add
		return self.get_base_stat('chr')
			
	def experience_by_level(self,  level = 1):		# Sets appropriate experience points based on level (By default,  identical to DnD's leveling)
		return sum(range(1, level)*self.leveling_rate)
	
	def level_by_experience(self,  exp = 0):		# Sets level based on experience points
		for i in range(1, 101):
			if sum(range(1, i)*self.leveling_rate) > exp:
				return i - 1
		return 1
	
	def set_name(self, name):
		self.name = name
		return self.name
		
	def get_name(self):
		return self.name
		
	def set_law_vs_chaos(self, add, absolute = False):
		if absolute:
			self.law_vs_chaos = add
		else:
			self.law_vs_chaos += add
	
	def set_good_vs_evil(self, add, absolute = False):
		if absolute:
			self.good_vs_evil = add
		else:
			self.good_vs_evil += add
	
	# Returns law vs chaos values
	def get_law_vs_chaos(self, value_word_combo=0): # 0 returns value,  1 returns word,  2 returns both,  -1 returns raw variable
		temp = [0, 0]

		if self.law_vs_chaos < 33:
			temp = [0, "chaotic"]
		elif self.law_vs_chaos > 67:
			temp = [2, "lawful"]
		else:
			temp = [1, "neutral"]
		
		if value_word_combo >= 0 and value_word_combo < 2:
			return temp[value_word_combo]
		elif value_word_combo == -1:
			return self.law_vs_chaos
		else:
			return temp


	def get_good_vs_evil(self, value_word_combo=0): # 0 returns value,  1 returns word,  2 returns both,  -1 returns raw variable
		temp = [0, 0]

		if self.good_vs_evil < 33:
			temp = [0, "evil"]
		elif self.good_vs_evil > 67:
			temp = [2, "good"]
		else:
			temp = [1, "neutral"]

		if value_word_combo >= 0 and value_word_combo < 2:
			return temp[value_word_combo]
		elif value_word_combo == -1:
			return self.good_vs_evil
		else:
			return temp

	# Get the alignment in different forms
	def get_alignment(self, value_word_combo=0): # 0 returns list of values (Lawful Evil = [2, 0]),  1 returns words (Lawful Evil = ["Lawful",  "Evil"],  2 returns a list holding two lists of values and words,  -1 returns the exact alignment variables
		temp = [self.get_law_vs_chaos(2), self.get_good_vs_evil(2)]
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
	
	def set_absolute_creature_level(self, creature_level=_core(None).get_default_creature_level()):
		if self._core(None).get_min_creature_level() <= creature_level <= self._core(None).get_max_creature_level():
			self.level = creature_level
		else:
			self.level = 1

a = creature(race = 'DOG', name = "Carl", exp=19673, law_vs_chaos=30, good_vs_evil=90, leveling_rate=1000)

print a.name,  a.race,  a.level,  a.experience,  a.get_alignment(1)
