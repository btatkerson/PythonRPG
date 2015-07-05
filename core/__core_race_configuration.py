'''
      Name: __core_race_configuration.py
    Author: Benjamin A
   Purpose: This is a core file for the engine that defines the boundaries of the races in the game.
            It limits race types and offers methods that provides information on the core components of races

'''

from core.__core_constants import core_constants



class core_race_configuration(core_constants):
    def __init__(self):
        core_constants.__init__(self)

        '''

         The size classes by name, occupying space in feet, and natural reach in feet. These are standard, but exceptions can be made
         to the the default reach distance and occupying space if necessary
         [name, space_in_feet, natural reach distance in feet, size_modifier]

        '''
        self.__size_classes = [[self.SIZECLASS.UNIQUE, 0, 0, 0],
                               [self.SIZECLASS.FINE, .5, 0, 8],
                               [self.SIZECLASS.DIMINUTIVE, 1, 0, 4],
                               [self.SIZECLASS.TINY, 2.5, 0, 2],
                               [self.SIZECLASS.SMALL, 5, 5, 1],
                               [self.SIZECLASS.MEDIUM, 5, 5, 0],
                               [self.SIZECLASS.LARGE_TALL, 10, 10, -1],
                               [self.SIZECLASS.LARGE_LONG, 10, 5, -1],
                               [self.SIZECLASS.HUGE_TALL, 15, 15, -2],
                               [self.SIZECLASS.HUGE_LONG, 15, 10, -2],
                               [self.SIZECLASS.GARGANTUAN_TALL, 20, 20, -4],
                               [self.SIZECLASS.GARGANTUAN_LONG, 20, 15, -4],
                               [self.SIZECLASS.COLOSSAL_TALL, 30, 30, -8],
                               [self.SIZECLASS.COLOSSAL_LONG, 30, 20, -8]]

        self.__DEFAULT_RACE_TYPE = 0 # Unique race type
        self.__DEFAULT_SIZE_CLASS_ID = 5 # Medium size class




        self.__DEFAULT_SIZE_CLASS_NAME = self.get_size_class_list()[self.get_default_size_class_id()][0]

        #
        self.__core_race_list = [self.__race_settings(name=self.__race_type_list[1],playable_race=True,size_class=self.get_size_class_list()[5]),
                                self.__race_settings(name=self.__race_type_list[2],playable_race=True,size_class=self.get_size_class_list()[5]),
                                self.__race_settings(name=self.__race_type_list[3],playable_race=True,size_class=self.get_size_class_list()[5]),
                                self.__race_settings(name=self.__race_type_list[4],playable_race=True,size_class=self.get_size_class_list()[4]),
                                self.__race_settings(name=self.__race_type_list[5],playable_race=True,size_class=self.get_size_class_list()[5]),
                                self.__race_settings(name=self.__race_type_list[6],playable_race=True,size_class=self.get_size_class_list()[4]),
                                self.__race_settings(name=self.__race_type_list[7],playable_race=True,size_class=self.get_size_class_list()[5])]

    def get_default_race_type(self):
        return self.__DEFAULT_RACE_TYPE

    def get_default_size_class_id(self):
        return self.__DEFAULT_SIZE_CLASS_ID
    
    def get_default_size_class_name(self):
        return self.__DEFAULT_SIZE_CLASS_NAME

    def get_race_type_name_by_value(self,race_type=0):
        if race_type in self.get_race_type_list():
            return self.get_race_type_list()[race_type]
        else:
            return self.get_race_type_list()[0]

    def get_race_type_value_by_name(self,race_type):
        if race_type in self.get_race_type_list()[race_type]:
            return self.get_race_type_list().index(race_type)

    def get_race_type_list(self):
        return self.CREATURERACE.get_index()

    def get_size_class_list(self):
        return self.__size_classes

    # Returns class size attributes by name, return_class_id=True returns the index on the size_class list, which is the ID
    def get_size_class_by_name(self, name=None, return_class_id=False):
        if name == None:
            name = self.get_default_size_class_name()

        if name in ['large','huge','gargantuan','colossal']:
            name += '_tall'

        # If there are size classes with a "tall" or "long", default will be "tall" if not specified.
        # For instance, "large_tall" and "large_long" are both valid for variable "name", but if name were to equal 'large',
        # 'large_tall' will be returned
        for i in range(0,len(self.get_size_class_list())):
            if name.lower() in self.get_size_class_list()[i]:
                if return_class_id:
                    return i
                else:
                    return self.get_size_class_list()[i]
                
        # If name wasn't found, the 'unique' size is returned
        if return_class_id:
            return 0
        else:
            return self.get_size_class_list()[0]
        
    # Returns class size by id  
    def get_size_class_by_id(self,id=None):
        if id < 0 or id >= len(self.get_size_class_list()) or id == None:
            id = self.get_default_size_class_id()

        return self.get_size_class_list()[id]

    # Returns size modifier by name.
    def get_size_modifier_by_name(self,name=None):
        return self.get_size_class_by_name(name)[3]

    # Returns the size modifier by the id
    def get_size_modifier_by_id(self,id=None):
        return self.get_size_class_by_id(id)[3]

    # Subclass of __core_race_configuration that structures race benefits and penalties and other things associated with
    # that particular race
    class __race_settings():
        def __init__(self,name,playable_race=False,favored_classes=[],favored_deities=[],size_class='',base_land_speed=None):
            self.CORECON = core_constants()
            self.race_name=name
            self.playable_race=playable_race
            self.favored_classes=favored_classes
            self.favored_deities=favored_deities
            self.size_class=size_class
            # self.base_land_speed=base_land_speed # Will not be used until future development, races all have a base land speed which determines how much far a creature can move in one round. This is not the only thing that will affect land speed.
            self.ability_bonuses = {self.CORECON.ABILITY.STR:0, 
                                    self.CORECON.ABILITY.INT:0, 
                                    self.CORECON.ABILITY.CON:0, 
                                    self.CORECON.ABILITY.WIS:0, 
                                    self.CORECON.ABILITY.DEX:0, 
                                    self.CORECON.ABILITY.CHR:0,
                                    self.CORECON.SAVINGTHROW.FOR:0,
                                    self.CORECON.SAVINGTHROW.REF:0,
                                    self.CORECON.SAVINGTHROW.WIL:0}

        # Set one, set all, set some, this is just to make the penalty/bonus dictionary simple to fill.
        # Example - A dwarf class gets a racial bonus of +2 constitution, but a penalty of a -2 charisma
        # This can be set by calling the function as so set_ability_bonus(con=2,chr=-2)
        def set_ability_bonuses(self,str=0,inte=0,con=0,wis=0,dex=0,chr=0,fortitude=0,reflex=0,will=0,absolute=True):
            if str or absolute:
                self.set_ability_bonus_single(self.CORECON.ABILITY.STR,str,absolute)
            if inte or absolute:
                self.set_ability_bonus_single(self.CORECON.ABILITY.INT,inte,absolute)
            if con or absolute:
                self.set_ability_bonus_single(self.CORECON.ABILITY.CON,con,absolute)
            if wis or absolute:
                self.set_ability_bonus_single(self.CORECON.ABILITY.WIS,wis,absolute)
            if dex or absolute:
                self.set_ability_bonus_single(self.CORECON.ABILITY.DEX,dex,absolute)
            if chr or absolute:
                self.set_ability_bonus_single(self.CORECON.ABILITY.CHR,chr,absolute)
            if fortitude or absolute:
                self.set_ability_bonus_single(self.CORECON.SAVINGTHROW.FOR,fortitude,absolute)
            if reflex or absolute:
                self.set_ability_bonus_single(self.CORECON.SAVINGTHROW.REF,reflex,absolute)
            if will or absolute:
                self.set_ability_bonus_single(self.CORECON.SAVINGTHROW.WIL,will,absolute)

        # Sets an individual ability at a time, can be used by itself or with "set_ability_bonuses"
        # 'absolute' == False adds variable 'add' to the ability given in the 'ability' parameter
        # 'absolute' == True sets the ability given in the 'ability' parameter to the value given in 'add', does not add to previous ability
        def set_ability_bonus_single(self,ability,add=0,absolute=False):
            if ability.lower() in self.ability_bonuses:
                if absolute:
                    self.ability_bonuses[ability] = add
                else:
                    self.ability_bonuses[ability] += add
                return self.ability_bonuses[ability]
            else:
                return -1

        # Temporarily here unless it ultimately goes unused, this is supposed to allow copying of ability bonuses and resetting them. Possibly
        # I... I don't think this is needed, but I should have thought about that before writing it. It wasn't a waste of YOUR time.
        def get_ability_bonus_dictionary(self):
            return self.ability_bonuses



