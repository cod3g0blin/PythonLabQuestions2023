#Write a generator function using **kwargs and print args one by one
def printKwargs1by1(**kwargs):
    for key,value in kwargs.items():
        print(f'key: {key}, value: {value}')
        yield value

generator = printKwargs1by1(a=1, b=2, c=3)
for value in generator:
    print(f'Recieved value: {value}')