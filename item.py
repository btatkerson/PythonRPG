'''
      Name: item.py
    Author: Benjamin A
   Purpose: The item class creates and base class object that defines properties and methods
            shared by all "items" in the game. It can be extended to create custom/specific items
            needed in game.
'''
import blueprints.blueprint as bp
import core.__core_constants_mod as ccs
import core.__core_item_configuration as core_item
import core.__core_weapon_configuration as core_weapon

from dice import dice

class item(bp.blueprint):
    def __init__(self, name=None, item_class=None, item_weight=None, base_cost=None, stack_size=None, droppable=None, stolen=None, plot=None, equippable_slots=None, description=None):
        bp.blueprint.__init__(self, 'it_gen', 0)
        self.item_name = None
        self.set_item_name(name)
        self.set_ref_name(self.get_item_name())

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
        if weight and core_item.get_min_item_weight() <= weight <= core_item.get_max_item_weight():
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
        if stack_size and core_item.get_min_stack_size() <= stack_size <= core_item.get_max_stack_size():
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






class weapon(item):
    def __init__(self,name=None, item_weight=None, base_cost=None, stack_size=None, droppable=None, stolen=None, plot=None, equippable_slots=None, description=None, base_damage=None, base_damage_type=None, critical_threat_minimum=None, critical_multiplier=None, required_proficiencies=None, weapon_size=None, two_handed=None, stackable=None, throwable=None, natural=None):
        self.natural = False
        self.set_natural_weapon(natural)

        item.__init__(self, name, ccs.ITEMCLASS.WEAPON, item_weight, base_cost, stack_size, droppable, stolen, plot, None, description)
        bp.blueprint.__init__(self, 'it_wep', 0)
        self.set_ref_name(self.get_item_name())
        
        self.base_damage = None
        self.set_base_damage(base_damage)

        self.base_damage_type = None
        self.set_base_damage_type(base_damage_type)

        # The minimum d20 roll needed to get a critical
        self.critical_threat_minimum = None 
        self.set_critical_threat_minimum(critical_threat_minimum)

        self.critical_multiplier = None
        self.set_critical_multiplier(critical_multiplier)

        self.required_proficiencies = None
        self.set_required_proficiencies(required_proficiencies)

        self.weapon_size = None
        self.set_weapon_size(weapon_size)

        self.two_handed = False
        self.set_two_handed(two_handed)

        self.stackable = False
        self.set_stackable(stackable)

        self.throwable = False
        self.set_throwable(throwable)

        # Overrides item.set_equippable_slots
        self.set_equippable_slots(equippable_slots)
        


    def set_equippable_slots(self, equippable_slots=None):
        '''
        Set the equippable slots for weapon type items.

        This overrides the item.set_equippable_slots method and uses self.natural to
        determine if the slot is valid
        '''

        if type(equippable_slots) != list:
            equippable_slots = [equippable_slots]

        if self.natural:
            equippable_slots = ccs.EQUIPMENTSLOTNATURAL.filter_list(equippable_slots)
        else:
            equippable_slots = ccs.EQUIPMENTSLOT.filter_list(equippable_slots)

        temp = []

        if len(equippable_slots) > 0:
            for i in equippable_slots:
                if self.natural and i in core_weapon.get_valid_weapon_natural_slot_list():
                    temp.append(i)
                elif i in core_weapon.get_valid_weapon_slot_list():
                    temp.append(i)

        if len(temp) > 0:
            self.equippable_slots = temp
            return 1

        self.equippable_slots = core_weapon.get_default_equippable_slot()
        return 0

    def get_base_damage(self):
        '''
        Returns string for the base damage die. This string can be used with the die
        class either with dice.str_d(str) or dice.set_default_die_by_str(str)
        
        String in format #d# where 3 rolls of a 6-sided die would be
        represented with '3d6'
        '''
        return self.base_damage

    def set_base_damage(self, base_damage=None):
        '''
        Set the base_damage with a string

        string in format #d# where 3 rolls of a 6-sided die would be
        represented with '3d6'
        '''
        temp = dice()
        
        if temp.set_default_die_by_str(base_damage):
            self.base_damage = base_damage
            return 1
        self.base_damage = core_weapon.get_default_base_damage()
        return 0

    def get_base_damage_type(self):
        '''
        Returns core_constant/string for the damage type done by the weapon
        '''
        return self.base_damage_type

    def set_base_damage_type(self, base_damage_type=None):
        '''
        Sets the base_damage_type for a weapon using a core_constant for 
        the damage type
        '''
        base_damage_type = ccs.DAMAGETYPE.verify(base_damage_type)

        if base_damage_type:
            self.base_damage_type = base_damage_type
            return 1

        self.base_damage_type = core_weapon.get_default_base_damage_type()
        return 0

    def get_threat_range(self):
        '''
        Returns a list of integers that would be valid d20 rolls to get critical hits
        '''
        return [i for i in range(self.get_critical_threat_minimum(),core_weapon.get_maximum_critical_threat_minimum()+1)]

    def get_critical_threat_minimum(self):
        '''
        Returns integer for the minimum roll required for a critical hit
        '''
        return self.critical_threat_minimum

    def set_critical_threat_minimum(self, critical_threat_minimum=None):
        if type(critical_threat_minimum) in [int,float]:
            if core_weapon.get_minimum_critical_threat_minimum() <= critical_threat_minimum <= core_weapon.get_maximum_critical_threat_minimum():
                self.critical_threat_minimum = int(critical_threat_minimum)
                return 1

        self.critical_threat_minimum = core_weapon.get_default_critical_threat_minimum()
        return 0

    def get_critical_multiplier(self):
        return self.critical_multiplier

    def set_critical_multiplier(self, critical_multiplier=None):
        if type(critical_multiplier) in [int,float]:
            if core_weapon.get_minimum_critical_multiplier() <= critical_multiplier <= core_weapon.get_maximum_critical_multiplier():
                self.critical_multiplier = int(critical_multiplier)
                return 1

        self.critical_threat_minimum = core_weapon.get_default_critical_multiplier()
        return 0

    def get_required_proficiencies(self):
        return self.required_proficiencies

    def set_required_proficiencies(self, proficiencies=None):
        if type(proficiencies) != list:
            proficiencies = [proficiencies]

        proficiencies = ccs.WEAPONPROFICIENCY.filter_list(proficiencies)

        if len(proficiencies) > 0:
            self.required_proficiencies = proficiencies
            return 1

        self.required_proficiencies = core_weapon.get_default_required_proficiencies()
        return 0

    def get_weapon_size(self):
        return self.weapon_size

    def set_weapon_size(self, weapon_size=None):
        weapon_size = ccs.SIZECLASS.verify(weapon_size)

        if weapon_size in core_weapon.get_valid_weapon_size_class_list():
            self.weapon_size = weapon_size
            return 1

        self.weapon_size = core_weapon.get_default_weapon_size_class()
        return 0

    def is_two_handed(self):
        return self.two_handed

    def set_two_handed(self, two_handed=None):
        if two_handed in [True, 1, False, 0]:
            self.two_handed = two_handed
            return 1

        self.two_handed = core_weapon.get_default_two_handed()
        return 0

    def is_stackable(self):
        return self.stackable 

    def set_stackable(self, stackable=None):
        if stackable in [True, 1, False, 0]:
            self.stackable = stackable
            return 1
        
        self.stackable = core_weapon.get_default_stackable()
        return 0

    def is_throwable(self):
        return self.throwable

    def set_throwable(self, throwable=None):
        if throwable in [True, 1, False, 0]:
            self.throwable = throwable
            return 1

        self.stackable = core_weapon.get_default_stackable()
        return 0

    def is_natural_weapon(self):
        return self.natural

    def set_natural_weapon(self, is_natural=None):
        if is_natural in [True, 1, False, 0]:
            self.natural = is_natural
            return 1

        self.natural = core_weapon.get_default_natural_weapon()
        return 0
