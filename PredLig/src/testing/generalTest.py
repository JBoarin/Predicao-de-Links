import unittest

import networkx
from formating.dblp.Formating import Formating
import matplotlib.pyplot as plt

#python -m unittest GeneralTestings

class GeneralTest(unittest.TestCase):
    
      
    
    
    def test_generating_graph(self):

        original = 'data/original/DBLP_Citation_2014_May/domains/ExemploMenor.txt'
        article = 'data/formatado/dblp_exemploMenor_article.txt'
        author = 'data/formatado/dblp_exemploMenor_author.txt'
        edge_file = 'data/formatado/dblp_exemploMenor_articlearthor.txt'
        graph_file = 'data/formatado/dblp_exemploMenor_graph.txt'
        
        format = Formating(original, article, author, edge_file, graph_file)
        networkx.draw_networkx(format.fullGraph)
        plt.show()
        
    def test_reading_graph(self):
        graph_file = 'data/formatado/dblp_exemploMenor_graph.txt'
        graph = networkx.read_gml(Formating.get_abs_file_path(graph_file))
        networkx.draw_networkx(graph)
        plt.show()
        
        
        
        
            
      
        
        
if __name__ == "__main__":
    unittest.main()