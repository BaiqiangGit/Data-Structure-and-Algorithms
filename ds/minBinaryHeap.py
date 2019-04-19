#!/usr/bin/env python
# -*- coding: utf-8 -*-
## Baiqiang XIA implementation of data structures

## min binary heap
class minBinaryHeap(object):
    
    ## init
    def __init__(self):
        self.heap = [0] ## make the first element 0
        self.heapSize = 0
        
    ## swim up ( for insert )
    ## put the element at the end of the array, if it's smaller than its parent, swarp value
    ## iterate this to the upper layer (compare with the parent of its parant)
    ## stop iter when no smaller than its parent, or array exhaused
    def swimUp(self, index):
        parentIndex = index // 2
        while parentIndex >= 1: ## cannot go upper than the root
            if self.heap[index] < self.heap[parentIndex]: ## if parent key is bigger
                self.heap[index], self.heap[parentIndex] = self.heap[parentIndex], self.heap[index] ## swarp values to swim up
            else:
                break
            parentIndex = parentIndex // 2       
          
    ## insert to min binary heap          
    def insert(self, key):
        self.heap.append(key)
        self.heapSize += 1
        self.swimUp(self.heapSize)
                
    ## swim down (for delete at root)
    ## swarp the root and last
    ## remove last
    ## swarp the root and its smaller child if needed, iterate this step
    def delete(self):
        if self.heapSize == 0:
            print('@empty binay heap!')
            return -1
        deleted = self.heap[1]
        self.heap[1] = self.heap[-1]
        self.heap.pop()
        self.heapSize -= 1
        self.swimDown(1)
        return deleted
        
    def swimDown(self, index):
        leftChildIndex = index * 2
        while leftChildIndex < self.heapSize: ## not exceed heap size, make sure this node has child
            minChildIndex = self.minChild(index) ## get the min value child
            if self.heap[minChildIndex] < self.heap[index]: ## when child is smaller than itself
                self.heap[minChildIndex], self.heap[index] = self.heap[index], self.heap[minChildIndex] ## swarp the values
            else: ## otherwise stop iteration
               break
            index = minChildIndex ## use two lines of code to make it more readable
            leftChildIndex = index *2
            
    ## return the index of its min child    
    def minChild(self, index):
        ## only left child exists
        if index * 2 + 1 > self.heapSize:
            return index * 2
        else:
            if self.heap[index*2] < self.heap[index*2 + 1]:
                return index*2
            else:
                return index * 2 + 1           
                    
    ## heapFromList
    def heapFromList(self, ls):
        self.heap = [0] + ls
        self.heapSize = len(ls)
        
        idx = len(ls) // 2 ## why ?
        while idx > 0:
            self.swimDown(idx)
            idx -= 1
            
    