import core.__core_constants_mod as ccs

__DEFAULT_BASE_DAMAGE = '1d4'
__DEFAULT_BASE_DAMAGE_TYPE = ccs.DAMAGETYPE.SLASHING


'''
This is a weapon with a standard roll-20 for a critical.
If a number such as 19 were to be used, the threat range
would be 19-20
'''
__DEFAULT_CRITICAL_THREAT_MINIMUM = 20 
__MAXIMUM_CRITICAL_THREAT_MINIMUM = 20 
__MINIMUM_CRITICAL_THREAT_MINIMUM = 10

__DEFAULT_CRITICAL_MULTIPLIER = 2
__MINIMUM_CRITICAL_MULTIPLIER = 2
__MAXIMUM_CRITICAL_MULTIPLIER = 8

__DEFAULT_REQUIRED_PROFICIENCIES = [ccs.WEAPONPROFICIENCY.SIMPLE]
__DEFAULT_EQUIPPABLE_SLOT = [ccs.EQUIPMENTSLOT.MAINHAND]
__VALID_WEAPON_SLOTS = [ccs.EQUIPMENTSLOT.MHD, ccs.EQUIPMENTSLOT.OHD, ccs.EQUIPMENTSLOT.ARR, ccs.EQUIPMENTSLOT.BOL]
__VALID_WEAPON_NATURAL_SLOTS = [ccs.EQUIPMENTSLOTNATURAL.CLM, ccs.EQUIPMENTSLOTNATURAL.CLO, ccs.EQUIPMENTSLOTNATURAL.SPE]

__DEFAULT_WEAPON_SIZE_CLASS = ccs.SIZECLASS.MEDIUM
__VALID_WEAPON_SIZE_CLASSES_LIST = [ccs.SIZECLASS.TINY, ccs.SIZECLASS.SMALL, ccs.SIZECLASS.MEDIUM, ccs.SIZECLASS.LARGE]

__DEFAULT_STACKABLE = False
__DEFAULT_TWO_HANDED = False
__DEFAULT_THROWABLE = False
__DEFAULT_NATURAL = False

def get_default_base_damage():
    return __DEFAULT_BASE_DAMAGE

def get_default_base_damage_type():
    return __DEFAULT_BASE_DAMAGE_TYPE

def get_default_critical_threat_minimum():
    return __DEFAULT_CRITICAL_THREAT_MINIMUM

def get_maximum_critical_threat_minimum():
    return __MAXIMUM_CRITICAL_THREAT_MINIMUM

def get_minimum_critical_threat_minimum():
    return __MINIMUM_CRITICAL_THREAT_MINIMUM

def get_default_critical_multiplier():
    return __DEFAULT_CRITICAL_MULTIPLIER

def get_minimum_critical_multiplier():
    return __MINIMUM_CRITICAL_MULTIPLIER

def get_maximum_critical_multiplier():
    return __MAXIMUM_CRITICAL_MULTIPLIER

def get_default_weapon_size_class():
    return __DEFAULT_WEAPON_SIZE_CLASS

def get_valid_weapon_size_class_list():
    return __VALID_WEAPON_SIZE_CLASSES_LIST

def get_default_required_proficiencies():
    return __DEFAULT_REQUIRED_PROFICIENCIES

def get_default_equippable_slot():
    return __DEFAULT_EQUIPPABLE_SLOT

def get_valid_weapon_slot_list():
    return __VALID_WEAPON_SLOTS

def get_valid_weapon_natural_slot_list():
    return __VALID_WEAPON_NATURAL_SLOTS

def get_default_stackable():
    return __DEFAULT_STACKABLE

def get_default_two_handed():
    return __DEFAULT_TWO_HANDED

def get_default_throwable():
    return __DEFAULT_THROWABLE

def get_default_natural_weapon():
    return __DEFAULT_NATURAL
