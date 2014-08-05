'''
	  Name: __core_item_configuration.py
	Author: Benjamin A
   Purpose: This is a core file for the engine that defines the boundaries of the items.
			Boundaries including item class types, stackability, etc.

'''
class core_item_configuration():
	def __init__(self):
		self.__item_class_list = ['unique','weapon','armor','apparel','potion','container','ammunition','placeable','magic']

	def get_item_class_list(self):
		return self.__item_class_list

	def is_valid_item_class(self,item_class=0):
		if (type(item_class)==int and 0 <= item_class < len(self.get_item_class_list())):
			return bool(self.get_item_class_name(item_class))
		elif type(item_class)==str:
			return bool(self.get_item_class_value_by_name(item_class))
		else:
			return False

	def get_item_class_name_by_value(self,item_class=0):
		if item_class in self.get_item_class_list():
			return self.get_item_class_list()[item_class]
		else:
			return self.get_item_class_list()[0]

	def get_item_class_value_by_name(self,item_class):
		temp={j:i for i,j in self.get_item_class_list().items()}
		if item_class.lower() in temp:
			return temp[item_class.lower()]
		else:
			return 0