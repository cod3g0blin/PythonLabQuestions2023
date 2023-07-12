def add(a,b):
    return a+b
def subst(a,b):
    if(a>b): 
        return a-b
    else: 
        return b-a
def multiply(a,b):
    return a*b
def divide(a,b):
    if b!=0:
        return a/b
    else:
        raise Exception("Cannot divide by Zero")
