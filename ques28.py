#Write a Python Program to filter the multiples of 10s from a given list.
def filter10sMultiple(list):
    multipleOf10=[]
    for element in list:
        if (element%10 == 0):
            multipleOf10.append(element)
    return multipleOf10

list = [10, 20, 30, 33, 44, 50, 55]

result = filter10sMultiple(list)
print(result)