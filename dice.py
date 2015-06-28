'''
	  Name: dice.py
	Author: Benjamin A
       Purpose: generate random dice rolls
'''

#import os
import random

class dice():
        def __init__(self,default_sides=20,default_occurances=1):
                self.def_occur = None
                self.def_sides = None
                self.setDefaultSides(default_sides) # This affects only self.d()
                self.setDefaultOccurances(default_occurances) # This affects all class roll methods

        def __call__(self,sides=None,occurances=None,return_average=False):
            '''
            This will return a dice roll of default sides and default amount of rolls
            simply by calling the instance as a functor.

            If default sides = 20 and default rolls = 1
            a = dice.dice()
            
            a.d() returns the default roll (1d20)
            a() would give the same result
            '''
            return self.d(sides,occurances,return_average)

        def setDefaultSides(self,num=None):
                '''
                Sets default sides for d() method
                '''
                if not num or type(num) != int or num < 1:
                        print('Not a valid side count')
                        if not self.def_sides:
                                print('Setting default side count to 20')
                                self.def_sides = 20
                else:
                        print('Default sides now set to',num)
                        self.def_sides = num

        def setDefaultOccurances(self,num=None):
                '''
                Sets default occurances for all die roll methods 
                '''
                if not num or type(num) != int or num < 1:
                        print('Not a valid amount of occurances')
                        if not self.def_occur:
                                print('Setting default amount of occurances to 1')
                                self.def_occur = 1
                else:
                        print('Default occurances now set to',num)
                        self.def_occur = num

        def d(self,sides=None, occurances=None, return_average=False):
                '''
		The main dice-roller, by default, it acts as a single throw of a d20 (or your initializer defaults). If you wanted to throw two d6 dice,
	  	you could type d(6,2) which returns a list consisting of 2 elements that are random values between 1 and 6.

                return_average returns a list filled with only the average value of the die filling the list "occurances" number of times. Useful for leveling purposes if trying to offer balance versus rolling dice for point increases.
		'''
                if not sides or type(sides) != int or sides < 0:
                        sides = self.def_sides
                if not occurances or type(occurances) != int or occurances < 0:
                        occurances = self.def_occur
                if return_average:
                    return [(sides+1)/2 for i in range(occurances)]
                return [random.randint(1,sides) for i in range(occurances)]
	
	
        def str_d(self,die_str=None,return_average=False):
                '''
			Takes input in the form of a string such as "2d6" (A six-sided die rolled twice) or "3 D 5"
			and parses it to return a list of die rolls

			Returns a default roll instead
		'''
                if die_str == None:
                        return self.d()
                try:
                        temp = [int(i) for i in die_str.lower().replace(" ","").split("d")]
                        if len(temp) == 2:
                                return self.d(temp[1],temp[0],return_average)
                        else:
                                raise ValueError
                except ValueError:
                        '''
                        Is triggered when either when the list is being generated and int(i) does
                        not have a number for i

			or

			If the length of the list is not 2 (which is the "3" and "5" in "3d5")
			'''
                        print("Input was invalid, returned 0")
                        return 0

        def d100(self, occurances=None, return_average=False):
                '''
                Returns a roll of a d100, 1 occurance by default. This is the same as self.d(100,1)
		'''
                return self.d(100, occurances, return_average)

        def d20(self, occurances=None, return_average=False):
                return self.d(20, occurances, return_average)
	
        def d12(self, occurances=None, return_average=False):
                return self.d(12, occurances, return_average)

        def d10(self, occurances=None, return_average=False):
                return self.d(10, occurances, return_average)

        def d8(self, occurances=None, return_average=False):
                return self.d(8, occurances, return_average)

        def d6(self, occurances=None, return_average=False):
                return self.d(6, occurances, return_average)
	
        def d4(self, occurances=None, return_average=False):
                return self.d(4, occurances, return_average)
