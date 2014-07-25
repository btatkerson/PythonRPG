class core_item_configuration():
	def __init__(self):
		self.__item_class_dictionary = {0:"unique",1:"weapon",2:"armor",3:"apparel",4:"potion",5:"container",6:"ammo",7:"placeable",8:"magic"}

	def get_item_class_dictionary(self):
		return self.__item_class_dictionary

	def is_valid_item_class(self,item_class=0):
		if (type(item_class)==int and item_class>0 and item_class<max(self.get_item_class_dictionary())):
			return bool(self.get_item_class_name(item_class))
		elif type(item_class)==str:
			return bool(self.get_item_class_value_by_name(item_class))
		else:
			return False

	def get_item_class_name_by_value(self,item_class=0):
		if item_class in self.get_item_class_dictionary():
			return self.get_item_class_dictionary()[item_class]
		else:
			return self.get_item_class_dictionary()[0]

	def get_item_class_value_by_name(self,item_class):
		temp={j:i for i,j in self.get_item_class_dictionary().items()}
		if item_class.lower() in temp:
			return temp[item_class.lower()]
		else:
			return 0