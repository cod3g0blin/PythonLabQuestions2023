'''Create a class MathOperations that demonstrates function overloading by defining multiple versions of
add. Method should be able to handle different number of arguments and perform addition accordingly'''

class MathOperations:
    def add(self, *args):
        if len(args)==0:
            return 0
        elif len(args)==1:
            return args[0]
        else:
            return sum(args)

math = MathOperations()
res1 = math.add()
print(f"Result of no arguments: {res1}")

res2 = math.add(40)
print(f'Result of 3 arguments: {res2}')