import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("gis_pop_rides.csv")
"""
sns.set(context="paper", font="monospace")



corrmat = df.corr()
print(corrmat)
f, ax = plt.subplots(figsize=(15,10))

sns.heatmap(corrmat)

f.tight_layout()
plt.show()
"""

df.drop(['CD_Label','CD_Name'],1,inplace=True)
for column in df:
    print(column)
    print(df['num_rides'].corr(df[column]))
