import numpy as np
from timeit import default_timer as timer


def pointless_sort(x):
    """
    This function always returns the same values to show how testing
    works, check out the `test/test_alg.py` file to see.
    """
    return np.array([1,2,3])

def bubblesort(x):

    """
    Sorts numpy array `x` by swapping adjacent elements when needed.
    Runtime goes with O(n^2).
    """
    
    start = timer()         # for measuring complexity
    assignments = 0             
    conditionals = 0
    
    conditionals += 2
    if not x.dtype == 'int64' and not x.dtype == 'float64':
        print("Must have only numbers.")
        return conditionals, assignments
      
    for i in range(0,np.size(x)):
        for j in range(np.size(x),i+1,-1):
        
            conditionals += 1
            
            if x[j-1]<x[j-2]:
            
                assignments += 3
                temp = x[j-1]
                x[j-1] = x[j-2]
                x[j-2] = temp
    
    end = timer()
    
    elapsedTime = np.round(end-start,3)     # in seconds
                   
    return conditionals, assignments, elapsedTime

def partition(x, first, last):

    """
    Partition step of quicksort function.
    Makes sure all components of one partition is less than the other.
    Input: numpy array x, with starting and ending indeces.
    Output: index of partition ("pivot").
    """
    
    conditionals = 0
    assignments = 0
    
    assignments += 2
    pivotVal = x[last]      #arbitrarily call the last value the "pivot value"
    pivotLoc = first-1      #this will move as we swap low values into start of x
    
    for ii in range(first,last):        # go through x (O(n))
    
        conditionals += 1
        if x[ii] <= pivotVal:
            
            assignments += 4
            
            pivotLoc += 1               # if your value is less than pivot value,
            t = x[ii]                   # move the pivot location up one slot
            x[ii] = x[pivotLoc]         # and swap x[pivotLoc] with your value ii
            x[pivotLoc] = t
    
    assignments += 3
    
    tt = x[pivotLoc+1]                  # finally, put the pivot value (which was
    x[pivotLoc+1] = x[last]             # arbitrarily chosen as the last value) and
    x[last] = tt                        # swap it into the pivotLoc
    


    # return the pivot location for quicksort
    return (pivotLoc + 1), conditionals, assignments       
    

def quicksort(x, first=None, last=None):

    """
    Sorts numpy array `x` from index "first" to "last"
        through "divide/conquer" recursive partitioning in place.
        Counters are used to keep track of complexity.
    Average runtime goes with O(n*lg n), worst-case n^2.
    """
    
    start = timer()
    assignments = 0
    conditionals = 0
    t1, t2, t3 = (0,0,0)
    
    conditionals += 1
    if not x.dtype == 'int64' and not x.dtype == 'float64':
        print("Must have only numbers.")
        return conditionals, assignments

    
    conditionals += 2
    if first is None:
        assignments += 1
        first = 0
    if last is None:
        assignments += 1
        last = np.size(x)-1
        
    conditionals += 1
    if first<last:
        assignments += 7
        
        pivot, c, a = partition(x,first,last)
        conditionals += c
        assignments += a
        c,a,t = quicksort(x,first,pivot-1)
        conditionals += c
        assignments += a
        c,a,t = quicksort(x,pivot+1,last)
        conditionals += c
        assignments += a
    
    end = timer()
    elapsedTime = end-start              # in seconds
        
    return conditionals, assignments, elapsedTime
    
