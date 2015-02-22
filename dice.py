'''
	  Name: dice.py
	Author: Benjamin A
   Purpose: generate random dice rolls
'''

#import os
import random

class dice():
	def __init__(self):
		None


	def d(self,sides=20, occurances=1):
		'''
		The main dice-roller, by default, it acts as a single throw of a d20. If you wanted to throw two d6 dice,
	  	you could type d(6,2) which returns a list consisting of 2 elements that are random values between 1 and 6.
		'''
		return [random.randint(1,sides) for i in range(0,occurances)]
	
	
	def str_d(self,die_str=None):
		'''
			Takes input in the form of a string such as "2d6" or "3 D 5"
			and parses it to return a list of die rolls

			Returns a d20 roll instead
		'''
		if die_str == None:
			return self.d(20)
		try:
			temp = [int(i) for i in die_str.lower().replace(" ","").split("d")]
			if len(temp) == 2:
				return self.d(temp[1],temp[0])
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

	def d100(self, occurances=1):
		'''
		Returns a roll of a d100, 1 occurance by default. This is the same as self.d(100,1)
		'''
		return self.d(100, occurances)

	def d20(self, occurances=1):
		return self.d(20, occurances)
	
	def d12(self, occurances=1):
		return self.d(12, occurances)

	def d10(self, occurances=1):
		return self.d(10, occurances)

	def d8(self, occurances=1):
		return self.d(8, occurances)

	def d6(self, occurances=1):
		return self.d(6, occurances)
	
	def d4(self, occurances=1):
		return self.d(4, occurances)

#a = dice()
#print(a.str_d("10d100"))
