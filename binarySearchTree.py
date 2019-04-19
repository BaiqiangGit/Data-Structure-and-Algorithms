#!/usr/bin/env python
# -*- coding: utf-8 -*-
## Baiqiang XIA implementation of data structures

## bst implementation
## ref: https://github.com/joeyajames/Python/blob/master/Trees/BinarySearchTree.py

## node 
class bst_node(object):
    ## init
    def __init__(self, key):
        self.key  = key
        self.left  = None
        self.right= None
        self.parent = None
        
## tree
class bst(object):
    ## init
    def __init__(self):
        self.root = None
    
    ## insert
    def insert(self, key):
        if not self.root:
            #print('@insert %d at root!'%key)
            self.root = bst_node(key)
            return 1
        else:
            return self.__insert(self.root, key)
            
    def __insert(self, node, key):
        if key < node.key:
            if node.left:
                return self.__insert(node.left, key)
            else:
                #print('@insert %d as left leaf!'%key)
                node.left = bst_node(key)
                node.left.parent = node
                return 1
        elif key > node.key:
            if node.right:
                return self.__insert(node.right, key)
            else:
                #print('@insert %d as right leaf!'%key)
                node.right = bst_node(key)
                node.right.parent = node
                return 1
        else:
             #print('@cannot insert duplicated keyue to bst!')
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
    def find(self, key):
        if not self.root:
            return False
        else:
            return self.__find(self.root, key)
            
    def __find(self, entry, key):
        if entry.key == key:
            return True
        elif entry.key > key and entry.left:
            return self.__find(entry.left, key)
        elif entry.key < key and entry.right:
            return self.__find(entry.right, key)
        return False
        
    ## inorder
    def inorder(self):
        if not self.root:
            print('@empty bst!')
        else:
            self.__inorder(self.root)
    def __inorder(self, entry):
        if entry.left: self.__inorder(entry.left)
        print(entry.key, end = '-')
        if entry.right: self.__inorder(entry.right)
        
    ## preorder
    def preorder(self):
        if not self.root:
            print('@empty tree!')
        else:
            self.__preorder(self.root)
    def __preorder(self, entry):
        print(entry.key, end = '-')
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
        print(entry.key, end = '-')
        
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
                print(each.key, end = '-')
                if each.left: next_layer.append(each.left)
                if each.right: next_layer.append(each.right)
            print()
            this_layer = next_layer
      
    ## delete function
    def delete(self, key):
        if not self.root:
            return False
        else:
            return self.__delete(self.root, key)        
    ## private counterpart

    def __delete(self, root, key):
        ## when a match is found
        if key == root.key:
            ## deleted node has 0 child
            if root.left is None and root.right is None:
                if root.parent is None:
                    self.root = None ## set root to None
                elif root.parent.left is root:
                    root.parent.left = None ## correct the link to parent
                elif root.parent.right is root:
                    root.parent.right = None ## correct the link to parent
                return True
            ## deleted node has left child
            elif root.left is not None and root.right is None:
                root.key = root.left.key  
                root.right= root.left.right ## 
                root.left  = root.left.left   ## be careful of the order of assignment, don't change root.left first
                if root.left: root.left.parent = root
                if root.right: root.right.parent = root
                return True
            ## deleted node has right child   
            elif root.right  is not None and root.left is None:
                root.key = root.right.key
                root.left  = root.right.left   ## 
                root.right= root.right.right ## be careful of the order of assignment, don't change root.right first
                if root.left: root.left.parent = root
                if root.right: root.right.parent = root
                return True
            ## deleted node has 2 children  
            elif root.right and root.left:
                ## get min right (inorder successor)
                min_right = root.right
                while min_right.left:
                    min_right = min_right.left
                ## change the key
                root.key = min_right.key
                ## remove the min_right node in the right subtree
                self.__delete(min_right, min_right.key) ## be careful here, the key to be deleted changes to min_right.key, 
                                                                              ## this line will direct to the code under 'if key == root.key:' 
                                                                              ## root should be min_right, not root.right, to reduce overlaped search (though result would be same)
                return True
        elif key < root.key:  
            if root.left:
                return self.__delete(root.left, key)
            else: ## end of search
                print('@delete failed, no match found!')
                return False
        elif key > root.key:
            if root.right:
                return self.__delete(root.right, key)
            else: ## end of search
                print('@delete failed, no match found!')
                return False

    ## is valid bst
    def is_valid_bst(self):
        if not self.root:
            return True
        else:
            return self.__is_valid_bst(self.root, float('-inf'), float('inf'))
    def __is_valid_bst(self, root, min, max):
        if root.key < min or root.key > max:
            return False
        else:
            left_ok = self.__is_valid_bst(root.left, min, root.key) if root.left else True
            right_ok = self.__is_valid_bst(root.right,  root.key, max) if root.right else True
            return left_ok and right_ok