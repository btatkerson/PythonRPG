'''
	  Name: __core_creature_configuration.py
	Author: Benjamin A
   Purpose: This is a core file for the engine that defines the boundaries of the skill set in the game.

'''
from core.__core_constants import core_constants

class core_skill_set_configuration(core_constants):
	def __init__(self):
		core_constants.__init__(self)
		# List of skills, 0 is 'unique' and unused during initialization

		self.skill_set_list_short =[self.SKILL.UNIQUE,
                                    self.SKILL.ANIMAL_EMPATHY,
                                    self.SKILL.APPRAISE,
                                    self.SKILL.BLUFF,
                                    self.SKILL.CONCENTRATION,
                                    self.SKILL.CRAFT_ARMOR,
                                    self.SKILL.CRAFT_TRAP,
                                    self.SKILL.CRAFT_WEAPON,
                                    self.SKILL.DISABLE_TRAP,
                                    self.SKILL.DISCIPLINE,
                                    self.SKILL.HEAL,
                                    self.SKILL.HIDE,
                                    self.SKILL.INTIMIDATE,
                                    self.SKILL.LISTEN,
                                    self.SKILL.LORE,
                                    self.SKILL.MOVE_SILENTLY,
                                    self.SKILL.OPEN_LOCK,
                                    self.SKILL.PARRY,
                                    self.SKILL.PERFORM,
                                    self.SKILL.PICK_POCKET,
                                    self.SKILL.RIDE,
                                    self.SKILL.SEARCH,
                                    self.SKILL.SET_TRAP,
                                    self.SKILL.SPELLCRAFT,
                                    self.SKILL.SPOT,
                                    self.SKILL.TAUNT,
                                    self.SKILL.TUMBLE,
                                    self.SKILL.USE_MAGIC_DEVICE]

		self.skill_set_list = ['unique',
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
		                        'move_silently',
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
		self.__DEFAULT_SKILL_SETTINGS_LIST =[
			{
			'keyID':0, # Unique
			'trained_skill':self.__DEFAULT_TRAINED_SKILL,
			'armor_penalty':self.__DEFAULT_ARMOR_PENALTY,
			'cross_class':self.__DEFAULT_CROSS_CLASS,
			'key_ability':self.__DEFAULT_KEY_ABILITY,
			'skill_points':self.__DEFAULT_SKILL_POINTS,
			'class_skills':self.__DEFAULT_CLASS_SKILLS,
			'synergy_skills':self.__DEFAULT_SYNERGY_SKILLS
			},
			{
			'keyID':1, # Animal Empathy
			'trained_skill':True,
			'armor_penalty':False,
			'cross_class':False,
			'key_ability':self.ABILITY.CHR,
			'skill_points':0,
			'class_skills':[self.CREATURECLASS.DRUID,self.CREATURECLASS.RANGER],
			'synergy_skills':[]
			},
			{
			'keyID':2, # Appraise
			'trained_skill':False,
			'armor_penalty':False,
			'cross_class':True,
			'key_ability':self.ABILITY.INT,
			'skill_points':0,
			'class_skills':[self.CREATURECLASS.BARD,self.CREATURECLASS.ROGUE],
			'synergy_skills':[]
			},
			{
			'keyID':3, # Bluff
			'trained_skill':True,
			'armor_penalty':False,
			'cross_class':True,
			'key_ability':self.ABILITY.CHR,
			'skill_points':0,
			'class_skills':[self.CREATURECLASS.BARD,self.CREATURECLASS.ROGUE],
			'synergy_skills':[]
			},
			{
			'keyID':4, # Concentration
			'trained_skill':False,
			'armor_penalty':False,
			'cross_class':True,
			'key_ability':self.ABILITY.CON,
			'skill_points':0,
			'class_skills':[self.CREATURECLASS.BARD,self.CREATURECLASS.CLERIC,self.CREATURECLASS.DRUID,self.CREATURECLASS.FIGHTER,self.CREATURECLASS.MONK,self.CREATURECLASS.PALADIN,self.CREATURECLASS.RANGER,self.CREATURECLASS.SORCERER,self.CREATURECLASS.WIZARD],
			'synergy_skills':[]
			},
			{
			'keyID':5, # Craft Armor
			'trained_skill':False,
			'armor_penalty':False,
			'cross_class':True,
			'key_ability':self.ABILITY.INT,
			'skill_points':0,
			'class_skills':[self.CREATURECLASS.BARBARIAN,self.CREATURECLASS.BARD,self.CREATURECLASS.CLERIC,self.CREATURECLASS.DRUID,self.CREATURECLASS.FIGHTER,self.CREATURECLASS.MONK,self.CREATURECLASS.PALADIN,self.CREATURECLASS.RANGER,self.CREATURECLASS.ROGUE,self.CREATURECLASS.SORCERER,self.CREATURECLASS.WIZARD], # All Classes,
			'synergy_skills':[]
			},
			{
			'keyID':6, # Craft Trap
			'trained_skill':False,
			'armor_penalty':False,
			'cross_class':True,
			'key_ability':self.ABILITY.INT,
			'skill_points':0,
			'class_skills':[self.CREATURECLASS.BARBARIAN,self.CREATURECLASS.BARD,self.CREATURECLASS.CLERIC,self.CREATURECLASS.DRUID,self.CREATURECLASS.FIGHTER,self.CREATURECLASS.MONK,self.CREATURECLASS.PALADIN,self.CREATURECLASS.RANGER,self.CREATURECLASS.ROGUE,self.CREATURECLASS.SORCERER,self.CREATURECLASS.WIZARD], # All Classes,
			'synergy_skills':[]
			},
			{
			'keyID':7, # Craft weapon
			'trained_skill':False,
			'armor_penalty':False,
			'cross_class':True,
			'key_ability':self.ABILITY.INT,
			'skill_points':0,
			'class_skills':[self.CREATURECLASS.BARBARIAN,self.CREATURECLASS.BARD,self.CREATURECLASS.CLERIC,self.CREATURECLASS.DRUID,self.CREATURECLASS.FIGHTER,self.CREATURECLASS.MONK,self.CREATURECLASS.PALADIN,self.CREATURECLASS.RANGER,self.CREATURECLASS.ROGUE,self.CREATURECLASS.SORCERER,self.CREATURECLASS.WIZARD], # All Classes,
			'synergy_skills':[]
			},
			{
			'keyID':8, # Disable Trap
			'trained_skill':True,
			'armor_penalty':False,
			'cross_class':True,
			'key_ability':self.ABILITY.INT,
			'skill_points':0,
			'class_skills':[self.CREATURECLASS.ROGUE],
			'synergy_skills':[self.SKILL.SET_TRAP], # Set Trap
			},
			{
			'keyID':9, # Discipline
			'trained_skill':False,
			'armor_penalty':False,
			'cross_class':True,
			'key_ability':self.ABILITY.STR,
			'skill_points':0,
			'class_skills':[self.CREATURECLASS.BARBARIAN,self.CREATURECLASS.BARD,self.CREATURECLASS.FIGHTER,self.CREATURECLASS.MONK,self.CREATURECLASS.PALADIN,self.CREATURECLASS.RANGER],
			'synergy_skills':[]
			},
			{
			'keyID':10, # Heal
			'trained_skill':False,
			'armor_penalty':False,
			'cross_class':False,
			'key_ability':self.ABILITY.WIS,
			'skill_points':0,
			'class_skills':[self.CREATURECLASS.BARBARIAN,self.CREATURECLASS.BARD,self.CREATURECLASS.CLERIC,self.CREATURECLASS.DRUID,self.CREATURECLASS.FIGHTER,self.CREATURECLASS.MONK,self.CREATURECLASS.PALADIN,self.CREATURECLASS.RANGER,self.CREATURECLASS.ROGUE,self.CREATURECLASS.SORCERER,self.CREATURECLASS.WIZARD], # All Classes
			'synergy_skills':[]
			},
			{
			'keyID':11, # Hide
			'trained_skill':False,
			'armor_penalty':False,
			'cross_class':True,
			'key_ability':self.ABILITY.DEX,
			'skill_points':0,
			'class_skills':[self.CREATURECLASS.BARD,self.CREATURECLASS.MONK,self.CREATURECLASS.RANGER,self.CREATURECLASS.ROGUE],
			'synergy_skills':[]
			},
			{
			'keyID':12, # Intimidate
			'trained_skill':False,
			'armor_penalty':False,
			'cross_class':True,
			'key_ability':self.ABILITY.CHR,
			'skill_points':0,
			'class_skills':[self.CREATURECLASS.BARBARIAN,self.CREATURECLASS.ROGUE],
			'synergy_skills':[]
			},
			{
			'keyID':13, # Listen
			'trained_skill':False,
			'armor_penalty':False,
			'cross_class':True,
			'key_ability':self.ABILITY.WIS,
			'skill_points':0,
			'class_skills':[self.CREATURECLASS.BARBARIAN,self.CREATURECLASS.BARD,self.CREATURECLASS.MONK,self.CREATURECLASS.RANGER,self.CREATURECLASS.ROGUE],
			'synergy_skills':[]
			},
			{
			'keyID':14, # Lore
			'trained_skill':False,
			'armor_penalty':False,
			'cross_class':True,
			'key_ability':self.ABILITY.INT,
			'skill_points':0,
			'class_skills':[self.CREATURECLASS.BARBARIAN,self.CREATURECLASS.BARD,self.CREATURECLASS.CLERIC,self.CREATURECLASS.DRUID,self.CREATURECLASS.FIGHTER,self.CREATURECLASS.MONK,self.CREATURECLASS.PALADIN,self.CREATURECLASS.RANGER,self.CREATURECLASS.ROGUE,self.CREATURECLASS.SORCERER,self.CREATURECLASS.WIZARD],
			'synergy_skills':[]
			},
			{
			'keyID':15, # Move Silently
			'trained_skill':False,
			'armor_penalty':False,
			'cross_class':True,
			'key_ability':self.ABILITY.DEX,
			'skill_points':0,
			'class_skills':[self.CREATURECLASS.BARD,self.CREATURECLASS.MONK,self.CREATURECLASS.RANGER,self.CREATURECLASS.ROGUE],
			'synergy_skills':[]
			},
			{
			'keyID':16, # Open Lock
			'trained_skill':True,
			'armor_penalty':False,
			'cross_class':True,
			'key_ability':self.ABILITY.DEX,
			'skill_points':0,
			'class_skills':[self.CREATURECLASS.ROGUE],
			'synergy_skills':[]
			},
			{
			'keyID':17, # Parry
			'trained_skill':False,
			'armor_penalty':False,
			'cross_class':True,
			'key_ability':self.ABILITY.DEX,
			'skill_points':0,
			'class_skills':[self.CREATURECLASS.BARBARIAN,self.CREATURECLASS.BARD,self.CREATURECLASS.CLERIC,self.CREATURECLASS.DRUID,self.CREATURECLASS.FIGHTER,self.CREATURECLASS.MONK,self.CREATURECLASS.PALADIN,self.CREATURECLASS.RANGER,self.CREATURECLASS.ROGUE,self.CREATURECLASS.SORCERER,self.CREATURECLASS.WIZARD],
			'synergy_skills':[]
			},
			{
			'keyID':18, # Perform
			'trained_skill':False,
			'armor_penalty':False,
			'cross_class':False,
			'key_ability':self.ABILITY.CHR,
			'skill_points':0,
			'class_skills':[self.CREATURECLASS.BARD],
			'synergy_skills':[]
			},
			{
			'keyID':19, # Persuade
			'trained_skill':False,
			'armor_penalty':False,
			'cross_class':True,
			'key_ability':self.ABILITY.CHR,
			'skill_points':0,
			'class_skills':[self.CREATURECLASS.BARD,self.CREATURECLASS.CLERIC,self.CREATURECLASS.DRUID,self.CREATURECLASS.MONK,self.CREATURECLASS.PALADIN,self.CREATURECLASS.ROGUE],
			'synergy_skills':[]
			},
			{
			'keyID':20, # Pick Pocket
			'trained_skill':True,
			'armor_penalty':True,
			'cross_class':True,
			'key_ability':self.ABILITY.DEX,
			'skill_points':0,
			'class_skills':[self.CREATURECLASS.BARD,self.CREATURECLASS.ROGUE],
			'synergy_skills':[]
			},
			{
			'keyID':21, # Ride
			'trained_skill':False,
			'armor_penalty':False,
			'cross_class':True,
			'key_ability':self.ABILITY.CHR,
			'skill_points':0,
			'class_skills':[self.CREATURECLASS.BARBARIAN,self.CREATURECLASS.FIGHTER,self.CREATURECLASS.PALADIN,self.CREATURECLASS.RANGER],
			'synergy_skills':[]
			},
			{
			'keyID':22, # Search
			'trained_skill':False,
			'armor_penalty':False,
			'cross_class':True,
			'key_ability':self.ABILITY.INT,
			'skill_points':0,
			'class_skills':[self.CREATURECLASS.RANGER,self.CREATURECLASS.ROGUE],
			'synergy_skills':[]
			},
			{
			'keyID':23, # Set Trap
			'trained_skill':True,
			'armor_penalty':False,
			'cross_class':True,
			'key_ability':self.ABILITY.DEX,
			'skill_points':0,
			'class_skills':[self.CREATURECLASS.RANGER,self.CREATURECLASS.ROGUE],
			'synergy_skills':[self.SKILL.DISABLE_TRAP] # Disable Trap
			},
			{
			'keyID':24, # Spellcraft
			'trained_skill':True,
			'armor_penalty':False,
			'cross_class':True,
			'key_ability':self.ABILITY.INT,
			'skill_points':0,
			'class_skills':[self.CREATURECLASS.BARD,self.CREATURECLASS.CLERIC,self.CREATURECLASS.SORCERER,self.CREATURECLASS.WIZARD],
			'synergy_skills':[]
			},
			{
			'keyID':25, # Spot
			'trained_skill':False,
			'armor_penalty':False,
			'cross_class':True,
			'key_ability':self.ABILITY.WIS,
			'skill_points':0,
			'class_skills':[self.CREATURECLASS.RANGER,self.CREATURECLASS.ROGUE],
			'synergy_skills':[]
			},
			{
			'keyID':26, # Taunt
			'trained_skill':False,
			'armor_penalty':False,
			'cross_class':True,
			'key_ability':self.ABILITY.CHR,
			'skill_points':0,
			'class_skills':[self.CREATURECLASS.BARBARIAN,self.CREATURECLASS.BARD,self.CREATURECLASS.PALADIN],
			'synergy_skills':[]
			},
			{
			'keyID':27, # Tumble
			'trained_skill':True,
			'armor_penalty':False,
			'cross_class':False,
			'key_ability':self.ABILITY.DEX,
			'skill_points':0,
			'class_skills':[self.CREATURECLASS.BARD,self.CREATURECLASS.MONK,self.CREATURECLASS.ROGUE],
			'synergy_skills':[],
			},
			{
			'keyID':28, # Use Magic Device
			'trained_skill':True,
			'armor_penalty':False,
			'cross_class':False,
			'key_ability':self.ABILITY.CHR,
			'skill_points':0,
			'class_skills':[self.CREATURECLASS.BARD,self.CREATURECLASS.ROGUE],
			'synergy_skills':[]
			}
		]


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
		if type(id) ==int:
			if 0 <= id < len(self.skill_set_list_short):
				return True
		elif id.lower() in self.skill_set_list or id.lower() in \
				self.skill_set_list_short:
			return True
		return False

	# Returns the name of the skill no matter the input. It's basically a safety measure for custom scripts
	# and developer scripts because it will allow the game to run even if an error is made such as a typo.
	def validate_skill(self,id=None):
		if self.is_skill(id):
			if type(id) ==int:
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

	def get_default_skill_settings_list(self):
		return self.__DEFAULT_SKILL_SETTINGS_LIST

		# print core_skill_set_configuration().get_skill_set_list()
