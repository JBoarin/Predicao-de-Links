'''
Created on Jun 16, 2015

@author: cptullio
'''
from featuring.FeatureBase import FeatureBase
import networkx
from datetime import datetime
import ast

class DomainTimeScorevTwo(FeatureBase):
    '''
    TimeScore modified by Carlos and Ronaldo
    '''
    def __repr__(self):
        return 'DTSv2'
    

    def __init__(self):
        super(DomainTimeScorevTwo, self).__init__()
        self.debugar = False
        
    
    def get_jacard_keywords(self, bagofWordsNode1, bagofWordsNode2):
        f = (float)(len(bagofWordsNode1.intersection(bagofWordsNode2)))
        x = (float)(len(bagofWordsNode1.union(bagofWordsNode2)))
        if x == 0:
            return 0
        return f/x
    
    def execute(self, node1, node2):
        
        #if node1=='1760' and node2 =='2003':
        #    self.debugar = True
        #else:
        #    self.debugar = False
        pair_common_neighbors  = self.get_common_neighbors(node1, node2)
        if len(pair_common_neighbors) == 0:
            return 0
        if self.debugar:
            print node1, node2, pair_common_neighbors
        
        timescoreValue = float(0)
        for pair_common_neighbor in pair_common_neighbors:
            timesofLinks = []
            objectsNode1 = self.get_ObjectsofLinks(self.graph, node1, pair_common_neighbor)
            objectsNode2 = self.get_ObjectsofLinks(self.graph, node2, pair_common_neighbor)
            
            
            timesofLinksNode1 = []
            timesofLinksNode2 = []
            bagofWordsNode1 = set()
            bagofWordsNode2 = set()
            
            for t1 in objectsNode1:
                timesofLinksNode1.append(t1[0])
                for bt1 in t1[1]:
                    bagofWordsNode1.add(bt1)
            for t2 in objectsNode2:
                timesofLinksNode2.append(t2[0])
                for bt2 in t2[1]:
                    bagofWordsNode2.add(bt2)
            
            timesofLinksNode1.sort(reverse=True)
            timesofLinksNode2.sort(reverse=True)
            timesofLinks.append(timesofLinksNode1)
            timesofLinks.append(timesofLinksNode2)
            
            jcKeyworkds = self.get_jacard_keywords(bagofWordsNode1, bagofWordsNode2)
            if self.debugar:
                print 'bags node1 and node2:', bagofWordsNode1, bagofWordsNode2
                print 'Jc keyworkds: ', jcKeyworkds
               
                print 'Times Nodes 1',timesofLinksNode1
                print 'Times Nodes 2',timesofLinksNode2
                print 'Times Links', timesofLinks
           
            #Harmonic Mean of Publications
            total = float(0)
            for publications in timesofLinks:
                total = total + 1/float(len(publications))
            hm = 2 / total
            if self.debugar:
                print 'Harmonic meam:', hm
            
            k =  int(self.parameter.t0_)  - int(max(list(timesofLinks))[0])
            decayfunction = (1 - self.parameter.decay) ** k
            control = (abs( max(timesofLinksNode1) - max(timesofLinksNode2) ) + 1)
            ts = (hm * decayfunction) + (jcKeyworkds * 4)  /  (control)
            timescoreValue = timescoreValue + ts 
            if self.debugar:
                print 'TS parcial:', timescoreValue
        return timescoreValue    
            
        