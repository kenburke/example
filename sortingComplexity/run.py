# You can do all of this in the `__main__.py` file, but this file exists
# to shows how to do relative import functions from another python file in
# the same directory as this one.

import numpy as np
from math import log
import sys
import matplotlib.pyplot as plt
from timeit import default_timer as timer
import progressbar as pb
from .algs import quicksort, bubblesort

def basic_test():
    """
    This function is called in `__main__.py`
    Tests the sorting algorithms on small datasets for visual inspection of results.
    """
    print("\nThis is `run()` from ", __file__)

    unsorted = np.random.rand(10)
    print("\n\tUnsorted input: ", unsorted)
    
    bsSorted = unsorted
    bubblesort(bsSorted)
    print("\n\tBubblesort output: ", bsSorted)
    
    qsSorted = unsorted
    quicksort(qsSorted)
    print("\n\tQuicksort output: ", qsSorted)
    
    print("\n\tBubblesort output == Quicksort output?  ", np.array_equal(bsSorted, qsSorted))
    
    return np.array_equal(bsSorted, qsSorted)
      
def complexity_experiment():
    """
    Tests complexity (as defined by time, assignments and conditionals) of
    the sorting algorithms as a function of input data size.
    """
    
    inputDataSizes = [100,200,300,400,500,600,700,800,900,1000]
    repsPerInputSize = 100
    
    assignments = np.zeros((2,len(inputDataSizes),repsPerInputSize))
    conditionals = np.zeros((2,len(inputDataSizes),repsPerInputSize))
    time = np.zeros((2,len(inputDataSizes),repsPerInputSize))
    
#    progress = 0
    bar = pb.ProgressBar(widgets=[
        ' [', pb.Timer(), '] ',
        pb.Bar(),
        ' (', pb.ETA(), ') ',
    ])
    
    checkpoints = {'0':4,'1':8,'2':16,'3':24,'4':36,'5':48,'6':60,'7':72,'8':84,'9':100}

    print("\n------------------------------------------------\n")        
    print("\tTesting Bubblesort Complexity:")
    print("\tinputDataSizes = ", inputDataSizes)
    print("\trepsPerInputSize = ", repsPerInputSize,"\n")

    for i in bar(range(0,len(inputDataSizes))):

        #run bubblesort many times for each input size
        for j in range(0,repsPerInputSize):
            data = np.random.rand(inputDataSizes[i])
            
            #time
            start = timer()
            
            c, a = bubblesort(data)
            
            end = timer()
            time[0,i,j] = np.round(end-start,3)     # in seconds
            
            #record conditionals and assignments
            conditionals[0,i,j] = c
            assignments[0,i,j,] = a
            
#         progress = checkpoints[str(i)]
#         if str(i) in checkpoints.keys():
#             update_progress(progress)
    
    print("\n------------------------------------------------\n")        
    print("\tTesting Quicksort Complexity:")
    print("\tinputDataSizes = ", inputDataSizes)
    print("\trepsPerInputSize = ", repsPerInputSize,"\n")
    
#    progress = 0
    bar = pb.ProgressBar(widgets=[
        ' [', pb.Timer(), '] ',
        pb.Bar(),
        ' (', pb.ETA(), ') ',
    ])

    for i in bar(range(0,len(inputDataSizes))):
    
        #run quicksort many times for each input size
        for j in range(0,repsPerInputSize):
            data = np.random.rand(inputDataSizes[i])
            
            #time
            start = timer()
            
            c, a = quicksort(data)
            
            end = timer()
            time[1,i,j] = np.round(end-start,3)     # in seconds

            #record conditionals and assignments
            conditionals[1,i,j] = c
            assignments[1,i,j] = a

#         progress = checkpoints[str(i)]    
#         if str(i) in checkpoints.keys():
#             update_progress(progress)
    
    print("\n------------------------------------------------\n")        
    
    complexity = {'assign':assignments,'cond':conditionals,'time':time}
    inputData = {'sizes':inputDataSizes,'reps':repsPerInputSize}
    
    return complexity, inputData

