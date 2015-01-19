class creature():
	def __init__(self, name = 'NAME', race = 'UNKNOWN', law_vs_chaos = 50, good_vs_evil = 50, level = 0, exp = 0, base_ac = 0, leveling_rate = 1000):
		self.name = name
		self.law_vs_chaos = 50
		self.good_vs_evil = 50
		self.race = race
		
		self.leveling_rate = leveling_rate # 1000 is the standard growth, the lower the number, the faster a character can level
		self.level = level or self.level_by_experience(exp)      # If level is zero, sets level by experience
		self.experience = exp or self.experience_by_level(level) # If experience is zero, sets experience based on level	
		
		self.base_stats={'str':0,'int':0,'con':0,'wis':0,'dex':0,'chr':0} # Dictionary for base stats
		self.base_armor_class = 0
		
		self.inventory = []

	def experience_by_level(self, level = 1):		# Sets appropriate experience points based on level (By default, identical to DnD's leveling)
		return sum(range(1,level)*self.leveling_rate)
	
	def level_by_experience(self, exp = 0):		# Sets level based on experience points
		for i in range(1,101):
			if sum(range(1,i)*self.leveling_rate) > exp:
				return i - 1
		return 1
	
	def set_name(self,name):
		self.name = name
		return self.name
		
	def get_name(self):
		return self.name
		
	def set_law_vs_chaos(self,add,absolute = False):
		if absolute:
			self.law_vs_chaos = add
		else:
			self.law_vs_chaos += add
	
	def set_good_vs_evil(self,add,absolute = False):
		if absolute:
			self.good_vs_evil = add
		else:
			self.good_vs_evil += add
	
	# Returns law vs chaos values
	def get_law_vs_chaos(self,value_word_combo=0): # 0 returns value, 1 returns word, 2 returns both, -1 returns raw variable
		temp = [0,0]

		if self.law_vs_chaos < 33:
			temp = [0,"chaotic"]
		elif self.law_vs_chaos > 67:
			temp = [2,"lawful"]
		else:
			temp = [1,"neutral"]
		
		if value_word_combo >= 0 and value_word_combo < 2:
			return temp[value_word_combo]
		elif value_word_combo == -1:
			return self.law_vs_chaos
		else:
			return temp

	def get_good_vs_evil(self,value_word_combo=0): # 0 returns value, 1 returns word, 2 returns both, -1 returns raw variable
		temp = [0,0]

		if self.good_vs_evil < 33:
			temp = [0,"evil"]
		elif self.good_vs_evil > 67:
			temp = [2,"good"]
		else:
			temp = [1,"neutral"]

		if 0 <= value_word_combo < 2:
			return temp[value_word_combo]
		elif value_word_combo == -1:
			return self.good_vs_evil
		else:
			return temp

	# Get the alignment in different forms
	def get_alignment(self,value_word_combo=0): # 0 returns list of values (Lawful Evil = [2,0]), 1 returns words (Lawful Evil = ["Lawful", "Evil"], 2 returns a list holding two lists of values and words, -1 returns the exact alignment variables
		temp = [self.get_law_vs_chaos(2),self.get_good_vs_evil(2)]
		if value_word_combo == 0:
			return [temp[0][0],temp[1][0]]
		elif value_word_combo == 1:
			if temp[0][0] == 1 and temp[1][0] == 1:
				return ["true", "neutral"]
			return [temp[0][1],temp[1][1]]
		elif value_word_combo == -1:
			return temp[self.get_law_vs_chaos(value_word_combo),self.get_good_vs_evil(value_word_combo)]
		else:
			return temp

			
	
	

a = creature(race = 'DOG',name = "Carl",exp=19673)

print a.name, a.race, a.level, a.experience
