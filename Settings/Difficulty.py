'''
Created on Oct 23, 2016

@author: nikita
'''
from enum import Enum

class Difficulty(Enum):
    '''
    
    '''
    #The player is given a helping hand.
    Easy = 0;
    
    #Standard implementation. Less randomization.
    Normal = 1;
    
    #Full implementation. Totally random stats.
    Classic = 2;
    
    #The player is hindered intentionally.
    Hard = 3;
        
