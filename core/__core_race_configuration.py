'''
	  Name: __core_race_configuration.py
	Author: Benjamin A
   Purpose: This is a core file for the engine that defines the boundaries of the races in the game.
            It limits race types and offers methods that provides information on the core components of races

'''

class core_race_configuration():
	def __init__(self):
		# The size classes by name, occupying space in feet, and natural reach in feet. These are standard, but exceptions can be made
		# to the the default reach distance and occupying space if necessary
							#  [name, space_in_feet, natural reach distance in feet]
		self.__size_classes = [['unique',0,0],
		                       ['fine', .5, 0],
		                       ['diminutive', 1, 0],
		                       ['tiny', 2.5, 0],
		                       ['small', 5, 5],
		                       ['medium', 5, 5],
		                       ['large_tall', 10, 10],
		                       ['large_long', 10, 5],
		                       ['huge_tall', 15, 15],
		                       ['huge_long', 15, 10],
		                       ['gargantuan_tall', 20, 20],
		                       ['gargantuan_long', 20, 15],
		                       ['colossal_tall', 30, 30],
		                       ['colossal_long', 30, 20]]

		self.__DEFAULT_RACE_TYPE = 0 # Unique race type
		self.__DEFAULT_SIZE_CLASS_ID = 5 # Medium size class

		# A list all all the possible race types, 0 = unique which will be used for override/custom classes
		self.__race_type_list = ["unique",
		                         "human",
		                         "elf",
		                         "dwarf",
		                         "gnome",
		                         "half-elf",
		                         "half-ling",
		                         "half-orc",
		                         "aberration",
		                         "animal",
		                         "beast",
		                         "construct",
		                         "dragon",
		                         "elemental",
		                         "fey",
		                         "giant",
		                         "goblinoid",
		                         "magical beast",
		                         "monstrous humanoid",
		                         "ooze",
		                         "orc",
		                         "outsider",
		                         "reptilian",
		                         "shapechanger",
		                         "undead",
		                         "vermin"]


		self.__DEFAULT_SIZE_CLASS_NAME = self.get_size_class_list()[self.get_default_size_class_id()][0]

		#
		self.__core_race_list = [self.__race_settings(name=self.__race_type_list[1],playable_race=True,size_class=self.get_size_class_list()[5]),
								self.__race_settings(name=self.__race_type_list[2],playable_race=True,size_class=self.get_size_class_list()[5]),
								self.__race_settings(name=self.__race_type_list[3],playable_race=True,size_class=self.get_size_class_list()[5]),
								self.__race_settings(name=self.__race_type_list[4],playable_race=True,size_class=self.get_size_class_list()[4]),
								self.__race_settings(name=self.__race_type_list[5],playable_race=True,size_class=self.get_size_class_list()[5]),
								self.__race_settings(name=self.__race_type_list[6],playable_race=True,size_class=self.get_size_class_list()[4]),
								self.__race_settings(name=self.__race_type_list[6],playable_race=True,size_class=self.get_size_class_list()[5])]

	def get_default_race_type(self):
		return self.__DEFAULT_RACE_TYPE

	def get_default_size_class_id(self):
		return self.__DEFAULT_SIZE_CLASS_ID
	
	def get_default_size_class_name(self):
		return self.__DEFAULT_SIZE_CLASS_NAME

	def is_valid_race_type(self,race_type=0):
		if (type(race_type)==int and race_type>0 and race_type<max(self.get_race_type_list())):
			return bool(self.get_race_type_name_by_value(race_type))
		elif type(race_type)==str:
			return bool(self.get_race_type_value_by_name(race_type))
		else:
			return False

	def get_race_type_name_by_value(self,race_type=0):
		if race_type in self.get_race_type_list():
			return self.get_race_type_list()[race_type]
		else:
			return self.get_race_type_list()[0]

	def get_race_type_value_by_name(self,race_type):
		if race_type in self.get_race_type_list()[race_type]:
			return self.get_race_type_list().index(race_type)

	def get_race_type_list(self):
		return self.__race_type_list

	def get_size_class_list(self):
		return self.__size_classes

	# Returns class size attributes by name, return_class_id=True returns the index on the size_class list, which is the ID
	def get_size_class_by_name(self, name=None, return_class_id=False):
		if name == None:
			name = self.get_default_size_class_name()

		# If there are size classes with a "tall" or "long", default will be "tall" if not specified.
		# For instance, "large_tall" and "large_long" are both valid for variable "name", but if name were to equal 'large',
		# 'large_tall' will be returned
		for i in range(0,len(self.get_size_class_list())):
			if name.lower() in self.get_size_class_list()[i]:
				if return_class_id:
					return i
				else:
					return self.get_size_class_list()[i]
				
		# If name wasn't found, the 'unique' size is returned
		if return_class_id:
			return 0
		else:
			return self.get_size_class_list()[0]
		
	# Returns class size by id	
	def get_size_class_by_id(self,id=None):
		if id == None:
			id = self.get_default_size_class_id()

		if 0 <= id <= len(self.get_size_class_list()):
			return self.get_size_class_list()[id]
		else:
			return self.get_size_class_list()[0]

	# Subclass of __core_race_configuration that structures race benefits and penalties and other things associated with
	# that particular race
	class __race_settings():
		def __init__(self,name,playable_race=False,favored_classes=[],favored_deities=[],size_class='',base_land_speed=None):
			self.race_name=name
			self.playable_race=playable_race
			self.favored_classes=favored_classes
			self.favored_deities=favored_deities
			self.size_class=size_class
			# self.base_land_speed=base_land_speed # Will not be used until future development, races all have a base land speed which determines how much
												   # far a creature can move in one round. This is not the only thing that will affect land speed.
			self.ability_bonuses = {'str':0, 'int':0, 'con':0, 'wis':0, 'dex':0, 'chr':0,'fortitude':0,'reflex':0,'will':0}

		# Set one, set all, set some, this is just to make the penalty/bonus dictionary simple to fill.
		# Example - A dwarf class gets a racial bonus of +2 constitution, but a penalty of a -2 charisma
		# This can be set by calling the function as so set_ability_bonus(con=2,chr=-2)
		def set_ability_bonuses(self,str=0,inte=0,con=0,wis=0,dex=0,chr=0,fortitude=0,reflex=0,will=0,absolute=True):
			if str or absolute:
				self.set_ability_bonus_single('str',str,absolute)
			if inte or absolute:
				self.set_ability_bonus_single('int',inte,absolute)
			if con or absolute:
				self.set_ability_bonus_single('con',con,absolute)
			if wis or absolute:
				self.set_ability_bonus_single('wis',wis,absolute)
			if dex or absolute:
				self.set_ability_bonus_single('dex',dex,absolute)
			if chr or absolute:
				self.set_ability_bonus_single('chr',chr,absolute)
			if fortitude or absolute:
				self.set_ability_bonus_single('fortitude',fortitude,absolute)
			if reflex or absolute:
				self.set_ability_bonus_single('reflex',reflex,absolute)
			if will or absolute:
				self.set_ability_bonus_single('will',will,absolute)

		# Sets an individual ability at a time, can be used by itself or with "set_ability_bonuses"
		# 'absolute' == False adds variable 'add' to the ability given in the 'ability' parameter
		# 'absolute' == True sets the ability given in the 'ability' parameter to the value given in 'add', does not add to previous ability
		def set_ability_bonus_single(self,ability,add=0,absolute=False):
			if ability.lower() in self.ability_bonuses:
				if absolute:
					self.ability_bonuses[ability] = add
				else:
					self.ability_bonuses[ability] += add
				return self.ability_bonuses[ability]
			else:
				return -1

		# Temporarily here unless it ultimately goes unused, this is supposed to allow copying of ability bonuses and resetting them. Possibly
		# I... I don't think this is needed, but I should have thought about that before writing it. It wasn't a waste of YOUR time.
		def get_ability_bonus_dictionary(self):
			return self.ability_bonuses


		''' Not sure this will be used either '''
		# def set_ability_bonus_by_dictionary(self,dict=None):
		# 	if dict:
		# 		for i in self.ability_bonuses:
		# 			self.set_ability_bonus_single(self,i,dict[i],absolute)
		# 	else:
		# 		return -1