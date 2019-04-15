# -*- coding: utf-8 -*-
## Baiqiang XIA implementation of data structures

# doubly linked list
# implemented as seperated classes: node and list
class dll_node(object):
    def __init__(self, val, pre = None, nxt = None):
        self.data = val
        self.prev = pre
        self.next = nxt
        
class doublyLinkedList(object):
    ## initialization
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
        
    ## print dll
    def printDLL(self):
        print('@print dll from head!')
        
        ## print root label
        if self.head:
            print('(root)', end = '')
        else:
            print('@print empty dll!')
        
        ## print nodes  
        cur = self.head
        cnt = 0
        while cur:
            if cur.next:
                print(cur.data, end = ' <==>')
            else:
                print(cur.data)
            cur = cur.next
            cnt += 1
            
        ## end printing
        print('@finished printing %d nodes of dll!'%cnt)
        return 1
    
    ## insert at head of dll
    def insert_at_head(self, val):    
        ## make dll node
        node = dll_node(val)        
        ## if dll is empty
        if not self.head:
            self.head = node
            self.tail = node
            print('@insert node to empty dll!')
            return 1
        ## if dll is not empty
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
            print('@insert node at head of dll!')
            return 1
        
        ## nothing happens here, just a habit
        return -1
        
    ## search node in dll
    def search(self, val):
        if not self.head:
            print('@dll is empty, can not search!')
        else:
            cur = self.head
            while cur: ## loop till the tail.next
                if cur.data == val:
                    print('@found node with value %d in dll!'%val)
                    return 1
                cur = cur.next
        print('@no node found with value %d!'%val)
        return -1
        
    ## delete node in dll
    def delete(self, val):
        ## empty dll
        if not self.head:
            print('@not able to delete node in empty dll!')
            return 1
        ## 1 node dll
        elif self.head == self.tail:
            if self.head.data == val:
                self.head = None
                self.tail = None
                print('@delete 1 node with value %d, now dll is empty!'%val)
                return 1
            else:
                print('@no matched node to delete!')
        ## >= 2 nodes dll     
        else:
            ## if head node matches, move the head to the next node, set to None the prev of new head
            if self.head.data == val:
                self.head = self.head.next
                self.head.prev = None
                print('@delete 1 node with value %d at head in dll!'%val)
                return 1
            ## if head does not match
            else:
                pre = self.head
                cur = self.head.next
                while cur != self.tail: ## tail matches should be handled differently
                    if cur.data == val:
                        pre.next = cur.next
                        cur.next.prev = cur.prev
                        print('@delete 1 node with value %d inside of dll!'%val)
                        return 1
                    
                    ## update pre, cur
                    pre = cur
                    cur = cur.next
                
                ## now cur points to self.tail
                if cur.data == val:
                    self.tail = cur.prev
                    cur.prev.next = None
                    print('@delete 1 node with value %d at tail of dll!'%val)
                    return 1
                    
                ## no match to delete
                else:
                    print('@no matched node with value %d in dll to delete!'%val)
                    return -1
                
                        
                        
                    
            
            
            