#Write a program to print following pattern

#   1
#   12
#   123
#   1234
#   12345
def Pattern1():
    for i in range(1,6):
        for j in range(1,i+1):
            print(j, end="")
        print()

#   A
#   BC
#   CDE
#   DEFG
def Pattern2():

    pass

#   4444
#   333
#   22
#   1
def Pattern3():
    pass

Pattern1()