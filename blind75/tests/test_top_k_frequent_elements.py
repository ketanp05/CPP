import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from top_k_frequent_elements import TopKFrequentElements

def test_top_k_frequent_elements_empty():
    solver = TopKFrequentElements()
    assert solver.topKFrequent([], 3) == []

# def test_top_k_frequent_elements_unique():
#     solver = TopKFrequentElements()
#     assert solver.topKFrequent([1,2,3,4,45,57,68], 2) == [1, 2]


