'''Write a program to illustrate following numpy array attributes, ndarray, ndim, nd.shape, ndarray.size, 
ndarray.dtype, ndarray.itemsize, ndarray.data'''

import numpy as np
def main():
    arr = np.array([[1,2,3],[2,3,4]])
    print("Array:\n",arr)
    print("Dimention: ", arr.ndim)
    print("Shape: ", arr.shape)
    print("Total number of elements: ", arr.size)
    print("Datatype: ", arr.dtype)
    print("Size in bytes of each elements: ", arr.itemsize)
    print("Buffer containing array elements", arr.data)


main()