import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from longest_consecutive_sequence import LongestCommonSequence

def test_longest_common_sequence_one():
    solver = LongestCommonSequence()
    assert solver.longest_common_seq([100, 4, 200, 1, 3, 2]) == 4

