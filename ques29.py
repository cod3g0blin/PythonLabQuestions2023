#Write a program which generates account number using random function for a given range
import random

def generateAccNo(min, max):
    return random.randint(min, max)

min = int(input("Enter the minimum value: "))
max = int(input("Enter the maximum value: "))
AccountNum = generateAccNo(min, max)
print("The account Number is ", AccountNum)