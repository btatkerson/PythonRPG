'''
      Name: item.py
    Author: Benjamin A
   Purpose: The item class creates and base class object that defines properties and methods
            shared by all "items" in the game. It can be extended to create custom/specific items
            needed in game.
'''


import core.__core_constants_mod as ccs
import core.__core_item_configuration as core_item
class item():
    def __init__(self, name=None, item_class=None, item_weight=None, base_cost=None, stack_size=None, droppable=None, stolen=None, plot=None, equippable_slots=None, description=None):
        self.item_name = None
        self.set_item_name(name)

        self.item_class = None
        self.set_item_class(item_class)

        self.item_weight = None
        self.set_item_weight(item_weight)

        self.base_cost = None
        self.set_base_cost(base_cost)
        
        self.stack_size = None
        self.set_stack_size(stack_size)

        self.droppable = None
        self.set_droppable(droppable)

        self.stolen = None
        self.set_stolen(stolen)

        self.plot = None
        self.set_plot(plot)

        self.equippable_slots = None
        self.set_equippable_slots(equippable_slots)

        self.description = None
        self.set_description(description)


    def get_item_name(self):
        '''
        Returns a string of the full item name, despite length of string
        '''
        return self.item_name

    def set_item_name(self, item_name=None):
        str_len = len(str(item_name)) 
        if str_len > core_item.get_max_item_name_length():
            self.item_name = str(item_name)[:core_item.get_max_item_name_length()]
            return 1

        elif core_item.get_min_item_name_length() <= str_len <= core_item.get_max_item_name_length():
            self.item_name = str(item_name)
            return 1
        
        self.item_name = core_item.get_default_item_name()

    def get_item_class(self):
        return self.item_class

    def set_item_class(self, item_class=None):
        item_class = ccs.ITEMCLASS.verify(item_class)
        if item_class:
            self.item_class = item_class
            return 1
        self.item_class = core_item.get_default_item_class()

    def get_item_weight(self):
        return self.item_weight

    def set_item_weight(self,weight=None):
        if core_item.get_min_item_weight() <= weight <= core_item.get_max_item_weight():
            self.item_weight = int(weight*10+.5)/10 # Rounds off to the nearest 0.1 lb
            return 1

        self.item_weight = core_item.get_default_item_weight()

    def get_base_cost(self):
        return self.base_cost

    def set_base_cost(self,cost=None):
        if type(cost) in [float, int]:
            if core_item.get_min_item_cost() <= cost <= core_item.get_max_item_cost():
                self.base_cost = cost
                return 1

        self.base_cost = core_item.get_default_item_cost()

    def is_stackable(self):
        return False if self.stack_size == 1 else True

    def get_stack_size(self):
        return self.stack_size

    def set_stack_size(self,stack_size=None):
        '''
        set_stack_size(int)

        If stack_size is 1, item is not stackable.
        '''
        if core_item.get_min_stack_size() <= stack_size <= core_item.get_max_stack_size():
            self.stack_size = int(stack_size)
            return 1
        
        self.set_stack_size = core_item.get_default_stack_size()

    def is_droppable(self):
        return self.droppable

    def set_droppable(self,droppable=None):
        if droppable is not None:
            droppable = bool(droppable)
            self.droppable = droppable
            return 1
        self.droppable = core_item.get_default_droppable()
       

    def is_stolen(self):
        return self.stolen

    def set_stolen(self,stolen=None):
        if stolen is not None:
            stolen = bool(stolen)
            self.stolen = stolen
            return 1
        self.stolen = core_item.get_default_stolen()


    def is_plot(self):
        return self.plot

    def set_plot(self,plot=None):
        if plot is not None:
            plot = bool(plot)
            self.plot = plot
            return 1

        self.plot = core_item.get_default_plot()

    def get_equippable_slots(self):
        return self.equippable_slots

    def set_equippable_slots(self,equippable_slots=None):
        if not equippable_slots:
            self.equippable_slots = core_item.get_default_equippable_slots()
            return 0
        elif type(equippable_slots) != list:
            equippable_slots = [equippable_slots]
        self.equippable_slots = ccs.EQUIPMENTSLOT.filter_list(equippable_slots)

    def get_description(self):
        return self.description

    def set_description(self, description=None):
        if type(description) == str:
            self.description = description
            return 1
        self.description = core_item.get_default_description()
