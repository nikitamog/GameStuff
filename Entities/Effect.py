'''
Created on Oct 24, 2016

@author: nikita
'''

class Effect(object):
    '''
    Creates a generic effect class. I can think of a few types
    1. Active (happens once or on command)
    2. Passive (applies every turn)
    3. OverTime (applies for n turns) 
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        