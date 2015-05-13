'''
      Name: __core_creature_configuration.py
   Purpose: This is a core file for the engine that defines the boundaries of the creatures in the game.
            It limits levels, defines EQUIPMENT slots available, etc.

'''
from core.__core_race_configuration import core_race_configuration
from core.__core_constants import core_constants

class core_creature_configuration(core_constants, core_race_configuration):

    def __init__(self):
        core_constants.__init__(self)
        core_race_configuration.__init__(self) # Inherits the core race configurations of the game, the creature configuration is highly involved with races
        self.__DEFAULT_ABILITY = 0 # strength
        self.__ABILITY_LIST_SHORT = [self.ABILITY.STR, self.ABILITY.INT, self.ABILITY.CON, self.ABILITY.WIS, self.ABILITY.DEX, self.ABILITY.CHR]
        self.__ABILITY_LIST = ['strength', 'intelligence', 'constitution', 'wisdom', 'dexterity', 'charisma']
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
        self.__DEFAULT_RACE = self.CREATURERACE.HUMAN
        self.__DEFAULT_CREATURE_CLASS = self.CREATURECLASS.FIGHTER
        self.__DEFAULT_SAVING_THROW = 0 # fortitude
        self.__SAVING_THROW_LIST = ['fortitude','reflex','will']
        self.__SAVING_THROW_LIST_SHORT = [self.SAVINGTHROW.FORTITUDE,self.SAVINGTHROW.REFLEX,self.SAVINGTHROW.WILL]
        self.__BASE_ATTACK_BONUS = [self.BASEATTACKBONUS.POOR,self.BASEATTACKBONUS.AVERAGE,self.BASEATTACKBONUS.GOOD,self.BASEATTACKBONUS.MONK]
        self.__BASE_SAVE_BONUS = [self.BASESAVEBONUS.POOR,self.BASESAVEBONUS.GOOD]
        self.__DEFAULT_BASE_ATTACK_BONUS = 0
        self.__DEFAULT_BASE_SAVE_BONUS = 0

        self.__EQUIPMENT_SLOTS = {"helmet":None,"armor":None,"main_hand":None,"off_hand":None,"amulet":None,
                                   "ring_1":None,"ring_2":None,"gloves":None,"cloak":None,"boots":None,"belt":None}

        
        self.__CHALLENGE_RATING_LIST = [self.__class_table_row_gen(1,[200,180,170,70,70,70,70,70]),
                                        self.__class_table_row_gen(1,[500,480,420,260,230,190,170,140,52]),
                                        self.__class_table_row_gen(1,[960,900,750,420,330,280,230,190,112,52]),
                                        self.__class_table_row_gen(1,[1440,1370,1200,630,530,420,330,280,230,190,112,52]),
                                        self.__class_table_row_gen(1,[2520,1920,1770,1050,770,630,530,400,330,260,165,127,48]),
                                        self.__class_table_row_gen(1,[3000,3150,2400,1520,1260,910,740,540,330,247,192,123,48]),
                                        self.__class_table_row_gen(1,[3000,4000,3780,2020,1810,1470,1050,840,450,367,254,185,137,48]),
                                        self.__class_table_row_gen(1,[3000,4000,5000,3090,2350,2090,1680,1190,712,502,371,247,206,144,42]),
                                        self.__class_table_row_gen(1,[3000,4000,5000,3850,3530,2690,2370,1890,1005,787,509,378,268,220,138,42]),
                                        self.__class_table_row_gen(1,[3000,4000,5000,3850,4200,3970,3020,2660,1575,1110,798,509,413,296,210,150,42,42]),
                                        self.__class_table_row_gen(1,[3000,4000,5000,3850,4200,4900,4410,3360,2205,1732,1115,771,550,443,276,228,156,84,42,42]),
                                        self.__class_table_row_gen(1,[3000,4000,5000,3850,4200,4900,5600,4850,2775,2415,1735,1087,846,585,408,300,234,162,84,84]),
                                        self.__class_table_row_gen(1,[3000,4000,5000,3850,4200,4900,5600,5950,3967,3022,2416,1686,1204,915,552,438,318,252,174,126]),
                                        self.__class_table_row_gen(1,[3000,4000,5000,3850,4200,4900,5600,5950,4725,4297,3008,2361,1831,1253,864,588,462,336,264,186,40]),
                                        self.__class_table_row_gen(1,[3000,4000,5000,3850,4200,4900,5600,5950,4725,5250,4096,2939,2554,1955,1176,906,630,492,354,288,200,40]),
                                        self.__class_table_row_gen(1,[3000,4000,5000,3850,4200,4900,5600,5950,4725,5250,4819,4268,3084,2650,1806,1260,948,672,504,378,300,250,40]),
                                        self.__class_table_row_gen(1,[3000,4000,5000,3850,4200,4900,5600,5950,4725,5250,4819,4819,4337,3325,2520,1932,1326,1050,714,558,450,350,300,40]),
                                        self.__class_table_row_gen(1,[3000,4000,5000,3850,4200,4900,5600,5950,4725,5250,4819,4819,4819,4378,3066,2646,2058,1428,1050,738,500,450,400,300,40]),
                                        self.__class_table_row_gen(1,[3000,4000,5000,3850,4200,4900,5600,5950,4725,5250,4819,4819,4819,4819,3990,3276,2838,2184,1470,1134,1000,800,600,400,200,40]),
                                        self.__class_table_row_gen(1,[3000,4000,5000,3850,4200,4900,5600,5950,4725,5250,4819,4819,4819,4819,4200,4200,3402,2982,2268,1596,1250,1000,800,600,400,200,40]),
                                        self.__class_table_row_gen(1,[3000,4000,5000,3850,4200,4900,5600,5950,4725,5250,4819,4819,4819,4819,4200,4200,4032,3468,2646,2352,1750,1500,1250,1000,500,400,200,40]),
                                        self.__class_table_row_gen(17,[6000,5000,4000,3000,2250,2000,1750,1500,1250,1000,750,50,40]),
                                        self.__class_table_row_gen(17,[6000,5000,4000,3000,2750,2500,2250,2000,1750,1500,1250,1000,750,40]),
                                        self.__class_table_row_gen(17,[6000,5000,5000,4000,3250,3000,2750,2500,2250,2000,1750,1500,1250,1000,40]),
                                        self.__class_table_row_gen(17,[6000,5000,5000,4000,3750,3500,3250,3000,2750,2500,2250,2000,1750,1500,1000,40]),
                                        self.__class_table_row_gen(18,[6000,5000,5000,4250,4000,3750,3500,3250,3000,2750,2500,2250,2000,1500,1000,40]),
                                        self.__class_table_row_gen(19,[6000,5000,4750,4500,4250,4000,3750,3500,3250,3000,2750,2500,2000,1500,1000,40]),
                                        self.__class_table_row_gen(20,[6000,5250,5000,4750,4500,4250,4000,3750,3500,3250,3000,2500,2000,1500,1000,40]),
                                        self.__class_table_row_gen(20,[6000,5750,5500,5250,5000,4750,4500,4250,4000,3750,3500,3000,2500,2000,1500,1000,40]),
                                        self.__class_table_row_gen(21,[6000,5750,5500,5250,5000,4750,4500,4250,4000,3750,3500,3000,2500,2000,1500,1000,40]),
                                        self.__class_table_row_gen(22,[6000,5750,5500,5250,5000,4750,4500,4250,4000,3750,3500,3000,2500,2000,1500,1000,40]),
                                        self.__class_table_row_gen(23,[6000,5750,5500,5250,5000,4750,4500,4250,4000,3750,3500,3000,2500,2000,1500,1000,40]),
                                        self.__class_table_row_gen(24,[6000,5750,5500,5250,5000,4750,4500,4250,4000,3750,3500,3000,2500,2000,1500,1000,40]),
                                        self.__class_table_row_gen(25,[6000,5750,5500,5250,5000,4750,4500,4250,4000,3750,3500,3000,2500,2000,1500,1000]),
                                        self.__class_table_row_gen(26,[6000,5750,5500,5250,5000,4750,4500,4250,4000,3750,3500,3000,2500,2000,1500]),
                                        self.__class_table_row_gen(27,[6000,5750,5500,5250,5000,4750,4500,4250,4000,3750,3500,3000,2500,2000]),
                                        self.__class_table_row_gen(28,[6000,5750,5500,5250,5000,4750,4500,4250,4000,3750,3500,3000,2500]),
                                        self.__class_table_row_gen(29,[6000,5750,5500,5250,5000,4750,4500,4250,4000,3750,3500,3000]),
                                        self.__class_table_row_gen(30,[6000,5750,5500,5250,5000,4750,4500,4250,4000,3750,3500]),
                                        self.__class_table_row_gen(31,[6000,5750,5500,5250,5000,4750,4500,4250,4000,3750]),
                                        self.__class_table_row_gen(32,[6000,5750,5500,5250,5000,4750,4500,4250,4000])]


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

    def __class_table_row_gen(self,init_level=None, init_list=None):
        '''
        Generates a list for challenge ratings where init level is the first level the 'init_list' 
        begins on and fills in zeroes after level exceeds challenge rating max.

        '''
        if not init_level or not init_list:
            return []
        return [init_list[0] for i in range(0,init_level-1)]+init_list+[0 for i in range(0,40-(init_level+len(init_list)-1))]

    def get_challenge_rating_table(self):
        return self.__CHALLENGE_RATING_LIST


    def get_rewarded_experience_by_challenge_rating(self,challenge_rating=None):
        if challenge_rating == None:
            challenge_rating = self.__DEFAULT_CHALLENGE_RATING

        if 0 < challenge_rating < 1:
            return [int(i*challenge_rating) for i in self.__CHALLENGE_RATING_LIST[0]]

        challenge_rating = min(max(int(challenge_rating),self.__MIN_CHALLENGE_RATING),self.__MAX_CHALLENGE_RATING)

        return self.__CHALLENGE_RATING_LIST[challenge_rating]

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

    def get_ability_list(self):
        return self.__ABILITY_LIST

    def get_ability_list_short(self):
        return self.__ABILITY_LIST_SHORT

    def get_saving_throw_list(self):
        return self.__SAVING_THROW_LIST

    def get_saving_throw_list_short(self):
        return self.__SAVING_THROW_LIST_SHORT

    def is_saving_throw(self,saving_throw=None):
        if 0 <= saving_throw < len(self.__SAVING_THROW_LIST) or saving_throw in self.__SAVING_THROW_LIST or \
                saving_throw in self.__SAVING_THROW_LIST_SHORT:
            return True
        return False

    # Returns the short name of the saving throw. This is based on input. Defaults to fortitude
    def validate_saving_throw(self,saving_throw=None):
        if self.is_saving_throw(saving_throw):
            if 0 <= saving_throw < len(self.__SAVING_THROW_LIST):
                return self.__SAVING_THROW_LIST_SHORT[saving_throw]
            elif saving_throw.lower() in self.__SAVING_THROW_LIST_SHORT:
                return saving_throw.lower()
            else:
                return self.__SAVING_THROW_LIST_SHORT[self.__SAVING_THROW_LIST.index(saving_throw.lower())]
        return self.__SAVING_THROW_LIST_SHORT[self.__DEFAULT_SAVING_THROW]

    def get_default_base_ability_score(self):
        return self.__DEFAULT_BASE_ABILITY_SCORE

    def get_default_ability(self):
        return self.__DEFAULT_ABILITY

    def is_ability(self,ability=None):
        if ability == None:
            return False
        if type(ability) == int:
            if 0<= ability < len(self.__ABILITY_LIST):
                return True
        elif ability.lower() in self.__ABILITY_LIST_SHORT or ability.lower() \
                in self.__ABILITY_LIST:
            return True
        return False

    # Returns the short name for the input 'ability'. Used for consistency purposes. This way, typing 'strength'
    # where the creature ability keys are shorthand ('strength' == self.ABILITY.STR), validate_ability is placed to assure
    # everything is called properly. Defaults to strength
    def validate_ability(self,ability=None):
        if self.is_ability(ability):

            if type(ability) == int:
                if 0 <= ability < len(self.__ABILITY_LIST):
                    return self.get_ability_list_short()[ability]
            elif ability.lower() in self.__ABILITY_LIST_SHORT:
                return ability.lower()
            else:
                return self.__ABILITY_LIST_SHORT[self.__ABILITY_LIST.index(ability.lower())]
        return self.get_ability_list_short()[self.get_default_ability()]

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

    def get_base_save_bonus_name_by_id(self,id=None):
        if id is None:
            id = self.__BASE_SAVE_BONUS

        if 0 <= id < len(self.__BASE_SAVE_BONUS):
            return self.__BASE_SAVE_BONUS[id]
        return self.__BASE_SAVE_BONUS[self.__DEFAULT_BASE_SAVE_BONUS]

    def get_base_save_bonus_id_by_name(self,name=None):
        if name is None:
            name = self.get_base_save_bonus_name_by_id(self.__DEFAULT_BASE_SAVE_BONUS)

        if name.lower() in self.__BASE_SAVE_BONUS:
            return list.index(self.__BASE_SAVE_BONUS,name.lower())
        return self.__DEFAULT_BASE_SAVE_BONUS

    # Returns a list of save bonuses for the 'poor', and 'good', id can be given as a value or the name value,
    # creature_level is fairly self-explanatory
    # 0 : 'poor',
    # 1 : 'good'
    def get_base_save_bonus(self,id=None,creature_level=1):
        if id is None:
            id = self.__DEFAULT_BASE_SAVE_BONUS

        if type(id) == str: # Turns a string-type 'id' into its numeric index
            if id.lower() in self.__BASE_SAVE_BONUS:
                id = list.index(self.__BASE_SAVE_BONUS,id.lower())

        if 0 <= id < len(self.__BASE_SAVE_BONUS):
            epic_bonus = max(0,round((creature_level-21)/2.0)) # All negative bonuses become zero.

            creature_level = max(min(20,creature_level),self.__MIN_BASE_LEVEL) # 20 is the maximum level of bonus
            # growth excluding epic bonuses. This also keeps the level from being no lower than whatever the minimum
            # base level

            if id == 0: # The base save bonus for a 'poor' level bonuses
                return int(int(creature_level/3) + epic_bonus)
            else: # The base save bonus for a 'good' level bonus
                return int(2 + int(creature_level/2) + epic_bonus)

        return 0

    def get_base_attack_bonus_name_by_id(self,id=None):
        if id is None:
            id = self.__BASE_ATTACK_BONUS

        if 0 <= id < len(self.__BASE_ATTACK_BONUS):
            return self.__BASE_ATTACK_BONUS[id]
        return self.__BASE_ATTACK_BONUS[self.__DEFAULT_BASE_ATTACK_BONUS]

    def get_base_attack_bonus_id_by_name(self,name=None):
        if name is None:
            name = self.get_base_attack_bonus_name_by_id(self.__DEFAULT_BASE_ATTACK_BONUS)

        if name in self.__BASE_ATTACK_BONUS:
            return list.index(self.__BASE_ATTACK_BONUS,name)
        return self.__DEFAULT_BASE_ATTACK_BONUS

    # Returns a list of attack bonuses for the 'poor', 'average', and 'good', if there are multiple attacks,
    # the sequential bonuses are provided. id can be given as a value or the name value
    # 0 : 'poor',
    # 1 : 'average',
    # 2 : 'good'
    def get_base_attack_bonus(self,id=None,creature_level=1):
        if id is None:
            id = self.__DEFAULT_BASE_ATTACK_BONUS

        if type(id) == str:
            if id.lower() in self.__BASE_ATTACK_BONUS:
                id = list.index(self.__BASE_ATTACK_BONUS,id.lower())

        if 0 <= id < len(self.__BASE_ATTACK_BONUS):
            temp_stack = []

            epic_bonus = max(0,round((creature_level-20)/2.0)) # All negative bonuses become zero.

            # This keeps the creature level between the minimum base level stat and no greater than 20,
            # for calculation purposes to add the epic bonuses in appropriately.
            creature_level = max(min(20,int(creature_level)),self.__MIN_BASE_LEVEL) # Attack bonuses do not grow after
            #  20.

            if id == 0: # The base attack bonus for a 'poor' level bonuses
                temp_stack = [i for i in range(1,int(creature_level/2)+1)][::-5] or [0]


            elif id == 1: # base attack bonus for 'average' level
                #temp_stack=sorted(list(set(list(set(sorted([3,6,9,12]+(range(0,16)))[0:creature_level]))[::-5])-set(
                # [i for i in range(0,int(creature_level>1))])))[::-1]
                # ^ This is too insane be more efficient than:
                for i in range(0,int((creature_level-1)/7.0+1)):
                    temp_stack.append(creature_level-int((creature_level-1)/4)-1-i*5)


            elif id == 3: # base attack bonus for the special case of an unarmed monk
                temp_stack=sorted(list(set(list(set(sorted([3,6,9,12]+([i for i in range(0,16)]))[0:creature_level]))[
                ::-3])-set(
                    [i for i in range(0,int(creature_level>1))])))[::-1]
                # ^ This is insane, but it works.

                # for i in range(0,max(1,int((creature_level+4)/4))):
                #   temp_stack.append(creature_level-(creature_level-1)/4-1-i*3)



            else: # The base save bonus for a 'good' level bonus
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

        return [0]

    def get_default_skill_set(self):
        return self.__DEFAULT_SKILL_SET


# a = core_creature_configuration()
#
# for i in range(1,61):
#   print( i,a.get_base_save_bonus(1,i))#,a.get_base_attack_bonus(1,i),a.get_base_attack_bonus(0,i)
