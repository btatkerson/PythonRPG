'''
	  Name: __core_item_configuration.py
	Author: Benjamin A
   Purpose: This is a core file for the engine that defines the boundaries of the items.
			Boundaries including item class types, stackability, etc.

'''
class core_item_configuration():
	def __init__(self):
		
		self.__DEFAULT_DROPPABLE = False
		self.__DEFAULT_ITEM_CLASS = 0
		self.__DEFAULT_ITEM_WEIGHT = 1.0 # Item weight in pounds (lbs) according to DnD ruleset.
		self.__DEFAULT_PLOT = False
		self.__DEFAULT_STACK_SIZE = 1
		self.__DEFAULT_STOLEN = False
		self.__MIN_ITEM_WEIGHT = 0.0
		self.__MIN_STACK_SIZE = 1
		self.__MAX_STACK_SIZE = 50000
		self.__ITEM_CLASS_LIST = ['unique','weapon','armor','apparel','potion','container','ammunition','placeable','magic','key']
		self.__WEAPON_CLASS_LIST = ['dagger','shortsword','longsword','greatsword']

	def get_default_droppable(self):
		return self.__DEFAULT_DROPPABLE

	def get_default_item_weight(self):
		return self.__DEFAULT_ITEM_WEIGHT

	def get_min_item_weight(self):
		return self.__MIN_ITEM_WEIGHT

	def get_default_plot(self):
		return self.__DEFAULT_PLOT

	def get_default_stack_size(self):
		return self.__DEFAULT_STACK_SIZE

	def get_default_stolen(self):
		return self.__DEFAULT_STOLEN

	def get_min_stack_size(self):
		return self.__MIN_STACK_SIZE

	def get_max_stack_size(self):
		return self.__MAX_STACK_SIZE

	def get_item_class_list(self):
		return self.__ITEM_CLASS_LIST

	def is_valid_item_class(self,item_class=0):
		if (type(item_class)==int and 0 <= item_class < len(self.get_item_class_list())):
			return bool(self.get_item_class_name_by_id(item_class))
		elif type(item_class)==str:
			return bool(self.get_item_class_id_by_name(item_class))
		else:
			return False

	def get_default_item_class(self):
		return self.__DEFAULT_ITEM_CLASS


	def get_item_class(self, item_class=None):
		if item_class is None:
			return self.get_default_item_class()

		if type(item_class) == str:
			return self.get_item_class_id_by_name(item_class)

		return self.get_item_class_name_by_id(item_class)

	def get_item_class_name_by_id(self, item_class=None):
		if item_class is None:
			item_class = self.get_default_item_class()
		if 0<= item_class < len(self.get_item_class_list()):
			return self.get_item_class_list()[item_class]
		return self.get_item_class_list()[self.__DEFAULT_ITEM_CLASS]

	def get_item_class_id_by_name(self, item_class=None):
		if item_class is None:
			item_class = self.get_default_item_class()

		if item_class.lower() in self.get_item_class_list():
			return list.index(self.get_item_class_list(),item_class.lower())
		return item_class



a = core_item_configuration()

print a.get_item_class_name_by_id(3)