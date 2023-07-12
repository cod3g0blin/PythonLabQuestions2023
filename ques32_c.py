#Write a decorator to find the the age of a person for given date of birth
from datetime import datetime
age = 0
def calculate_age(func):
    def wrapper(dateOfBirth):
        dob = datetime.strptime(dateOfBirth,'%y-%m-%d')
        today = datetime.now()
        age = today.year - dob.year

        if today.month < dob.month or (today.month==dob.month and today.day<dob.day) :
            age -=1
        return func(dateOfBirth, age)
    return wrapper

def printAge(dateOfBirth,age):
    print("Age is",age)

printAge("2001-07-09")