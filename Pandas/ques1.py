'''Concatenate two dataframes using the following conditions 
a) German cars = {'company': ['ford', 'mercedes', 'BMW', 'audi']
                  'price': [200000, 300000, 350000, 600000]}
b) Japaneses cars = {'company': ['toyota', 'honda', 'nissan', 'mitsubishi']
                  'price': [300000, 250000,  600000, 350000]}'''

import pandas as pd
germanCars = pd.DataFrame({'company': ['ford', 'mercedes', 'BMW', 'audi'],
                           'price': [200000, 300000, 350000, 600000]})
japaneseCars = pd.DataFrame({'company': ['toyota', 'honda', 'nissan', 'mitsubishi'],
                             'price': [300000, 250000,  600000, 350000]})

concatenated_df = pd.concat([germanCars, japaneseCars])
print(concatenated_df)

