'''

'''

class percbar():
	def __init__(self):
		None
	
	def disp(self,part=0,total=100,width=100,perc_tag=False,perc_precision=2):
		'''
		Displays a text bar to demonstrate percentage

		If given 3/4 = 75%
		part = 3
		total = 4

		width -- the amount of spaces used in the bar

		perc_tag -- Set to False by default, when True, a numerical percentage is displayed next to the bar

		perc_precision -- The amount of decimal places after the percentage label
		'''
		spaces = round(part*width/total)
		perc=''
		if perc_tag:
			perc = '{:.2%}'.format(part/total)

		temp = '|'+''.join(['-' for i in range(0,spaces)]+[' ' for i in range(0,width-spaces)])+'| '+perc
		return temp

a = percbar()	
print(a.disp(34,100,60,True))

