import sys

# from core.__core_race_configuration import z
#
# print z()
#
#
# class a():
# 	def __init__(self,name='Test'):
# 		self.a1 = "Hello!"
# 		self.name = name
#
# 	def getName(self):
# 		return self.name
#
# class b(a):
# 	def __init__(self):
# 		a.__init__(self,"Benjamin")
#
# 	def sayHello(self):
# 		print "Hello,",self.getName()+"!"
#
# x = b()
#
# x.sayHello()

#
# class z():
# 	def __init__(self,name=""):
# 		self.name = name
# 		self.selfStorage = None
#
# 	def get_name(self):
# 		return self.name
#
# 	def set_child(self,x):
# 		self.selfStorage = x
#
# 	def child(self):
# 		return self.selfStorage
#
# a = z("Ben")
# print a.get_name(),sys.getsizeof(a)
# b=a.set_child(z("Frodo"))
# print a.child().get_name(),sys.getsizeof(a)
# a.child().set_child(z("moth"))
# print a.child().child().get_name(),sys.getsizeof(a)


# class a():
# 	def __init__(self):
# 		self.z = "Hi"
# 		self.b().pri()
#
# 	class b():
# 		def __init__(self):
# 			self.z = "Bye"
#
# 		def pri(self):
# 			print self.z
#
# 	def pri(self):
# 		print self.z
#
# a().pri()

#
def carry(num):
	if 0 <= num <=4:
		return 0
	return 1
#
# for i in range(1,51):
# 	num = str(2**i)
# 	li=[]
# 	for j in list(num):
# 		li.append(carry(int(j)))
# 	print  i,li[::-1],num

from core.time_tester import time_tester
a = time_tester()
for i in range(0,5):
	print a.elapsed()
	raw_input("Enter!")
