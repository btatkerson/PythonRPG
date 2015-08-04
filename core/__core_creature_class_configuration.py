'''
  Name: __core_creature_class_configuration.py
Author: Benjamin A
   Purpose: This is a core file for the engine that defines the boundaries of the classes in the game.
    THIS... is going to be mad cray.

'''
import core.__core_constants_mod as ccs


__DEFAULT_ALIGNMENT_RESTRICTIONS = []

__DEFAULT_NUMBER_OF_HIT_DIE = 1
__DEFAULT_HIT_DIE_VALUE = 6
__DEFAULT_HIT_DIE_MODIFIER = 0

__MINIMUM_HIT_DIE_SCORE = 1

__DEFAULT_PROFICIENCIES = []

__DEFAULT_UNAVAILABLE_FEATS = []

__DEFAULT_SPELLCASTING_SCHOOL = ccs.SPELLCASTING_SCHOOL.NONMAGICAL

__DEFAULT_FAVORED_SKILLS = []
__DEFAULT_SKILL_POINTS_EARNED = 1
__MINIMUM_SKILL_POINTS_EARNED = 1
__MAXIMUM_SKILL_POINTS_EARNED = 20

__DEFAULT_BASE_ATTACK_BONUS = ccs.BASEATTACKBONUS.AVERAGE
__DEFAULT_BASE_SAVE_BONUS = ccs.BASESAVEBONUS.POOR


def get_default_alignment_restrictions():
    return __DEFAULT_ALIGNMENT_RESTRICTIONS

def get_default_number_of_hit_die():
    return __DEFAULT_NUMBER_OF_HIT_DIE

def get_default_hit_die_value():
    return __DEFAULT_HIT_DIE_VALUE

def get_default_hit_die_modifier():
    return __DEFAULT_HIT_DIE_MODIFIER

def get_minimum_hit_die_score():
    return __MINIMUM_HIT_DIE_SCORE

def get_default_proficiencies():
    return __DEFAULT_PROFICIENCIES

def get_default_unavailable_feats():
    return __DEFAULT_UNAVAILABLE_FEATS

def get_default_spellcasting_school():
    return __DEFAULT_SPELLCASTING_SCHOOL

def get_default_favored_skills():
    return __DEFAULT_FAVORED_SKILLS

def get_default_skill_points_earned():
    return __DEFAULT_SKILL_POINTS_EARNED

def get_minimum_skill_points_earned():
    return __MINIMUM_SKILL_POINTS_EARNED

def get_maximum_skill_points_earned():
    return __MAXIMUM_SKILL_POINTS_EARNED

def get_default_base_attack_bonus():
    return __DEFAULT_BASE_ATTACK_BONUS

def get_default_base_save_bonus():
    return __DEFAULT_BASE_SAVE_BONUS
