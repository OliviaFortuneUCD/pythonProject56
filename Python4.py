import pandas as pd
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

Ourdf = pd.read_csv('GBvideos.csv')

x=Ourdf['channel_title'].head(7)
y=Ourdf['likes'].head(7)
y1=Ourdf['views'].head(7)
plt.plot(x,y)
plt.plot(x,y1)