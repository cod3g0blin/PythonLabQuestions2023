#Write Python function to print the age of a person for a given date of birth using **kwargs
from datetime import datetime

def calculate_age(**kwargs):
    current_date = datetime.now()

    if "year" in kwargs and "month" in kwargs and "day" in kwargs:
        birth_date = datetime(kwargs["year"], kwargs["month"], kwargs["day"])
        age = current_date.year - birth_date.year

        if current_date.month < birth_date.month:
            age -= 1
        elif current_date.month == birth_date.month and current_date.day < birth_date.day:
            age -= 1

        print("Age:", age)
    else:
        print("Invalid input. Please provide 'year', 'month', and 'day'.")

# Example usage:
calculate_age(year=2001, month=11, day=9)