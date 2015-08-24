
'''
      Name: __race_settings.py
    Author: Benjamin A
      Date: Jul 7, 2015
    
   Purpose: This holds basic settings that only technically affect the playable classes. When choosing
            which race to play as, certain races will affect how a character will play and progress.
            
            Two prime examples of racial effects that occur in common gameplay would be favored classes
            and ability bonuses. 

            Favored classes are used when determining XP penalties for multiclassing. If a class is favored,
            then a secondary class will not add a multiclass penalty. For humans and half-elves, the highest
            level class does not count against multiclassing since all classes are technically "favored"

            Ability bonuses are available for all player races (with the exception of humans and half-elves)
            A halfling gets a Str -2 and Dex +2 added to any checks

'''

import core.__core_constants_mod as ccs


class race_settings():
    def __init__(self, playable_race=None,favored_classes=None,favored_deities=None,size_class=None,ability_bonuses=None,base_land_speed=None):

        self.__playable_race=None
        self.set_playable_race(playable_race)
        
        self.__favored_classes=None
        self.set_favored_classes(favored_classes)

        # self.__favored_deities=favored_deities


        self.__size_class=None
        self.set_size_class(size_class)
        
        # self.base_land_speed=base_land_speed # Will not be used until future development, races all have a base land speed which determines how much far a creature can move in one round. This is not the only thing that will affect land speed.
        self.__ability_bonuses = {ccs.ABILITY.STR:0, 
                                ccs.ABILITY.INT:0, 
                                ccs.ABILITY.CON:0, 
                                ccs.ABILITY.WIS:0, 
                                ccs.ABILITY.DEX:0, 
                                ccs.ABILITY.CHR:0}

        self.set_ability_bonus_by_dictionary(ability_bonuses)



    def set_playable_race(self, playable_race):
        if playable_race:
            self.__playable_race = True
        else:
            self.__playable_race = False

    def get_playable_race(self):
        return self.__playable_race

    is_playable_race = get_playable_race

    def set_favored_classes(self,favored_classes):
        if type(favored_classes) == list:
            hold = []
            for i in favored_classes:
                temp = ccs.CREATURECLASS.verify(i)
                if temp:
                    hold.append(temp)
            self.__favored_classes = hold
            if hold != []:
                return True
           
            
        else:
            if ccs.CREATURECLASS.verify(favored_classes):
                self.__favored_classes = [ccs.CREATURECLASS.verify(favored_classes)]
                return True

        self.__favored_classes = []
        return False
                
    def get_favored_classes(self):
        return self.__favored_classes


    def get_size_class(self):
        return self.__size_class

    def set_size_class(self, size_class=None):
        if ccs.SIZECLASS.verify(size_class):
            self.__size_class = ccs.SIZECLASS.verify(size_class)
        else:
            self.__size_class = False

               
        

    def set_ability_bonuses(self,str=0,inte=0,con=0,wis=0,dex=0,chr=0,absolute=True):
        '''
        Set one, set all, set some, this is just to make the penalty/bonus dictionary simple to fill.
        Example - A dwarf class gets a racial bonus of +2 constitution, but a penalty of a -2 charisma
        This can be set by calling the function as so set_ability_bonus(con=2,chr=-2)
        '''
        if str or absolute:
            self.set_ability_bonus_single(ccs.ABILITY.STR,str,absolute)
        if inte or absolute:
            self.set_ability_bonus_single(ccs.ABILITY.INT,inte,absolute)
        if con or absolute:
            self.set_ability_bonus_single(ccs.ABILITY.CON,con,absolute)
        if wis or absolute:
            self.set_ability_bonus_single(ccs.ABILITY.WIS,wis,absolute)
        if dex or absolute:
            self.set_ability_bonus_single(ccs.ABILITY.DEX,dex,absolute)
        if chr or absolute:
            self.set_ability_bonus_single(ccs.ABILITY.CHR,chr,absolute)

    def set_ability_bonus_single(self,ability,add=0,absolute=False):
        '''
        Sets an individual ability at a time, can be used by itself or with "set_ability_bonuses"
        'absolute' == False adds variable 'add' to the ability given in the 'ability' parameter
        'absolute' == True sets the ability given in the 'ability' parameter to the value given in 'add', does not add to previous ability
        '''
        ability = ccs.ABILITY.verify(ability)
        if ability:
            if absolute:
                self.__ability_bonuses[ability] = add
            else:
                self.__ability_bonuses[ability] += add
            return self.__ability_bonuses[ability]
        else:
            return -1
    
    def set_ability_bonus_by_dictionary(self, ability_bonuses=None):
        if type(ability_bonuses) == dict:
            added = False # Tells if anything was affected by the input ability_bonuses
            for i in ccs.ABILITY.filter_list(list(ability_bonuses.keys())):
                added = True
                self.set_ability_bonus_single(i,ability_bonuses[i],True)
            if added:
                return 1

        return False



    def get_ability_bonus(self,ability=None):
        '''
        Returns ability bonus (ex. +2) for whichever ability given
        '''
        if ccs.ABILITY.verify(ability):
            return self.__ability_bonuses[ccs.ABILITY.verify(ability)]
        return False
    
    def get_ability_bonus_dictionary(self):
        '''
        Returns the ability bonus dictionary
        '''
        return self.__ability_bonuses
