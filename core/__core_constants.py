'''
Name: _core_constants.py

Description:
    This class stores the common-core constants that will be used in-game accross various classes
    For instance, the creature in-game class "BARBARIAN" is used for things like maybe weapon requirements,
    custom dialogs, level progression system, etc. Instead of the name "BARBARIAN" applying only to
    core__creature files (which, the creatures would be "barbarians" in-game), the constants for them
    can be used universally.
'''


class core_constants():

    class _core_const_ability():
        '''
        Used as a class to hold constants for creature abilities
        '''
        def __init__(self):
                self.STR=self.STRENGTH='str'
                self.INT=self.INTELLIGENCE='int'
                self.CON=self.CONSTITUTION='con'
                self.WIS=self.WISDOM='wis'
                self.DEX=self.DEXTERITY='dex'
                self.CHR=self.CHARISMA='chr'

    class _core_const_baseAttackBonus():
        '''
        Used as a class to hold constants for base attack bonuses
        '''
        def __init__(self):
                self.GOOD = 'good' # Returns the constant for 'good' attack bonuses
                self.AVERAGE = self.AVRG = 'average' # Returns the constant for 'average' attack bonuses
                self.POOR = 'poor' # Returns the constant for 'poor' attack bonuses
                self.MONK = 'monk' # Returns the constant for 'monk' attack bonuses

    class _core_const_baseSaveBonus():
        '''
        Used as a class to hold constants for base save bonuses
        '''
        def __init__(self):
                self.GOOD = 'good' # Returns the constant for 'good' save bonuses
                self.POOR = 'poor' # Returns the constant for 'poor' save bonuses

    class _core_const_creatureClass():
        '''
        Used to provide constants for valid creature classes
        '''
        def __init__(self):
                self.UNIQUE = self.UNI = 'uni'
                self.BARBARIAN = self.BBN = 'bbn'
                self.BARD = self.BRD = 'brd'
                self.CLERIC = self.CLR = 'clr'
                self.DRUID = self.DRD = 'drd'
                self.FIGHTER = self.FTR = 'ftr'
                self.MONK = self.MNK = 'mnk'
                self.PALADIN = self.PLD = 'pld'
                self.RANGER = self.RGR = 'rgr'
                self.ROGUE = self.ROG = 'rog'
                self.SORCERER = self.SOR = 'sor'
                self.WIZARD = self.WIZ = 'wiz'
    
    class _core_const_creatureRace():
        '''
        Used for holding the core races of the game
        '''
        def __init__(self):
                self.UNIQUE = 'unique'
                self.ABERRATION = 'aberration'
                self.ANIMAL = 'animal'
                self.BEAST = 'beast'
                self.CONSTRUCT = 'construct'
                self.DRAGON = 'dragon'
                self.DWARF = 'dwarf'
                self.ELEMENTAL = 'elemental'
                self.ELF = 'elf'
                self.FEY = 'fey'
                self.GIANT = 'giant'
                self.GOBLINOID = 'goblinoid'
                self.HALFELF = 'halfelf'
                self.HALFORC = 'halforc'
                self.HALFLING = 'halfling'
                self.HUMAN = 'human'
                self.MAGICAL_BEAST = 'magical_beast'
                self.OOZE = 'ooze'
                self.ORC = 'orc'
                self.OUTSIDER = 'outsider'
                self.REPTILIAN = 'reptilian'
                self.SHAPECHANGER = 'shapechanger'
                self.UNDEAD = 'undead'
                self.VERMIN = 'vermin'

                
    class _core_const_savingThrow():
        '''
        Used as a class to hold constants for saving throws
        '''
        def __init__(self):
                self.FOR=self.FORTITUDE='for' # Returns constant for fortitude saving throw
                self.REF=self.REFLEX='ref' # Returns constant for reflex saving throw
                self.WIL=self.WILL='wil' # Returns constant for will saving throw

    class _core_const_skill():
        '''
        Used as a class to hold possible skills for a creature
        '''
        def __init__(self):
                self.UNI = self.UNIQUE = 'uni'
                self.ANI = self.ANIMAL_EMPATHY = 'ani'
                self.APR = self.APPRAISE = 'apr'
                self.BLF = self.BLUFF = 'blf'
                self.CNC = self.CONCENTRATION = 'cnc'
                self.CAR = self.CRAFT_ARMOR = 'car'
                self.CTR = self.CRAFT_TRAP = 'ctr'
                self.CWE = self.CRAFT_WEAPON = 'cwe'
                self.DTR = self.DISABLE_TRAP = 'dtr'
                self.DIS = self.DISCIPLINE = 'dis'
                self.HEL = self.HEAL = 'hel'
                self.HID = self.HIDE = 'hid'
                self.ITM = self.INTIMIDATE = 'itm'
                self.LIS = self.LISTEN = 'lis'
                self.LOR = self.LORE = 'lor'
                self.MOV = self.MOVE_SILENTLY = 'mov'
                self.OPL = self.OPEN_LOCK = 'opl'
                self.PRY = self.PARRY = 'pry'
                self.PFM = self.PERFORM = 'pfm'
                self.PSD = self.PERSUADE = 'psd'
                self.PIC = self.PICK_POCKET = 'pic'
                self.RID = self.RIDE = 'rid'
                self.SRC = self.SEARCH = 'src'
                self.STR = self.SET_TRAP = 'str'
                self.SPL = self.SPELLCRAFT = 'spl'
                self.SPT = self.SPOT = 'spt'
                self.TNT = self.TAUNT = 'tnt'
                self.TBL = self.TUMBLE = 'tbl'
                self.UMD = self.USE_MAGIC_DEVICE = 'umd'


    def __init__(self):
        self.ABILITY = self._core_const_ability()
        self.BASEATTACKBONUS = self._core_const_baseAttackBonus()
        self.BASESAVEBONUS = self._core_const_baseSaveBonus()
        self.CREATURECLASS = self._core_const_creatureClass()
        self.CREATURERACE = self._core_const_creatureRace()
        self.SAVINGTHROW = self._core_const_savingThrow()
        self.SKILL = self._core_const_skill()
