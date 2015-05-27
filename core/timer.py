from time import time
class timer():
	def __init__(self):
		self.marker = [time()]
		self.last_mark = self.marker[0]
		self.last_time_length = 0
		self.active = True

	def start(self):
		if not self.active:
			self.last_mark = time()
			self.active = True
			return 0
		return 1

	def pause(self):
		if self.active:
			self.last_time_length=self.last_time_length+(time()-self.last_mark())
			self.active=0
			return 0
		return 1

	def reset(self,start=False):
		self.last_mark = time()
		self.last_time_length = 0
		self.active = start


	def elapsed(self):
		if self.active:
			return self.last_time_length+(time()-self.last_mark)
