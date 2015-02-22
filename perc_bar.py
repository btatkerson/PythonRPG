'''
Name: perc_bar.py

Creates a text bar of custom width and displays percentage of first number relative to the second.
'''

class perc_bar():
	def __init__(self):
		None
	
	def perc(self,num=0,den=100,width=100,perc_label=False):
		num = abs(num)
		den = abs(den)
		complete = 0
		if den == 0:
			return ""

		
		complete = round(num/den*width)
		if perc_label:
			perc_label = " {:.2f} %".format(num/den*100)
		else:
			perc_label = ""
			
		return "|" + ''.join(['-' for i in range(0,complete)]+[' ' for i in range(0,width-complete)]) + "|" + perc_label 
