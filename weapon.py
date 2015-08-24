

import core.__core_constants_mod as ccs
import core.__core_weapon_configuration as core_weapon
from item import item
from dice import dice

class weapon(item):
    def __init__(self,name=None, item_weight=None, base_cost=None, stack_size=None, droppable=None, stolen=None, plot=None, equippable_slots=None, description=None, base_damage=None, base_damage_type=None, critical_threat_minimum=None, critical_multiplier=None, required_proficiencies=None, weapon_size=None, two_handed=None, stackable=None, throwable=None, natural=None):
        self.natural = False
        self.set_natural_weapon(natural)

        item.__init__(self, name, ccs.ITEMCLASS.WEAPON, item_weight, base_cost, stack_size, droppable, stolen, plot, None, description)

        
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
