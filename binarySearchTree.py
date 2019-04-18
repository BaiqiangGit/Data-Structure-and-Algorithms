#!/usr/bin/env python
# -*- coding: utf-8 -*-
## Baiqiang XIA implementation of data structures

## binary search tree: nodes are ordered by their keys
## bst criteria:
##(1) is binary tree 
##(2) left.key < cur.key < right.key if left or right exists
##(3) no duplicate nodes

class bst_node(object):
    ## initialization
    def __init__(self, val, parent = None, left = None, right = None):
        self.data = val
        self.parent = parent
        self.right = right
        self.left   = left
    
class binarySearchTree(object):
    ## init function
    def __init__(self, root = None):
        self.root = root
        
    ## print binary search tree
    def printBST(self):
        ## if empty tree
        if not self.root:
            print('@tree is empty!')
            return 1    
        ## if non-empty tree
        else:
            this_layer = [self.root]
            while this_layer:
                next_layer = []
                for node in this_layer:
                    print(node.data, end = '-')
                    if node.left:   next_layer.append(node.left)
                    if node.right: next_layer.append(node.right)
                print('\n')
                this_layer = next_layer
            print('@finished printing bst!')
            return 1
            
    ## insert node
    def insert(self, val):
        ## empty tree
        if self.root is None:
            self.root = bst_node(val)
            print('@insert as root of bst!')
            return 1
        ## non empty tree
        else:
            ## current root
            cur = self.root
            while True:
                ## duplicate check
                if val == cur.data: 
                    print('@insert failed, duplicated node found!')
                    return -1
                    
                ## left subtree
                if val < cur.data: 
                    ## find place to insert
                    if not cur.left:
                        cur.left = bst_node(val, cur)
                        #cur.left.parent = cur
                        print('@insert node as left leaf node of bst!')
                        return 1
                    ## not find 
                    else:
                        cur = cur.left
                        
                ## right subtree
                elif val > cur.data:
                    ## find place to insert
                    if not cur.right:
                        cur.right = bst_node(val, cur)
                        #cur.right.parent = cur
                        print('@insert node as right leaf node of bst!')
                        return 1
                    ## not yet
                    else:
                        cur = cur.right
        
        ## nothing happens here, just a habit
        print('@insert error if see this message!')
        return -1
        
    ## tree height
    
    ## search val (find)
    def search(self, val):
        ## empty tree
        if self.root is None:
            print('@tree is empty, no found!')
            return 1
        ## non-empty tree
        else:
            cur = self.root
            while cur:
                if cur.data == val:
                    print('@value %d found in bst!'%val)
                    return 1
                elif val < cur.data:
                    cur = cur.left
                else:
                    cur = cur.right
        ## return
        print('@value %d not found in bst!'%val)
        return -1
        
    ## delete value (can also implement into node)
    ## -- delete from empty tree
    ## -- delete from non-empty tree
    ##     -- delete at entry/root node
    ##         -- node has 1 child
    ##         -- node has 2 children
    ##     -- delete at middle node
    ##         -- node has 1 child
    ##         -- node has 2 children
    ##     -- delete at leaf node
    
    def delete(self, val, entryNode):
        ## empty tree
        if not entryNode:
            return False
        ## non-empty tree
        else:
            ## not found, continue in left branch
            if val < entryNode.data:
                self.delete(val, entryNode.left)
            ## not found, continue in right branch
            elif val > entryNode.data:
                self.delete(val, entryNode.right)
            ## found and delete
            else:
                ## when cur has both left and right children
                if entryNode.left and entryNode.right:
                    inorder_successor = entryNode
                    while inorder_successor.left:
                        inorder_successor = inorder_successor.left
                    entryNode.data = inorder_successor.data
                    self.delete(val, inorder_successor) ## iterate, as inorder_successor may has right subtree                    
                ## cur only has a valid left child
                elif entryNode.left:
                    print('do something here') 
                ## cur only has a valid right child
                elif entryNode.right:
                    print('do something here')
                ## cur has no child, cur is a leaf node
                else:
                    if cur.
