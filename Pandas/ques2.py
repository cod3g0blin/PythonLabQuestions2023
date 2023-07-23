'''Create two data frames using the following two Dictionaries, Merge two dataframes, 
and append the second dataframes as a new coloumn to first dataframe
a) car_price = {'company': ['toyota', 'honda', 'BMW', 'audi']
                  'price': [200000, 300000, 350000, 600000]}
b) car_horsepower = {'company': ['toyota', 'honda', 'BMW', 'audi']
                  'horsepower': [300, 145,  600, 350]}'''

import pandas as pd

car_price = {'company': ['toyota', 'honda', 'BMW', 'audi'],
            'price': [200000, 300000, 350000, 600000]}
car_horsepower = {'company': ['toyota', 'BMW', 'honda', 'audi'],
                  'horsepower': [300, 145,  600, 350]}

df1 = pd.DataFrame(car_price)
df2 = pd.DataFrame(car_horsepower)

#print(df1,'\n',df2)
merged_df = pd.merge(df1, df2, on='company')
print(merged_df)

car_count = merged_df.shape[0]
print("Number of cars: ",car_count)

most_expensive = merged_df['price'].max()
most_expensive_index = merged_df['price'].index.max()
print(most_expensive)
print("The most expensice car is: ",merged_df['company'][most_expensive_index],'\t', merged_df['price'][most_expensive_index],'\t', merged_df['horsepower'][most_expensive_index])