'''
  Name: __core_item_configuration.py
Author: Benjamin A
   Purpose: This is a core file for the engine that defines the boundaries of the items.
        Boundaries including item class types, stackability, etc.

'''
import core.__core_constants_mod as ccs

__DEFAULT_ITEM_NAME = "Unidentified Item"
__MAX_ITEM_NAME_LENGTH = 24
__MIN_ITEM_NAME_LENGTH = 3
__DEFAULT_ITEM_COST = 1
__MIN_ITEM_COST = 0
__MAX_ITEM_COST = 120000000
__DEFAULT_DROPPABLE = True
__DEFAULT_ITEM_CLASS = ccs.ITEMCLASS.MISCELLANEOUS
__DEFAULT_ITEM_WEIGHT = 1.0 # Item weight in pounds (lbs) according to DnD ruleset.
__DEFAULT_PLOT = False
__DEFAULT_STACK_SIZE = 1
__DEFAULT_STOLEN = False
__MIN_ITEM_WEIGHT = 0.0
__MAX_ITEM_WEIGHT = 50000
__MIN_STACK_SIZE = 1
__MAX_STACK_SIZE = 50000
__DEFAULT_EQUIPPABLE_SLOTS = [] # When empty, an item can not be equip into any inventory slots.
__DEFAULT_DESCRIPTION = "An object of no particular interest."

def get_default_item_name():
    return __DEFAULT_ITEM_NAME

def get_max_item_name_length():
    return __MAX_ITEM_NAME_LENGTH

def get_min_item_name_length():
    return __MIN_ITEM_NAME_LENGTH

def get_default_item_cost():
    return __DEFAULT_ITEM_COST

def get_min_item_cost():
    return __MIN_ITEM_COST

def get_max_item_cost():
    return __MAX_ITEM_COST

def get_default_droppable():
    return __DEFAULT_DROPPABLE

def get_default_item_weight():
    return __DEFAULT_ITEM_WEIGHT

def get_min_item_weight():
    return __MIN_ITEM_WEIGHT

def get_max_item_weight():
    return __MAX_ITEM_WEIGHT

def get_default_plot():
    return __DEFAULT_PLOT

def get_default_stack_size():
    return __DEFAULT_STACK_SIZE

def get_default_stolen():
    return __DEFAULT_STOLEN

def get_min_stack_size():
    return __MIN_STACK_SIZE

def get_max_stack_size():
    return __MAX_STACK_SIZE

def get_default_item_class():
    return __DEFAULT_ITEM_CLASS

def get_default_equippable_slots():
    return __DEFAULT_EQUIPPABLE_SLOTS

def get_default_description():
    return __DEFAULT_DESCRIPTION
