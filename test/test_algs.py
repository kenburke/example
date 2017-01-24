import numpy as np
from example import algs

def test_pointless_sort():
    # generate random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort always returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))

    # generate a new random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort still returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))

def test_bubblesort():
    # Actually test bubblesort here. It might be useful to think about
    # some edge cases for your code, where it might fail. Some things to
    # think about: (1) does your code handle 0-element arrays without
    # failing, (2) does your code handle characters?

    #duplicates test
    x = np.array([1,2,4,0,1])  
    algs.bubblesort(x)
    assert np.array_equal(x, np.array([0,1,1,2,4]))

    #test empty vector
    x = np.array([])
    algs.bubblesort(x)
    assert np.array_equal(x, np.array([]))
    
    #test single element vector
    x = np.array([2])
    algs.bubblesort(x)
    assert np.array_equal(x, np.array([2]))
    
    #test negative values (and even size vector)
    x = np.array([-10,12,-2,5,-7,0])
    algs.bubblesort(x)
    assert np.array_equal(x, np.array([-10,-7,-2,0,5,12]))
    

def test_quicksort():

    x = np.array([1,2,4,0,1])
    # for now, just attempt to call the quicksort function, should
    # actually check output
    algs.quicksort(x)
