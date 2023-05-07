#Check odd/even
num=int(input("Enter a number to be chechked: "))
if(num % 2==0):
    print("The number ", num, "is an even number.")
else:
    print("The number ", num, "is an odd number.")


#GCD
num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))

while num2 != 0:
    temp = num1 % num2
    num1 = num2
    num2 = temp

print(num1)
