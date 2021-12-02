import pandas as pd
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
import seaborn as sns

# making data frame from csv file
# we build an index to make a quicker search

df = pd.read_csv("Stores.csv", index_col="Customer_Number")
#print the header
print(df.head)

#reterieve by row
#print(df.iloc[[0]])

#reterieve by row 2
#print(df.iloc[[1]])

#reterive by 0 to 1
#print(df.iloc[[0, 1]])


#print(df.iloc[-1]) # last row of data frame

#print(df.iloc[:,0]) # first column of data frame (first_name)

#print(df.iloc[0:5]) # first five rows of dataframe

#Why do we set the index. To make it quicker and searchable
df.set_index("Customer_name", inplace=True)

#search for tescos
#print(df.loc['Tescos'])

#search for tescos
#print("I was searching for Tescos....." , df.loc['Tescos'])


#print(df.loc[df['email'].str.endswith("@aldi.com")])
#x=df['cost']
#y=df['price']
#sns.lineplot(data=df, x=x, y=y)

