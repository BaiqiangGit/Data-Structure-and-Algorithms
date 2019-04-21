#!/usr/bin/env python
# -*- coding: utf-8 -*-
## Baiqiang XIA implementation of data structures

## circular queue (ring buffer)
## key point: from front to rear (inclusive) the number of elements should not exceed a constant (qsize)
## references: 
## https://www.pythoncentral.io/circular-queue/
## https://www.geeksforgeeks.org/circular-queue-set-1-introduction-array-implementation/

class circularQueue(object):
    ## init function
    def __init__(self, qsize):
        self.queue = [None] * qsize ## think this as a buffer, max size is self.limit
        self.qsize  = qsize
        self.front = -1 ## pointer to head, place to pop
        self.rear  = -1 ## pointer to tail, next place is to insert
        
    ## print function
    def __str__(self):
        return ' '.join([str(f) for f in self.queue[self.front:self.rear+1]]) if self.rear >= self.front else ' '.join([str(f) for f in self.queue[self.front:]]) + ' ' + ' '.join([str(f) for f in self.queue[:self.rear+1]])
   
    ## enqueue function
    ## change the value at front
    ## move the pointer one step forward
    ## when pointer == self.qsize, reset to 0
    def enqueue(self, data):
        ## check if queue is full (when next insert will be at self.front, self.rear is just behind self.front in circle)
        ## two cases (1) self.front - self.rear = 1 (2) self.rear = self.qsize - 1, self.front = 0
        if self.rear + 1 == self.front or (self.rear == self.qsize-1 and self.front == 0):
            print('@circular queue is full, enqueue failed!')
            return False
        ## check if the queue is empty
        ## can use self.front or self.rear as indicator
        elif self.front == -1:
            self.front = self.rear = 0
            self.queue[0] = data
            return True
        ## when queue is not empty and not full
        ## just move the rear to next
        else:
            self.rear += 1            
            if self.rear == self.qsize:
                self.rear = 0
            self.queue[self.rear] = data
            return True
            
    ## dequeue function
    ## change front pointer to move forward in circle
    ## no delete !!! just append, or move pointer
    def dequeue(self):
        ## check if queue is empty
        if self.front == -1:
            print('@cannot dequeue in empty queue!')
            return False
            
        ## queue has one element, reset to default
        ## this happends after insertion of first element
        ## and deletion until the last element
        elif self.front == self.rear:
            data = self.queue[self.front]
            self.front = self.rear = -1
            return data
        
        ## queue has more than 1 element
        else:
            data = self.queue[self.front]
            self.front  += 1
            if self.front == self.qsize:
                self.front = 0
            return data
            
        
            
        
            
            
        