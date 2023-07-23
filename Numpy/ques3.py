'''Write a program to demonstrate Numpy arrays creation functions
np.zeroes(): Creates an array of zeroes
np.ones(): Creates an array of 1s
np.empty(): Creates an empty array
np.full(): Creates a full array
np.eye(): Creates an identity matrix
np.random.random(): Creates an array with random values'''

import numpy as np

zeros_array = np.zeros((2,3))
print(zeros_array)

ones_array = np.ones((2,3))
print(ones_array)

empty_array = np.empty((3,2))
print(empty_array)

full_array = np.full((3,3),4)
print(full_array)

eye_array = np.eye(3)
print(eye_array)

random_array = np.random.random((2,3))
print(random_array)