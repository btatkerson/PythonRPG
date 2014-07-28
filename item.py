'''
	  Name: item.py
	Author: Benjamin A
   Purpose: The item class creates and base class object that defines properties and methods
            shared by all "items" in the game. It can be extended to create custom/specific items
            needed in game.
'''


from core.__core_item_configuration import core_item_configuration
class item():
	def __init__(self,name="Unknown",ref_id="0"):
		self.item_name = name

		self.item_ref_id = ref_id

		# self.item_class
		# self.item_subclass
		# self.item_base_value
		# self.item_base_weight
		# self._event_item_on_use
		# self._event_item_on_pickup
		# self._event_item_on_drop
		# self._event_item_on_heartbeat

	# A short method in most classes that calls the core settings for that particular class
	def _core(self):
		return core_item_configuration()


print item()._core()

