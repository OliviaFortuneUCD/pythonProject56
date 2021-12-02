import seaborn as sns
tips = sns.load_dataset('tips')


#sns.scatterplot(x="total_bill", y="tip", data=tips)

#sns.lineplot(x="size", y="tip",data=tips)

#sns.barplot(x="day", y="tip", data = tips)


#sns.countplot(x='smoker',data=tips)

sns.relplot(x="total_bill", y="tip", col="sex",
          hue="smoker", style="size",
           data=tips)