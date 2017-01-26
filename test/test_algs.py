import numpy as np
from sortingComplexity import algs

def test_pointless_sort():
    # generate random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort always returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))

    # generate a new random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort still returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))
    
    assert 1 == 2

def test_bubblesort():

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
    
    #test char (should not change it)
    x = np.array([10,2,5,7,'r'])
    algs.bubblesort(x)
    assert np.array_equal(x, np.array([10,2,5,7,'r']))

def test_quicksort():

    #duplicates test
    x = np.array([1,2,4,0,1])  
    algs.quicksort(x)
    assert np.array_equal(x, np.array([0,1,1,2,4]))

    #test empty vector
    x = np.array([])
    algs.quicksort(x)
    assert np.array_equal(x, np.array([]))
    
    #test single element vector
    x = np.array([2])
    algs.quicksort(x)
    assert np.array_equal(x, np.array([2]))
    
    #test negative values (and even size vector)
    x = np.array([-10,12,-2,5,-7,0])
    algs.quicksort(x)
    assert np.array_equal(x, np.array([-10,-7,-2,0,5,12]))
    
    #test char (should not change it)
    x = np.array([10,2,5,7,'r'])
    algs.quicksort(x)
    assert np.array_equal(x, np.array([10,2,5,7,'r']))