def complexity_visualize(complexity, inputData):
    """
    Plots results of complexity_experiment()
    """
    
    
    ##### Organize Data
    
    
    #first get averages and stdev of assign, cond and time for each input data size for bubblesort
    meanBSAssign = np.average(complexity['assign'][0,:,:],axis=1)
    meanBSCond = np.average(complexity['cond'][0,:,:],axis=1)
    meanBSTime = np.average(complexity['time'][0,:,:],axis=1)
    stdBSAssign = np.std(complexity['assign'][0,:,:],axis=1)
    stdBSCond = np.std(complexity['cond'][0,:,:],axis=1)
    stdBSTime = np.std(complexity['time'][0,:,:],axis=1)
    
    #now quicksort
    meanQSAssign = np.average(complexity['assign'][1,:,:],axis=1)
    meanQSCond = np.average(complexity['cond'][1,:,:],axis=1)
    meanQSTime = np.average(complexity['time'][1,:,:],axis=1)
    stdQSAssign = np.std(complexity['assign'][1,:,:],axis=1)
    stdQSCond = np.std(complexity['cond'][1,:,:],axis=1)
    stdQSTime = np.std(complexity['time'][1,:,:],axis=1)
    
    
    ##### Plot all results, on log and scalar scales
    
    
    fig1 = plt.figure(figsize=(20,10))
    st = fig1.suptitle('Runtime, Assignments, Conditionals Comparison\nBubblesort (red) vs Quicksort (blue)\n',
        fontsize="x-large")
    
    #plot Runtime Differences (log scale)
    plt.subplot(231)
    plt.errorbar(inputData['sizes'],meanBSTime,yerr=stdBSTime,color="r")
    plt.errorbar(inputData['sizes'],meanQSTime,yerr=stdQSTime,color="b")
        
    plt.yscale('log')
    plt.ylabel('log')
    plt.title('Runtime (seconds)', fontsize=10)
    
    plt.axis([0.95*min(inputData['sizes']),1.1*max(inputData['sizes']),
        0.95*min(min(meanBSTime),min(meanQSTime)),1.3*max(max(meanBSTime),max(meanQSTime))])  
                      
    #plot Runtime Differences
    plt.subplot(234)
    plt.errorbar(inputData['sizes'],meanBSTime,yerr=stdBSTime,color="r")
    plt.errorbar(inputData['sizes'],meanQSTime,yerr=stdQSTime,color="b")
        
    plt.xlabel('Input Data Size')
    plt.ylabel('scalar')
    
    plt.axis([0.95*min(inputData['sizes']),1.1*max(inputData['sizes']),
        0.95*min(min(meanBSTime),min(meanQSTime)),1.2*max(max(meanBSTime),max(meanQSTime))])  
                  
    #plot Assign Differences (log)
    plt.subplot(232)
    plt.errorbar(inputData['sizes'],meanBSAssign,yerr=stdBSAssign,color="r")
    plt.errorbar(inputData['sizes'],meanQSAssign,yerr=stdQSAssign,color="b")
        
    plt.yscale('log')
    plt.title('Assignments', fontsize=10)
    
    plt.axis([0.95*min(inputData['sizes']),1.1*max(inputData['sizes']),
        0.95*min(min(meanBSAssign),min(meanQSAssign)),1.2*max(max(meanBSAssign),max(meanQSAssign))])  
                  
    #plot Assign Differences
    plt.subplot(235)
    plt.errorbar(inputData['sizes'],meanBSAssign,yerr=stdBSAssign,color="r")
    plt.errorbar(inputData['sizes'],meanQSAssign,yerr=stdQSAssign,color="b")
        
    plt.xlabel('Input Data Size')
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

    plt.axis([0.95*min(inputData['sizes']),1.1*max(inputData['sizes']),
        0.95*min(min(meanBSAssign),min(meanQSAssign)),1.2*max(max(meanBSAssign),max(meanQSAssign))])  
        
    #plot Conditionals Differences (log)
    plt.subplot(233)
    plt.errorbar(inputData['sizes'],meanBSCond,yerr=stdBSCond, color="r")
    plt.errorbar(inputData['sizes'],meanQSCond,yerr=stdQSCond,color="b")
        
    plt.yscale('log')
    plt.title('Conditionals', fontsize=10)

    plt.axis([0.95*min(inputData['sizes']),1.1*max(inputData['sizes']),
        0.95*min(min(meanBSCond),min(meanQSCond)),1.2*max(max(meanBSCond),max(meanQSCond))])  
                  
    #plot Conditionals Differences
    plt.subplot(236)
    plt.errorbar(inputData['sizes'],meanBSCond,yerr=stdBSCond, color="r")
    plt.errorbar(inputData['sizes'],meanQSCond,yerr=stdQSCond,color="b")
        
    plt.xlabel('Input Data Size')
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

    plt.axis([0.95*min(inputData['sizes']),1.1*max(inputData['sizes']),
        0.95*min(min(meanBSCond),min(meanQSCond)),1.2*max(max(meanBSCond),max(meanQSCond))])  

    #show and save                  
    plt.show()

    st.set_y(0.95)
    fig1.subplots_adjust(top=0.85)
    
    fig1.savefig("plots/allComplexities.png")
    
    
    ##### Plot time results on log-log scale, to show it's a power function
    
    #generate approximate functions for N^2 and N*lgN times (hand-tuned constants)
    
    approxSquareComparison = np.array(inputData['sizes'])**2/(1500000.)
    logInput = [log(y,2) for y in inputData['sizes']]
    nLogNComparison = np.array(inputData['sizes'])*np.array(logInput)/(600000.)
    
    #plot data alongside estimates
    
    fig2 = plt.figure(figsize=(10,5))
    st = fig2.suptitle('Runtime on log-log axes\nBubblesort (red) vs Quicksort (blue) : N^2 (solid black) vs N*lgN (dashed black)',
        fontsize="large")
    
    plt.errorbar(inputData['sizes'],meanBSTime,yerr=stdBSTime,color="r")
    plt.errorbar(inputData['sizes'],meanQSTime,yerr=stdQSTime,color="b")
    plt.plot(inputData['sizes'],approxSquareComparison,'k-')
    plt.plot(inputData['sizes'],nLogNComparison,'k--')
        
    plt.yscale('log')
    plt.xscale('log')
    plt.ylabel('Runtime (seconds, log)')
    plt.xlabel('Input Data Size (log)')
        
    plt.axis([0.95*min(inputData['sizes']),1.1*max(inputData['sizes']),
        0.01*min(min(meanBSTime),min(meanQSTime)),1.8*max(max(meanBSTime),max(meanQSTime))])  
    
    #show and save  
                    
    plt.show()    
    fig2.savefig("plots/timeComplexityLogLog.png")
    
    

def complexity_test():

    complexity, inputData = complexity_experiment()
    
    complexity_visualize(complexity, inputData)

def update_progress(progress):
    sys.stdout.write('\r')
    sys.stdout.write('[{0}{1}] {2}%'.format('#'*(progress//2),' '*(50-progress//2),progress,progress))    
    sys.stdout.flush()
    