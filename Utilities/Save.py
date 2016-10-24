'''
Created on Oct 13, 2016

@author: nikita

This class' goal is to read and write save files in the local
source folder.

WriteSave() - Store a player's information in a separate file.
ReadSave(file) - read a save file so and initialize the objects
    using the data.


'''
import pickle

class WriteSave(object):
    '''
    classdocs
    Write a class to file.
    '''


    def __init__(self):
        '''
        Constructor
        '''
        barray = [1, 5, 7, 5, 8]
        #writes barray into barray.pickle
        with open('barray.pickle', 'wb') as f:
            pickle.dump(barray, f)
        print('this is done')
        
        
        
    def print(self, stuff):
        print(stuff)

class ReadSave(object):
    
    def __init__(self):
        