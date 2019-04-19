#!/usr/bin/env python
# -*- coding: utf-8 -*-
## Baiqiang XIA implementation of data structures

## binary search tree
class bstnode(object):

    ##init
    def __init__(self, key):
        self.key = key
        self.left  = None
        self.right= None
        self.parent = None
        
    ## display     
    def display(self):
        lines, _, _, _ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
        
class bsttree(object):

    ## init 
    def __init__(self):
        self.root = None

    ## insert
    def insert(self, key):
        if not self.root:
            self.root = bstnode(key)
            return True
        else:
            return self.__insert(self.root, key)
    ## private
    def __insert(self, root, key):
        ## left branch
        if key < root.key:
            if root.left:
                return self.__insert(root.left, key)
            else:
                root.left = bstnode(key)
                root.left.parent = root
                return True
        ## right branch
        elif key > root.key:
            if root.right:
                return self.__insert(root.right, key)
            else:
                root.right = bstnode(key)
                root.right.parent = root
                return True
        ## insert conflict
        else:
            print('@insert conflict, node already exists!')
            return False
    
    ## print bst
    def printbst(self):
        if not self.root:
            print('@print emptry tree!')
        else:
            self.__printbst(self.root)
    ## private __printbst
    def __printbst(self, root):
        ## recursive
        cur = root
        if cur:
            self.__printbst(cur.left)
            print(cur.key, end = '-')
            self.__printbst(cur.right)
        ## finish
        return
        
    ## public is_valid_bst
    def is_valid_bst(self):
        if not self.root:
            return True
        else:
            return self.__is_valid_bst(self.root, float('-inf'), float('inf'))
    ## private __is_valid_bst
    def __is_valid_bst(self, root, min, max):
        if min > root.key or max < root.key:
            return False
        else:
            left_ok   = self.__is_valid_bst(root.left  , min,  root.key) if root.left else True
            right_ok = self.__is_valid_bst(root.right, root.key, max) if root.right else True
            return left_ok and right_ok
        
    ## count
    def count(self):
        if not self.root:
            return 0
        else:
            return self.__count(self.root)
    ## __count
    def __count(self, root):
        if root.left and root.right:
            return 1 + self.__count(root.left) + self.__count(root.right)
        elif root.left:
            return 1 + self.__count(root.left)
        elif root.right:
            return 1  + self.__count(root.right)
        else:
            return 1
            
    ## height
    def height(self):
        if not self.root:
            return 0
        else:
            return self.__height(self.root)
    def __height(self, root):
        if root.left and root.right:
            return 1 + max(self.__height(root.left), self.__height(root.right))
        elif root.left:
            return 1 + self.__height(root.left)
        elif root.right:
            return 1 + self.__height(root.right)
        else:
            return 1
            
    ## delete
    def delete(self, key):
        if not self.root:
            print('@cannot delete in empty tree!')
            return False
        else:
            return self.__delete(self.root, key)
    def __delete(self, root, key):        
        ## left branch
        if key < root.key:
            if not root.left:
                return False
            else:
                return self.__delete(root.left, key)
        ## right branch
        elif key > root.key:
            if not root.right:
                return False
            else:
                return self.__delete(root.right, key)
        ## here to delete
        else:
            ## if root has 2 children
            if root.left and root.right:
                ## inorder successor
                min_right = root.right
                while min_right.left:
                    min_right = min_right.left
                ## update key
                root.key = min_right.key
                ## iterate delete
                return self.__delete(min_right, min_right.key)
                
            ## if root has left child
            elif root.left:
                root.key = root.left.key ## update key
                root.right= root.left.right ## update left/right children
                root.left  = root.left.left
                if root.right:
                    root.right.parent = root ## update parent links
                if root.left:
                    root.left.parent = root
                return True
                
            ## if root has right child
            elif root.right:
                root.key = root.right.key ## update key
                root.left = root.right.left ## update left/right children
                root.right= root.right.right
                if root.right:
                    root.right.parent = root ## update parent links
                if root.left:
                    root.left.parent = root
                return True
                
            ## if root has no child
            else:
                if root is root.parent.left:
                    root.parent.left = None
                elif root is root.parent.right:
                    root.parent.light = None
                return True
    ## depth first traversal
    def depthFirst(self, mode = 'inorder'):
        if not self.root:
            print('@empty tree!')
        else:
            self.__depthFirst(self.root, mode)
    def __depthFirst(self, root, mode):
        cur = root
        if cur:
            if mode == 'preorder':
                print(cur.key, end = '-')
                self.__depthFirst(cur.left, mode)
                self.__depthFirst(cur.right, mode)
            elif mode == 'inorder':
                self.__depthFirst(cur.left, mode)
                print(cur.key, end = '-')
                self.__depthFirst(cur.right, mode)
            elif mode == 'postorder':
                self.__depthFirst(cur.left, mode)
                self.__depthFirst(cur.right, mode)
                print(cur.key, end = '-')
                
    ## bread first traversal
    def breadFirst(self):
        if not self.root:
            print('@empty tree!')
        else:
            cur = self.root
            this_layer = [cur]
            while this_layer:
                next_layer = []
                for each in this_layer:
                    print(each.key, end = '-')
                    if each.left: next_layer.append(each.left)
                    if each.right: next_layer.append(each.right)
                print()
                this_layer = next_layer
     
