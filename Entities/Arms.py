'''
Created on Oct 24, 2016

@author: nikita
Contains Weaponry, Armor, and Jewelery generic types
'''

from Entities.Item import Item

class Weapon(Item):
    '''
    classdocs
    '''


    def __init__(self, mindamage=0, maxdamage=0,
                 worth=0, description=''):
        '''
        Constructor
        '''
        #consider crit?
        #add class/race restrictions
        self.mindamage = mindamage
        self.maxdamage = maxdamage
        Item.__init__(self, worth, description)
        
        
class Shield(Item):
    '''uses the defence stat'''
    
    def __init__(self, defence=0, worth=0, description=''):
        self.defence = defence
        Item.__init__(self, worth, description)
    
    
class Armor(Item):
    '''
    consider toughness
    '''
    
    def __init__(self, armor=0, worth=0, description=''):
        
        self.armor = armor
        Item.__init__(self, worth, description)
        
class HeadWear(Armor):
    
    def __init__(self, armor=0, worth=0, description=''):
        Armor.__init__(self, armor, worth, description)
        
class ChestWear(Armor):
    
    def __init__(self, armor=0, worth=0, description=''):
        Armor.__init__(self, armor, worth, description)
        
class LegWear(Armor):
    
    def __init__(self, armor=0, worth=0, description=''):
        Armor.__init__(self, armor, worth, description)
        
class FootWear(Armor):
    
    def __init__(self, armor=0, worth=0, description=''):
        Armor.__init__(self, armor, worth, description)
        
class Gloves(Armor):
    
    def __init__(self, armor=0, worth=0, description=''):
        Armor.__init__(self, armor, worth, description)
        
class Amulet(Item):
    #add stat effect
    def __init__(self, armor=0, worth=0, description=''):
        Item.__init__(self, worth, description)
        
class Ring(Item):
    #add stat effect
    def __init__(self, armor=0, worth=0, description=''):
        Item.__init__(self, worth, description)
        

