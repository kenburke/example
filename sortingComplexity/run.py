# You can do all of this in the `__main__.py` file, but this file exists
# to shows how to do relative import functions from another python file in
# the same directory as this one.
import numpy as np
from .algs import quicksort, bubblesort

def run_stuff():
    """
    This function is called in `__main__.py`
    """
    print("This is `run()` from ", __file__)

    x = np.random.rand(10)
    print("\n\tUnsorted input: ", x)

    print("\n\tBubble sort output: ", bubblesort(x))
    print("\n\tQuick sort output: ", quicksort(x))
