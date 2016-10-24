'''
Created on Oct 23, 2016

@author: nikita
'''
from Entities.Character import BaseChar

class Warrior(BaseChar):
    '''
    classdocs
    '''
    

    def __init__(self, level=0, name='', race='Human'):
        '''
        Constructor
        '''
        BaseChar.__init__(self, level, name, race)
        
        #set class
        self.charclass = 'Warrior'
        
        #set hitdie
        self.hitdie = 8
        
        #set health
        self.setHealth()
        
        
        
        
        
        
        