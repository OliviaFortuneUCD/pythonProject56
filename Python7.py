import pandas as pd
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

Ourdf = pd.read_csv('GBvideos.csv')


def best_videos(list, title):

    list.sort_values(by="views",ascending=False).set_index("title").head(5).plot.bar(figsize=(10,5))
    plt.yticks(rotation=60, fontsize=5)
    plt.xticks(rotation=90, fontsize=5)
    plt.title(title, fontsize=5)
    plt.legend(handlelength=5, fontsize=5)
    plt.show()

list = Ourdf[["title","views"]].sort_values(by="views",ascending=True).drop_duplicates("title",keep="last")
title = "\nThe best 5 videos viewed on Youtube\n"
best_videos(list, title)