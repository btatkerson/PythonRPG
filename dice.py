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

	# The main dice-roller, by default, it acts as a single throw of a d20. If you wanted to throw two d6 dice,
	# you could type d(6,2) which returns a list consisting of 2 elements that are random values between 1 and 6.

	def d(self,sides=20, occurances=1):
		temp = []
		for i in range(0,occurances):
			temp.append(random.randint(1,sides))
		return temp

	def d100(self, occurances=1):
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

# a = dice()
#
# print a.d(20,10)