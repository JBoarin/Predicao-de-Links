'''
Created on Aug 2, 2015

@author: cptullio
'''
from parametering.ParameterUtil import ParameterUtil
from formating.duarte.DuarteFormatting import DuarteFormatting
from parametering.Parameterization import Parameterization
from calculating.VariableSelection import VariableSelection
from calculating.Calculate import Calculate
from analysing.Analyse import Analyse
from datetime import datetime

if __name__ == '__main__':
    util = ParameterUtil(parameter_file = 'data/parameterDuarteBC.txt')
    duarte = DuarteFormatting(util.graph_file)
    duarte.readingOrginalDataset(50)
    duarte.saveGraph()
    myparams = Parameterization(util.top_rank, util.distanceNeighbors,util.lengthVertex, util.t0, util.t0_, util.t1, util.t1_, util.FeaturesChoiced, util.graph_file, util.trainnig_graph_file, util.test_graph_file, util.decay)
    print "Selecting Nodes", datetime.today()
    selecting = VariableSelection(myparams.trainnigGraph, util.nodes_notlinked_file)
    calc = Calculate(myparams, selecting, util.calculated_file, util.ordered_file)
    calc.orderingCalculate()
    analyse = Analyse(myparams, util.ordered_file, util.analysed_file)