#Write a function to Display the Fibonacci Sequences up to nth Term Where n is Provided by the User
nthTerm=int(input("Enter the nth term of the Fibonacci series: "))
n1=0
n2=1
sum=0
i=2

print("Fibonacci Series:")
print(n1)
print(n2)

while i<nthTerm:
    sum=n1+n2
    print(sum)
    n1=n2
    n2=sum
    i+=1
