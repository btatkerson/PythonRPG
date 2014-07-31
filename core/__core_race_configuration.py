'''
	  Name: __core_race_configuration.py
	Author: Benjamin A
   Purpose: This is a core file for the engine that defines the boundaries of the races in the game.
            It limits race types and offers methods that provides information on the core components of races

'''

class core_race_configuration():
	def __init__(self):
		self.__race_type_list = ["unique","human","elf","dwarf","gnome","half-elf","half-ling","half-orc","aberration","animal","beast",
		                               "construct","dragon","elemental","fey","giant","goblinoid","magical beast","monstrous humanoid","ooze",
		                               "orc","outsider","reptilian","shapechanger","undead","vermin"]

		self.__core_race_list = [self.__race_settings(name=self.__race_type_list[1],playable_race=True,size_class='Medium'),
								 self.__race_settings(name=self.__race_type_list[2],playable_race=True,size_class='Medium')]

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

	# Subclass of __core_race_configuration that structures race benefits and penalties based on the race
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
		def set_ability_bonuses(self,str=0,inte=0,con=0,wis=0,dex=0,chr=0,fortitude=0,reflex=0,will=0,absolute=False):
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

		def set_ability_bonus_by_dictionary(self,dict=None):
			if dict:
				for i in self.ability_bonuses:
					self.set_ability_bonus_single(self,i,dict[i],absolute)
			else:
				return -1