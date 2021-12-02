import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# loading of a dataframe from seaborn
exercise = sns.load_dataset("exercise")


sea = sns.FacetGrid(exercise, col="time",
                    height=4, aspect=.5)

sea.map(sns.barplot, "diet", "pulse",
       order=["no fat", "low fat"])

