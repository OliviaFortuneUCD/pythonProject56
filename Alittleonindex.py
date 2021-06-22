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


print(df.iloc[[0, 1]])