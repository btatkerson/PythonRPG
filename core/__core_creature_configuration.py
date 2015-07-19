'''
      Name: __core_creature_configuration.py
   Purpose: This is a core file for the engine that defines the boundaries of the creatures in the game.
            It limits levels, defines EQUIPMENT slots available, etc.

'''
from core.__core_race_configuration import core_race_configuration
from core.__core_constants import core_constants

class core_creature_configuration(core_race_configuration):

    def __init__(self):
        core_race_configuration.__init__(self) # Inherits the core race configurations of the game, the creature configuration is highly involved with races

        self.ccs = core_constants()
        self.__DEFAULT_ABILITY = self.ccs.ABILITY.STR # strength
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
        self.__DEFAULT_CURRENT_HIT_POINTS = self.__DEFAULT_BASE_HIT_POINTS
        self.__MIN_CURRENT_HIT_POINTS = -10
        self.__MAX_CURRENT_HIT_POINTS = 10000
        self.__MIN_CHALLENGE_RATING = 0
        self.__MAX_CHALLENGE_RATING = 40
        self.__DEFAULT_CHALLENGE_RATING = 1
        self.__DEFAULT_DEITY = None         # <          TO-DO              >  
        self.__DEFAULT_EXPERIENCE = 0
        self.__MIN_EXPERIENCE = 0
        self.__MAX_EXPERIENCE = sum(range(self.__MIN_BASE_LEVEL,self.__MAX_BASE_LEVEL+1))
        self.__DEFAULT_BASE_LEVEL_RATE = 1000 # Each level costs 1000*base_level
        self.__DEFAULT_GOOD_VS_EVIL = 50 # Neutral
        self.__MIN_GOOD_VS_EVIL = 0
        self.__MAX_GOOD_VS_EVIL = 100
        self.__DEFAULT_LAW_VS_CHAOS = 50 # Neutral
        self.__MIN_LAW_VS_CHAOS = 0
        self.__MAX_LAW_VS_CHAOS = 100
        self.__DEFAULT_NAME = 'MissingName'
        self.__DEFAULT_PLAYABLE_CHARACTER = False
        self.__DEFAULT_RACE = self.ccs.CREATURERACE.HUMAN
        self.__DEFAULT_CREATURE_CLASS = self.ccs.CREATURECLASS.FIGHTER
        self.__DEFAULT_SAVING_THROW = self.ccs.SAVINGTHROW.FORTITUDE # fortitude
        self.__DEFAULT_BASE_ATTACK_BONUS = self.ccs.BASEATTACKBONUS.AVERAGE
        self.__DEFAULT_BASE_SAVE_BONUS = self.ccs.BASESAVEBONUS.GOOD

        self.__EQUIPMENT_SLOTS = {"helmet":None,"armor":None,"main_hand":None,"off_hand":None,"amulet":None,
                                   "ring_1":None,"ring_2":None,"gloves":None,"cloak":None,"boots":None,"belt":None}

        
        self.__CHALLENGE_RATING_LIST = []
        self.generate_challenge_rating_list()
        
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

    def get_default_base_level(self):
        return self.__DEFAULT_BASE_LEVEL

    def get_min_base_level(self):
        return self.__MIN_BASE_LEVEL

    def get_max_base_level(self):
        return self.__MAX_BASE_LEVEL

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

    def get_default_good_vs_evil(self):
        return self.__DEFAULT_GOOD_VS_EVIL

    def get_min_good_vs_evil(self):
        return self.__MIN_GOOD_VS_EVIL

    def get_max_good_vs_evil(self):
        return self.__MAX_GOOD_VS_EVIL

    def get_default_law_vs_chaos(self):
        return self.__DEFAULT_LAW_VS_CHAOS

    def get_min_law_vs_chaos(self):
        return self.__MIN_LAW_VS_CHAOS

    def get_max_law_vs_chaos(self):
        return self.__MAX_LAW_VS_CHAOS

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

    def get_base_save_bonus(self,base_save_bonus=None,creature_level=1):
        '''
        Returns a list of save bonuses for the 'poor', and 'good', base_save_bonus can be given as a value or the name value,
        creature_level is fairly self-explanatory
        0 : 'poor',
        1 : 'good'
        '''
        base_save_bonus = self.ccs.BASESAVEBONUS.verify(base_save_bonus)

        if base_save_bonus:
            epic_bonus = max(0,round((creature_level-21)/2.0)) # All negative bonuses become zero.

            creature_level = max(min(20,creature_level),self.__MIN_BASE_LEVEL) # 20 is the maximum level of bonus
            # growth excluding epic bonuses. This also keeps the level from being no lower than whatever the minimum
            # base level

            if base_save_bonus == self.ccs.BASESAVEBONUS.POOR: # The base save bonus for a 'poor' level bonuses
                return int(int(creature_level/3) + epic_bonus)

            else: # The base save bonus for a 'good' level bonus
                return int(2 + int(creature_level/2) + epic_bonus)

        return self.get_base_save_bonus(self.get_default_base_save_bonus(),creature_level)

    # Returns a list of attack bonuses for the 'poor', 'average', and 'good', if there are multiple attacks,
    # the sequential bonuses are provbase_save_bonused. base_save_bonus can be given as a value or the name value
    # 0 : 'poor',
    # 1 : 'average',
    # 2 : 'good'

    def get_default_base_attack_bonus(self):
        return self.__DEFAULT_BASE_ATTACK_BONUS

    def get_base_attack_bonus(self,base_attack_bonus=None,creature_level=1):
        base_attack_bonus = self.ccs.BASEATTACKBONUS.verify(base_attack_bonus)
        

        if base_attack_bonus:
            print(base_attack_bonus)
            temp_stack = []

            '''
            All negative bonuses become zero.
            Useful because it's always in the sum of the return,
            whether epic or not
            '''
            epic_bonus = max(0,round((creature_level-20)/2.0)) 

            # This keeps the creature level between the minimum base level stat and no greater than 20,
            # for calculation purposes to add the epic bonuses in appropriately.
            creature_level = max(min(20,int(creature_level)),self.__MIN_BASE_LEVEL) # Attack bonuses do not grow after
            #  20.

            if base_attack_bonus == self.ccs.BASEATTACKBONUS.POOR: # The base attack bonus for a 'poor' level bonuses
                temp_stack = [i for i in range(1,int(creature_level/2)+1)][::-5] or [0]

            elif base_attack_bonus == self.ccs.BASEATTACKBONUS.AVERAGE: 
                '''
                 base attack bonus for 'average' level
                temp_stack=sorted(list(set(list(set(sorted([3,6,9,12]+(range(0,16)))[0:creature_level]))[::-5])-set(
                 [i for i in range(0,int(creature_level>1))])))[::-1]
                 ^ This is too insane be more efficient than:
                '''
                for i in range(0,int((creature_level-1)/7.0+1)):
                    temp_stack.append(creature_level-int((creature_level-1)/4)-1-i*5)

            elif base_attack_bonus == self.ccs.BASEATTACKBONUS.MONK: # base attack bonus for the special case of an unarmed monk
                temp_stack=sorted(list(set(list(set(sorted([3,6,9,12]+([i for i in range(0,16)]))[0:creature_level]))[
                ::-3])-set(
                    [i for i in range(0,int(creature_level>1))])))[::-1]
                # ^ This is insane, but it works.

                # for i in range(0,max(1,int((creature_level+4)/4))):
                #   temp_stack.append(creature_level-(creature_level-1)/4-1-i*3)

            else: # The base attack bonus for a 'good' level bonus
                temp_stack = range(1,creature_level+1)[::-5]
                # range(1,creature_level+1) is a list of all numbers 1 to creature_level, [::-5] starts at the
                # end of the list (creature_level) and returns a number every five it can move backward in the list.
                # creature_level : 7
                # range(1,7+1) => range(1,8) = [1,2,3,4,5,6,7]
                # range(1,8)[::-1] = [7,6,5,4,3,2,1] it starts at the end and moves back one listing; everything in reverse
                # range(1,8)[::-2] = [7,  5,  3,  1]
                # range(1,8)[::-3] = [7,    4,    1]
                # range(1,8)[::-4] = [7,      3    ]
                # range(1,8)[::-5] = [7,        2  ]
                # range(1,8)[::-6] = [7,          1]
                # So...
                # # range(1,20+1)[::-5] = [20,15,10,5]
                
                # for i in range(0,int((creature_level-1)/5.0+1)):
                #   temp_stack.append(creature_level-i*5)

            return [int(i+epic_bonus) for i in temp_stack] # Returns the attacks with appropriate epic bonuses added in.

        return self.get_base_attack_bonus(self.get_default_base_attack_bonus(),creature_level)



    def get_default_skill_set(self):
        return self.__DEFAULT_SKILL_SET


# a = core_creature_configuration()
#
# for i in range(1,61):
#   print( i,a.get_base_save_bonus(1,i))#,a.get_base_attack_bonus(1,i),a.get_base_attack_bonus(0,i)
