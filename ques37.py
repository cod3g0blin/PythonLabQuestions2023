'''Operator Overloading Excercise
Create a class Vector that represents a mathematical vector, implement operator overloading for addition(+)
substraction(-) operations betwen two vector objects'''

class Vector:
    def __init__(self, *components):
        self.components = components

    def __str__(self):
        return f'Vector: {self.components}'
    
    def __add__(self, other):
        if len(self.components)!=len(other.components):
            raise ValueError("Vector must have the same number of components for addition")
        result = [a+b for a,b in zip(self.components, other.components)]
        return Vector(*result)
    
    def __sub__(self, other):
        if len(self.components)!=len(other.components):
            raise ValueError("Vector must have the same number of components for addition")
        result = [a-b for a,b in zip(self.components, other.components)]
        return Vector(*result)

v1 = Vector(1,2,3)
v2 = Vector(4,5,6)
print(f"Addition: {v1+v2}")
print(f"Substraction: {v2-v1}")

