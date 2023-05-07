#Write a Program to Read marks from user and Find the percentage of marks of student
noOfSubjects=int(input("Enter the number of subjects: "))
marks=[]
i=0
totalMarks=0
while i<noOfSubjects:
    r=float(input("Enter the marks of "+ str(i+1)+ " subject: "))
    marks.append(r)
    totalMarks+=marks[i]
    i+=1

percentage=totalMarks/noOfSubjects
print("The percentage: ",percentage)
