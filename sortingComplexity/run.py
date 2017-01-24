# You can do all of this in the `__main__.py` file, but this file exists
# to shows how to do relative import functions from another python file in
# the same directory as this one.

import numpy as np
from .algs import quicksort, bubblesort

def basic_test():
    """
    This function is called in `__main__.py`
    Tests the sorting algorithms on small datasets for visual inspection of results.
    """
    print("This is `run()` from ", __file__)

    unsorted = np.random.rand(10)
    print("\n\tUnsorted input: ", unsorted)
    
    bsSorted = unsorted
    bubblesort(bsSorted)
    print("\n\tBubblesort output: ", bsSorted)
    
    qsSorted = unsorted
    quicksort(qsSorted)
    print("\n\tQuicksort output: ", qsSorted)
    
    print("\n\tBubblesort output == Quicksort output?  ", np.array_equal(bsSorted, qsSorted))
      
def complexity_test():
    """
    Tests complexity (as defined by time, assignments and conditionals) of
    the sorting algorithms as a function of input data size.
    """
    
    inputDataSizes = [100,200,300,400,500,600,700,800,900,1000,2000,5000]
    repsPerInputSize = 100
    
    assignments = np.zeros((len(inputDataSizes),repsPerInputSize),2)
    conditionals = np.zeros((len(inputDataSizes),repsPerInputSize),2)
    time = np.zeros((len(inputDataSizes),repsPerInputSize),2)
    
    progress = 0
    checkpoints = {'1':2,'2':4,'3':6,'4':9,'5':12,'6':15,'7':18,'8':21,'9':25,'10':50,'11':100}
    
    print("\n\tTesting Bubblesort Complexity:")
    print("\n\tinputDataSizes = ", inputDataSize)
    print("\n\trepsPerInputSize = ", repsPerInputSize,"\n")
    update_progress(progress)

    for i in range(0,len(inputDataSizes)):
        
        #run bubblesort many times for each input size
        for j in range(0,repsPerInputSize):
            data = np.random.rand(inputDataSizes[i])
            c, a, t = algs.bubblesort(data)
            conditionals[i,j,0] = c
            assignments[i,j,0] = a
            time[i,j,0] = t
                
        if i in checkpoints.keys():
            update_progress(progress)
    
    print("\n------------------------------------------------")        
    print("\n\tTesting Quicksort Complexity:")
    print("\n\tinputDataSizes = ", inputDataSize)
    print("\n\trepsPerInputSize = ", repsPerInputSize,"\n")
    progress = 0
    update_progress(progress)

    for i in range(0,len(inputDataSizes)):
        
        #run quicksort many times for each input size
        for j in range(0,repsPerInputSize):
            data = np.random.rand(inputDataSizes[i])
            c, a, t = algs.quicksort(data)
            conditionals[i,j,1] = c
            assignments[i,j,1] = a
            time[i,j,1] = t
                
        if i in checkpoints.keys():
            update_progress(progress)
    
    return assignments, conditionals, time
    
def update_progress(progress):
    print('\r[{0}] {1}%'.format('#'*(progress/10),progress,end='')
    