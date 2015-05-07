'''
Name: _core_constants.py

Description:
    This class stores the common-core constants that will be used in-game accross various classes
    For instance, the creature in-game class "BARBARIAN" is used for things like maybe weapon requirements,
    custom dialogs, level progression system, etc. Instead of the name "BARBARIAN" applying only to
    core__creature files (which, the creatures would be "barbarians" in-game), the constants for them
    can be used universally.
'''

class index_reader:
    '''
    Used for reading common data in the constant classes
    ''' 

    def __init__(self):
        None

    def is_real(self,val=None):
        if not val:
            return False,False
        else:
            if type(val) == int:
                return True, dict(zip(range(1,len(self.INDEX)+1),self.INDEX))[val]
            else:
                if val in self.INDEX:
                    return True, val
            return False,False
    
    def verify(self,val=None):
        real,value = self.is_real(val)
        if real:
            return value
        else:
            return False
    
    def get_long_name(self,val=None):
        constant = self.verify(val)
        return dict(zip(self.INDEX,self.INDEX_LONG))[constant]



class core_constants():

    class _core_const_ability(index_reader):
        '''
        Used as a class to hold constants for creature abilities
        '''
        def __init__(self):
                index_reader.__init__(self)
                self.STR=self.STRENGTH='str'
                self.INT=self.INTELLIGENCE='int'
                self.CON=self.CONSTITUTION='con'
                self.WIS=self.WISDOM='wis'
                self.DEX=self.DEXTERITY='dex'
                self.CHR=self.CHARISMA='chr'

                self.INDEX=[self.STR,self.INT,self.CON,self.WIS,self.DEX,self.CHR]
                self.INDEX_LONG=['strength','intelligence','constitution','wisdom','dexterity','charisma']

    class _core_const_baseAttackBonus(index_reader):
        '''
        Used as a class to hold constants for base attack bonuses
        '''
        def __init__(self):
                index_reader.__init__(self)
                self.GOOD = 'good' # Returns the constant for 'good' attack bonuses
                self.AVERAGE = self.AVRG = 'avrg' # Returns the constant for 'average' attack bonuses
                self.POOR = 'poor' # Returns the constant for 'poor' attack bonuses
                self.MONK = 'monk' # Returns the constant for 'monk' attack bonuses

                self.INDEX = [self.POOR,self.AVERAGE,self.GOOD,self.MONK]
                self.INDEX_LONG=['poor','average','good','monk']

    class _core_const_baseSaveBonus(index_reader):
        '''
        Used as a class to hold constants for base save bonuses
        '''
        def __init__(self):
                index_reader.__init__(self)
                self.GOOD = 'good' # Returns the constant for 'good' save bonuses
                self.POOR = 'poor' # Returns the constant for 'poor' save bonuses

                self.INDEX = [self.POOR,self.GOOD]
                self.INDEX_LONG = ['poor','good']

    class _core_const_creatureClass(index_reader):
        '''
        Used to provide constants for valid creature classes
        '''
        def __init__(self):
                index_reader.__init__(self)
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

                self.INDEX = [self.UNI,self.BBN,self.BRD,self.CLR,self.DRD,self.FTR,self.MNK,self.PLD,self.RGR,self.ROG,self.SOR,self.WIZ]
                self.INDEX_LONG = ["unique","barbarian","bard","cleric","druid","fighter","monk","paladin","ranger","rogue","sorcerer","wizard"]
    
    class _core_const_creatureRace(index_reader):
        '''
        Used for holding the core races of the game
        '''
        def __init__(self):
                index_reader.__init__(self)
                self.UNI = self.UNIQUE = 'unique'
                self.ABR = self.ABERRATION = 'aberration'
                self.ANI = self.ANIMAL = 'animal'
                self.BST = self.BEAST = 'beast'
                self.CON = self.CONSTRUCT = 'construct'
                self.DRG = self.DRAGON = 'dragon'
                self.DWF = self.DWARF = 'dwarf'
                self.ELM = self.ELEMENTAL = 'elemental'
                self.ELF = 'elf'
                self.FEY = 'fey'
                self.GNT = self.GIANT = 'giant'
                self.GOB = self.GOBLINOID = 'goblinoid'
                self.HFE = self.HALFELF = 'halfelf'
                self.HFO = self.HALFORC = 'halforc'
                self.HFL = self.HALFLING = 'halfling'
                self.HUM = self.HUMAN = 'human'
                self.MAG = self.MAGICAL_BEAST = 'magical_beast'
                self.OOZ = self.OOZE = 'ooze'
                self.ORC = 'orc'
                self.OUT = self.OUTSIDER = 'outsider'
                self.REP = self.REPTILIAN = 'reptilian'
                self.SHP = self.SHAPECHANGER = 'shapechanger'
                self.UND = self.UNDEAD = 'undead'
                self.VRM = self.VERMIN = 'vermin'

                self.INDEX = [self.UNI,self.ABR,self.ANI,self.BST,self.CON,
                              self.DRG,self.DWF,self.ELM,self.ELF,self.FEY,
                              self.GNT,self.GOB,self.HFE,self.HFO,self.HFL,
                              self.HUM,self.MAG,self.OOZ,self.ORC,self.OUT,
                              self.REP,self.SHP,self.UND,self.VRM]

                self.INDEX_LONG = ['unique','aberration','animal','beast','construct',
                                   'dragon','dwarf','elemental','elf','fey',
                                   'giant','goblin','half-elf','half-orc','half-ling',
                                   'human','magical beast','ooze','orc','outsider',
                                   'reptilian','shapechanger','undead','vermin']
                
    class _core_const_savingThrow(index_reader):
        '''
        Used as a class to hold constants for saving throws
        '''
        def __init__(self):
                index_reader.__init__(self)
                self.FOR=self.FORTITUDE='for' # Returns constant for fortitude saving throw
                self.REF=self.REFLEX='ref' # Returns constant for reflex saving throw
                self.WIL=self.WILL='wil' # Returns constant for will saving throw

                self.INDEX = [self.FOR,self.REF,self.WIL]
                self.INDEX_LONG = ['fortitude','reflex','will']

    class _core_const_equipment_slots(index_reader):
        '''
        Used as a class to hold constants for the possible equipment slots on the creature class
        '''
        def __init__(self):
            index_reader.__init__(self)
            self.MHD = self.MAINHAND = 'mhd'
            self.OHD = self.OFFHAND = 'ohd'
            self.ARM = self.ARMOR = 'arm'
            self.HLM = self.HELMET = 'hlm'
            self.GLV = self.GLOVES = 'glv'
            self.CLK = self.CLOAK = 'clk'
            self.BTS = self.BOOTS = 'bts'
            self.BLT = self.BELT = 'blt' # Mmm, bacon
            self.AMU = self.AMULET = 'amu'
            self.RG1 = self.RING1 = 'rg1'
            self.RG2 = self.RING2 = 'rg2'
            self.ARR = self.ARROWS = 'arr'
            self.BOL = self.BOLTS = 'bol'
            self.BUL = self.BULLETS = 'bul'

            self.INDEX = [self.MHD,self.OHD,self.ARM,self.HLM,
                          self.GLV,self.CLK,self.BTS,self.BLT,
                          self.AMU,self.RG1,self.RG2,self.ARR,
                          self.BOL,self.BUL]

            self.INDEX_LONG = ['mainhand','offhand','armor','helmet',
                               'gloves','cloak','boots','belt',
                               'amulet','first ring','second ring','arrows',
                               'bolts','bullets']

    class _core_const_skill(index_reader):
        '''
        Used as a class to hold possible skills for a creature
        '''
        def __init__(self):
                index_reader.__init__(self)
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

                self.INDEX = [self.UNI,self.ANI,self.APR,self.BLF,self.CNC,
                              self.CAR,self.CTR,self.CWE,self.DTR,self.DIS,
                              self.HEL,self.HID,self.ITM,self.LIS,self.LOR,
                              self.MOV,self.OPL,self.PRY,self.PFM,self.PSD,
                              self.PIC,self.RID,self.SRC,self.STR,self.SPL,
                              self.SPT,self.TNT,self.TBL,self.UMD]

                self.INDEX_LONG = ['unique', 'animal empathy', 'appraise', 'bluff', 'concentration',
                                   'craft armor', 'craft trap', 'craft weapon', 'disable trap','discipline',
                                   'heal', 'hide', 'intimidate', 'listen', 'lore',
                                   'move silently', 'open lock', 'parry', 'perform', 'persuade',
                                   'pick pocket', 'ride', 'search', 'set trap', 'spellcraft',
                                   'spot', 'taunt', 'tumble', 'use magic device']


    def __init__(self):
        self.ABILITY = self._core_const_ability()
        self.BASEATTACKBONUS = self._core_const_baseAttackBonus()
        self.BASESAVEBONUS = self._core_const_baseSaveBonus()
        self.CREATURECLASS = self._core_const_creatureClass()
        self.CREATURERACE = self._core_const_creatureRace()
        self.EQUIPMENTSLOT = self._core_const_equipment_slots()
        self.SAVINGTHROW = self._core_const_savingThrow()
        self.SKILL = self._core_const_skill()
