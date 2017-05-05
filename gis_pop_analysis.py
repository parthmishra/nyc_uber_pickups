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

#df.drop(['CD_Label','CD_Name','CvLFZ.1','OChU6Z','OCh6t17Z','Wrkr16plM'],1,inplace=True)
output  = {}
for column in df:

    if type(df[column][0]) != str:
        corr = df['num_rides'].corr(df[column])
        output[column] = corr


output = pd.DataFrame.from_dict(output,orient="index",names=['Statistic','Correlation'])
output.sort()
output.to_csv('gis_pop_corr.csv')
