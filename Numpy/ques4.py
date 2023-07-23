'''Create a matrix A and B and perform the following operations on matrix
a) A+B
b) A*B
c) Scalar multiplication
d) Transpose'''

import numpy as np

a = np.array([[1,2],[5,6]])
b = np.array([[1,3],[4,6]])

print(a+b)
print(a*b) #line by line multiplication
print(np.matmul(a,b)) #matrix multiplication
print(a*7)
print(7*a)
print(np.transpose(a))