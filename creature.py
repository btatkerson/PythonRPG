'''
     Name: creature.py
    Author: Benjamin A
 Purpose: The creature class creates an object with relevant methods to in-game creatures, npcs, pcs, etc
 This class can be used to create subclasses that inherit all the common traits of creatures, 
 but extended to define specific and even custom creatures.
 
'''

from core.__core_creature_configuration import core_creature_configuration
# from core.__core_creature_class_configuration import core_creature_class_configuration
import core.__core_constants_mod as ccs
from core.verbose import verbose
from skill_set import skill_set
from dice import dice
from percbar import percbar
from item import item, weapon


class creature(verbose, dice): 
    # A short method in most classes that calls the core settings for that particular class.
    def _core(self): 
        return core_creature_configuration()

    def __init__(self, playable_character=None, name=None, creature_class=None, race=None, size_class=None, challenge_rating=None, deity=None, law_vs_chaos=None, good_vs_evil=None, base_hit_points=None, base_level=None, base_attack_bonus=None, exp=None, base_armor_class=None, base_level_rate=None, str=None, inte=None, chr=None, dex=None, con=None, wis=None, verbo=False): 

        # Initialize inherited classes
        verbose.__init__(self,verbo)
        dice.__init__(self)


        self.playable_character=playable_character or self._core().get_default_playable_character()


        self.name=name or self._core().get_default_name()

        self.race=None
        self.__racial_ability_bonuses = None # this is set from the core after the race is determined
        self.set_race(race)

        self.size_class = None
        self.set_size_class(size_class)



        self.deity=deity or self._core().get_default_deity()


        self.alignment_law_vs_chaos = None
        self.alignment_good_vs_evil = None

        self.alignment_law_vs_chaos=law_vs_chaos or self._core().get_default_alignment_law_vs_chaos()# Scale 0 - 100. 0-32= Chaotic, 33-67= Neutral, 68-100= Law
        self.alignment_good_vs_evil=good_vs_evil or self._core().get_default_alignment_good_vs_evil()# Scale 0 - 100. 0-32= Evil, 33-67= Neutral, 68-100= Good

        self.base_hit_points=base_hit_points or self._core().get_default_base_hit_points()
        self.current_hit_points=self.base_hit_points
        self.challenge_rating = challenge_rating or self._core().get_default_challenge_rating()
        
        # 1000 is the standard growth, the lower the number, the faster a character will level up
        # 1000*base_level is the default experience needed to advance to the next level
        self.base_level_rate=base_level_rate or self._core().get_default_base_level_rate() 

        self.hit_die = None
        self.base_level=None
        self.experience=None

        if base_level:
            self.set_experience_by_base_level(base_level)
        elif exp:
            self.set_base_level_by_experience(exp)
        else:
            self.set_experience_by_base_level(1)
        

        self.__last_experience_earned = 0 # Used for logging
        self.skill_set=skill_set()

        self.base_attack_bonus = None
        self.set_base_attack_bonus_type(base_attack_bonus)
        self.base_saving_throw_bonus={i: 0 for i in ccs.SAVINGTHROW.get_index()}
        


        # Dictionary of base_abilities
        self.base_abilities={ccs.ABILITY.STR:str or self._core().get_default_base_ability_score(),
                             ccs.ABILITY.INT:inte or self._core().get_default_base_ability_score(),
                             ccs.ABILITY.CON:con or self._core().get_default_base_ability_score(),
                             ccs.ABILITY.WIS:wis or self._core().get_default_base_ability_score(),
                             ccs.ABILITY.DEX:dex or self._core().get_default_base_ability_score(),
                             ccs.ABILITY.CHR:chr or self._core().get_default_base_ability_score()}

        self.base_armor_class = None
        self.set_base_armor_class(base_armor_class)

        self.inventory=[] # Holds list of items, an inventory system is in the future.

        self.creature_class = None
        self.set_creature_class(creature_class)

        self.primary_equipment_slot_type = None
        self.equipment_standard_slots = None
        self.equipment_natural_slots = None
        self.generate_initial_equipment_slots()
        

    def get_base_level(self): 
        '''
        Returns the base_level of the creature
        '''
        return self.base_level

    def get_experience(self):
        '''
        Returns the total creature experience points
        '''
        return self.experience
    
    def get_last_experience_earned(self):
        '''
        Returns the last amount of XP rewarded to the creature class
        '''
        return self.__last_experience_earned

    def get_experience_needed_to_level(self):
        '''
        Returns the experience needed in order to level up
        '''
        temp = sum([i * self.base_level_rate for i in range(1, self.base_level+1)]) - self.experience
        if temp > 0:
            return temp
        return 0


    def set_creature_class(self, creature_class=None):
        '''
        Sets the creature class based on verified input for creature_class

        Otherwise, a default class will be given
        '''

        creature_class = ccs.CREATURECLASS.verify(creature_class)

        if creature_class:
            self.creature_class = creature_class
            self.set_base_attack_bonus_type(set_by_class=True)
            self.set_base_saving_throw_bonus_types(set_by_class=True)
            self.set_hit_die(set_by_class=True)
            return 1

        self.set_creature_class(self._core().get_default_creature_class())


    
    def get_hit_die(self):
        '''
        Returns the hit_die function

        YOU ARE PROBABLY LOOKING FOR GET_HIT_DIE_ROLL()
        '''
        return self.hit_die

    def get_hit_die_roll(self):
        '''
        Returns a list of die rolls using self.hit_die dice object
        '''
        return self.hit_die()

    def set_hit_die(self, hit_die=None, set_by_class=False):
        '''
        Sets the self.hit_die to a dice() class

        If set_by_class is True, the hit die will pull from the builtin hit die related to
        the creature class set on self.creature_class

        RECOMMENDED:
        Just run self.set_creature_class() at initialization and don't worry about it (:
        '''
        if set_by_class:
            self.hit_die = self._core().get_class_hit_die(self.creature_class)
            return 1 

        if type(hit_die) == str:
            self.hit_die = dice(die_str=hit_die)
            if self.hit_die():
                return 1

        elif isinstance(hit_die, dice):
            self.hit_die = hit_die
            return 1

        self.hit_die = self.set_hit_die(self._core().get_default_hit_die())
        

    def get_experience_toward_next_level(self):
        '''
        Returns the current experience earned toward the next level
        
        This is used for tracking progress.
        '''
        return self.experience - sum([i*self.base_level_rate for i in range(1,self.base_level)])

    def get_experience_total_for_current_level(self):
        '''
        Returns the total experience needed to level up for that particular level

        Level 3 = 3000 (lvl 3 * 1000 (base level rate))
        '''
        return self.base_level_rate*self.base_level

    def get_base_attack_bonus_type(self):
        '''
        Returns the type of base_attack_bonus a creature has
        '''
        return self.base_attack_bonus

    def get_base_attack_bonus(self): 
        '''
        Returns a list of integers for the attack bonuses based on level and attack bonus type
        '''
        return self._core().get_base_attack_bonus(self.base_attack_bonus, self.base_level) 

    def set_base_attack_bonus_type(self, base_attack_bonus=None, set_by_class=False, creature_class=None):
        '''
        set_base_attack_bonus_type(ccs.BASEATTACKBONUS)
        set_base_attack_bonus_type(set_by_class=bool)
        set_base_attack_bonus_type(creature_class=ccs.CREATURECLASS)

        Sets the base attack bonus for creature combat.

        GOOD, AVERAGE, and POOR are acceptable inputs for 'base_attack_bonus'

        if set_by_class is True, the base_attack_bonus_type is set to the builtin type for the class 
        that NEEDS TO BE set on the creature prior to using this parameter

        if creature_class is a valid ccs.CREATURECLASS, the base_attack_bonus_type will be set to
        the builtin attack bonus for that given class
        '''

        if set_by_class or creature_class:
            if creature_class:
                creature_class = ccs.CREATURECLASS.verify(creature_class)
                if creature_class:
                    self.base_attack_bonus = self._core().get_class_base_attack_bonus(creature_class)
                    return 1
            elif self.creature_class:
                self.base_attack_bonus = self._core().get_class_base_attack_bonus(self.creature_class)
                return 1
 
        base_attack_bonus = ccs.BASEATTACKBONUS.verify(base_attack_bonus)

        if base_attack_bonus:
            self.base_attack_bonus = base_attack_bonus
            return 1

        self.base_attack_bonus = self._core().get_default_base_attack_bonus()

    def get_base_saving_throw_bonus(self, saving_throw=None):
        '''
        Returns an integer for the base saving throw based on the type of saving throw and the creature level
        '''
        saving_throw = ccs.SAVINGTHROW.verify(saving_throw)

        if saving_throw:
            return self._core().get_base_save_bonus(self.base_saving_throw_bonus[saving_throw], self.base_level)
        return self._core().get_base_save_bonus(self.base_saving_throw_bonus[self._core().get_default_saving_throw()], self.base_level) 

    def get_saving_throw(self, saving_throw=None):
        '''
        Returns an integer for the complete saving throw bonus accounting for the 
        base save bonus and the modifiers on the creature provided a correct saving throw
        '''

        saving_throw = ccs.SAVINGTHROW.verify(saving_throw)
        if saving_throw:
            base_save = self.get_base_saving_throw_bonus(saving_throw)
            if saving_throw == ccs.SAVINGTHROW.REF:
                return base_save + self.get_mod_dex()
            elif saving_throw == ccs.SAVINGTHROW.WIL:
                return base_save + self.get_mod_wis()
            else:
                return base_save + self.get_mod_con()
        return self.get_base_saving_throw_bonus()


    def get_saving_throw_reflex(self):
        '''
        Returns an integer of the reflex saving throw bonus with modifiers accounted for
        '''
        return self.get_saving_throw(ccs.SAVINGTHROW.REF)
    
    def get_saving_throw_will(self):
        '''
        Returns an integer of the will saving throw bonus with modifiers accounted for
        '''
        return self.get_saving_throw(ccs.SAVINGTHROW.WIL)

    def get_saving_throw_fortitude(self):
        '''
        Returns an integer of the fortitude saving throw bonus with modifiers accounted for
        '''
        return self.get_saving_throw(ccs.SAVINGTHROW.FOR)
     
    get_saving_throw_ref = get_saving_throw_reflex
    get_saving_throw_wil = get_saving_throw_will
    get_saving_throw_for = get_saving_throw_fortitude

    def get_base_saving_throw_bonus_types(self, saving_throw=None):
        '''
        Returns a dictionary of core constants for the saving throw bonus type used for each type of saving throw
        base_saving_throw returns only the bonus type core constant for the saving throw given
        '''
        saving_throw = ccs.SAVINGTHROW.verify(saving_throw)
        if saving_throw:
            return self.base_saving_throw_bonus[saving_throw]
        return self.base_saving_throw_bonus

    def set_base_saving_throw_bonus_types(self, refl=None, will=None, fort=None, set_by_class=False, creature_class=None):
        '''
        set_base_saving_throw_bonus_types(int, int, int)
        set_base_saving_throw_bonus_types(set_by_class=bool)
        set_base_saving_throw_bonus_types(creature_class=ccs.CREATURECLASS)

        Sets the saving throw bonuses to self.base_saving_throw_bonus dictionary.

        'refl', 'will', and 'fort' can be used all together or called specifically if not setting all at once.

        'refl', 'will', and 'fort' parameters are not used when valid parameters for 'set_by_class' or 'creature_class'
        are given. 

        If 'creature_class' is provided, the bonuses are taken from the builtin bonuses for that class
        
        If 'set_by_class' is set to True, the bonuses are set by the creature class that has been previously
        set on that creature. self.creature_class must already be set for this to work.
        '''

        if set_by_class or creature_class:
            if creature_class:
                creature_class = ccs.CREATURECLASS.verify(creature_class)
                if creature_class:
                    self.base_saving_throw_bonus = self._core().get_class_base_save_bonuses(creature_class)
                    return 1
            elif self.creature_class:
                self.base_saving_throw_bonus = self._core().get_class_base_save_bonuses(self.creature_class)
                return 1
            
        refl = ccs.BASESAVEBONUS.verify(refl)
        will = ccs.BASESAVEBONUS.verify(will)
        fort = ccs.BASESAVEBONUS.verify(fort)

        if refl:
            self.base_saving_throw_bonus[ccs.SAVINGTHROW.REF] = refl
        if will:
            self.base_saving_throw_bonus[ccs.SAVINGTHROW.WIL] = will
        if fort:
            self.base_saving_throw_bonus[ccs.SAVINGTHROW.FOR] = fort

        for i in self.base_saving_throw_bonus:
            if not self.base_saving_throw_bonus[i]:
                self.base_saving_throw_bonus[i] = self._core().get_default_base_save_bonus()

    def get_base_hit_points(self):
        '''
        Returns the base hit points of a creature. The base hit points are the total hit points set for the creature.
        This number only changes with creature level.
        '''
        return self.base_hit_points

    def set_base_hit_points(self,add=None,absolute=None):
        '''
        set_base_hit_points(int)
        set_base_hit_points(int,bool)

        sets the base hit points for a creature by adding 'add' to the base hit points.
        'add' should be a positive OR negative integer 

        'absolute' == True will set the base hit points to the value given for 'add'

        '''

        
        if not add:
            return False
        elif not absolute:
            self.base_hit_points += add
        else:
            self.base_hit_points = min(max(self.base_hit_points,
                                           self._core().get_min_base_hit_points()),
                                           self._core().get_max_base_hit_points())
        
    def get_current_hit_points(self):
        '''
        Returns the hit points a creature has at any given point in time.
        This would be used to determine whether or not a creature is alive.
        '''
        return self.current_hit_points

    def set_current_hit_points(self,add=None,absolute=None):
        if not add:
            return False
        elif not absolute:
            self.current_hit_points = max(min(self.current_hit_points + add, self.base_hit_points),self._core().get_min_current_hit_points())
        else:
            self.current_hit_points = min(max(self.current_hit_points,self._core().get_min_current_hit_points()),self.get_base_hit_points())

    def get_challenge_rating(self):
        '''
        Returns a float for the challenge rating of a creature
        '''
        return self.challenge_rating

    def set_challenge_rating(self,val=None):
        '''
        Sets the creature challenge rating to a numerical value
        '''
        if not val:
            return 

        if type(val) in [int,float]:
            if self._core().get_min_challenge_rating() <= val < 1:
                self.challenge_rating = val
            else:
                self.challenge_rating = min(max(val,self._core().get_min_challenge_rating()),self._core().get_max_challenge_rating())

        else:
            self.challenge_rating = self._core().get_default_challenge_rating()

    def is_alive(self):
        '''
        Returns True if creature has current hit points greater than 0
        '''
        if self.get_current_hit_points() > 0:
            return True
        else:
            return False

    def is_dead(self):
        '''
        Returns True is a character has 0 or less current hit points
        '''
        return not self.is_alive()

    def get_base_armor_class(self):
        '''
        Returns the base AC for the creature. (The AC with no modifiers or armor bonuses)
        '''
        return self.base_armor_class

    def set_base_armor_class(self,val=None):
        if not val:
            self.base_armor_class = self._core().get_default_base_armor_class()
        else:
            if self._core().get_min_base_armor_class() <= val <= self._core().get_max_base_armor_class():
                self.base_armor_class = val
            else:
                self.base_armor_class = self._core().get_default_base_armor_class()               

    def get_armor_class(self):
        '''
        Returns the armor class with modifiers
        '''
        return self.base_armor_class + self.get_ability_modifier(ccs.ABILITY.DEX) + self.get_size_class().get_size_modifier()

    def get_AC(self):
        return self.get_armor_class()

    def get_attack_roll(self,verbo=False):
        '''
        attack_roll() returns a lists of lists. The sum of the elements in each list will return
        the total for the attack roll
        
        The lists currently contain two numbers [d20, AB, SCM, SMD,] where

        d20 = the number on the dice roll (d20)
            - This is used for determining criticals (hits/misses)
            
         AB = attack bonus
            - Pulled from the base_attack_bonus determined by the creature's class
        
        SCM = size class modifier
            - Determined by creature race, or whatever size was assigned

        SMD = strength modifier
            - Modifier from creature strength score
        '''
        roll_list=[]
        for i in self.get_base_attack_bonus():
            temp = sum(self.d20())
            if 1 < temp <= 20:
                roll_list.append([temp, i, self.get_size_class().get_size_modifier(), self.get_mod_str()])
            else:
                roll_list.append([0,0])
        return roll_list

            
    def get_damage_roll(self,*args, verbo= False): 
        '''
        damage_roll() returns a dice roll that will soon be based on the weapon the creature is carrying
        '''
        types = [type(i) for i in args]

        if self.get_primary_equipment_slot_type() == ccs.EQUIPMENTSLOTTYPE.STANDARD:
            if self.get_equipment_slot_item(ccs.EQUIPMENTSLOT.MHD):
                weapon_info = self.get_equipment_slot_item(ccs.EQUIPMENTSLOT.MHD)
            elif self.get_equipment_slot_item(ccs.EQUIPMENTSLOTNATURAL.CLAWMAINHAND):
                weapon_info = self.get_equipment_slot_item(ccs.EQUIPMENTSLOTNATURAL.CLM)
            else:
                weapon_info = weapon("Unarmed Bludgeon Generic", 0, 0, 0, 0, 0 ,0 , [ccs.EQUIPMENTSLOTNATURAL.CLM, ccs.EQUIPMENTSLOTNATURAL.CLO], "Generic, unarmed bludgeon attack", '1d3', ccs.DAMAGETYPE.BLU, 20, 2, ccs.WEAPONPROFICIENCY.CRE,0,0,0,0,1)

        else:
            if self.get_equipment_slot_item(ccs.EQUIPMENTSLOTNATURAL.CLM):
                weapon_info = self.get_equipment_slot_item(ccs.EQUIPMENTSLOTNATURAL.CLM)
            else:
                weapon_info = weapon("Unarmed Bludgeon Generic", 0, 0, 0, 0, 0 ,0 , [ccs.EQUIPMENTSLOTNATURAL.CLM, ccs.EQUIPMENTSLOTNATURAL.CLO], "Generic, unarmed bludgeon attack", '1d3', ccs.DAMAGETYPE.BLU, 20, 2, ccs.WEAPONPROFICIENCY.CRE,0,0,0,0,1)


        if types == [bool]:
            critical = args[0][0]

        elif types == [list]:
            if args[0][0] in weapon_info.get_threat_range():
                critical = True
            elif args[0][0] == 0:
                return [0]
            else:
                critical = False

        else:
            critical = False



        if critical: 
            print("Critical!")
            roll=sum(self.str_d(weapon_info.get_base_damage()))*weapon_info.get_critical_multiplier()
            # damage = max(roll + self.get_mod_str(),1)
            damage = [roll, self.get_mod_str()]
        else:
            roll = sum(self.str_d(weapon_info.get_base_damage()))
            # damage = max(roll + self.get_mod_str(),0)
            damage = [roll, self.get_mod_str()]

        return damage

    def get_skill_set(self): 
        return self.skill_set

    def get_skill(self, skill=None): 
        return self.skill_set.get_skill(skill)

    def set_all_base_ability_score(self, str=0, inte=0, con=0, wis=0, dex=0, chr=0, absolute=False): 
        '''
        Sets all the base abilities at once, or whichever are provided.
        absolute== False : Base ability has parameter added to it (str=1==> self.base_abilities[ccs.ABILITY.STR] += 1)
        absolute== True : Base ability is set to parameter (str=1==> self.base_abilities[ccs.ABILITY.STR]=1)
        '''

        if str: 
            self.set_base_str(str, absolute)
        if inte: 
            self.set_base_int(inte, absolute)
        if con: 
            self.set_base_con(con, absolute)
        if wis: 
            self.set_base_wis(wis, absolute)
        if dex: 
            self.set_base_dex(dex, absolute)
        if chr: 
            self.set_base_chr(chr, absolute)

        return self.base_abilities
    
    def set_base_ability_score(self, ability=None, add=0, absolute=False): 
        '''
        Allows one base ability to be modified at a time
        '''
        ability = ccs.ABILITY.verify(ability)
        if ability:
            if absolute: 
                self.base_abilities[ability]=add
            else: 
                self.base_abilities[ability] += add
        else: 
            return self._core().get_default_base_ability_score()

        # Makes sure the base ability is valid and keeps the value within range
        if self.base_abilities[ability] > self._core().get_max_base_ability_score(): 
            self.base_abilities[ability]= self._core().get_max_base_ability_score()
        elif self.base_abilities[ability] < self._core().get_min_base_ability_score(): 
            self.base_abilities[ability]= self._core().get_min_base_ability_score()

        return self.base_abilities[ability]

    def get_base_ability_score(self, ability=None): 
        ''' Returns base ability value for any valid ability provided '''
        ability = ccs.ABILITY.verify(ability)

        if ability:
            return self.base_abilities[ability]
        return self._core().get_default_base_ability_score()

    def get_ability_score(self, ability=None):
        '''
        Returns the ability scores that are modified for things such as race
        '''
        ability = ccs.ABILITY.verify(ability)

        if ability:
            return self.get_base_ability_score(ability) + self.get_racial_ability_bonus(ability)
        return self._core().get_default_base_ability_score()

        return self.get_base_ability_score(ccs.ABILITY.STR)

    def get_base_str(self): 
        '''
        Returns the base ability score for the Strength ability
        '''
        return self.get_base_ability_score(ccs.ABILITY.STR)


    def set_base_str(self, add, absolute=False): 
        '''
        Sets the base ability score for the Strength ability
        Variable 'add' will add any value placed in the parameter to the base ability. If variable 'absolute' is set to True, 
        the base ability will be set to the value provided for variable 'add'
        '''
        return self.set_base_ability_score(ccs.ABILITY.STR, add, absolute)

    def get_base_int(self): 
        '''
        Returns the base ability score for the Intelligence ability
        '''
        return self.get_base_ability_score(ccs.ABILITY.INT)

    def set_base_int(self, add, absolute=False): 
        '''
        Sets the base ability score for the Intelligence ability
        Variable 'add' will add any value placed in the parameter to the base ability. If variable 'absolute' is set to True, 
        the base ability will be set to the value provided for variable 'add'
        '''
        return self.set_base_ability_score(ccs.ABILITY.INT, add, absolute)

    def get_base_con(self): 
        '''
        Returns the base ability score for the Constitution ability
        '''
        return self.get_base_ability_score(ccs.ABILITY.CON)

    def set_base_con(self, add, absolute=False): 
        '''
        Sets the base ability score for the Constitution ability
        Variable 'add' will add any value placed in the parameter to the base ability. If variable 'absolute' is set to True, 
        the base ability will be set to the value provided for variable 'add'
        '''
        return self.set_base_ability_score(ccs.ABILITY.CON, add, absolute)

    def get_base_wis(self): 
        '''
        Returns the base ability score for the Wisdom ability
        '''
        return self.get_base_ability_score(ccs.ABILITY.WIS)

    def set_base_wis(self, add, absolute=False): 
        '''
        Sets the base ability score for the Wisdom ability
        Variable 'add' will add any value placed in the parameter to the base ability. If variable 'absolute' is set to True, 
        the base ability will be set to the value provided for variable 'add'
        '''
        return self.set_base_ability_score(ccs.ABILITY.WIS, add, absolute)

    def get_base_dex(self): 
        '''
        Returns the base ability score for the Dexterity ability
        '''
        return self.get_base_ability_score(ccs.ABILITY.DEX)

    def set_base_dex(self, add, absolute=False): 
        '''
        Sets the base ability score for the Dexterity ability
        Variable 'add' will add any value placed in the parameter to the base ability. If variable 'absolute' is set to True, 
        the base ability will be set to the value provided for variable 'add'
        '''
        return self.set_base_ability_score(ccs.ABILITY.DEX, add, absolute)

    def get_base_chr(self): 
        '''
        Returns the base ability score for the Charisma ability
        '''
        return self.get_base_ability_score(ccs.ABILITY.CHR)

    def set_base_chr(self, add, absolute=False): 
        '''
        Sets the base ability score for the Charisma ability
        Variable 'add' will add any value placed in the parameter to the base ability. If variable 'absolute' is set to True, 
        the base ability will be set to the value provided for variable 'add'
        '''
        return self.set_base_ability_score(ccs.ABILITY.CHR, add, absolute)

    def set_experience(self, add=None):
        '''
        This method sets the creature experience by adding input value 'add' to self.experience
        If a creature class is passed to the function as parameter 'add' (as in, your PC kills a monster 'creature'), the
        defeated creature's challenge rating is determined and appropriate experience is given to the victoring creature
        '''
        if add:
            if type(add) in [int,float]:
                if self.experience + int(add) >= self.get_experience_needed_to_level():
                    prev_experience = self.experience
                    self.experience = min(int(sum(range(1,self.base_level+2))*self.base_level_rate-1),int(add)+self.experience)
                    self.__last_experience_earned = self.experience - prev_experience
                else:
                    self.__last_experience_earned = int(add)
                    self.experience += int(add)
            else:
                if isinstance(add,creature):
                    exp = self._core().get_rewarded_experience_by_challenge_rating_and_level(add.get_challenge_rating(),self.get_base_level())
                    if self.experience + exp >= self.get_experience_needed_to_level():
                        prev_experience = self.experience
                        self.experience = min(int(sum(range(1,self.base_level+2))*self.base_level_rate-1),exp+self.experience)
                        self.__last_experience_earned = self.experience - prev_experience
                    else:
                        self.__last_experience_earned = exp
                        self.experience += exp


    def set_experience_by_base_level(self, base_level=None): 
        '''
        Sets appropriate experience points based on base_level (By default, identical to DnD's base_level)
        '''
        if not base_level:
            base_level = self._core().get_default_base_level()

        if self._core().get_min_base_level() <= base_level <= self._core().get_max_base_level():
            self.base_level = base_level
            self.experience = sum([i * self.base_level_rate for i in range(1, base_level)])
            return 1
        else:
            self.base_level = self._core().get_default_base_level()
            self.set_experience_by_base_level(self.base_level)
        return 0

    def set_base_level_by_experience(self, exp=None):       
        '''
        Returns base_level based on experience, if the experience is greater than what's needed
        to reach the maximum base_level, then the maximum base_level allowed is returned.
        '''
        if not exp:
            self.base_level = self._core().get_default_base_level()
            self.set_experience_by_base_level(self.base_level)
            return 0

        for i in range(1, self._core().get_max_base_level() + 1): 
            if sum([i * self.base_level_rate for i in range(1, i)]) > exp: 
                self.base_level = i-1
                self.set_experience_by_base_level(self.base_level)
                return 1

        self.base_level = self._core().get_max_base_level()
        self.set_experience_by_base_level(self.base_level)
        return 1
    
    def set_name(self, name=None): 
        '''
        set_name(str)

        Set the name of the creature using a string
        '''
        if name:
            self.name = str(name)
            return 1
        self.name = self._core().get_default_name()

        
    def get_name(self): 
        '''
        Returns a string for the name of the creature
        '''

        return self.name

    def get_race(self):
        '''
        Returns the ccs.CREATURERACE for the creature  
        '''
        return self.race

    def set_race(self,race=None):
        '''
        Sets the race of the class or returns a default if an improper race is provided.
        This also sets any racial ability bonuses for the playable races (Human, Halfling, etc.)
        '''
        race = ccs.CREATURERACE.verify(race)
        if race:
            self.__racial_ability_bonuses = self._core().get_race_information(race).get_ability_bonus_dictionary()
            self.race = race
            return 1
        else:
            self.set_race(self._core().get_default_race())
            return 0

    def get_primary_equipment_slot_type(self):
        return self.primary_equipment_slot_type

    def set_primary_equipment_slot_type(self, slot_type=None):
        slot_type = ccs.EQUIPMENTSLOTTYPE.verify(slot_type)

        if slot_type:
            self.primary_equipment_slot_type = slot_type
            return 1

        self.primary_equipment_slot_type = self._core().get_default_primary_equipment_slot_type()

    def get_equipment_standard_slots(self):
        return self.equipment_standard_slots

    def get_equipment_natural_slots(self):
        return self.equipment_natural_slots

    def get_equipment_slot_item(self, slot=None):
        '''
        Returns the item in from the given equipment slot, both standard and natural
        '''
        if ccs.EQUIPMENTSLOT.verify(slot):
            return self.equipment_standard_slots[ccs.EQUIPMENTSLOT.verify(slot)]
        elif ccs.EQUIPMENTSLOTNATURAL.verify(slot):
            return self.equipment_natural_slots[ccs.EQUIPMENTSLOTNATURAL.verify(slot)]
        else:
            print("Invalid slot!")

        return None


    def set_equipment_slot_item(self, equipment_slot=None, equippable_item=None):
        natural = False

        if ccs.EQUIPMENTSLOT.verify(equipment_slot):
            equipment_slot = ccs.EQUIPMENTSLOT.verify(equipment_slot)
        elif ccs.EQUIPMENTSLOTNATURAL.verify(equipment_slot):
            equipment_slot = ccs.EQUIPMENTSLOTNATURAL.verify(equipment_slot)
            natural = True
        else:
            return 0

        if not equippable_item:
            if natural:
                print(ccs.EQUIPMENTSLOTNATURAL.get_long_name(equipment_slot),"is now empty.")
                self.equipment_natural_slots[equipment_slot]=None
            else:
                print(ccs.EQUIPMENTSLOT.get_long_name(equipment_slot),"is now empty.")
                self.equipment_standard_slots[equipment_slot]=None

        if isinstance(equippable_item,weapon):
            if equippable_item.is_natural_weapon() and natural:
                for i in equippable_item.get_equippable_slots():
                    if i == equipment_slot:
                        self.equipment_natural_slots[equipment_slot]=equippable_item
                        return 1

            else:
                if equipment_slot == ccs.EQUIPMENTSLOT.OFFHAND and ccs.EQUIPMENTSLOT.MAINHAND in equippable_item.get_equippable_slots() and self.equipment_standard_slots[ccs.EQUIPMENTSLOT.MAINHAND] == None:
                    self.equipment_standard_slots[ccs.EQUIPMENTSLOT.MAINHAND] = equippable_item
                    return 1
                
                for i in equippable_item.get_equippable_slots():
                    if i == equipment_slot:
                        self.equipment_standard_slots[equipment_slot]=equippable_item
                        return 1
        return 0

    def generate_initial_equipment_slots(self):
        '''
        Generates the initial empty equipment slots, both standard and natural.

        Standard slots are the slots used for things such as weapons (main/off hand),
        armor (torso), helmet (head), amulets, gloves, boots, etc. These are slots
        that will be most commonly used for the playable races and others with 
        anthropomorphic (human-shaped) qualities.

        Natural slots are most commonly used for creatures that wouldn't use
        equipment such as weapons and armor. Natural weapons and armor are built for
        these purposes
        '''
        self.equipment_standard_slots = self._core().get_default_equipment_standard_slots()
        self.equipment_natural_slots = self._core().get_default_equipment_natural_slots()

        # This will eventually set the unarmed attacks as natural weapons for playable races
        if self._core().get_race_information(self.race).is_playable_race():
            self.primary_equipment_slot_type = ccs.EQUIPMENTSLOTTYPE.STANDARD
        else:
            self.primary_equipment_slot_type = ccs.EQUIPMENTSLOTTYPE.NATURAL



    def get_size_class(self):
        return self.size_class

    def set_size_class(self, size_class=None, override=False):
        '''
        This sets the size class of creatures. If a creature belongs in the playable races
        category, the size class is automatically pulled from the core settings which
        grant perks and penalties depending on which race the creature belongs to, unless 
        override is True.
        '''
        if self._core().is_playable_race(self.race) and not override:
            self.size_class = self._core().get_size_class_information_by_race(self.race)
        else:
            size_class = ccs.SIZECLASS.verify(size_class)

            if size_class:
                self.size_class = self._core().get_size_class_information(size_class)
            else:
                self.size_class = self._core().get_size_class_information(self._core().get_default_size_class())

    def get_racial_ability_bonus_dict(self):
        return self.__racial_ability_bonuses

    def get_racial_ability_bonus(self,ability):
        ability = ccs.ABILITY.verify(ability)

        if ability:
            return self.get_racial_ability_bonus_dict()[ability]
        return self._core().get_default_ability_bonus()

    def set_law_vs_chaos(self, add, absolute=False): 
        '''
        Sets the law_vs_chaos value keeping it within restricted values
        '''
        if absolute: 
            self.alignment_law_vs_chaos= add
            if self.alignment_law_vs_chaos < self._core().get_min_law_vs_chaos(): 
                self.alignment_law_vs_chaos= self._core().get_min_law_vs_chaos()
            elif self.alignment_law_vs_chaos > self._core().get_max_law_vs_chaos(): 
                self.alignment_law_vs_chaos= self._core().get_max_law_vs_chaos()
        else: 
            self.alignment_law_vs_chaos += add
            self.set_law_vs_chaos(self.alignment_law_vs_chaos + add, True)

        return self.alignment_law_vs_chaos

    def set_good_vs_evil(self, add, absolute=False): 
        '''
        Sets the good_vs_evil value keeping it within restricted values
        '''
        if absolute: 
            self.alignment_good_vs_evil= add
            if self.alignment_good_vs_evil < self._core().get_min_good_vs_evil(): 
                self.alignment_good_vs_evil= self._core().get_min_good_vs_evil()
            elif self.alignment_good_vs_evil > self._core().get_max_good_vs_evil(): 
                self.alignment_good_vs_evil= self._core().get_max_good_vs_evil()
        else: 
            self.set_good_vs_evil(self.alignment_good_vs_evil + add,True)

        return self.alignment_good_vs_evil

    def get_alignment_law_vs_chaos(self, value=False): 
        '''
        By default, this returns the core constant pertaining to the creature's alignment
        
        If value == True, the numerical value used for holding the alignment is returned
        '''
        if value:
            return self.alignment_law_vs_chaos
        return self._core().get_alignment_law_vs_chaos(self.alignment_law_vs_chaos)

    def isChaotic(self): 
        if self.get_alignment_law_vs_chaos()== ccs.ALIGNMENT.CHAOTIC: 
            return True
        return False

    def isNeutralLvC(self): 
        '''
        Returns true if creature is neutral in respect to "Law Vs Chaos" (as opposed to "Good Vs Evil")
        '''
        if self.get_alignment_law_vs_chaos()== ccs.ALIGNMENT.NEUTRALLvC: 
            return True
        return False

    def isLawful(self): 
        if self.get_alignment_law_vs_chaos()== ccs.ALIGNMENT.LAWFUL: 
            return True
        return False

    def get_alignment_good_vs_evil(self, value=False): 
        '''
        Returns the core constant for good/evil alignment
        
        If value == True, the numeric value used for storing the good/evil alignment is returned
        '''
        if value:
            return self.alignment_good_vs_evil
        return self._core().get_alignment_good_vs_evil(self.alignment_good_vs_evil)


    # Return quick checks for creature alignments
    def isGood(self): 
        if self.get_alignment_good_vs_evil()== ccs.ALIGNMENT.GOOD: 
            return True
        return False

    # Returns true if creature is neutral in respect to "Good Vs Evil" (as opposed to "Law Vs Chaos")
    def isNeutralGvE(self): 
        if self.get_alignment_good_vs_evil()== ccs.ALIGNMENT.NEUTRALGvE: 
            return True
        return False

    def isEvil(self): 
        if self.get_alignment_good_vs_evil()== ccs.ALIGNMENT.EVIL: 
            return True
        return False

    # Get the alignment in different forms
    def get_alignment(self, value=0): 
        '''
        0 returns list of core constants (Lawful Evil=[ccs.ALIGNMENT.LAWFUL,ccs.ALIGNMENT.EVIL]), 
        1 returns the values used for holding the alignment in a list (Lawful Evil might be [82,7])
        2 returns words (Lawful Evil=["Lawful", "Evil"], 
        '''
        if value:
            gve = self.get_alignment_good_vs_evil()
            lvc = self.get_alignment_law_vs_chaos()
            if value == 2:
                if lvc == ccs.ALIGNMENT.NEUTRALLvC and gve == ccs.ALIGNMENT.NEUTRALGvE:
                    return ["True","Neutral"]
                return[ccs.ALIGNMENT.get_long_name(lvc),ccs.ALIGNMENT.get_long_name(gve)] 
            elif value == 1:
                return [self.get_alignment_law_vs_chaos(1),self.get_alignment_good_vs_evil(1)]
            return [lvc,gve]


    def isChaoticEvil(self): 
        if self.isChaotic() and self.isEvil(): 
            return True
        return False

    def isChaoticNeutral(self): 
        if self.isChaotic() and self.isNeutralGvE(): 
            return True
        return False

    def isChaoticGood(self): 
        if self.isChaotic() and self.isGood(): 
            return True
        return False

    def isNeutralEvil(self): 
        if self.isNeutralLvC() and self.isEvil(): 
            return True
        return False

    def isTrueNeutral(self): 
        if self.isNeutralLvC() and self.isNeutralGvE(): 
            return True
        return False

    isNeutralNeutral = isTrueNeutral # This is to create a consistant structure when using auto-complete

    def isNeutralGood(self): 
        if self.isNeutralLvC() and self.isGood(): 
            return True
        return False

    def isLawfulEvil(self): 
        if self.isLawful() and self.isEvil(): 
            return True
        return False

    def isLawfulNeutral(self): 
        if self.isLawful() and self.isNeutralGvE(): 
            return True
        return False

    def isLawfulGood(self): 
        if self.isLawful() and self.isGood(): 
            return True
        return False

    # Sets the creature level exactly and gives the
    def set_absolute_base_level(self, base_level=None, set_experience=True): 
        if base_level == None: 
            return self._core().get_default_base_level()
        if self._core().get_min_base_level() <= base_level <= self._core().get_max_base_level(): 
            self.base_level= base_level
        elif base_level < self._core().get_min_base_level(): 
            self.base_level= self._core().get_min_base_level()
        elif base_level > self._core().get_max_base_level(): 
            self.base_level= self._core().get_max_base_level()
        else: 
            self.base_level= self._core().get_default_base_level()

        if set_experience: 
            self.set_experience_by_base_level(self.base_level)

        return self.base_level
    
    def get_ability_modifier(self, ability=None): 
        ''' Gets the ability modifier for whatever ability score is given to it '''
        ability = ccs.ABILITY.verify(ability)
        if ability: 
            return self._core().ability_modifier_from_score(self.get_ability_score(ability)) 
        else: 
            return self._core().ability_modifier_from_score(self._core().get_default_base_ability_score())

    def get_mod_str(self): 
        '''Returns the strength modifier'''
        return self.get_ability_modifier(ccs.ABILITY.STR)

    def get_mod_int(self): 
        '''Returns the intelligence modifier'''
        return self.get_ability_modifier(ccs.ABILITY.INT)

    def get_mod_con(self): 
        '''Returns the constitution modifier'''
        return self.get_ability_modifier(ccs.ABILITY.CON)

    def get_mod_wis(self): 
        '''Returns the wisdom modifier'''
        return self.get_ability_modifier(ccs.ABILITY.WIS)

    def get_mod_dex(self): 
        '''Returns the dexterity modifier'''
        return self.get_ability_modifier(ccs.ABILITY.DEX)

    def get_mod_chr(self): 
        '''Returns the charisma modifier'''
        return self.get_ability_modifier(ccs.ABILITY.CHR)

    '''
    Gives the ability modifier functions a long-hand form
    '''
    get_mod_strength = get_mod_str
    get_mod_intelligence = get_mod_int
    get_mod_constitution = get_mod_con
    get_mod_wisdom = get_mod_wis
    get_mod_dexterity = get_mod_dex
    get_mod_charisma = get_mod_chr

    def stat_display(self):
        perc = percbar()
        print("Name:",self.name,"| Level:",self.base_level, "| Armor Class:",self.get_armor_class(),"| Alignment:",' '.join(self.get_alignment(2)).title())
        print("Race:",self.race.title(),"| Class:",self.creature_class.upper())
        print("Experience:",perc.disp(self.get_experience_toward_next_level(),self.get_experience_total_for_current_level(),50),str(self.get_experience_toward_next_level())+"/"+str(self.get_experience_total_for_current_level()))
        print('STR:',self.get_ability_score(ccs.ABILITY.STR),"/",self.get_mod_str(),"| CON:",self.get_ability_score(ccs.ABILITY.CON),"/",self.get_mod_con(),"| DEX:",self.get_ability_score(ccs.ABILITY.DEX),"/",self.get_mod_dex())
        print('INT:',self.get_ability_score(ccs.ABILITY.INT),"/",self.get_mod_int(),"| WIS:",self.get_ability_score(ccs.ABILITY.WIS),"/",self.get_mod_wis(),"| CHR:",self.get_ability_score(ccs.ABILITY.CHR),"/",self.get_mod_chr())
        print('        HP:',perc.disp(self.get_current_hit_points(),self.get_base_hit_points(),50),str(self.get_current_hit_points())+'/'+str(self.get_base_hit_points()))

    def stat_display_short(self):
        perc = percbar(None,None,50)
        print("Name:",self.name,"| Lvl:",self.base_level,"| Race:", ccs.CREATURERACE.get_long_name(self.race),"| Class:",self.creature_class.upper())
        print("        HP:", perc.disp(self.get_current_hit_points(),self.get_base_hit_points(),None,True,2))


####################################################### TEST CODE ######################################################
# a= creature(race='DOG', name="Carl", exp=19673, law_vs_chaos=30, good_vs_evil=90, base_level_rate=1000, verbose=True)
# 
# print(a.name, a.race, a.base_level, a.experience, a.get_experience_needed_to_level(),a.get_experience_toward_next_level(),a.get_alignment(1), \
# a.set_base_str(24), a.get_ability_modifier(ccs.ABILITY.STR))
# print(a.base_saving_throw_bonus)
# print('Attack!: ', a.attack_roll())
# print(a.get_skill_set().get_skill(10).get_class_skills())
# a.get_skill(10).set_base_skill_points(5)
# print(a.get_skill(10).get_base_skill_points())
# a.get_skill(10).set_base_skill_points(7)
# print(a.get_skill(10).get_base_skill_points())
# a.get_skill(10).set_base_skill_points(21, True)
# print(a.get_skill(10).get_base_skill_points())
# print(a.get_skill(11).get_skill_name())
# a = creature(base_level=20,str=4)
# print(a.attack_roll())
# a.stat_display()
# print(a.get_experience())
