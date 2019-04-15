#!/usr/bin/env python
# -*- coding: utf-8 -*-
## Baiqiang XIA implementation of data structures


## array 
class array(object):

    ## initialization
    def __init__(self, length, dtype = int):
        self.length = length
        self.dtype  = dtype
        self.data    = [dtype(0) ] * self.length
        
    ## overload init function
    def __init__( self, ls):
        if not ls:
            self.data = ls
            self.length = 0
            self.dtype = None
        else:
            self.data = ls
            self.dtype = type(ls[0])
            self.length = len(ls)
            
    ## print function
    def printArray(self):
        print(self.data)
    
    ## insert function
    def insert(self, val, position):
        if 0 <= position <= self.length:
            self.data = self.data[:position] + [val] + self.data[position:]
            self.length += 1
            print('@insert %d to position %d'%(position, val))
            return 1
        else:
            print('@insert position should be integer within [%d, %d]'%(0, self.length))
            return -1
            
    def delete(self, val):
        ## including empty array
        for idx, ival in enumerate(self.data):
            if ival == val:
                print('@find and delete %d at position %d'%(val, idx))
                self.data = self.data[:idx] + self.data[idx+1:] 
                self.length -= 1
                return 1
        print('@no matched value to delete!')
        return -1
    