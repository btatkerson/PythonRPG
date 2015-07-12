'''
      Name: __core_skill_set_configuration.py
    Author: Benjamin A
   Purpose: This is a core file for the engine that defines the boundaries of the skill set in the game.

'''
from core.__core_constants import core_constants as core_constants

class core_skill_set_configuration():
    def __init__(self):
        # List of skills, 0 is 'unique' and unused during initialization

        self.__DEFAULT_TRAINED_SKILL = False
        self.__DEFAULT_ARMOR_PENALTY = False
        self.__DEFAULT_CROSS_CLASS = True
        self.__DEFAULT_KEY_ABILITY = None
        self.__DEFAULT_SKILL_POINTS = 0
        self.__MIN_SKILL_POINTS = 0
        self.__MAX_SKILL_POINTS = 255
        self.__DEFAULT_SKILL_ID = core_constants().SKILL.UNI
        self.__DEFAULT_CLASS_SKILLS = []
        self.__DEFAULT_SYNERGY_SKILLS = []
        self.__DEFAULT_SKILL_SETTINGS_DICT = {
        
            core_constants().SKILL.UNI:{
            'keyID':0, # Unique
            'trained_skill':self.__DEFAULT_TRAINED_SKILL,
            'armor_penalty':self.__DEFAULT_ARMOR_PENALTY,
            'cross_class':self.__DEFAULT_CROSS_CLASS,
            'key_ability':self.__DEFAULT_KEY_ABILITY,
            'skill_points':self.__DEFAULT_SKILL_POINTS,
            'class_skills':self.__DEFAULT_CLASS_SKILLS,
            'synergy_skills':self.__DEFAULT_SYNERGY_SKILLS
            },
            core_constants().SKILL.ANI:{
            'keyID':1, # Animal Empathy
            'trained_skill':True,
            'armor_penalty':False,
            'cross_class':False,
            'key_ability':core_constants().ABILITY.CHR,
            'skill_points':0,
            'class_skills':[core_constants().CREATURECLASS.DRUID, core_constants().CREATURECLASS.RANGER],
            'synergy_skills':[]
            },
            core_constants().SKILL.APR:{
            'keyID':2, # Appraise
            'trained_skill':False,
            'armor_penalty':False,
            'cross_class':True,
            'key_ability':core_constants().ABILITY.INT,
            'skill_points':0,
            'class_skills':[core_constants().CREATURECLASS.BARD, core_constants().CREATURECLASS.ROGUE],
            'synergy_skills':[]
            },
            core_constants().SKILL.BLF:{
            'keyID':3, # Bluff
            'trained_skill':True,
            'armor_penalty':False,
            'cross_class':True,
            'key_ability':core_constants().ABILITY.CHR,
            'skill_points':0,
            'class_skills':[core_constants().CREATURECLASS.BARD, core_constants().CREATURECLASS.ROGUE],
            'synergy_skills':[]
            },
            core_constants().SKILL.CNC:{
            'keyID':4, # Concentration
            'trained_skill':False,
            'armor_penalty':False,
            'cross_class':True,
            'key_ability':core_constants().ABILITY.CON,
            'skill_points':0,
            'class_skills':[core_constants().CREATURECLASS.BARD, core_constants().CREATURECLASS.CLERIC, core_constants().CREATURECLASS.DRUID,
                            core_constants().CREATURECLASS.FIGHTER, core_constants().CREATURECLASS.MONK, core_constants().CREATURECLASS.PALADIN,
                            core_constants().CREATURECLASS.RANGER, core_constants().CREATURECLASS.SORCERER, core_constants().CREATURECLASS.WIZARD], 
            'synergy_skills':[]
            },
            core_constants().SKILL.CAR:{
            'keyID':5, # Craft Armor
            'trained_skill':False,
            'armor_penalty':False,
            'cross_class':True,
            'key_ability':core_constants().ABILITY.INT,
            'skill_points':0,
            'class_skills':core_constants().CREATURECLASS.get_index(), # All Classes, 
            'synergy_skills':[]
            },
            core_constants().SKILL.CTR:{
            'keyID':6, # Craft Trap
            'trained_skill':False,
            'armor_penalty':False,
            'cross_class':True,
            'key_ability':core_constants().ABILITY.INT,
            'skill_points':0,
            'class_skills':core_constants().CREATURECLASS.get_index(), # All Classes, 
            'synergy_skills':[]
            },
            core_constants().SKILL.CWE:{
            'keyID':7, # Craft weapon
            'trained_skill':False,
            'armor_penalty':False,
            'cross_class':True,
            'key_ability':core_constants().ABILITY.INT,
            'skill_points':0,
            'class_skills':core_constants().CREATURECLASS.get_index(), # All Classes, 
            'synergy_skills':[]
            },
            core_constants().SKILL.DTR:{
            'keyID':8, # Disable Trap
            'trained_skill':True,
            'armor_penalty':False,
            'cross_class':True,
            'key_ability':core_constants().ABILITY.INT,
            'skill_points':0,
            'class_skills':[core_constants().CREATURECLASS.ROGUE],
            'synergy_skills':[core_constants().SKILL.SET_TRAP], # Set Trap
            },
            core_constants().SKILL.DIS:{
            'keyID':9, # Discipline
            'trained_skill':False,
            'armor_penalty':False,
            'cross_class':True,
            'key_ability':core_constants().ABILITY.STR,
            'skill_points':0,
            'class_skills':[core_constants().CREATURECLASS.BARBARIAN, core_constants().CREATURECLASS.BARD, core_constants().CREATURECLASS.FIGHTER,
                            core_constants().CREATURECLASS.MONK, core_constants().CREATURECLASS.PALADIN, core_constants().CREATURECLASS.RANGER], 
            'synergy_skills':[]
            },
            core_constants().SKILL.HEL:{
            'keyID':10, # Heal
            'trained_skill':False,
            'armor_penalty':False,
            'cross_class':False,
            'key_ability':core_constants().ABILITY.WIS,
            'skill_points':0,
            'class_skills':core_constants().CREATURECLASS.get_index(), # All Classes
            'synergy_skills':[]
            },
            core_constants().SKILL.HID:{
            'keyID':11, # Hide
            'trained_skill':False,
            'armor_penalty':False,
            'cross_class':True,
            'key_ability':core_constants().ABILITY.DEX,
            'skill_points':0,
            'class_skills':[core_constants().CREATURECLASS.BARD, core_constants().CREATURECLASS.MONK, core_constants().CREATURECLASS.RANGER, 
                            core_constants().CREATURECLASS.ROGUE], 
            'synergy_skills':[]
            },
            core_constants().SKILL.ITM:{
            'keyID':12, # Intimidate
            'trained_skill':False,
            'armor_penalty':False,
            'cross_class':True,
            'key_ability':core_constants().ABILITY.CHR,
            'skill_points':0,
            'class_skills':[core_constants().CREATURECLASS.BARBARIAN, core_constants().CREATURECLASS.ROGUE], 
            'synergy_skills':[]
            },
            core_constants().SKILL.LIS:{
            'keyID':13, # Listen
            'trained_skill':False,
            'armor_penalty':False,
            'cross_class':True,
            'key_ability':core_constants().ABILITY.WIS,
            'skill_points':0,
            'class_skills':[core_constants().CREATURECLASS.BARBARIAN, core_constants().CREATURECLASS.BARD, core_constants().CREATURECLASS.MONK, 
                            core_constants().CREATURECLASS.RANGER, core_constants().CREATURECLASS.ROGUE], 
            'synergy_skills':[]
            },
            core_constants().SKILL.LOR:{
            'keyID':14, # Lore
            'trained_skill':False,
            'armor_penalty':False,
            'cross_class':True,
            'key_ability':core_constants().ABILITY.INT,
            'skill_points':0,
            'class_skills':[core_constants().CREATURECLASS.BARBARIAN, core_constants().CREATURECLASS.BARD, core_constants().CREATURECLASS.CLERIC, 
                            core_constants().CREATURECLASS.DRUID, core_constants().CREATURECLASS.FIGHTER, core_constants().CREATURECLASS.MONK, 
                            core_constants().CREATURECLASS.PALADIN, core_constants().CREATURECLASS.RANGER, core_constants().CREATURECLASS.ROGUE, 
                            core_constants().CREATURECLASS.SORCERER, core_constants().CREATURECLASS.WIZARD], 
            'synergy_skills':[]
            },
            core_constants().SKILL.MOV:{
            'keyID':15, # Move Silently
            'trained_skill':False,
            'armor_penalty':False,
            'cross_class':True,
            'key_ability':core_constants().ABILITY.DEX,
            'skill_points':0,
            'class_skills':[core_constants().CREATURECLASS.BARD, core_constants().CREATURECLASS.MONK, core_constants().CREATURECLASS.RANGER, 
                            core_constants().CREATURECLASS.ROGUE], 
            'synergy_skills':[]
            },
            core_constants().SKILL.OPL:{
            'keyID':16, # Open Lock
            'trained_skill':True,
            'armor_penalty':False,
            'cross_class':True,
            'key_ability':core_constants().ABILITY.DEX,
            'skill_points':0,
            'class_skills':[core_constants().CREATURECLASS.ROGUE], 
            'synergy_skills':[]
            },
            core_constants().SKILL.PRY:{
            'keyID':17, # Parry
            'trained_skill':False,
            'armor_penalty':False,
            'cross_class':True,
            'key_ability':core_constants().ABILITY.DEX,
            'skill_points':0,
            'class_skills':[core_constants().CREATURECLASS.BARBARIAN, core_constants().CREATURECLASS.BARD, core_constants().CREATURECLASS.CLERIC, 
                            core_constants().CREATURECLASS.DRUID, core_constants().CREATURECLASS.FIGHTER, core_constants().CREATURECLASS.MONK, 
                            core_constants().CREATURECLASS.PALADIN, core_constants().CREATURECLASS.RANGER, core_constants().CREATURECLASS.ROGUE, 
                            core_constants().CREATURECLASS.SORCERER, core_constants().CREATURECLASS.WIZARD], 
            'synergy_skills':[]
            },
            core_constants().SKILL.PFM:{
            'keyID':18, # Perform
            'trained_skill':False,
            'armor_penalty':False,
            'cross_class':False,
            'key_ability':core_constants().ABILITY.CHR,
            'skill_points':0,
            'class_skills':[core_constants().CREATURECLASS.BARD],
            'synergy_skills':[]
            },
            core_constants().SKILL.PSD:{
            'keyID':19, # Persuade
            'trained_skill':False,
            'armor_penalty':False,
            'cross_class':True,
            'key_ability':core_constants().ABILITY.CHR,
            'skill_points':0,
            'class_skills':[core_constants().CREATURECLASS.BARD, core_constants().CREATURECLASS.CLERIC, core_constants().CREATURECLASS.DRUID, 
                            core_constants().CREATURECLASS.MONK, core_constants().CREATURECLASS.PALADIN, core_constants().CREATURECLASS.ROGUE], 
            'synergy_skills':[]
            },
            core_constants().SKILL.PIC:{
            'keyID':20, # Pick Pocket
            'trained_skill':True,
            'armor_penalty':True,
            'cross_class':True,
            'key_ability':core_constants().ABILITY.DEX,
            'skill_points':0,
            'class_skills':[core_constants().CREATURECLASS.BARD, core_constants().CREATURECLASS.ROGUE], 
            'synergy_skills':[]
            },
            core_constants().SKILL.RID:{
            'keyID':21, # Ride
            'trained_skill':False,
            'armor_penalty':False,
            'cross_class':True,
            'key_ability':core_constants().ABILITY.CHR,
            'skill_points':0,
            'class_skills':[core_constants().CREATURECLASS.BARBARIAN, core_constants().CREATURECLASS.FIGHTER, core_constants().CREATURECLASS.PALADIN, 
                            core_constants().CREATURECLASS.RANGER], 
            'synergy_skills':[]
            },
            core_constants().SKILL.SRC:{
            'keyID':22, # Search
            'trained_skill':False,
            'armor_penalty':False,
            'cross_class':True,
            'key_ability':core_constants().ABILITY.INT,
            'skill_points':0,
            'class_skills':[core_constants().CREATURECLASS.RANGER, core_constants().CREATURECLASS.ROGUE], 
            'synergy_skills':[]
            },
            core_constants().SKILL.STR:{
            'keyID':23, # Set Trap
            'trained_skill':True,
            'armor_penalty':False,
            'cross_class':True,
            'key_ability':core_constants().ABILITY.DEX,
            'skill_points':0,
            'class_skills':[core_constants().CREATURECLASS.RANGER, core_constants().CREATURECLASS.ROGUE], 
            'synergy_skills':[core_constants().SKILL.DISABLE_TRAP] # Disable Trap
            },
            core_constants().SKILL.SPL:{
            'keyID':24, # Spellcraft
            'trained_skill':True,
            'armor_penalty':False,
            'cross_class':True,
            'key_ability':core_constants().ABILITY.INT,
            'skill_points':0,
            'class_skills':[core_constants().CREATURECLASS.BARD, core_constants().CREATURECLASS.CLERIC, core_constants().CREATURECLASS.SORCERER, 
                            core_constants().CREATURECLASS.WIZARD], 
            'synergy_skills':[]
            },
            core_constants().SKILL.SPT:{
            'keyID':25, # Spot
            'trained_skill':False,
            'armor_penalty':False,
            'cross_class':True,
            'key_ability':core_constants().ABILITY.WIS,
            'skill_points':0,
            'class_skills':[core_constants().CREATURECLASS.RANGER, core_constants().CREATURECLASS.ROGUE], 
            'synergy_skills':[]
            },
            core_constants().SKILL.TNT:{
            'keyID':26, # Taunt
            'trained_skill':False,
            'armor_penalty':False,
            'cross_class':True,
            'key_ability':core_constants().ABILITY.CHR,
            'skill_points':0,
            'class_skills':[core_constants().CREATURECLASS.BARBARIAN, core_constants().CREATURECLASS.BARD, core_constants().CREATURECLASS.PALADIN], 
            'synergy_skills':[]
            },
            core_constants().SKILL.TBL:{
            'keyID':27, # Tumble
            'trained_skill':True,
            'armor_penalty':False,
            'cross_class':False,
            'key_ability':core_constants().ABILITY.DEX,
            'skill_points':0,
            'class_skills':[core_constants().CREATURECLASS.BARD, core_constants().CREATURECLASS.MONK, core_constants().CREATURECLASS.ROGUE], 
            'synergy_skills':[],
            },
            core_constants().SKILL.UMD:{
            'keyID':28, # Use Magic Device
            'trained_skill':True,
            'armor_penalty':False,
            'cross_class':False,
            'key_ability':core_constants().ABILITY.CHR,
            'skill_points':0,
            'class_skills':[core_constants().CREATURECLASS.BARD, core_constants().CREATURECLASS.ROGUE], 
            'synergy_skills':[]
            }
        }



    def get_default_trained_skill(self):
        return self.__DEFAULT_TRAINED_SKILL

    def get_default_armor_penalty(self):
        return self.__DEFAULT_ARMOR_PENALTY

    def get_default_cross_class(self):
        return self.__DEFAULT_CROSS_CLASS

    def get_default_key_ability(self):
        return self.__DEFAULT_KEY_ABILITY

    def get_default_skill_points(self):
        return self.__DEFAULT_SKILL_POINTS

    def get_min_skill_points(self):
        return self.__MIN_SKILL_POINTS

    def get_max_skill_points(self):
        return self.__MAX_SKILL_POINTS

    def get_default_skill_id(self):
        return self.__DEFAULT_SKILL_ID

    def get_default_class_skills(self):
        return self.__DEFAULT_CLASS_SKILLS

    def get_default_synergy_skills(self):
        return self.__DEFAULT_SYNERGY_SKILLS

    def get_default_skill_settings_dict(self):
        return self.__DEFAULT_SKILL_SETTINGS_DICT

        # print core_skill_set_configuration().get_skill_set_list()
