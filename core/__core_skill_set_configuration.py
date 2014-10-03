'''
	  Name: __core_creature_configuration.py
	Author: Benjamin A
   Purpose: This is a core file for the engine that defines the boundaries of the skill set in the game.

'''

class core_skill_set_configuration():
	def __init__(self):
		# List of skills, 0 is 'unique' and unused during initialization
		self.skill_set_list =  ['unique',
								'animal_empathy',
								'appraise',
								'bluff',
								'concentration',
								'craft_armor',
								'craft_trap',
								'craft_weapon',
								'disable_trap',
								'discipline',
								'heal',
								'hide',
								'intimidate',
								'listen',
								'lore',
								'open_lock',
								'parry',
								'perform',
								'persuade',
								'pick_pocket',
								'ride',
								'search',
								'set_trap',
								'spellcraft',
								'spot',
								'taunt',
								'tumble',
								'use_magic_device']

		self.skill_set_list_short =['uni',
									'ani',
									'apr',
									'blf',
									'cnc',
									'car',
									'ctr',
									'cwe',
									'dtr',
									'dis',
									'hel',
									'hid',
									'itm',
									'lis',
									'lor',
									'opl',
									'pry',
									'pfm',
									'psd',
									'pic',
									'rid',
									'src',
									'str',
									'spl',
									'spt',
									'tnt',
									'tbl',
									'umd']

		self.__DEFAULT_TRAINED_SKILL = False
		self.__DEFAULT_ARMOR_PENALTY = False
		self.__DEFAULT_CROSS_CLASS = True
		self.__DEFAULT_KEY_ABILITY = None
		self.__DEFAULT_SKILL_POINTS = 0
		self.__MIN_SKILL_POINTS = 0
		self.__MAX_SKILL_POINTS = 255
		self.__DEFAULT_SKILL_ID = 0
		self.__DEFAULT_CLASS_SKILLS = []
		self.__DEFAULT_SYNERGY_SKILLS = []


	def get_skill_set_list(self):
		return self.skill_set_list

	def get_skill_set_list_short(self):
		return self.skill_set_list_short

	def get_skill_set_id_by_name(self,name=None):
		if name.lower() in self.skill_set_list:
			return self.skill_set_list.index(name.lower())
		elif name.lower() in self.skill_set_list_short:
			return self.skill_set_list_short.index(name.lower())
		return self.__DEFAULT_SKILL_ID

	def get_skill_set_name_by_id(self,id=None):
		if 0<id<len(self.skill_set_list):
			return self.skill_set_list[id]
		return self.skill_set_list[self.__DEFAULT_SKILL_ID]


	def is_skill(self,id=None):
		if id == None:
			return False
		if 0 <= id < len(self.skill_set_list_short) or id.lower() in self.skill_set_list or id.lower() in \
				self.skill_set_list_short:
			return True
		return False

	# Returns the name of the skill no matter the input. It's basically a safety measure for custom scripts
	# and developer scripts because it will allow the game to run even if an error is made such as a typo.
	def validate_skill(self,id=None):
		if self.is_skill(id):
			if 0 <= id < len(self.skill_set_list_short):
				return self.skill_set_list_short[id]
			elif id.lower() in self.skill_set_list_short:
				return id.lower()
			else:
				return self.skill_set_list_short[self.skill_set_list.index(id)]
		return self.skill_set_list_short[self.__DEFAULT_SKILL_ID]

	def get_skill_name_long(self,id):
		return self.skill_set_list[self.skill_set_list_short.index(self.validate_skill(id))]

	def get_default_trained_skill(self):
		return self.__DEFAULT_TRAINED_SKILL

	def get_default_armor_penalty(self):
		return self.__DEFAULT_ARMOR_PENALTY

	def get_default_cross_class(self):
		return self.__DEFAULT_CROSS_CLASS

	def get_default_key_ability(self):
		return self.__DEFAULT_KEY_ABILITY

	def get_default_skill_points(self):
		return self.__DEFAULT_SKILL_POINTS

	def get_min_skill_points(self):
		return self.__MIN_SKILL_POINTS

	def get_max_skill_points(self):
		return self.__MAX_SKILL_POINTS

	def get_default_skill_id(self):
		return self.__DEFAULT_SKILL_ID

	def get_default_class_skills(self):
		return self.__DEFAULT_CLASS_SKILLS

	def get_default_synergy_skills(self):
		return self.__DEFAULT_SYNERGY_SKILLS

# print core_skill_set_configuration().get_skill_set_list()