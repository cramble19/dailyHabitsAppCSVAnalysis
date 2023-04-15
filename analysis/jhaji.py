#import relevant libraries

import pandas as pd
import numpy as np
import os
from IPython.display import display
#import qgrid

# # Set display options for pandas dataframes
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', None)
# pd.set_option('display.max_rows', None)

#import csv file using pandas
data = pd.read_csv('C:/Users/admin/Documents/GitHub/dailyHabitsAppCSVAnalysis/Checkmarks.csv')
cols = data.columns[:-1]
#print(cols)
#print(data.head())

row=data.iloc[0]
print(row)

# new_data = data.iloc[:, ::2]
# print(new_data.head())


