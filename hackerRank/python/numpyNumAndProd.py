# sum

# The sum tool returns the sum of array elements over a given axis.

# import numpy

# my_array = numpy.array([ [1, 2], [3, 4] ])

# print numpy.sum(my_array, axis = 0)         #Output : [4 6]
# print numpy.sum(my_array, axis = 1)         #Output : [3 7]
# print numpy.sum(my_array, axis = None)      #Output : 10
# print numpy.sum(my_array)                   #Output : 10
# By default, the axis value is None. Therefore, it performs a sum over all the dimensions of the input array.

# prod

# The prod tool returns the product of array elements over a given axis.

# import numpy

# my_array = numpy.array([ [1, 2], [3, 4] ])

# print numpy.prod(my_array, axis = 0)            #Output : [3 8]
# print numpy.prod(my_array, axis = 1)            #Output : [ 2 12]
# print numpy.prod(my_array, axis = None)         #Output : 24
# print numpy.prod(my_array)                      #Output : 24
# By default, the axis value is None. Therefore, it performs the product over all the dimensions of the input array.

# Task

# You are given a 2-D array with dimensions X.
# Your task is to perform the  tool over axis  and then find the  of that result.

# Input Format

# The first line of input contains space separated values of  and .
# The next  lines contains  space separated integers.

# Output Format

# Compute the sum along axis 0. Then, print the product of that sum.

# Sample Input

# 2 2
# 1 2
# 3 4
# Sample Output

# 24
# Explanation

# The sum along axis  = [ ]
# The product of this sum = 

import numpy as np

n, m = map(int, input().split())
a = np.array([input().split() for _ in range(n)], int)
print(np.prod(np.sum(a, axis=0)))
