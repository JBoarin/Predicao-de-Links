'''
Created on 8 de jul de 2015

@author: CarlosPM
'''
from featuring.AASFeature import AASFeature
from featuring.CNFeature import CNFeature
from featuring.JCFeature import JCFeature
from featuring.PAFeature import PAFeature
from formating.dblp.Formating import Formating
from featuring.TimeScore import TimeScore

class ParameterUtil(object):
    


    def __init__(self, parameter_file):
        parameterFile = Formating.get_abs_file_path(parameter_file)
        
        AllFeatures = []
        AllFeatures.append(AASFeature())
        AllFeatures.append(CNFeature())
        AllFeatures.append(JCFeature())
        AllFeatures.append(PAFeature())
        AllFeatures.append(TimeScore())
        
        self.FeaturesChoiced = []
        
        with open(parameterFile) as f:
            lines = f.readlines()
            f.close()
        for line in lines:
            line = line.strip()
            line = line.replace('\n','')
            cols = line.split('\t')
            if cols[0] == 'original_file':
                self.original_file = cols[1]
            if cols[0] == 'graph_file':
                self.graph_file = cols[1]
            if cols[0] == 'trainnig_graph_file':
                self.trainnig_graph_file = cols[1]
            if cols[0] == 'test_graph_file':
                self.test_graph_file = cols[1]
            if cols[0] == 'nodes_notlinked_file':
                self.nodes_notlinked_file = cols[1]
            if cols[0] == 'calculated_file':
                self.calculated_file = cols[1]
            if cols[0] == 'ordered_file':
                self.ordered_file = cols[1]
            if cols[0] == 'analysed_file':
                self.analysed_file = cols[1]
            if cols[0] == 'distanceNeighbors':
                self.distanceNeighbors = int(cols[1])
            if cols[0] == 'lengthVertex':
                self.lengthVertex = int(cols[1])
            if cols[0] == 't0':
                self.t0 = int(cols[1])
            if cols[0] == 't0_':
                self.t0_ = int(cols[1])
            if cols[0] == 't1':
                self.t1 = int(cols[1])
            if cols[0] == 't1_':
                self.t1_ = int(cols[1])
            if cols[0] == 'decay':
                self.decay = float(cols[1])
            if cols[0] == 'top_rank':
                self.top_rank = int(cols[1])
            if cols[0] == 'features':
                features = cols[1].split(';')
                for feature in features:
                    featureandweight = feature.split(':')
                    self.FeaturesChoiced.append([AllFeatures[int(featureandweight[0])], int(featureandweight[1])])
                
                
        