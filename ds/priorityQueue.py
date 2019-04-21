#!/usr/bin/env python
# -*- coding: utf-8 -*-
## Baiqiang XIA implementation of data structures

## Priority Queue is an extension of the queue with following properties.
## 1) An element with high priority is dequeued before an element with low priority.
## 2) If two elements have the same priority, they are served according to their order in the queue.

class priorityQueue(object):
    ## init
    def __init__(self):
        self.pqueue = []
        
    ## print
    def __str__(self):
        return ' '.join([str(f) for f in self.pqueue])

    ## check if it is empty
    def is_empty(self):
        return self.pqueue == []
        
    ## insert
    def enqueue(self, data):
        self.pqueue.append(data)
        
    ## delete
    def dequeue(self):
        if self.is_empty():
            print("@queue is empty, dequeue failed!")
            return False
        else:
            max_idx = 0
            for idx, _ in enumerate(self.pqueue, 0):
                if self.pqueue[max_idx]< self.pqueue[idx]:
                    max_idx = idx
            return self.pqueue.pop(max_idx)
            