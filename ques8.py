#enter a number and then prints all the even numbers from 0 to that number.
num=int(input("Enter a number to print all the even numbers upto that number: "))
for i in range(0,num):
    if i%2==0 :
        print(i)