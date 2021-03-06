'''
Created on Jun 15, 2015

@author: cptullio
'''
import networkx
from formating.dblp.Formating import Formating
import os.path
from datetime import datetime
import gc


class Parameterization(object):
    
    
    def generating_Test_Graph(self ):
        if not os.path.exists(Formating.get_abs_file_path(self.filePathTestGraph)):
            if self.graph == None:
                print "Reading Full graphs", datetime.today()
                self.graph = Formating.reading_graph(self.filePathGraph)
            print "Generating Testing graphs", datetime.today()
        
            self.testGraph = Formating.get_graph_from_period(self.graph, self.t1, self.t1_)
            networkx.write_graphml(self.testGraph, Formating.get_abs_file_path(self.filePathTestGraph))
        else:
            print "Reading testing graph", datetime.today()
            self.testGraph = Formating.reading_graph(self.filePathTestGraph)
            
    def generating_Training_Graph(self):
        if not os.path.exists(Formating.get_abs_file_path(self.filePathTrainingGraph)):
            if self.graph == None:
                print "Reading Full graphs", datetime.today()
                self.graph = Formating.reading_graph(self.filePathGraph)
            
            print "Generating Trainnig graphs", datetime.today()
           
            self.trainnigGraph = Formating.get_graph_from_period(self.graph, self.t0, self.t0_)
            
            networkx.write_graphml(self.trainnigGraph, Formating.get_abs_file_path(self.filePathTrainingGraph))
        else:
            print "Reading Trainnig graph", datetime.today()
            self.trainnigGraph = Formating.reading_graph(self.filePathTrainingGraph)
        
        for feature in self.featuresChoice:
            feature[0].graph = self.trainnigGraph
    
    def get_edges(self, graph):
        myedges = list([n,d] for n,d in graph.nodes(data=True) if d['node_type'] == 'E')
        result = len(myedges)
        del myedges
        myedges = None
        gc.collect()
        return result
    
    def get_nodes(self, graph):
        mynodes = list([n,d] for n,d in graph.nodes(data=True) if d['node_type'] == 'N') 
        result =  len(mynodes)
        del mynodes
        mynodes = None
        gc.collect()
        return result
    
    
    def __init__(self, keyword_decay, lengthVertex, t0, t0_, t1, t1_, featuresChoice, filePathGraph, filePathTrainingGraph, filePathTestGraph, decay, FullGraph = None):
        self.lengthVertex = lengthVertex
        self.featuresChoice = featuresChoice
        self.keyword_decay = keyword_decay
        self.decay = decay
        self.t0_ = t0_
        self.t0 = t0
        self.t1 = t1
        self.t1_ = t1_
        self.graph = FullGraph
        self.filePathGraph = filePathGraph
        self.filePathTrainingGraph = filePathTrainingGraph
        self.filePathTestGraph = filePathTestGraph
        self.linkObjects = {}
        self.debugar = False
     
        
       
         
        