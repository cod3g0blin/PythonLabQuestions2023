'''Write a program to basic arithmetic opertions on numpy array'''

import numpy as np
def main():
    arr1 = np.array([10,15,20])
    arr2 = np.array([12,20,24])
    print("Addition:", arr1+arr2)
    print("Scaler Addition: ", arr2+5)
    print("Substraction: ", arr2-arr1)
    print("Scaler Substration: ", arr2-4)
    print("Multiplication: ", arr1*arr2)
    print("Scaler Multiplication: ", arr2*2)
    print("Division: ", arr2/arr1)
    print("Scaler division: ", arr2/2)
    print("Square root: ", np.sqrt(arr1))
    print("Power of array: ",np.power(arr2,2))

main()