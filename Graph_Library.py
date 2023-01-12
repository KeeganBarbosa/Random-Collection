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
                edgeset.append({vertex,neighbour})
        return(edgeset)
    
    def get_connected_components(self):
        seen = set()
        components = []
        for v in self.graph:
            if v not in seen:
                component = []
                nodes = {v}
                while nodes:
                    v = nodes.pop()
                    seen.add(v)
                    component.append(v)
                    nodes.update(self.graph[v].difference(seen))
                    components.append(component)
        return(components)
   
    def is_connected(self):
        if len(self.graph.edges)>len(self.graph.vertices)*(len(self.graph.vertices)-1)/2:
            return("Graph is connected.")
        if len(self.graph.get_connected_components)==1:
            return("Graph is connected.")
        else:
            return("Graph is disconnected.")