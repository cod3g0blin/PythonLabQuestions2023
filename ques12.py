#Write Python function to print n prime numbers
num=int(input("Enter a limiting number: "))
for i in range(2,num):
    count=0
    for k in range(2,i):
        if(i%k==0):
            count+=1
            break
    
    if(count==0):
        print(i)
        