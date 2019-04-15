# -*- coding: utf-8 -*-
## Baiqiang XIA implementation of data structures

# singly linked list
# implemented as seperated classes: node and list
class sll_node(object):
    def __init__(self, val, nxt = None):
        self.data = val
        self.next = nxt
       
class singlyLinkedList(object):

    ## initialization
    def __init__(self, head = None):
        self.head = head
        
    ## print sll
    def printSLL(self):
        cur = self.head
        cnt = 0
        print('(head)', end = '')
        while cur:
            print(cur.data, end = ' -->')
            cur = cur.next
            cnt += 1
        print('\n@finished printing sll of %d nodes'%cnt)
        return 1
    
    ## insert at tail of sll
    def insert_at_tail(self, val):
        ## when sll is empty
        if not self.head:
            self.head = sll_node(val)
            print('@insert at tail to empty sll!')
            return 1
        ## when sll is not empty
        else:
            cur = self.head
            while cur.next:
                cur = cur.next ## until cur.next is None, but cur is not None
            ## now pointer is at the tail, put added node as tail.next
            cur.next = sll_node(val)
            print('@insert at tail of sll!')
            return 1
            
    ## insert at head of sll
    def insert_at_head(self, val):
            self.head = sll_node(val, None) if not self.head else sll_node(val, self.head)
            print('@insert at head of sll!')
            return 1
            # long version
            # if not self.head:
                # self.head = sll_node(val)
                # print('@insert node as head to empty sll!')
                # return 1
            # else:
                # self.head = sll_node(val, self.head)
                # print('@insert node as head of sll!')
                # return 1
                
    ## search for a node with value in sll
    def search(self, val):
        cur = self.head
        while cur:
            if cur.data == val:
                print('@value %d found in sll!'%val)
                return 1
            cur = cur.next
        print('@value %d not found in sll!'%val)
        return -1
    
    ## delete a node with value
    def delete(self, val):
        ## if sll is empty
        if not self.head:
            print('@sll is empty, no node to delete!')
            return 1
        ## if sll head is the match
        elif self.head.data == val:
                self.head = self.head.next
                print('@delete at sll head!')
                return 1
        ## if sll head is not the match
        else:
            cur = self.head
            nxt = self.head.next
            while nxt:
                if nxt.data == val: ## if find match at next
                    cur.next = nxt.next ## link to the next next 
                    print('@delete node inside sll!')
                    return 1
                cur = nxt
                nxt = cur.next
        ## no found
        print('@deletion failed, no matched node found!')
        return -1
        
    ## reverse sll
    def reverse(self):
        ## for empty sll
        if not self.head:
            print('@sll is empty!')
            return 1
        ## for single node sll
        elif not self.head.next:
            print('@sll has only 1 node, no need to reverse!')
            return 1
        ## for multi nodes sll
        else:
            pre = None
            cur = self.head
            while cur:
                nxt = cur.next ## buffer the cur.next
                cur.next = pre ## change cur.next to pre
                pre = cur ## move forward 1 node
                cur = nxt ## move forward 1 node
            ## at the end of loop, cur is None,  pre is the last valid node
            self.head = pre
            print('@finished reversing sll!')
            return 1
            