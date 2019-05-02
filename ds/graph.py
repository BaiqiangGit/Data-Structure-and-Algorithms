#!/usr/bin/env python
# -*- coding: utf-8 -*-
## Baiqiang XIA implementation of data structures

## Graph represented as Adjacency List
class directedGraph(object):
    ## init
    def __init__(self):
        self.graph = {} ## adjacency diction
        
    ## add Edge
    def addEdge(self, fromVertex, toVertex):
        ## check if vertex exists:
        if fromVertex in self.graph:
            self.graph[fromVertex].append(toVertex)
        else:
            self.graph[fromVertex] = [toVertex] ## initialize as list
            
    ## print
    def __str__(self):
        output = []
        for each in self.graph:
            output.append(' '.join([str(each) + '--->' + str(f) for f in self.graph[each]]))
        return '\n'.join(output)
        
    ## bread first search (traversal), assuming all node are connected
    ## the task is to visit all the nodes
    def breadFirst_baiqiang(self, entryVertex):
    
        ## record the visited vetex, to avoid visiting same node again
        visited = set()
        
        ## maintain a stack to keep the vertices to be visited
        this_level = set([entryVertex])
        
        ## iterate till exhausted
        while this_level:
            next_level = set()
            for vertex in this_level:
                if not vertex in visited:
                    visited.add(vertex)
                    print(vertex, end = ' ')
                    next_level = next_level.union(set(self.graph[vertex]))
            print()
            this_level = next_level
            
    ## bread first search 
    ## https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
    def breadFirst_geek4geek(self, entryVertex):
    
        ## maintain a boolean list to indicate visited or not
        visited = [False] * len(self.graph)
    
        ## create a  queue (strict bread first, FIFO)
        queue = []
        
        ## enqueue the entry vertex
        queue.append(entryVertex)
        
        ## iterate
        while queue:
            ## dequeue from the front
            cur = queue.pop(0)
            print(cur, end = ' ')
            
            ## check connected vertices
            for nxt in self.graph[cur]:
                if visited[nxt] == False:
                    queue.append(nxt) ## enqueue at the tail
                    visited[nxt] = True
    
    ### depth first search
    def DFS(self, start):
        
        ## mark all vertices as not visited at beginning
        visited = [False] * len(self.graph)
        
        ## call private helper func
        self.__dfs(start, visited)
        
    def __dfs(self, cur, visited):
        
        ## print and mark current
        print(cur, end = ' ')
        visited[cur] = True
        
        ## recur to its adjacent vertices
        for ver in self.graph[cur]:
            if visited[ver] == False:
                self.__dfs(ver, visited)
                
        