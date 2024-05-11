import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from decode_string import DecodeString

def test_decode_string_one():
    solver = DecodeString()
    assert solver.decodeString("3[a]2[bc]") ==  "aaabcbc"

def test_decode_string_two():
    solver = DecodeString()
    assert solver.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"
