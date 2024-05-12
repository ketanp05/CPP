import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from product_of_array_except_self import ProductExceptSelf

def test_product_of_array_except_self_one():
    solver = ProductExceptSelf()
    assert solver.product_except_self([1,2,3,4]) == [24,12,8,6]

def test_product_of_array_except_self_two():
    solver = ProductExceptSelf()
    assert solver.product_except_self([-1,1,0,-3,3]) == [0,0,9,0,0]