'''
     Name: creature.py
    Author: Benjamin A
 Purpose: The creature class creates an object with relevant methods to in-game creatures, npcs, pcs, etc
 This class can be used to create subclasses that inherit all the common traits of creatures, 
 but extended to define specific and even custom creatures.
 
'''

from core.__core_creature_configuration import core_creature_configuration
# from core.__core_creature_class_configuration import core_creature_class_configuration
from core.__core_constants import core_constants
from core.verbose import verbose
#from skill_set import skill_set
from dice import dice
from percbar import percbar


class creature(verbose, dice): 
    # A short method in most classes that calls the core settings for that particular class.
    def _core(self): 
        return core_creature_configuration()

    def __init__(self, playable_character=None, name=None, creature_class=None, race=None, challenge_rating=None, deity=None, law_vs_chaos=None, good_vs_evil=None, base_hit_points=None, base_level=None, exp=None, base_armor_class=None, base_level_rate=None, str=None, inte=None, chr=None, dex=None, con=None, wis=None, verbo=False): 

        # Initialize inherited classes
        verbose.__init__(self,verbo)
        dice.__init__(self)

        self.playable_character=playable_character or self._core().get_default_playable_character()
        self.name=name or self._core().get_default_name()
        self.creature_class = creature_class or self._core().get_default_creature_class()
        self.race=race or self._core().get_default_race()
        self.deity=deity or self._core().get_default_deity()
        self.law_vs_chaos=law_vs_chaos or self._core().get_default_law_vs_chaos()# Scale 0 - 100. 0-32= Chaos, 33-67= Neutral, 68-100= Law
        self.good_vs_evil=good_vs_evil or self._core().get_default_good_vs_evil()# Scale 0 - 100. 0-32= Evil, 33-67= Neutral, 68-100= Good

        self.base_hit_points=base_hit_points or self._core().get_default_base_hit_points()
        self.current_hit_points=self.base_hit_points
        self.challenge_rating = challenge_rating or self._core().get_default_challenge_rating()

        self.base_level_rate=base_level_rate or self._core().get_default_base_level_rate() # 1000 is the standard growth, the lower the number, the faster a character can base_level
        self.base_level=base_level or self.set_base_level_by_experience(exp) or self._core().get_default_base_level() # If base_level is zero, sets base_level by experience
        self.experience=exp or self.set_experience_by_base_level(self.base_level)
        ''' If experience is zero, sets experience based on base_level. Defaults to 0 experience base_level 1 when no parameters entered.'''

        self.__last_experience_earned = 0 # Used for logging
        self.skill_set=0 #skill_set()

        self.base_saving_throw_bonus={i: 0 for i in core_constants().SAVINGTHROW.get_index()}

        # Dictionary of base_abilities
        self.base_abilities={core_constants().ABILITY.STR:str or self._core().get_default_base_ability_score(),
                             core_constants().ABILITY.INT:inte or self._core().get_default_base_ability_score(),
                             core_constants().ABILITY.CON:con or self._core().get_default_base_ability_score(),
                             core_constants().ABILITY.WIS:wis or self._core().get_default_base_ability_score(),
                             core_constants().ABILITY.DEX:dex or self._core().get_default_base_ability_score(),
                             core_constants().ABILITY.CHR:chr or self._core().get_default_base_ability_score()}

        self.base_armor_class = None
        self.set_base_armor_class(base_armor_class)

        self.inventory=[] # Holds list of items, an inventory system is in the future.

    # Returns the base_level of the creature
    def get_base_level(self): 
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

    def base_attack_bonus(self): 
        '''
        Returns the attack bonuses based on level and attack-ability
        '''
        return self._core().get_base_attack_bonus(2, self.base_level) # <---------------------------------------- Not always two, fix it!

    def get_base_hit_points(self):
        return self.base_hit_points

    def set_base_hit_points(self,add=None,absolute=None):
        if not add:
            return False
        elif not absolute:
            self.base_hit_points += add
        else:
            self.base_hit_points = min(max(self.base_hit_points,self._core().get_min_base_hit_points()),self._core().get_max_base_hit_points())
        
    def get_current_hit_points(self):
        return self.current_hit_points

    def set_current_hit_points(self,add=None,absolute=None):
        if not add:
            return False
        elif not absolute:
            self.current_hit_points = max(min(self.current_hit_points + add, self.base_hit_points),self._core().get_min_current_hit_points())
        else:
            self.current_hit_points = min(max(self.current_hit_points,self._core().get_min_current_hit_points()),self.get_base_hit_points())

    def get_challenge_rating(self):
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
        if self.current_hit_points > 0:
            return True
        else:
            return False

    def is_dead(self):
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
        return self.base_armor_class + self.get_ability_modifier(core_constants().ABILITY.DEX)

    def get_AC(self):
        return self.get_armor_class()

    def attack_roll(self,verbo=False):
        '''
        attack_roll() returns a lists of 2-valued lists. The lists contain two numbers [a,b] where
        a = the number on the dice roll (d20)
        b = the dice roll + attack bonus + strength modifier
        
        Variable "a" allows for the damage roll to account for the threat range for criticals
        Variable "b" would be used against opponents AC
        '''
        roll_list=[]
        for i,j in zip(self.base_attack_bonus(),self.d20(len(self.base_attack_bonus()))):
            if 1 < j <= 20:
                roll_list.append([j,j+i+self.mod_str()])
            else:
                roll_list.append([0,0])
        return roll_list
            
    def damage_roll(self,critical=False,verbo=False): 
        '''
        damage_roll() returns a dice roll that will soon be based on the weapon the creature is carrying

        argument "critical" returns a critical hit roll that will be based on the weapon the creature is carrying
        '''
        damage = 0
        if critical: 
            roll=sum(self.d(6,3))
            damage = max(roll + self.mod_str(),1)
        else:
            roll = sum(self.d(4,2))
            damage = max(roll + self.mod_str(),0)

        return damage

    def get_skill_set(self): 
        return self.skill_set

    def get_skill(self, id=None): 
        return self.skill_set.get_skill(id)

    # Sets all the base abilities at once, or whichever are provided.
    # absolute== False : Base ability has parameter added to it (str=1==> self.base_abilities[core_constants().ABILITY.STR] += 1)
    # absolute== True : Base ability is set to parameter (str=1==> self.base_abilities[core_constants().ABILITY.STR]=1)
    def set_all_base_ability_score(self, str=0, inte=0, con=0, wis=0, dex=0, chr=0, absolute=False): 
        # if statements necessary. If absolute=true
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
        ability = core_constants().ABILITY.verify(ability)
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

    # Returns base ability value for any valid ability provided
    def get_base_ability_score(self, ability=None): 
        ability = core_constants().ABILITY.verify(ability)

        if ability:
           return self.base_abilities[ability]
        return self._core().get_default_base_ability_score()

    # Returns the base ability score for the Strength ability
    def get_base_str(self): 
        return self.get_base_ability_score(core_constants().ABILITY.STR)

    # Sets the base ability score for the Strength ability
    # Variable 'add' will add any value placed in the parameter to the base ability. If variable 'absolute' is set to True, 
    # the base ability will be set to the value provided for variable 'add'
    def set_base_str(self, add, absolute=False): 
        return self.set_base_ability_score(core_constants().ABILITY.STR, add, absolute)

    # Returns the base ability score for the Intelligence ability
    def get_base_int(self): 
        return self.get_base_ability_score(core_constants().ABILITY.INT)

    # Sets the base ability score for the Intelligence ability
    # Variable 'add' will add any value placed in the parameter to the base ability. If variable 'absolute' is set to True, 
    # the base ability will be set to the value provided for variable 'add'
    def set_base_int(self, add, absolute=False): 
        return self.set_base_ability_score(core_constants().ABILITY.INT, add, absolute)

    # Returns the base ability score for the Constitution ability
    def get_base_con(self): 
        return self.get_base_ability_score(core_constants().ABILITY.CON)

    # Sets the base ability score for the Constitution ability
    # Variable 'add' will add any value placed in the parameter to the base ability. If variable 'absolute' is set to True, 
    # the base ability will be set to the value provided for variable 'add'
    def set_base_con(self, add, absolute=False): 
        return self.set_base_ability_score(core_constants().ABILITY.CON, add, absolute)

    # Returns the base ability score for the Wisdom ability
    def get_base_wis(self): 
        return self.get_base_ability_score(core_constants().ABILITY.WIS)

    # Sets the base ability score for the Wisdom ability
    # Variable 'add' will add any value placed in the parameter to the base ability. If variable 'absolute' is set to True, 
    # the base ability will be set to the value provided for variable 'add'
    def set_base_wis(self, add, absolute=False): 
        return self.set_base_ability_score(core_constants().ABILITY.WIS, add, absolute)

    # Returns the base ability score for the Dexterity ability
    def get_base_dex(self): 
        return self.get_base_ability_score(core_constants().ABILITY.DEX)

    # Sets the base ability score for the Dexterity ability
    # Variable 'add' will add any value placed in the parameter to the base ability. If variable 'absolute' is set to True, 
    # the base ability will be set to the value provided for variable 'add'
    def set_base_dex(self, add, absolute=False): 
        return self.set_base_ability_score(core_constants().ABILITY.DEX, add, absolute)

    # Returns the base ability score for the Charisma ability
    def get_base_chr(self): 
        return self.get_base_ability_score(core_constants().ABILITY.CHR)

    def set_base_chr(self, add, absolute=False): 
        '''
        Sets the base ability score for the Charisma ability
        Variable 'add' will add any value placed in the parameter to the base ability. If variable 'absolute' is set to True, 
        the base ability will be set to the value provided for variable 'add'
        '''
        return self.set_base_ability_score(core_constants().ABILITY.CHR, add, absolute)

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


    def set_experience_by_base_level(self, base_level=1): 
        '''
        Sets appropriate experience points based on base_level (By default, identical to DnD's base_level)
        '''
        return sum([i * self.base_level_rate for i in range(1, base_level)])

    def set_base_level_by_experience(self, exp=0):       
        '''
        Returns base_level based on experience, if the experience is greater than what's needed
        to reach the maximum base_level, then the maximum base_level allowed is returned.
        '''
        if not exp:
            return exp 

        for i in range(1, self._core().get_max_base_level() + 1): 
            if sum([i * self.base_level_rate for i in range(1, i)]) > exp: 
                return i - 1
        return self._core().get_max_base_level()
    
    def set_name(self, name): 
        self.name= name
        return self.name
        
    def get_name(self): 
        return self.name

    def set_law_vs_chaos(self, add, absolute=False): 
        '''
        Sets the law_vs_chaos value keeping it within restricted values
        '''
        if absolute: 
            self.law_vs_chaos= add
            if self.law_vs_chaos < self._core().get_min_law_vs_chaos(): 
                self.law_vs_chaos= self._core().get_min_law_vs_chaos()
            elif self.law_vs_chaos > self._core().get_max_law_vs_chaos(): 
                self.law_vs_chaos= self._core().get_max_law_vs_chaos()
        else: 
            self.law_vs_chaos += add

        return self.law_vs_chaos

    def set_good_vs_evil(self, add, absolute=False): 
        '''
        Sets the good_vs_evil value keeping it within restricted values
        '''
        if absolute: 
            self.good_vs_evil= add
            if self.good_vs_evil < self._core().get_min_good_vs_evil(): 
                self.good_vs_evil= self._core().get_min_good_vs_evil()
            elif self.good_vs_evil > self._core().get_max_good_vs_evil(): 
                self.good_vs_evil= self._core().get_max_good_vs_evil()
        else: 
            self.good_vs_evil += add

        return self.good_vs_evil

    def get_law_vs_chaos(self, value_word_combo=0): 
        '''
        Returns law vs chaos values and or "lawful", "chaotic", and "neutral"
        0 returns value, 1 returns word, 2 returns both, -1 returns raw variable
        '''
        temp=[0, 0]

        if self.law_vs_chaos < 33: 
            temp= [0, "chaotic"]
        elif self.law_vs_chaos > 67: 
            temp= [2, "lawful"]
        else: 
            temp= [1, "neutral"]
        
        if 0 <= value_word_combo < 2: 
            return temp[value_word_combo]
        elif value_word_combo== -1: 
            return self.law_vs_chaos
        else: 
            return temp

    def isChaotic(self): 
        if self.get_law_vs_chaos()== 0: 
            return True
        return False

    # Returns true if creature is neutral in respect to "Law Vs Chaos" (as opposed to "Good Vs Evil")
    def isNeutralLvC(self): 
        if self.get_law_vs_chaos()== 1: 
            return True
        return False

    def isLawful(self): 
        if self.get_law_vs_chaos()== 2: 
            return True
        return False

    # Returns "evil", "good", or "neutral" based on good_vs_evil value
    def get_good_vs_evil(self, value_word_combo=0): # 0 returns value, 1 returns word, 2 returns both, -1 returns raw variable
        temp=[0, 0]

        if self.good_vs_evil < 33: 
            temp= [0, "evil"]
        elif self._core().get_max_base_ability_score() >= self.good_vs_evil > 67: 
            temp= [2, "good"]
        else: 
            temp= [1, "neutral"]

        if 0 <= value_word_combo < 2: 
            return temp[value_word_combo]
        elif value_word_combo== -1: 
            return self.good_vs_evil
        else: 
            return temp

    # Return quick checks for creature alignments
    def isGood(self): 
        if self.get_good_vs_evil()== 2: 
            return True
        return False

    # Returns true if creature is neutral in respect to "Good Vs Evil" (as opposed to "Law Vs Chaos")
    def isNeutralGvE(self): 
        if self.get_good_vs_evil()== 1: 
            return True
        return False

    def isEvil(self): 
        if self.get_good_vs_evil()== 0: 
            return True
        return False

    # Get the alignment in different forms
    def get_alignment(self, value_word_combo=0): 
        '''
        0 returns list of values (Lawful Evil=[2, 0]), 
        1 returns words (Lawful Evil=["Lawful", "Evil"], 
        2 returns a list holding two lists of values and words, 
        -1 returns the exact alignment variables
        '''
        temp=[self.get_law_vs_chaos(2), self.get_good_vs_evil(2)]
        if value_word_combo== 0: 
            return [temp[0][0], temp[1][0]]
        elif value_word_combo== 1: 
            if temp[0][0]== 1 and temp[1][0]== 1: #
                return ["true", "neutral"]
            return [temp[0][1], temp[1][1]]
        elif value_word_combo== -1: 
            return [self.get_law_vs_chaos(value_word_combo), self.get_good_vs_evil(value_word_combo)]
        else: 
            return temp

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
        ability = core_constants().ABILITY.verify(ability)
        if ability: 
            return self._core().ability_modifier_from_score(self.get_base_ability_score(ability))
        else: 
            return self._core().ability_modifier_from_score(self._core().get_default_base_ability_score())

    def mod_str(self): 
        '''Returns the strength modifier'''
        return self.get_ability_modifier(core_constants().ABILITY.STR)

    def mod_int(self): 
        '''Returns the intelligence modifier'''
        return self.get_ability_modifier(core_constants().ABILITY.INT)

    def mod_con(self): 
        '''Returns the constitution modifier'''
        return self.get_ability_modifier(core_constants().ABILITY.CON)

    def mod_wis(self): 
        '''Returns the wisdom modifier'''
        return self.get_ability_modifier(core_constants().ABILITY.WIS)

    def mod_dex(self): 
        '''Returns the dexterity modifier'''
        return self.get_ability_modifier(core_constants().ABILITY.DEX)

    def mod_chr(self): 
        '''Returns the charisma modifier'''
        return self.get_ability_modifier(core_constants().ABILITY.CHR)

    def stat_display(self):
        perc = percbar()
        print("Name:",self.name,"| Level:",self.base_level, "| Armor Class:",self.get_armor_class(),"| Alignment:",' '.join(self.get_alignment(1)).title())
        print("Race:",self.race.title(),"| Class:",self.creature_class.upper())
        print("Experience:",perc.disp(self.get_experience_toward_next_level(),self.get_experience_total_for_current_level(),50),str(self.get_experience_toward_next_level())+"/"+str(self.get_experience_total_for_current_level()))
        print('STR:',self.base_abilities[core_constants().ABILITY.STR],"/",self.mod_str(),"| CON:",self.base_abilities[core_constants().ABILITY.CON],"/",self.mod_con(),"| DEX:",self.base_abilities[core_constants().ABILITY.DEX],"/",self.mod_dex())
        print('INT:',self.base_abilities[core_constants().ABILITY.INT],"/",self.mod_int(),"| WIS:",self.base_abilities[core_constants().ABILITY.WIS],"/",self.mod_wis(),"| CHR:",self.base_abilities[core_constants().ABILITY.CHR],"/",self.mod_chr())
        print('HP:',perc.disp(self.get_current_hit_points(),self.get_base_hit_points(),50),str(self.get_current_hit_points())+'/'+str(self.get_base_hit_points()))

    def stat_display_short(self):
        perc = percbar(None,None,50)
        print("Name:",self.name,"| Lvl:",self.base_level,"| Race:", core_constants().CREATURERACE.get_long_name(self.race),"| Class:",self.creature_class.upper())
        print("HP:", perc.disp(self.get_current_hit_points(),self.get_base_hit_points(),None,True,2))


####################################################### TEST CODE ######################################################
# a= creature(race='DOG', name="Carl", exp=19673, law_vs_chaos=30, good_vs_evil=90, base_level_rate=1000, verbose=True)
# 
# print(a.name, a.race, a.base_level, a.experience, a.get_experience_needed_to_level(),a.get_experience_toward_next_level(),a.get_alignment(1), \
# a.set_base_str(24), a.get_ability_modifier(core_constants().ABILITY.STR))
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
