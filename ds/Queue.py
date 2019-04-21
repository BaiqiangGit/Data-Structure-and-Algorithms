#!/usr/bin/env python
# -*- coding: utf-8 -*-
## Baiqiang XIA implementation of data structures

## vanilla Queue
class Queue(object):
    ## init
    def __init__(self, limit):
        self.front = None
        self.rear = None
        self.limit = limit
        self.size = 0
        self.__queue = []
    ## insert/ enqueue
    def enqueue(self, data):
        if self.size >= self.limit:
            print('@queue is already full, enqueue fail!')
            return False
        if self.size == 0:
            self.front = self.rear = 0
            self.__queue.append(data)
            self.size += 1
        else:
            self.rear += 1
            self.__queue.append(data)
            self.size += 1
        return True
        
    ## delete/dequeue
    def dequeue(self):
        if self.size == 0:
            print('@can not dequeue in empty queue!')
            return False
        elif self.size == 1:
            print('@queue has 1 element, reset to empty after dequeue!')
            self.front = self.rear = None
            self.size -= 1
            return self.__queue.pop()
        else:
            self.rear -= 1
            self.size -= 1
            return self.__queue.pop()
    
    ## overload print function
    def __str__(self):
        return ' '.join([str(f) for f in self.__queue])