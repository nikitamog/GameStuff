'''
Created on Oct 23, 2016

@author: nikita
'''
#for racial adjustments
from Entities import Races
from RNG import Dice

class BaseChar(object):
    '''
    Incorporates the base stats of a character.
    Maybe make a default character with standard equipment?
    
    Str, Dex, Con, Int, Lck, Cha
    
    Health - Will be increased by hit dice + Con. 
           - All characters have the same base health at lvl 0.
    
    '''
    
    def __init__(self, level=0, name='', race='Human'):
        '''
        Create a base class with default attributes
        '''
        self.name = name
        self.level= level
        
        #set Base Health and Stat Average
        self.basehealth = 5
        statavg = 5
        
        #set base attributes
        stats = ('Str', 'Dex', 'Con', 'Int', 'Lck', 'Cha')
        self.attributes = {x:statavg for x in stats}
        
        #set race. Apply Adjustment.
        self.race = race
        if(self.race != 'Human'):
            for key in Races.adjustments[race].keys():
                self.attributes[key] += Races.adjustments[race][key]
        
        #set default character class
        self.charclass = 'Commoner'
        
        #set default hitdie
        self.hitdie = 6
        
        
        #set health
        self.setHealth()
       
        
        
    def __str__(self, *args, **kwargs):
        
        return self.race + ' ' + self.charclass + ' ' + self.name
    
    def levelUpHealth(self):
        
        #allow character to lose health?
        self.health += Dice.dn(self.hitdie)
        self.health += (self.attributes['Con'] - 5)
        
    def levelUp(self):
        self.levelUpHealth()
        
    def setHealth(self):
        self.health = self.basehealth
        for _ in range(0, self.level):
            self.levelUpHealth()
        