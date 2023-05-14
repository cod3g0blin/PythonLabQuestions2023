#Leap Year
year=int(input("Enter a year to be checked: "))

if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    print(year, " is a leap year")
else:
    print(year, " is not a leap year")

#the Sum of Digits in a Number
num=int(input("Enter a number to print the sum of its digits: "))
sum=int(0)

while num>0:
    r=int(num%10)
    sum+=r
    num/=10

    print("Sum of the digits: ",sum)