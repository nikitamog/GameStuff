'''
Created on Oct 23, 2016

@author: nikita
'''

import random


def d4():
    return random.randint(1, 4)
    
def d6():
    return random.randint(1, 6)
    
def d8():
    return random.randint(1, 8)
    
def d10():
    return random.randint(1, 10)
    
def d12():
    return random.randint(1, 12)
    
def d20():
    return random.randint(1, 20)
    
def d30():
    return random.randint(1, 30)
    
def d100():
    return random.randint(1, 100)
    
def dn(n):
    '''
    Roll dice with N sides
    '''
    return random.randint(1, n)
        