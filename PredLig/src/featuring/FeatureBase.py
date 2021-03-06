'''
Created on Jun 16, 2015

@author: cptullio
'''
from abc import abstractmethod
import networkx as networkx

class FeatureBase(object):
    '''
    Base class for help prepare the features will be used
    '''
    def __init__(self):
        self.graph = None
        self.neighbors_node1 = None
        self.myneighbors = {}
        self.neighbors_node2 = None
        self.parameter = None
        self.debugar = False
    
    
    def get_ObjectsofLinks(self, graph, node1, node2):
        result = []
        for node in networkx.common_neighbors(graph, node1, node2):
            if node in self.parameter.linkObjects:
                if self.debugar:
                    print "already found the time for paper ", node
            else:
                if self.debugar:
                    print "rescuing time from paper: ", str(node)
                
                MaxAmplitude = self.parameter.t0_ - 3
                if self.debugar:
                    print 'amplitude maxima:' , MaxAmplitude
                paper = list(d for n,d in graph.nodes(data=True) if d['node_type'] == 'E' and n == node )
                if self.debugar:
                    print 'Informacoes sobre o paper:' ,paper
                if paper[0]['time'] >= MaxAmplitude:
                    self.parameter.linkObjects[node] = [paper[0]['time'], eval(paper[0]['keywords'])]
            if self.debugar:
                print 'Informacoes sobre o paper ja na memoria:' , self.parameter.linkObjects[node]
            result.append(self.parameter.linkObjects[node])
        
        return result

    
    def generate_all_node_neighborsfromNode(self, node1):
        if node1 in self.myneighbors:
            return self.myneighbors[node1]
        self.myneighbors[node1] = set(self.all_node_neighbors(node1))
        return self.myneighbors[node1]
   
       
    @abstractmethod
    def execute(self, node1, node2):
        raise RuntimeError('not implemented')
    
    def all_neighbors(self, node):
        neighbors = set()
        for neighbor in list(networkx.all_neighbors(self.graph, node)):
            neighbors.add(neighbor)
        return neighbors - set([node])
    
    #from graph where the edge is define by other type of node
    def all_node_neighbors(self, node):
        neighbors = set()
        for node_edge in list(networkx.all_neighbors(self.graph, node)):
            for neighbor in list(networkx.all_neighbors(self.graph, node_edge)):
                neighbors.add(neighbor)
        return neighbors - set([node])
    
    
    def get_common_neighbors(self, node1, node2):
        neighbors_node_1 = self.generate_all_node_neighborsfromNode(node1)
        neighbors_node_2 = self.generate_all_node_neighborsfromNode(node2)
        return neighbors_node_1.intersection(neighbors_node_2)    
    
        
    
