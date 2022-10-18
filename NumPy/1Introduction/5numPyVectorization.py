#from course: https://www.educative.io/courses/from-python-to-numpy/m2qBD4J6lL9
import numpy as np

#Vectorized Approach can be found from two ways:
#Itertools: https://docs.python.org/3/library/itertools.html
#Using Itertools
from modules import tools #get timeit function from tools.py(custom module)
from itertools import accumulate #get accumulate function from built accumulate module
import random 
def random_walk_faster(n=1000):
  steps = random.choices([-1,+1], k=n)
  return [0]+list(accumulate(steps))#get the total number of steps

walk = random_walk_faster(1000) 
tools.timeit("random_walk_faster(n=10000)", globals())# calculates the total loops and time per loop

#Using Numpy
def random_walk_fastest(n=1000):
    # No 's' in NumPy choice (Python offers choice & choices)
    steps = np.random.choice([-1,+1], n)
    return np.cumsum(steps) #return the cumulative sum of the steps along a given axis.

walk = random_walk_fastest(1000)
tools.timeit("random_walk_fastest(n=1000)", globals())
#calculates the total loops and time per loop