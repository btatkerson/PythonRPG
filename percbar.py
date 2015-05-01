'''
Name: percbar.py
Author: Benjamin A.

Creates a text bar of custom width and displays percentage of first number relative to the second.
'''

class percbar():
    def __init__(self,def_part=None,def_total=None,def_width=None,def_perc_tag=None,def_perc_precision=None):
        self.__DEFAULT_PART = None
        self.__DEFAULT_TOTAL = None
        self.__DEFAULT_BAR_WIDTH = None
        self.__DEFAULT_PERC_TAG = None
        self.__DEFAULT_PERC_PRECISION = None
        
        self.set_default_part(def_part) # Any number less than or equal to 0 given will automatically default to 0
        self.set_default_total(def_total) # Any number less than or equal to 0 given will automatically default to 1
        self.set_default_bar_width(def_width) # Any number less than or equal to 0 given will automatically default to 100
        self.set_default_perc_tag(def_perc_tag)
        self.set_default_perc_precision(def_perc_precision) # Any number less than or equal to 0 given will automatically default to 2
    
    def set_default_part(self,part):
        if not part:
            part = 0
        self.__DEFAULT_PART = (part+abs(part))/2 or 0 # Any number less than or equal to 0 given will automatically default to 0

    def get_default_part(self):
        return self.__DEFAULT_PART
    
    def set_default_total(self,total):
        if not total:
            total = 0
        self.__DEFAULT_TOTAL = (total+abs(total))/2 or 0 # Any number less than or equal to 0 given will automatically default to 1

    def get_default_total(self):
        return self.__DEFAULT_TOTAL

    def set_default_bar_width(self,width):
        if not width:
            width = 0
        self.__DEFAULT_BAR_WIDTH = (width+abs(width))/2 or 100 # Any number less than or equal to 0 given will automatically default to 100

    def get_default_bar_width(self):
        return self.__DEFAULT_BAR_WIDTH        

    def set_default_perc_tag(self,perc_tag):
        if not perc_tag:
            perc_tag = 0
        self.__DEFAULT_PERC_TAG = bool(perc_tag) or False

    def get_default_perc_tag(self):
        return self.__DEFAULT_PERC_TAG

    def set_default_perc_precision(self,perc_precision):
        if not perc_precision:
            perc_precision = 0
        self.__DEFAULT_PERC_PRECISION = (perc_precision+abs(perc_precision))/2 or 2 # Any number less than or equal to 0 given will automatically default to 2

    def get_default_perc_precision(self):
        return self.__DEFAULT_PERC_PRECISION

    def disp(self,part=None,total=None,width=None,perc_tag=None,perc_precision=None):
        '''
        Displays a text bar to demonstrate percentage

        If given 3/4 = 75%
        part = 3
        total = 4

        width -- the amount of spaces used in the bar

        perc_tag -- Set to False by default, when True, a numerical percentage is displayed next to the bar

        perc_precision -- The amount of decimal places after the percentage label
        '''
        part = part or self.__DEFAULT_PART
        total = total or self.__DEFAULT_TOTAL
        width = width or self.__DEFAULT_BAR_WIDTH
        perc_tag = perc_tag or self.__DEFAULT_PERC_TAG
        perc_precision = perc_precision or self.__DEFAULT_PERC_PRECISION

        
        spaces = round(part*width/total)
        perc=''
        if perc_tag:
            perc = '{:.2%}'.format(part/total)

        temp = '|'+''.join(['-' for i in range(0,max(0,int(spaces)))]+[' ' for i in range(0,int(width-max(0,int(spaces))))])+'| '+perc
        return temp
