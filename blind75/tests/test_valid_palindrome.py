import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from valid_palindrome import ValidPalindrome

def test_valid_palindrome_one():
    solver = ValidPalindrome()
    assert solver.valid_palindrome("A man, a plan, a canal: Panama") == True

def test_valid_palindrome_two():
    solver = ValidPalindrome()
    assert solver.valid_palindrome("hello world") == False