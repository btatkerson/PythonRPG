'''
	  Name: verbose.py
	Author: Benjamin A
   Purpose: Allows verbosity control that is easily implemented/inherited into classes,
'''

class verbose():
	def __init__(self,active=False):
		self.activated = active

	# Toggles the global verbosity for the class by default OR sets global verbosity to input 'active'
	def verbo_toggle(self,active=None):
		if active == None:
			if self.activated:
				self.activated = False
			else:
				self.activated = True
		else:
			self.activated = active

	# Returns verbosity activation status
	def verbo_isActivated(self):
		if self.activated:
			return True
		return False

	# Activates global verbosity for class
	def verbo_Activate(self):
		self.activated = True
	# Deactivates global verbosity for class
	def verbo_Deactivate(self):
		self.activated = False

	# Prints input 'statement' if input 'override' is True OR attribute 'self.activated' is True.
	def verbo(self,statement=None,override=False):
		if override or self.verbo_isActivated():
			print statement



