#!/usr/bin/env python
# -*- coding: utf-8 -*-
## Baiqiang XIA implementation of data structures

## max binary heap
## like a binary tree, but parent.key > child.key

class maxBinaryHeap(object):
    
    ## init
    def __init__(self):
        self.heap = [0]
        self.heapSize = 0
        
    ## insert 
    def insert(self, key):
        self.heap.append(key) ## add to end
        self.heapSize += 1 ## increase index
        self.swimUp(self.heapSize)
        
    def swimUp(self, index):
        father_index = index // 2
        while father_index >= 1:
            if self.heap[father_index] < self.heap[index]: ## when father node key is smaller
                self.heap[father_index], self.heap[index] = self.heap[index], self.heap[father_index] ## swarp
                index = father_index
                father_index = father_index//2
            else:
                break
            
    ## delete
    def delete(self):
        if self.heapSize == 0:
            print('@empty heap!')
            return
        else:
            deleted = self.heap[1]
            self.heap[1], self.heap[-1] = self.heap[-1], self.heap[1]
            self.heap.pop()
            self.heapSize -= 1
            self.swimDown(1)
            return deleted
            
    def swimDown(self, index):
        left_child_index = index * 2
        while left_child_index < self.heapSize: ## when no child, no loop
            max_child_index = self.maxChild(index)
            if self.heap[index] < self.heap[max_child_index]:
                self.heap[index], self.heap[max_child_index] = self.heap[max_child_index], self.heap[index]
                index = max_child_index
                left_child_index = index * 2
            else:
                break
                
    def maxChild(self, index):
        if index * 2 + 1 <= self.heapSize:  ## two children
            if self.heap[index * 2] > self.heap[index * 2 + 1]:
                return index * 2
            else:
                return index * 2 + 1
        else:
            return index * 2
            
    def heapFromList(self, ls):
        self.heapSize = len(ls)
        self.heap = [0] + ls
        idx = len(ls) // 2
        while idx >= 1 :
            self.swimDown(idx)
            idx -= 1
