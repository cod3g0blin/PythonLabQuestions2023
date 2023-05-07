#Write a Program to Find the Sum of All Odd and Even Numbers up to a Number Specified by the User. Using functions
def oddSum(num):
    sum=0
    for k in range(0, num):
        if(k%2==0):
            sum+=k
    return sum

def evenSum(num):
    sum=0
    for k in range(0, num):
        if(k%2!=0):
            sum+=k
    return sum

num=int(input("Enter the number: "))
print(oddSum(num)) 
print(evenSum(num))