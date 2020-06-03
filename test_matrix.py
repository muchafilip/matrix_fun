import pytest
import random
from matrix_class_final import Matrix
from testing_class import ask_user


def test_random():
    pass


def test_user_input():
    pass
    
def test_mul():
    m1 = Matrix([[1, 2], [2, 3]])
    m2 = Matrix([[3], [2]])
    result1 = [[7], [12]]
    
    assert m1.multiply(m2) == result1

def test_mul2():
    m3 = Matrix([[1,2,3,4],[4,3,2,1]])
    m4 = Matrix([[1,2],[1,2],[2,3],[2,3]])
    result2 = [[17,27],[13,23]]

    assert m3.multiply(m4) == result2
