import numpy as np

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
	
	print("Unsorted Input :   ", x)
	
	for i in range(0,np.size(x)):
		for j in range(np.size(x),i+1,-1):
			if x[j-1]<x[j-2]:
				temp = x[j-1]
				x[j-1] = x[j-2]
				x[j-2] = temp
				
	print("\nSorted Output :  ", x, "\n\n")
	
	return x

def quicksort(x):
    """
    Describe how you are sorting `x`
    """

    return x

