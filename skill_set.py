'''
	  Name: skill_set.py
	Author: Benjamin A
   Purpose: This is the 'skill_set' class which controls and maintains the skills all creatures get in-game.

'''

from core.__core_skill_set_configuration import core_skill_set_configuration
from core.__core_creature_configuration import core_creature_configuration
from core.__core_creature_class_configuration import core_creature_class_configuration
'''from dice import dice'''

class skill_set():
	class skill():
		def __init__(self,skill_id=None,base_skill_points=None,trained_skill=None,armor_penalty=None,key_ability=None,
		             cross_class=None, class_skills=None, synergy_skills=None):
			self.skill_id = core_skill_set_configuration().validate_skill(skill_id) or \
			                core_skill_set_configuration().get_default_skill_id()


			self.base_skill_points = core_skill_set_configuration().get_default_skill_points()
			self.set_base_skill_points(base_skill_points)

			self.trained_skill = self.__false_default(trained_skill,core_skill_set_configuration().get_default_trained_skill())
			self.armor_penalty = self.__false_default(armor_penalty, core_skill_set_configuration().get_default_armor_penalty())
			self.cross_class = self.__false_default(cross_class,core_skill_set_configuration().get_default_cross_class())
			self.key_ability = core_creature_configuration().validate_ability(key_ability)
			self.class_skills = core_skill_set_configuration().get_default_class_skills()
			self.set_class_skills(class_skills)
			self.synergy_skills = core_skill_set_configuration().get_default_synergy_skills()
			self.set_synergy_skills(synergy_skills)
		'''
		The method of "a or b" where if 'a' is the initial input and 'b' is the core_setting is no good for
		booleans during the initialization process. In non-boolean 'a or b'

		'a or b' is always going to return True if either one is True. True > False > None
		False or True = True
		None or True = True
		None or False = False

		So, I hope that explains why the function below is needed, otherwise we wouldn't get a return of "False" if
		that was the initial input.

		This is used because if a boolean attribute is given as input during the initialization process, 'False' needs
		to be checked for and returned if that was requested.
		'''

		def __false_default(self,check,core_setting):
			if check == False:
				return check
			return core_setting

		def get_skill_id(self):
			return self.skill_id

		def get_skill_name(self):
			return core_skill_set_configuration().get_skill_name_long(self.skill_id)

		def set_base_skill_points(self,add=None,absolute=False):
			if add == None:
				add = 0
			if absolute:
				self.base_skill_points = min(max(core_skill_set_configuration().get_min_skill_points(),add),
				                             core_skill_set_configuration().get_max_skill_points())
			else:
				self.base_skill_points = min(max(core_skill_set_configuration().get_min_skill_points(),
				                                 self.base_skill_points+add),
				                             core_skill_set_configuration().get_max_skill_points())

		# This is used to get the 'base' skill points, synergy bonuses do not get included
		def get_base_skill_points(self):
			return self.base_skill_points

		def is_trained_skill(self):
			return self.trained_skill

		# is (affected by) armor penalties
		def is_armor_penalty(self):
			return self.trained_skill

		def is_cross_class(self):
			return self.cross_class

		def set_key_ability(self,key_ability=None):
			if core_creature_configuration().is_ability(key_ability):
				self.key_ability = key_ability.lower()
			if not self.key_ability:
				self.key_ability = core_skill_set_configuration().get_default_key_ability()

		def get_key_ability(self):
			return self.key_ability


		def get_class_skills(self):
			return self.class_skills

		def set_class_skills(self,class_set=None):
			if class_set == None:
				return core_skill_set_configuration().get_default_class_skills()
			elif type(class_set) == str:
				class_set = [class_set]
			temp = []
			for i in class_set:
				temp.append(core_creature_class_configuration().validate_class(i))

			self.class_skills = sorted(list(set(temp)))

		# Checks if a certain class is in the class skill set
		def is_class_skill(self,id=None):
			if id == None:
				return False
			if core_creature_class_configuration().validate_class(id) in self.class_skills:
				return True
			return False

		def get_synergy_skills(self):
			return self.synergy_skills

		def set_synergy_skills(self,synergy_set=None):
			if synergy_set == None:
				return core_skill_set_configuration().get_default_synergy_skills()
			elif type(synergy_set) == str:
				synergy_set = [synergy_set]
			temp = []
			for i in synergy_set:
				temp.append(core_skill_set_configuration().validate_skill(i))

			self.synergy_skills = sorted(list(set(temp)))

		# Checks if a certain class is in the synergy skill set
		def is_synergy_skill(self,id=None):
			if id==None:
				return False
			if core_skill_set_configuration().validate_skill(id) in self.synergy_skills:
				return True
			return False

	def _core(self):
		return core_skill_set_configuration()

	def __init__(self):
		# self.skill_list = {i:self.skill(skill_name=i,base_skill_points=dice().d()[0]) for i in self._core().get_skill_set_list_short()}

		# This is really should not be altered with ANYTHING other than a proper custom script.
		# I will implement the custom script API later.
		self.skill_list = self.__generate_skill_list()



	# This takes all the initial skill settings that are defined in the core_skill_set_configuration.py class and
	# interprets them (it's a list of dictionaries)
	def __generate_skill_list(self):
		skill_defaults = core_skill_set_configuration().get_default_skill_settings_list()

		temp={self._core().validate_skill(i):self.skill(
							skill_id=skill_defaults[i]['keyID'], trained_skill=skill_defaults[i]['trained_skill'],
		                    armor_penalty=skill_defaults[i]['armor_penalty'],key_ability=skill_defaults[i]['key_ability'],
		                    cross_class=skill_defaults[i]['cross_class'],class_skills=skill_defaults[i]['class_skills'],
		                    synergy_skills=skill_defaults[i]['synergy_skills'])
		      for i in range(0,len(self._core().get_skill_set_list_short()))}
		return temp

	def get_skill_list(self):
		return self.skill_list

	def get_skill(self,skillID=None):
		return self.skill_list[self._core().validate_skill(skillID)] or self.skill()
		# The 'or self.skill()' allows 'get_skill' to autofill methods, it will never default to 'self.skill()' no
		# matter the input to skillID.

	# Returns the sum of the base points for the skill and any synergy bonuses, this will be the commonly
	# used of the two 'get points' methods.

	def get_points(self,skillID=None):
		skill = self.get_skill(skillID)
		bonus_points = 0
		if skill.get_synergy_skills():
			for i in skill.get_synergy_skills():
				bonus_points += int(self.get_skill(i).get_base_skill_points()/5)*2
		return skill.get_base_skill_points()+bonus_points

	# Used to... I don't quite remember what I wrote this for...
	def is_skill_instance(self,skill=skill()):
		if isinstance(skill,self.skill):
			return True
		return -1

	# This is used as a 'skill check'. However, this is going to be moved to a different segment
	def check_against(self, skillID=None, roll_points=None):
		skill = self.get_skill(skillID)

		if roll_points >= skill.get_base_skill_points():
			return True
		else:
			return False

#print skill_set().get_skill(16).get_skill_id()
