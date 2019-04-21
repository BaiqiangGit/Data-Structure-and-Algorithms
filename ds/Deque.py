#!/usr/bin/env python
# -*- coding: utf-8 -*-
## Baiqiang XIA implementation of data structures

## double ended queue
class deque(object):
    ## init
    def __init__(self, limit):
        self.deque = []
        self.size = 0
        self.limit = limit
    
    ## print
    def __str__(self):
        return ' '.join([str(f) for f in self.deque])
    
    ## helpers
    def is_empty(self):
        return True if self.size == 0 else False
    def is_full(self):
        return True if self.size == self.limit else False
        
    ## insert
    def insertRear(self, data):
        if self.is_full():
            print('@queue is full, insertion rear failed!')
            return False
        else:
            self.deque.insert(0, data)
            self.size += 1
            return True 
    
    def insertFront(self, data):
        if self.is_full():
            print('@queue is full, insertion front failed!')
            return False
        else:
            self.deque.append(data)
            self.size += 1
            return True
    ## delete
    def deleteRear(self):
        if self.is_empty():
            print('@queue is empty, deletion rear failed!')
            return False
        else:
            self.size -= 1
            return self.deque.pop(0)
    def deleteFront(self):
        if self.is_empty():
            print('@queue is empty, deletion front failed!')
            return False
        else:
            self.size -= 1
            return self.deque.pop()
            
    