#!/usr/bin/env python
# -*- coding: utf-8 -*-
## Baiqiang XIA implementation of data structures

## bst implementation
## reference: https://github.com/joeyajames/Python/blob/master/Trees/BinarySearchTree.py

## node 
class bst_node(object):
    ## init
    def __init__(self, val):
        self.val  = val
        self.left  = None
        self.right= None
        self.parent = None
        
## tree
class bst(object):
    ## init
    def __init__(self):
        self.root = None
    
    ## insert
    def insert(self, val):
        if not self.root:
            print('@insert %d at root!'%val)
            self.root = bst_node(val)
            return 1
        else:
            return self.__insert(self.root, val)
            
    def __insert(self, node,val):
        if val < node.val:
            if node.left:
                return self.__insert(node.left, val)
            else:
                print('@insert %d as left leaf!'%val)
                node.left = bst_node(val)
                node.left.parent = node
                return 1
        elif val > node.val:
            if node.right:
                return self.__insert(node.right, val)
            else:
                print('@insert %d as right leaf!'%val)
                node.right = bst_node(val)
                node.right.parent = node
                return 1
        else:
             print('@cannot insert duplicated value to bst!')
             return -1
             
    ## height
    def height(self):
        if not self.root:
            return 0
        else:
            return self.__height(self.root)
            
    def __height(self, entry):
        if entry.left and entry.right:
            return 1  + max(self.__height(entry.left), self.__height(entry.right))
        elif entry.left:
            return 1 + self.__height(entry.left)
        elif entry.right:
            return 1 + self.__height(entry.right)
        else:
            return 1
    
    ## count
    def count(self):
        if not self.root:
            return 0
        else:
            return self.__count(self.root)
    def __count(self, entry):
        if entry.left and entry.right:
            return 1 + self.__count(entry.left) + self.__count(entry.right)
        elif entry.left:
            return 1 + self.__count(entry.left)
        elif entry.right:
            return 1 + self.__count(entry.right)
        else:
            return 1
            
    ## find
    def find(self, val):
        if not self.root:
            return False
        else:
            return self.__find(self.root, val)
            
    def __find(self, entry, val):
        if entry.val == val:
            return True
        elif entry.val > val and entry.left:
            return self.__find(entry.left, val)
        elif entry.val < val and entry.right:
            return self.__find(entry.right, val)
        return False
        
    ## inorder
    def inorder(self):
        if not self.root:
            print('@empty bst!')
        else:
            self.__inorder(self.root)
    def __inorder(self, entry):
        if entry.left: self.__inorder(entry.left)
        print(entry.val, end = '-')
        if entry.right: self.__inorder(entry.right)
        
    ## preorder
    def preorder(self):
        if not self.root:
            print('@empty tree!')
        else:
            self.__preorder(self.root)
    def __preorder(self, entry):
        print(entry.val, end = '-')
        if entry.left: self.__preorder(entry.left)
        if entry.right: self.__preorder(entry.right)
        
    ## postorder
    def postorder(self):
        if not self.root:
            print('@empty tree!')
        else:
            self.__postorder(self.root)
    def __postorder(self, entry):
        if entry.left: self.__postorder(entry.left)
        if entry.right: self.__postorder(entry.right)
        print(entry.val, end = '-')
        
    ## bread first traversal
    def breadFirst(self):
        if not self.root:
            print("@empty tree!")
        else:
            self.__breadFirst(self.root)
    def __breadFirst(self, entry):
        this_layer = [entry]
        while this_layer:
            next_layer = []
            for each in this_layer:
                print(each.val, end = '-')
                if each.left: next_layer.append(each.left)
                if each.right: next_layer.append(each.right)
            print()
            this_layer = next_layer
            
    ## delete
    def delete(self, val):
        if not self.root:
            print('@cannot delete node in empty tree!')
            return False
        else:
            return self.__delete(self.root, val)
            
    def __delete(self, entry, val):
        ## case 1: left subtree
        if entry.val > val: 
            if entry.left:
                return self.__delete(entry.left, val)
            else:
                print('@cannot find value L!')
                return False
        ## case 2: right subtree
        elif entry.val < val:
            if entry.right:
                return self.__delete(entry.right, val)
            else:
                print('@cannot find value R!')
                return False
        ## case 3: current node matches
        else:
            if entry.left and entry.right: ## case 3.1: current node has 2 children
                ## get the replaced node
                inorder_successor = entry.right
                while inorder_successor.left:
                    inorder_successor = inorder_successor.left
                ## change entry value
                entry.val = inorder_successor.val
                ## continue delete until reach leaf node
                return self.__delete(inorder_successor, val) 
                    
            elif entry.left: ## case 3.2: current node has left child
                entry.val = entry.left.val
                entry.left = entry.left.left
                entry.right = entry.left.right
                return True
                
            elif entry.right: ## case 3.3: current node has right child
                entry.val = entry.right.val
                entry.left   = entry.right.left
                entry.right = entry.right.right
                return True
                
            else: ## case 3.4: current node has 0 child
                if not entry.parent: ## delete root node
                    print('@delete at root of single node tree!')
                    self.root = None
                elif entry is entry.parent.left: ## entry as left child
                    entry.parent.left = None
                else: ## entry as right child
                    entry.parent.right = None
                return True
                    