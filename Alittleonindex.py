import pandas as pd
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

# making data frame from csv file
# we build an index to make a quicker search

df = pd.read_csv("Stores.csv", index_col="Customer_Number")

print(df.head)

#reterieve by row
print(df.iloc[[0]])

#reterieve by row 2
print(df.iloc[[2]])

#reterive by 0 to 1
print(df.iloc[[0, 1]])


print(df.iloc[-1]) # last row of data frame

print(df.iloc[:,0]) # first column of data frame (first_name)

print(df.iloc[0:5]) # first five rows of dataframe