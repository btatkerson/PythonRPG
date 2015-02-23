'''
	  Name: __core_creature_class_configuration.py
	Author: Benjamin A
   Purpose: This is a core file for the engine that defines the boundaries of the classes in the game.
            THIS... is going to be mad cray.

'''


class core_creature_class_configuration():
	class creature_Class():
		'''
		Used to provide constants for valid creature classes
		'''
		def __init__(self):
			self.UNIQUE = self.UNI = 'uni'
			self.BARBARIAN = self.BBN = 'bbn'
			self.BARD = self.BRD = 'brd'
			self.CLERIC = self.CLR = 'clr'
			self.DRUID = self.DRD = 'drd'
			self.FIGHTER = self.FTR = 'ftr'
			self.MONK = self.MNK = 'mnk'
			self.PALADIN = self.PLD = 'pld'
			self.RANGER = self.RGR = 'rgr'
			self.ROGUE = self.ROG = 'rog'
			self.SORCERER = self.SOR = 'sor'
			self.WIZARD = self.WIZ = 'wiz'

	def __init__(self):
		self.creatureClass = self.creature_Class()

		# Used for short hand convenience purposes
		self.class_name_list_short=[self.creatureClass.UNIQUE,
					    self.creatureClass.BARBARIAN,
					    self.creatureClass.BARD,
					    self.creatureClass.CLERIC,
					    self.creatureClass.DRUID,
					    self.creatureClass.FIGHTER,
					    self.creatureClass.MONK,
					    self.creatureClass.PALADIN,
					    self.creatureClass.RANGER,
					    self.creatureClass.ROGUE,
					    self.creatureClass.SORCERER,
					    self.creatureClass.WIZARD]

		self.class_name_list_long= ['unique',
									'barbarian',
									'bard',
									'cleric',
									'druid',
									'fighter',
									'monk',
									'paladin',
									'ranger',
									'rogue',
									'sorcerer',
									'wizard']


		self.__DEFAULT_CLASS_ID = 5 # Fighter


	def get_class_name_by_id(self,id=None):
		if 0 <= id < len(self.class_name_list_long):
			return self.class_name_list_long[id]
		return self.class_name_list_long[self.__DEFAULT_CLASS_ID]

	def get_class_id_by_name(self,id=None):
		if id == None:
			return self.__DEFAULT_CLASS_ID
		id = id.lower()

		if id in self.class_name_list_long:
			return self.class_name_list_long.index(id)
		elif id in self.class_name_list_short:
			return self.class_name_list_short.index(id)

		return self.__DEFAULT_CLASS_ID

	def is_class(self,id=None):
		if type(id)==int:
			if 0 <= id < len(self.class_name_list_short):
				return True
		elif id.lower() in self.class_name_list_long or id.lower() in \
				self.class_name_list_short:
			return True
		return False

	# Returns the shorthand form of the class names for standard use across development. Defaults to fighter
	def validate_class(self,id=None):
		if self.is_class(id):
			if type(id)==int:
				if 0 <= id < len(self.class_name_list_short):
					return self.class_name_list_short[id]
			elif id.lower() in self.class_name_list_short:
				return id.lower()
			else:
				return self.class_name_list_short[self.class_name_list_long.index(id)]
		return self.class_name_list_short[self.__DEFAULT_CLASS_ID]


	def get_default_class_id(self):
		return self.__DEFAULT_CLASS_ID
