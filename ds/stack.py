#!/usr/bin/env python
# -*- coding: utf-8 -*-
## Baiqiang XIA implementation of data structures

## Stack
## elements ordered by time of arrival
## Last in first out (LIFO)

class stack(object):
    ## init
    def __init__(self, size):
        self.stack = []
        self.size = size
        
    ## print
    def __str__(self):
        return ' '.join([str(f) for f in self.stack])
        
    ## push in stack
    def push(self, data):
        if len(self.stack) == self.size:
            print('@stack if full!')
            return False
        else:
            self.stack.append(data)
            return True
            
    ## pop in stack
    def pop(self):
        if not self.stack:
            print('@stack is empty!')
            return False
        else:
            return self.stack.pop()
            
    ## peek in stack (no remove)
    def peek(self):
        if not self.stack:
            print('@stack is empty!')
            return False
        else:
            return self.stack[-1]
            
    