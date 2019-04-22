#!/usr/bin/env python
# -*- coding: utf-8 -*-
## Baiqiang XIA implementation of data structures

## Graph Implementation as Ajacency List
class graph(object):
    ## init
    def __init__(self):
        self.dict = {} ## adjacency diction
        
    ## add Edge
    def addEdge(self, fromVertex, toVertex):
        ## check if vertex exists:
        if fromVertex in self.dict:
            self.dict[fromVertex].append(toVertex)
        else:
            self.dict[fromVertex] = [toVertex]
    ## print
    def __str__(self):
        output = []
        for each in self.dict:
            output.append(' '.join([str(each) + '--->' + str(f) for f in self.dict[each]]))
        return '\n'.join(output)
