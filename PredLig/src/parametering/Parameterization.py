'''
Created on Jun 15, 2015

@author: cptullio
'''
import networkx
from formating.dblp.Formating import Formating
import os.path
from datetime import datetime


class Parameterization(object):
    
    def __init__(self, top_rank, distanceNeighbors, lengthVertex, t0, t0_, t1, t1_, featuresChoice, filePathGraph, filePathTrainingGraph, filePathTestGraph, decay, FullGraph = None):
        self.distanceNeighbors = distanceNeighbors
        self.lengthVertex = lengthVertex
        self.featuresChoice = featuresChoice
        self.top_rank = top_rank
        if FullGraph == None: 
            self.graph = Formating.reading_graph(filePathGraph)
        else:
            self.graph = FullGraph
        self.decay = decay
        self.t0_ = t0_
        if not os.path.exists(Formating.get_abs_file_path(filePathTrainingGraph)):
            print "Generating Trainnig graphs", datetime.today()
       
            self.trainnigGraph = Formating.get_graph_from_period(self.graph, t0, t0_)
            networkx.write_graphml(self.trainnigGraph, Formating.get_abs_file_path(filePathTrainingGraph))
        else:
            self.trainnigGraph = Formating.reading_graph(filePathTrainingGraph)
       
        if not os.path.exists(Formating.get_abs_file_path(filePathTestGraph)):
            print "Generating Testing graphs", datetime.today()
        
            self.testGraph = Formating.get_graph_from_period(self.graph, t1, t1_)
            networkx.write_graphml(self.testGraph, Formating.get_abs_file_path(filePathTestGraph))
        else:
            self.testGraph = Formating.reading_graph(filePathTestGraph)
        
         
        for feature in self.featuresChoice:
            feature[0].graph = self.trainnigGraph
        