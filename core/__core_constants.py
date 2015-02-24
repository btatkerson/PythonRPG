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
	
	class _core_const_creatureRace():
		'''
		Used for holding the core races of the game
		'''
		def __init__(self):
			self.HUMAN = 'human'
			self.DWARF = 'dwarf'
			self.ELF = 'elf'
			self.HALFELF = 'halfelf'
			self.HALFORC = 'halforc'
			self.HALFLING = 'halfling'

			
	class _core_const_savingThrow():
		'''
		Used as a class to hold constants for saving throws
		'''
		def __init__(self):
			self.FOR=self.FORTITUDE='for' # Returns constant for fortitude saving throw
			self.REF=self.REFLEX='ref' # Returns constant for reflex saving throw
			self.WIL=self.WILL='wil' # Returns constant for will saving throw

	def __init__(self):
		self.ABILITY = self._core_const_ability()
		self.BASEATTACKBONUS = self._core_const_baseAttackBonus()
		self.BASESAVEBONUS = self._core_const_baseSaveBonus()
		self.CREATURECLASS = self._core_const_creatureClass()
		self.CREATURERACE = self._core_const_creatureRace()
		self.SAVINGTHROW = self._core_const_savingThrow()
