
# coding: utf-8

# In[3]:

get_ipython().magic(u'matplotlib inline')

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[96]:

boroughs = []
bor_names = loc_puma.borough.unique()
bor_names = np.delete(bor_names, 3)

for i in loc_puma.borough.unique():
    if (i == 'EWR'):
        continue
    u_b = loc_puma.loc[loc_puma['borough'] == i]
    boroughs.append(u_b)
    
medIncome = []
for i in range(len(boroughs)):
    medIncome.append(boroughs[i]['medIncome'].mean())


# In[97]:

y_pos = np.arange(len(bor_names))
plt.bar(y_pos, medIncome, align='center', alpha=0.5)
plt.xticks(y_pos, bor_names)
plt.ylabel('Average Income')
plt.title('Average Income of New York City Boroughs')
 
plt.show()


# In[164]:

pickup_td = uber_2015.Pickup_date
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
hours = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


# In[168]:

month = []
hour = []
for i in pickup_td:
    temp = i.split(" ")
    month.append(temp[0].split("-")[1])
    hour.append(temp[1].split(":")[0])
    


# In[163]:

pickups_per_hour = pd.Series(hour).value_counts(sort=False)
print(pickups_per_hour)
total_pph = [602178, 394510, 260603, 183655, 173038, 193523, 288533, 443543, 583348, 593437, 520092, 516716, 533021, 537909, 584463, 649414, 737170, 863990, 987093, 1007464, 948574, 930462, 922954, 814789]


# In[169]:

pickups_per_month = pd.Series(month).value_counts(ascending=True)
print(pickups_per_month)


# In[259]:

y_pos = np.arange(len(hours))
plt.bar(y_pos, total_pph, align='center', alpha=0.5)
plt.xticks(y_pos, hours)
plt.ylabel('Number of Uber pickups')
plt.title('Total Number of Uber pickups per hour between January-June in 2015')
 
plt.show()


# In[262]:

y_pos = np.arange(len(months))
plt.bar(y_pos, pickups_per_month, align='center', alpha=0.5)
plt.xticks(y_pos, months)
plt.ylabel('Number of Uber pickups')
plt.title('Number of Uber pickups January-June in 2015')
 
plt.show()


# In[19]:

loc_puma = pd.read_csv('~/Documents/nyc_uber_pickups/locations_with_puma.csv')


# In[209]:

uber_2015 = pd.read_csv('~/Documents/nyc_uber_pickups/uber-raw-data-janjune-15.csv')


# In[256]:

id_freq = uber_2015.locationID.value_counts()
ids = uber_2015.locationID.value_counts().index
location = []
top_freq = []
for i in range(10):
    location.append(loc_puma.loc[loc_puma['locationID'] == ids[i]].zone.values[0])
    top_freq.append(id_freq.iloc[i])


# In[266]:

y_pos = np.arange(len(location))
plt.bar(y_pos, top_freq, align='center', alpha=0.5)
plt.xticks(y_pos, location, rotation=70)
plt.ylabel('Number of Uber pickups')
plt.title('Most popular Uber pickup locations New York City, January-June in 2015')
 
plt.show()


# In[ ]:



