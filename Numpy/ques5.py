'''a) Create a 5x5 array of integers between 0(inclusive) and 10(exclusive)
b) Create a sequence of equally gapped 5 numbers in range 0 to 100
c) Convert 1D array to 3D array
d) Convert all four elements of array from float to integer datatype
e) Stact two numpy arrays as horizontally and vertically
f) From two arrays extract the indices in which the elements in the two arrays match'''

import numpy as np

arr1 = np.random.randint(0,10,(2,3),int)
print(arr1)

arr2 = np.linspace(0,100,6)
print(arr2)

arr3 = np.reshape(arr2,(2,3))
print(arr3)

arr4 = arr3.astype(int)
print(arr4)


arr1 = arr1.reshape((1,6))
verticalStack = np.vstack((arr1,arr2))
print(verticalStack)

arr1 = arr1.reshape((6,1))
arr2 = arr2.reshape((6,1))
horizontallyStack = np.hstack((arr1,arr2))
print(horizontallyStack)


arrx = np.array([1,2,3,4,5])
arry = np.array([5,4,3,4,1])
matchIndices = np.where(arrx!=arry)
print(matchIndices)