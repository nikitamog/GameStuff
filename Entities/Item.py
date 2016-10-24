'''
Created on Oct 23, 2016

@author: nikita
'''

class Item(object):
    '''
    Types of items I can imagine
    1. Equipment
    2. Consumable
    3. Quest Item
    4. Component (for crafting)
    '''


    def __init__(self, worth=0, description=''):
        '''
        Constructor
        '''
        self.worth = worth
        self.description = description
        