import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from group_anagrams import GroupAnagramsProblem

def test_group_anagrams_basic():
    solver = GroupAnagramsProblem()
    assert solver.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

def test_group_anagrams_empty():
    solver = GroupAnagramsProblem()
    assert solver.groupAnagrams([]) == []

def test_group_anagrams_no_anagrams():
    solver = GroupAnagramsProblem()
    assert solver.groupAnagrams(["irrelevant", "hello", "shit"]) == [["irrelevant"], ["hello"], ["shit"]]