'''
	  Name: tree.py
	Author: Benjamin A
   Purpose: This is a class that manages tree structures of data

'''



class tree():
	def __init__(self,key='default',value=None):
		self.dictionary = {key:value}

		# These are the key generators for
		self.key_gen_child = ('child_'+str(i) for i in range(0,1000))
		self.key_gen_branch = ('branch_'+str(i) for i in range(0,1000))

	def add_child(self,key=None,value=None):
		if key==None:
			key = self.key_gen_child.next()
		self.dictionary[key]=value

	def add_branch(self,key='default'):
		self.dictionary[key]=tree()
