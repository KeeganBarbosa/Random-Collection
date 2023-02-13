# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 09:37:13 2023

@author: Owner
"""

class Graphs(object):
    def __init__(self,graph=None):
        if graph==None:
            graph={}
        self.graph=graph
    
    def nbhd(self,vertex):
        return(self.graph[vertex])
    
    def vertices(self):
        return(self._graph.keys())
    
    def edges(self):
        edgeset=[]
        for vertex in self.graph:
            for neighbour in self.graph[vertex]:
                if {vertex,neighbour} not in edgeset:
                    edgeset.append({vertex,neighbour})
        return(edgeset)
    
"""Below is a collection of graph operations of importance. All rely on applications of BFS."""
    
def BFS(G,vertex):
    seen = []
    queue = []
    queue.append(vertex)
    seen.append(vertex)
    while queue:
        stage= queue.pop(0)
        for nextvertex in G[stage]:
            if nextvertex not in seen:
                seen.append(nextvertex)
                queue.append(nextvertex)
    return(seen)



def get_connected_components(Input):
    seen = set()
    components = []
    for v in Input:
        if v not in seen:
            component = []
            nodes = {v}
            while nodes:
                v = nodes.pop()
                seen.add(v)
                component.append(v)
                nodes.update(Input[v].difference(seen))
                if component not in components:
                    components.append(component)
        return(components)
   

def is_connected(Input):
    if len(get_connected_components(Input))==1:
        return("Graph is connected.")
    else:
        return("Graph is disconnected.")        


"""The below could be further optimized, but is functional."""
def distance(Graph,v,w):
    seen={}
    queue=[]
    seen.add(v)
    queue.append(v)
    d=0
    if v==w:
        return(d)
    else:
        while queue:
            d+=1
            for vertex in queue:
                for neighbour in G[vertex]:
                    if neighbour == w:
                        return(d)
                    else:
                        if neighbour not in seen:
                            queue.pop()
                            seen.add(neighbour)
                            queue.append(neighbour)
            
            
        

G={1:{2,3},2:{1},3:{1}}

print(BFS(G,3))

