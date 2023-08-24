'''#Write a Python Program to filter the multiples of 10s from a given list.
def filter10sMultiple(list):
    multipleOf10=[]
    for element in list:
        if (element%10 == 0):
            multipleOf10.append(element)
    return multipleOf10'''

def filter10sMultiple(ittlist):
    return list(filter(lambda x:x%10==0 , ittlist))

givenlist = [10, 20, 30, 33, 44, 50, 55]

result = filter10sMultiple(givenlist)
print(result)