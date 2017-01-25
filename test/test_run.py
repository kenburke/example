import numpy as np
from sortingComplexity import run

def test_basic_test():
    #asserts that the outputs of both algorithms in "basic test" are equivalent
    assert run.basic_test()
    
def test_complexity_experiment_and_vis():

    c,i = run.complexity_experiment()
    
    #format of output is correct (two dictionaries)
    assert type(c)==dict
    assert type(i)==dict