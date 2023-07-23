import pandas as pd

a = [5,10,7]

myseries = pd.Series(a, index=['x','y','z'])
print(myseries)
print(myseries["y"])

calories = {"day1": 400, "day2": 350, "day3": 500}
myvar = pd.Series(calories)
#myvar = pd.Series(calories, index=["day1","day3"])
print(myvar)

