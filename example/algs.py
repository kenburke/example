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

def qsPartition(x, first, last):
	"""
	Partition step of quicksort function.
	Makes sure all components of one partition is less than the other.
	Input: numpy array x, with starting and ending indeces.
	Output: index of partition ("pivot").
	"""
	
	pivotVal = x[last]		#arbitrarily call the last value the "pivot value"
	pivotLoc = first-1		#this will move as we swap low values into start of x
	
	for ii in range(first,last):		# go through x (O(n))
		if x[ii] <= pivotVal:
			pivotLoc += 1				# if your value is less than pivot value,
			t = x[ii]					# move the pivot location up one slot
			x[ii] = x[pivotLoc]			# and swap x[pivotLoc] with your value ii
			x[pivotLoc] = t
	
	tt = x[pivotLoc+1]					# finally, put the pivot value (which was
	x[pivotLoc+1] = x[last]				# arbitrarily chosen as the last value) and
	x[last] = tt						# swap it into the pivotLoc
	
	return (pivotLoc + 1)				# return the pivot location for quicksort
			
	

def quicksort(x, first, last):
    """
    Sorts numpy array `x` from index "first" to "last"
    	through "divide/conquer" recursive partitioning in place.
    Average runtime goes with O(n*lg n), worst-case n^2.
    """
    
    if first<last:
    	pivot = qsPartition(x,first,last)
    	quicksort(x,first,pivot-1)
    	quicksort(x,pivot+1,last)

    return x

