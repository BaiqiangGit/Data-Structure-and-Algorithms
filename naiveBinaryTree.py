#!/usr/bin/env python
# -*- coding: utf-8 -*-
## Baiqiang XIA implementation of data structures

## naive binary tree: nodes are not ordered by their keys

class treeNode(object):
    def __init__(self, key, parent = None, leftChild = None, rightChild = None):
        self.key = key
        self.parent = parent
        self.left = leftChild
        self.right = rightChild
        
class naiveBinaryTree(object):

    ## initialization
    def __init__(self, root = None):
        self.root = root
        
    ## print tree in bfs fashion
    def traverse_bfs(self):
        ## empty tree
        if not self.root:
            print('@print empty tree!')
            return 1
        ## non-empty tree
        else:
            this_level = [self.root]
            while this_level: ## when this level has no nodes, finish loop
                next_level = []
                for node in this_level:
                    print(node.key, end = '-')
                    if node.left: next_level.append(node.left)
                    if node.right: next_level.append(node.right)
                print()
                this_level = next_level
        ## only a habit to return something
        return 1
        
    ## insert node in bfs fashion
    def insert(self, val):
        ## if tree is empty
        if self.root == None:
            print('@add as root node of the tree!')
            self.root = treeNode(val)
        ## if tree is not empty
        else:
            this_level = [self.root]
            while this_level:
                next_level = []
                for node in this_level:
                    ## check left child
                    if node.left:
                        next_level.append(node.left)
                    else:
                        node.left = treeNode(val)
                        print('@add as lf-child of a node!')
                        return 1
                        
                    ## check right child
                    if node.right:
                        next_level.append(node.right)
                    else:
                        node.right = treeNode(val)
                        print('@add as rt-child of a node')
                        return 1
                        
                ## when this level is full, move to check next level
                this_level = next_level
    
    ## preorder depth first traversal
    def traverse_dfs_preorder(self, entryNode, layer_cnt = 0, layer_nm = 'root'):
        ## for invalid entryNode
        if not entryNode:
            return
        ## for valid entryNode
        else:
            print('%s node, layer %d with key %d'%(layer_nm, layer_cnt, entryNode.key))
            self.traverse_dfs_preorder(entryNode.left, layer_cnt + 1, 'left')
            self.traverse_dfs_preorder(entryNode.right, layer_cnt + 1, 'right')
            
    ## inorder depth first traversal
    def traverse_dfs_inorder(self, entryNode, layer_cnt = 0, layer_nm = 'root'):
        ## for invalid entryNode
        if not entryNode:
            return
        ## for valid entryNode
        else:
            self.traverse_dfs_preorder(entryNode.left, layer_cnt + 1, 'left')
            print('%s node, layer %d with key %d'%(layer_nm, layer_cnt, entryNode.key))
            self.traverse_dfs_preorder(entryNode.right, layer_cnt + 1, 'right')
            
    ## inorder depth first traversal
    def traverse_dfs_postorder(self, entryNode, layer_cnt = 0, layer_nm = 'root'):
        ## for invalid entryNode
        if not entryNode:
            return
        ## for valid entryNode
        else:
            self.traverse_dfs_preorder(entryNode.left, layer_cnt + 1, 'left')
            self.traverse_dfs_preorder(entryNode.right, layer_cnt + 1, 'right')
            print('%s node, layer %d with key %d'%(layer_nm, layer_cnt, entryNode.key))
            
                                       
            
            
