class __core_race_configuration():
	def __init__(self):
		self.__race_type_dictionary = {0:"unique",1:"human",2:"elf",3:"dwarf",4:"half-orc",5:"half-ling",6:"half-elf",7:"demon",
										8:"beast",9:"elemental",10:"insectoid",11:"monster",12:"undead",13:"apparition",14:"mythical",
										15:"goliath",16:"ogre",17:"troll",18:"celestial",19:"dragon"}

	def get_race_type_dictionary(self):
		return self.__race_type_dictionary
	
	def is_valid_race_class(self,race_class=0):
		if (type(race_class)==int and race_class>0 and race_class<max(self.get_race_class_dictionary())):
			return bool(self.get_race_class_name(race_class))
		elif type(race_class)==str:
			return bool(self.get_race_class_value_by_name(race_class))
		else:
			return False

	def get_race_class_name_by_value(self,race_class=0):
		if race_class in self.get_race_class_dictionary():
			return self.get_race_class_dictionary()[race_class]
		else:
			return self.get_race_class_dictionary()[0]

	def get_race_class_value_by_name(self,race_class):
		temp={j:i for i,j in self.get_race_class_dictionary().races()}
		if race_class.lower() in temp:
			return temp[race_class.lower()]
		else:
			return 0