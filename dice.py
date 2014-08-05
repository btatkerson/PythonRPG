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
	# you could type d(6,2) which is the sum of two, six-side die rolls.

	def d(self,sides=20, occurances=1):
		temp = 0
		for i in range(0,occurances):
			temp += random.randint(1,sides)
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

a = dice()

for i in range(0,100):
	print a.d(30,20)