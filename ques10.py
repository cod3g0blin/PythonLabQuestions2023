#read percentage from user and print Grade
#percentage         Grade 
#percentage >=80      O 
#percentage >=75      A+ 
#percentage >=70      A 
#percentage >=65      B+ 
#percentage >=60      B 
#percentage >=55     Pass

percentage=int(input("Enter a percentage: "))

if(percentage>=80):
    print("Grade: O")
elif(percentage>=75):
    print("Grade: A+")
elif(percentage>=70):
    print("Grade: A")
elif(percentage>=65):
    print("Grade: B+")
elif(percentage>=60):
    print("Grade: B")
elif(percentage>=55):
    print("Grade: PASS")
else:
    print("Grade: Fail")