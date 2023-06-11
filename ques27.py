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
    list=['A', 'B', 'C', 'D', 'E', 'F', 'G']
    count=1
    i = 0
    f = 1
    while (f<=len(list)):
        print((list[i:f]))
        i+=1
        f+=2

#   4444
#   333
#   22
#   1
def Pattern3():
    for i in range(4,0,-1):
        for j in range(1,i+1):
            print(i, end="")
        print()

#       *
#      **
#     ***
#    ****
#   *****
def Pattern4():
    for i in range(1,6):
        for j in range(i,6):
            print(" ",end="")
        for k in range(1,i+1):
            print("*", end="")
        print()

#       *
#      ***
#     *****
#    *******
#   *********
def Pattern5():
    for i in range(1,6):
        for j in range(i,6):
            print(" ",end="")
        for k in range(1,i+1):
            print("*", end="")
        for l in range(1,i):
            print("*", end="")
        print()

#       *
#      * *
#     * * *
#    * * * *
#   * * * * *
def Pattern6():
    for i in range(1,6):
        for j in range(i,6):
            print(" ",end="")
        for k in range(1,i+1):
            print("* ", end="")
        print()

#   1
#   01
#   101
#   0101
def Pattern7():
    ch=0
    for i in range(1,5):
        if i%2==0:
            ch=1
        else:
            ch=0
        for j in range(1,i+1):
            if ch==0:
                ch=1
            else:
                ch=0
            print(ch, end="")
        print()
        



Pattern1()
Pattern2()
Pattern3()
Pattern4()
Pattern5()
Pattern6()
Pattern7()