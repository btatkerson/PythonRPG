'''
      Name: __core_creature_configuration.py
   Purpose: This is a core file for the engine that defines the boundaries of the creatures in the game.
            It limits levels, defines EQUIPMENT slots available, etc.

'''
from core.__core_race_configuration import core_race_configuration
from core.__creature_class_settings import core_creature_class_settings
from dice import dice

import core.__core_constants_mod as ccs

class core_creature_configuration(core_race_configuration):

    def __init__(self):
        core_race_configuration.__init__(self) # Inherits the core race configurations of the game, the creature configuration is highly involved with races

        self.__DEFAULT_ABILITY = ccs.ABILITY.STR # strength
        self.__DEFAULT_BASE_ARMOR_CLASS = 10
        self.__MIN_BASE_ARMOR_CLASS = 1
        self.__MAX_BASE_ARMOR_CLASS = 50
        self.__DEFAULT_BASE_ABILITY_SCORE = 10
        self.__MIN_BASE_ABILITY_SCORE = 1
        self.__MAX_BASE_ABILITY_SCORE = 255
        self.__DEFAULT_BASE_HIT_POINTS = 10
        self.__MIN_BASE_HIT_POINTS = 1
        self.__DEFAULT_BASE_LEVEL = 0 # This is technically fixed to go to 1 because of |
        self.__MIN_BASE_LEVEL = 1     # THIS <------------------------------------------'
        self.__MAX_BASE_LEVEL = 40    # See the creature.py "set_base_level" function
        self.__MAX_STANDARD_LEVEL = 20 # after this level, epic bonuses are considered
        self.__DEFAULT_CURRENT_HIT_POINTS = self.__DEFAULT_BASE_HIT_POINTS
        self.__MIN_CURRENT_HIT_POINTS = -10
        self.__MAX_CURRENT_HIT_POINTS = 10000
        self.__MIN_CHALLENGE_RATING = 0
        self.__MAX_CHALLENGE_RATING = 40
        self.__DEFAULT_CHALLENGE_RATING = 1
        self.__DEFAULT_DEITY = None         # <          TO-DO              >  
        self.__DEFAULT_EXPERIENCE = 0
        self.__MIN_EXPERIENCE = 0
        self.__MAX_EXPERIENCE = sum(range(self.__MIN_BASE_LEVEL,self.__MAX_BASE_LEVEL+1)) # This gets used with the __DEFAULT_BASE_LEVEL_RATE
        self.__DEFAULT_BASE_LEVEL_RATE = 1000 # Each level costs 1000*base_level

        self.__DEFAULT_HIT_DIE = '1d8'

        self.__DEFAULT_ALIGNMENT_GOOD_VS_EVIL = 50 # Neutral
        self.__MIN_ALIGNMENT_GOOD_VS_EVIL = 0
        self.__MAX_ALIGNMENT_GOOD_VS_EVIL = 100
        self.__MAX_ALIGNMENT_EVIL = 30
        self.__MIN_ALIGNMENT_GOOD = 70

        self.__DEFAULT_ALIGNMENT_LAW_VS_CHAOS = 50 # Neutral
        self.__MIN_ALIGNMENT_LAW_VS_CHAOS = 0
        self.__MAX_ALIGNMENT_CHAOS = 30 # Everything between MAX_ALI_CHAOS and MIN_ALI_LAW is considered neutral
        self.__MIN_ALIGNMENT_LAW = 70
        self.__MAX_ALIGNMENT_LAW_VS_CHAOS = 100

        self.__DEFAULT_NAME = 'MissingName'
        self.__DEFAULT_PLAYABLE_CHARACTER = False
        self.__DEFAULT_RACE = ccs.CREATURERACE.HUMAN
        self.__DEFAULT_CREATURE_CLASS = ccs.CREATURECLASS.UNIQUE


        self.__DEFAULT_BASE_ATTACK_BONUS = ccs.BASEATTACKBONUS.AVERAGE
        self.__DEFAULT_BASE_SAVE_BONUS = ccs.BASESAVEBONUS.GOOD
        self.__DEFAULT_SAVING_THROW = ccs.SAVINGTHROW.FORTITUDE # fortitude

        self.__DEFAULT_PRIMARY_EQUIPMENT_SLOT_TYPE = ccs.EQUIPMENTSLOTTYPE.NATURAL
        self.__EQUIPMENT_STANDARD_SLOTS = {i:None for i in ccs.EQUIPMENTSLOT.get_index()}
        self.__EQUIPMENT_NATURAL_SLOTS = {i:None for i in ccs.EQUIPMENTSLOTNATURAL.get_index()}

        
        self.__CHALLENGE_RATING_LIST = []
        self.generate_challenge_rating_list()

        self.__CREATURE_CLASS_TABLE = {i:None for i in ccs.CREATURECLASS.get_index()}
        self.generate_class_settings()
        
    def generate_challenge_rating_list(self):
        '''
        This generates a table of xp values based on creature level and enemy challenge ratings

        Each line is a level from 1-40
        Each separated value per line is based on the opponent's challenge rating

        '''
        self.__CHALLENGE_RATING_LIST = []
        with open("./data/xptable.csv") as f:
            for i in f:
                self.__CHALLENGE_RATING_LIST.append([int(j) for j in i.split()])
        f.close()


    def generate_class_settings(self):
        '''
        Reads the creature class file that holds each classes standard settings
        '''

        temp = None
        with open("./data/creature_class_table.csv") as f:
            temp = f.read()
        f.close()
        temp = temp.split("\n")
        temp.pop(0)
        temp.pop()

        for i,j in enumerate(temp):
            temp[i] = j.split(";")
            temp[i][0] = ccs.CREATURECLASS.verify(temp[i][0])

            if temp[i][1] != '0':
                temp[i][1] = ccs.ALIGNMENT.filter_list(temp[i][1].split())
            
            temp[i][7] = ccs.SKILL.filter_list(temp[i][7].split())

            temp[i][8] = ccs.SPELLCASTING_SCHOOL.verify(temp[i][8])

            temp[i][10] = ccs.BASEATTACKBONUS.verify(temp[i][10])

            for k in range(11,14):
                temp[i][k] = ccs.BASESAVEBONUS.verify(temp[i][k])


        for i in temp:
            base_saves = {ccs.SAVINGTHROW.REF: i[11],
                          ccs.SAVINGTHROW.FOR: i[12],
                          ccs.SAVINGTHROW.WIL: i[13]}

            self.__CREATURE_CLASS_TABLE[i[0]]= core_creature_class_settings(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],base_saves)


    def get_class_information(self,creature_class=None):
        '''
        Returns the class settings for the input creature_class
        '''
        creature_class = ccs.CREATURECLASS.verify(creature_class)
        if creature_class:
            return self.__CREATURE_CLASS_TABLE[creature_class] or core_creature_class_settings()
        return self.__CREATURE_CLASS_TABLE[self.get_default_creature_class()]

    def get_class_hit_die(self,creature_class=None):
        '''
        Returns the hit die related to a creature class
        '''
        creature_class = self.get_class_information(creature_class)
        d = dice(creature_class.get_hit_die_value(),creature_class.get_number_of_hit_dice())
        return d

    def get_class_alignment_restrictions(self, creature_class=None):
        '''
        Returns the alignment for a particular class
        '''
        return self.get_class_information(creature_class).get_alignment_restrictions()

    def get_class_spellcasting_school(self, creature_class=None):
        '''
        Returns the spellcasting school core constant for a particular class
        '''
        return self.get_class_information(creature_class).get_spellcasting_school()

    def get_class_base_attack_bonus(self, creature_class=None):
        '''
        Returns the base attack bonus core constant for a particular class
        '''
        return self.get_class_information(creature_class).get_base_attack_bonus()

    def is_class_skill(self,creature_class=None,skill=None):
        '''
        Returns True if skill is a class/favored skill for the creature race
        '''
        return self.get_class_information(creature_class).is_favored_skill(skill)

    def get_class_skills(self,creature_class=None):
        '''
        Returns list of valid class/favored skills for the creature class
        '''
        return self.get_class_information(creature_class).get_favored_skills()

    def get_class_skill_points_earned(self,creature_class=None, int_mod=None):
        '''
        Returns the skill points a class gains on level up

        Uses the base_intelligence modifier and adds it to the base skill points determined by the
        creature class
        '''
        return self.get_class_information(creature_class).get_skill_points_earned() 

    def get_class_base_save_bonuses(self, creature_class=None, saving_throw=None):
        '''
        Returns the saving throw bonuses dictionary related to the creature class 

        If saving_throw, only the bonus for that saving throw type is returned
        '''
        creature_class = ccs.CREATURECLASS.verify(creature_class)
        saving_throw = ccs.SAVINGTHROW.verify(saving_throw)

        if saving_throw:
            return self.get_class_information(creature_class).get_base_save_bonuses()[saving_throw]
        return self.get_class_information(creature_class).get_base_save_bonuses()


    def ability_modifier_from_score(self,score):
        '''
        Converts ability scores to their modifiers
        score:modifier =>
           1: -5,
         2-3: -4,
         4-5: -3
        ~~~~~~~~
       10-11:  0,
       16-17: +3, so on and so forth

        This is a critical calculation to the core gameplay.
        '''
        if score < self.get_min_base_ability_score():
            score = self.get_min_base_ability_score()

        return int((score-10)/2)

    def get_challenge_rating_table(self):
        return self.__CHALLENGE_RATING_LIST


    def get_rewarded_experience_by_challenge_rating_and_level(self,challenge_rating=None,level=None):
        if challenge_rating == None:
            challenge_rating = self.__DEFAULT_CHALLENGE_RATING

        if level == None:
            level = self.__DEFAULT_BASE_LEVEL

        if 0 < challenge_rating < 1:
            return int(self.__CHALLENGE_RATING_LIST[level-1][0]*challenge_rating)

        challenge_rating = min(max(int(challenge_rating),self.__MIN_CHALLENGE_RATING),self.__MAX_CHALLENGE_RATING)

        return int(self.__CHALLENGE_RATING_LIST[level-1][challenge_rating])

    def get_default_base_armor_class(self):
        return self.__DEFAULT_BASE_ARMOR_CLASS
    
    def get_min_base_armor_class(self):
        return self.__MIN_BASE_ARMOR_CLASS

    def get_max_base_armor_class(self):
        return self.__MAX_BASE_ARMOR_CLASS

    def get_default_base_level_rate(self):
        return self.__DEFAULT_BASE_LEVEL_RATE

    def get_default_hit_die(self):
        return self.__DEFAULT_HIT_DIE

    def get_default_base_level(self):
        return self.__DEFAULT_BASE_LEVEL

    def get_min_base_level(self):
        return self.__MIN_BASE_LEVEL

    def get_max_base_level(self):
        return self.__MAX_BASE_LEVEL

    def get_max_standard_level(self):
        '''
        This is the last level a creature can hit before epic bonuses begin
        '''
        return self.__MAX_STANDARD_LEVEL

    def get_min_base_ability_score(self):
        return self.__MIN_BASE_ABILITY_SCORE

    def get_max_base_ability_score(self):
        return self.__MAX_BASE_ABILITY_SCORE

    def get_saving_throw_list(self):
        return self.__SAVING_THROW_LIST

    def get_saving_throw_list_short(self):
        return self.__SAVING_THROW_LIST_SHORT

    def get_default_base_ability_score(self):
        return self.__DEFAULT_BASE_ABILITY_SCORE

    def get_default_ability(self):
        return self.__DEFAULT_ABILITY

    def get_default_experience(self):
        return self.__DEFAULT_EXPERIENCE(self)

    def get_min_experience(self):
        return self.__MIN_EXPERIENCE

    def get_max_experience(self):
        return self.__MAX_EXPERIENCE

    def get_default_alignment_good_vs_evil(self):
        return self.__DEFAULT_ALIGNMENT_GOOD_VS_EVIL

    def get_default_alignment_evil(self): # Used for default value for evil
        return (self.__MIN_ALIGNMENT_GOOD_VS_EVIL+self.__MAX_ALIGNMENT_EVIL)//2

    def get_default_alignment_good(self): # Default value of good alignment
        return (self.__MAX_ALIGNMENT_GOOD_VS_EVIL+self.__MIN_ALIGNMENT_GOOD)//2

    def get_default_alignment_neutralgve(self):
        return (self.__MAX_ALIGNMENT_EVIL+self.__MIN_ALIGNMENT_GOOD)//2

    def get_min_alignment_good_vs_evil(self):
        return self.__MIN_ALIGNMENT_GOOD_VS_EVIL

    def get_max_alignment_good_vs_evil(self):
        return self.__MAX_ALIGNMENT_GOOD_VS_EVIL

    def get_default_alignment_law_vs_chaos(self):
        return self.__DEFAULT_ALIGNMENT_LAW_VS_CHAOS

    def get_default_alignment_chaos(self):
        return (self.__MAX_ALIGNMENT_CHAOS+self.__MIN_ALIGNMENT_LAW_VS_CHAOS)//2

    def get_default_alignment_law(self):
        return (self.__MAX_ALIGNMENT_LAW_VS_CHAOS+self.__MIN_ALIGNMENT_LAW)//2 

    def get_default_alignment_neutrallvc(self):
        return (self.__MAX_ALIGNMENT_CHAOS+self.__MIN_ALIGNMENT_LAW)//2

    def get_min_alignment_law_vs_chaos(self):
        return self.__MIN_ALIGNMENT_LAW_VS_CHAOS

    def get_max_alignment_law_vs_chaos(self):
        return self.__MAX_ALIGNMENT_LAW_VS_CHAOS

    def get_default_playable_character(self):
        return self.__DEFAULT_PLAYABLE_CHARACTER

    def get_default_creature_class(self):
        return self.__DEFAULT_CREATURE_CLASS

    def get_default_race(self):
        return self.__DEFAULT_RACE

    def get_default_name(self):
        return self.__DEFAULT_NAME

    def get_default_base_hit_points(self):
        return self.__DEFAULT_BASE_HIT_POINTS

    def get_min_base_hit_points(self):
        return self.__MIN_BASE_HIT_POINTS

    def get_min_current_hit_points(self):
        return self.__MIN_CURRENT_HIT_POINTS

    def get_max_current_hit_points(self):
        return self.__MAX_CURRENT_HIT_POINTS

    def get_min_challenge_rating(self):
        return self.__MIN_CHALLENGE_RATING

    def get_max_challenge_rating(self):
        return self.__MAX_CHALLENGE_RATING

    def get_default_challenge_rating(self):
        return self.__DEFAULT_CHALLENGE_RATING

    def get_default_deity(self):
        return self.__DEFAULT_DEITY

    def get_default_base_save_bonus(self):
        return self.__DEFAULT_BASE_SAVE_BONUS

    def get_default_saving_throw(self):
        return self.__DEFAULT_SAVING_THROW

    def get_base_save_bonus(self,base_save_bonus=None,creature_level=1):
        '''
        Returns a list of save bonuses for the 'poor', and 'good', base_save_bonus can be given as a value or the name value,
        creature_level is fairly self-explanatory
        0 : 'poor',
        1 : 'good'
        '''
        base_save_bonus = ccs.BASESAVEBONUS.verify(base_save_bonus)

        if base_save_bonus:
            epic_bonus = max(0,round((creature_level-self.__MAX_STANDARD_LEVEL-1)/2.0)) # All negative bonuses become zero.

            creature_level = max(min(self.__MAX_STANDARD_LEVEL,creature_level),self.__MIN_BASE_LEVEL) # 20 is the maximum level of bonus
            # growth excluding epic bonuses. This also keeps the level from being no lower than whatever the minimum
            # base level

            if base_save_bonus == ccs.BASESAVEBONUS.POOR: # The base save bonus for a 'poor' level bonuses
                return int(int(creature_level/3) + epic_bonus)

            else: # The base save bonus for a 'good' level bonus
                return int(2 + int(creature_level/2) + epic_bonus)

        return self.get_base_save_bonus(self.get_default_base_save_bonus(),creature_level)

    def get_default_primary_equipment_slot_type(self):
        return self.__DEFAULT_PRIMARY_EQUIPMENT_SLOT_TYPE

    def get_default_equipment_standard_slots(self):
        return self.__EQUIPMENT_STANDARD_SLOTS

    def get_default_equipment_natural_slots(self):
        return self.__EQUIPMENT_NATURAL_SLOTS

    def get_default_base_attack_bonus(self):
        return self.__DEFAULT_BASE_ATTACK_BONUS

    def get_base_attack_bonus(self,base_attack_bonus=None,creature_level=1):
        '''
        Returns a list of attack bonuses for the 'poor', 'average', and 'good', if there are multiple attacks,
        the sequential bonuses are provbase_save_bonused. base_save_bonus can be given as a value or the name value
        0 : 'poor',
        1 : 'average',
        2 : 'good'
        '''
        base_attack_bonus = ccs.BASEATTACKBONUS.verify(base_attack_bonus)
        

        if base_attack_bonus:
            temp_stack = []

            '''
            All negative bonuses become zero.
            Useful because it's always in the sum of the return,
            whether epic or not
            '''
            epic_bonus = max(0,round((creature_level-self.__MAX_STANDARD_LEVEL)/2.0)) 

            # This keeps the creature level between the minimum base level stat and no greater than 20,
            # for calculation purposes to add the epic bonuses in appropriately.
            creature_level = max(min(self.__MAX_STANDARD_LEVEL,int(creature_level)),self.__MIN_BASE_LEVEL) # Attack bonuses do not grow after
            #  20.

            if base_attack_bonus == ccs.BASEATTACKBONUS.POOR: # The base attack bonus for a 'poor' level bonuses
                temp_stack = [i for i in range(1,int(creature_level/2)+1)[::-5]] or [0]

            elif base_attack_bonus == ccs.BASEATTACKBONUS.AVERAGE: 
                temp_stack = [i for i in range(1,int((creature_level+1)*3/4)+1)[::-5]]

            elif base_attack_bonus == ccs.BASEATTACKBONUS.MONK: # base attack bonus for the special case of an unarmed monk
                temp_stack = [i for i in range(1,int((creature_level+1)*3/4)+1)[::-3]]


                '''
                temp_stack=sorted(list(set(list(set(sorted([3,6,9,12]+([i for i in range(0,16)]))[0:creature_level]))[
                ::-3])-set(
                    [i for i in range(0,int(creature_level>1))])))[::-1]
                # ^ This is insane, but it works.
                '''

            else: # The base attack bonus for a 'good' level bonus
                temp_stack = [i for i in range(1,creature_level+1)[::-5]]
                '''
                range(1,creature_level+1) is a list of all numbers 1 to creature_level, [::-5] starts at the
                end of the list (creature_level) and returns a number every five it can move backward in the list.
                creature_level : 7
                range(1,7+1) => range(1,8) = [1,2,3,4,5,6,7]
                range(1,8)[::-1] = [7,6,5,4,3,2,1] it starts at the end and moves back one listing; everything in reverse
                range(1,8)[::-2] = [7,  5,  3,  1]
                range(1,8)[::-3] = [7,    4,    1]
                range(1,8)[::-4] = [7,      3    ]
                range(1,8)[::-5] = [7,        2  ]
                range(1,8)[::-6] = [7,          1]
                So...
                range(1,20+1)[::-5] = [20,15,10,5]
                
                for i in range(0,int((creature_level-1)/5.0+1)):
                  temp_stack.append(creature_level-i*5)
                '''

            return [int(i+epic_bonus) for i in temp_stack] # Returns the attacks with appropriate epic bonuses added in.

        return self.get_base_attack_bonus(self.get_default_base_attack_bonus(),creature_level)



    def get_default_skill_set(self):
        return self.__DEFAULT_SKILL_SET

    def get_alignment_good_vs_evil(self,alignment=None):
        '''
        Returns the Good/Evil alignment constant
        '''

        try:
            alignment = int(alignment)
        except:
            alignment = self.get_default_alignment_good_vs_evil()

        if alignment <= self.__MAX_ALIGNMENT_EVIL:
            return ccs.ALIGNMENT.EVIL
        elif self.__MIN_ALIGNMENT_GOOD <= alignment:
            return ccs.ALIGNMENT.GOOD
        return ccs.ALIGNMENT.NEUTRALGvE

    def get_alignment_law_vs_chaos(self,alignment=None):
        '''
        Returns the law/chaos alignment constant
        '''
        try:
            alignment = int(alignment)
        except:
            alignment = self.get_default_alignment_law_vs_chaos()

        if alignment <= self.__MAX_ALIGNMENT_CHAOS:
            return ccs.ALIGNMENT.CHAOTIC
        elif self.__MIN_ALIGNMENT_LAW <= alignment:
            return ccs.ALIGNMENT.LAW
        return ccs.ALIGNMENT.NEUTRALLvC


    def get_alignment_constant(self, alignment_law_vs_chaos=None, alignment_good_vs_evil=None):
        '''
        Returns a ccs.ALIGNMENT constant for the specific alignment a creature has.
        
        get_alignment_constant(ccs.ALIGNMENT.LAWFUL, ccs.ALIGNMENT.GOOD)
        This is meant to take and LvC ccs.ALIGNMENT and a GvE ccs.ALIGNMENT and convert
        down to a single constant that can be used for passing information
        '''
        alignment_law_vs_chaos = ccs.ALIGNMENT.verify(alignment_law_vs_chaos)
        alignment_good_vs_evil = ccs.ALIGNMENT.verify(alignment_good_vs_evil)

        if alignment_law_vs_chaos in [ccs.ALIGNMENT.LAW, ccs.ALIGNMENT.NTL, ccs.ALIGNMENT.CHAOTIC] and \
        alignment_good_vs_evil in [ccs.ALIGNMENT.GOD, ccs.ALIGNMENT.NTG, ccs.ALIGNMENT.EVL]:
            return {ccs.ALIGNMENT.LAW: {ccs.ALIGNMENT.GOD:ccs.ALIGNMENT.LAG,
                                        ccs.ALIGNMENT.NTL:ccs.ALIGNMENT.LAN,
                                        ccs.ALIGNMENT.EVL:ccs.ALIGNMENT.LAE},
                    ccs.ALIGNMENT.NTL: {ccs.ALIGNMENT.GOD:ccs.ALIGNMENT.NEG,
                                        ccs.ALIGNMENT.NTL:ccs.ALIGNMENT.NEN,
                                        ccs.ALIGNMENT.EVL:ccs.ALIGNMENT.NEE},
                    ccs.ALIGNMENT.CHA: {ccs.ALIGNMENT.GOD:ccs.ALIGNMENT.CHG,
                                        ccs.ALIGNMENT.NTL:ccs.ALIGNMENT.CHN,
                                        ccs.ALIGNMENT.EVL:ccs.ALIGNMENT.CHE}}[alignment_law_vs_chaos][alignment_good_vs_evil]

        return self.get_alignment_constant(self.get_alignment_law_vs_chaos(self.get_default_alignment_law_vs_chaos()),self.get_alignment_good_vs_evil(self.get_default_alignment_good_vs_evil()))

    
    def get_alignment_list_from_constant(self, alignment=None):
        '''

        '''
        alignment = ccs.ALIGNMENT.verify(alignment)
        alignment_dict = {ccs.ALIGNMENT.LAG: [ccs.ALIGNMENT.LAWFUL, ccs.ALIGNMENT.GOOD],
                          ccs.ALIGNMENT.LAN: [ccs.ALIGNMENT.LAWFUL, ccs.ALIGNMENT.NEUTRALGvE], 
                          ccs.ALIGNMENT.LAE: [ccs.ALIGNMENT.LAWFUL, ccs.ALIGNMENT.EVIL], 
                          ccs.ALIGNMENT.NEG: [ccs.ALIGNMENT.NEUTRALLvC, ccs.ALIGNMENT.GOOD],
                          ccs.ALIGNMENT.NEN: [ccs.ALIGNMENT.NEUTRALLvC, ccs.ALIGNMENT.NEUTRALGvE], 
                          ccs.ALIGNMENT.NEE: [ccs.ALIGNMENT.NEUTRALLvC, ccs.ALIGNMENT.EVIL], 
                          ccs.ALIGNMENT.CHG: [ccs.ALIGNMENT.CHAOTIC, ccs.ALIGNMENT.GOOD],
                          ccs.ALIGNMENT.CHN: [ccs.ALIGNMENT.CHAOTIC, ccs.ALIGNMENT.NEUTRALGvE], 
                          ccs.ALIGNMENT.CHE: [ccs.ALIGNMENT.CHAOTIC, ccs.ALIGNMENT.EVIL]} 
        
 
        
        if alignment in alignment_dict:
            return alignment_dict[alignment]
            
        return self.get_alignment_list_from_constant(self.get_alignment_constant())




# a = core_creature_configuration()
