'''
      Name: verbose.py
    Author: Benjamin A
   Purpose: Allows verbosity control that is easily implemented/inherited into classes,
'''

class verbose():
    def __init__(self,active=False, separator=''):
        self.activated = active
        self.separator = separator

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

    def verbo_set_separator(self, sep=None):
        if sep or sep == '':
            if type(sep) == str:
                self.separator = sep
                return 1
        self.separator = ' '
        return 0


    # Prints input 'statement' if input 'override' is True OR attribute 'self.activated' is True.
    def verbo(self,statement=None,override=False):
        if override or self.verbo_isActivated():
            if type(statement) == tuple:
                for i in statement:
                    print(i, end=self.separator)
                print('')
                return 1

            elif type(statement) == str:
                print(statement)
                return 1

            return 0
