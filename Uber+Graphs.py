
# coding: utf-8

# In[109]:

get_ipython().magic(u'matplotlib inline')

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# In[18]:

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


# In[110]:

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


# In[267]:

y_pos = np.arange(len(hours))
plt.bar(y_pos, total_pph, align='center', alpha=0.5)
plt.xticks(y_pos, hours)
plt.ylabel('Number of Uber pickups')
plt.xlabel('Hour of the day')
plt.title('Total Number of Uber pickups per hour between January-June in 2015')
 
plt.show()


# In[262]:

y_pos = np.arange(len(months))
plt.bar(y_pos, pickups_per_month, align='center', alpha=0.5)
plt.xticks(y_pos, months)
plt.ylabel('Number of Uber pickups')
plt.title('Number of Uber pickups January-June in 2015')
 
plt.show()


# In[13]:

loc_puma = pd.read_csv('~/Documents/nyc_uber_pickups/locations_with_puma.csv', index_col=None)


# In[6]:

uber_2015 = pd.read_csv('~/Documents/uber_kaggle_data/uber-raw-data-janjune-15.csv')


# In[88]:

len(uber_2015)


# In[4]:

uber_apr_2014 = pd.read_csv('~/Documents/uber_kaggle_data/uber-raw-data-apr14.csv')
uber_aug_2014 = pd.read_csv('~/Documents/uber_kaggle_data/uber-raw-data-aug14.csv') 
uber_jun_2014 = pd.read_csv('~/Documents/uber_kaggle_data/uber-raw-data-jun14.csv')
uber_july_2014 = pd.read_csv('~/Documents/uber_kaggle_data/uber-raw-data-jul14.csv')
uber_sep_2014 = pd.read_csv('~/Documents/uber_kaggle_data/uber-raw-data-sep14.csv')
uber_may_2014 = pd.read_csv('~/Documents/uber_kaggle_data/uber-raw-data-may14.csv')


# In[95]:

id_freq = uber_2015.locationID.value_counts()
ids = uber_2015.locationID.value_counts().index
location = []
top_freq = []
for i in range(10):
    location.append(loc_puma.loc[loc_puma['locationID'] == ids[i]].zone.values[0])
    top_freq.append(id_freq.iloc[i])


# In[100]:

borough_ids = []
borough_counts = []
borough_pop = []
for i in bor_names:
    borough_ids.append(loc_puma.loc[loc_puma['borough'] == i, 'locationID'])
    borough_pop.append(loc_puma.loc[loc_puma['borough'] == i, 'totalPop'])
    


# In[111]:

Staten_Island = uber_2015.loc[uber_2015['locationID'].isin(borough_ids[0])]
Queens = uber_2015.loc[uber_2015['locationID'].isin(borough_ids[1])]
Manhattan = uber_2015.loc[uber_2015['locationID'].isin(borough_ids[2])]
Brooklyn = uber_2015.loc[uber_2015['locationID'].isin(borough_ids[3])]
Bronx = uber_2015.loc[uber_2015['locationID'].isin(borough_ids[4])]
arr_bor = [Staten_Island, Queens, Manhattan, Brooklyn, Bronx]


# In[105]:

bor_pop = []
for i in range(len(borough_pop)):
    bor_pop.append(sum(borough_pop[i]))

print(bor_pop)


# In[101]:

bor_pick = []
bor_pick.append(len(Staten_Island))
bor_pick.append(len(Queens))
bor_pick.append(len(Manhattan))
bor_pick.append(len(Brooklyn))
bor_pick.append(len(Bronx))


# In[126]:

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
hours = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


# In[129]:

pph_bor = []
ppm_bor = []
for j in arr_bor:
    pickup_td = j.Pickup_date
    month = []
    hour = []
    for i in pickup_td:
        temp = i.split(" ")
        month.append(temp[0].split("-")[1])
        hour.append(temp[1].split(":")[0])
    pph_bor.append(pd.Series(hour).value_counts().sort_index())
    ppm_bor.append(pd.Series(month).value_counts().sort_index())


# In[135]:

y_pos = np.arange(len(months))
for i in ppm_bor:
    plt.plot(y_pos, i)
    
plt.legend(bor_names,
           columnspacing=1.0, labelspacing=0.0,
           handletextpad=0.0, handlelength=1.5,
           fancybox=True, shadow=True)

plt.xticks(y_pos, months, rotation=70)
plt.ylabel('Number of Pickups')
plt.title('Pickups in NYC boroughs Jan-June 2015')

plt.show()


# In[138]:

y_pos = np.arange(len(hours))
for i in pph_bor:
    plt.plot(y_pos, i)
    
plt.legend(bor_names,
           columnspacing=1.0, labelspacing=0.0,
           handletextpad=0.0, handlelength=1.5,
           fancybox=True, shadow=True)

plt.xticks(y_pos, hours)
plt.ylabel('Number of Pickups')
plt.title('Pickups in NYC boroughs per hour Jan-June 2015')

plt.show()


# In[108]:

y_pos = np.arange(len(bor_names))
plt.bar(y_pos, bor_pop, align='center', alpha=0.5)
plt.xticks(y_pos, bor_names, rotation=70)
plt.ylabel('Population of Borough')
plt.title('Population of NYC boroughs')
 
plt.show()


# In[106]:

y_pos = np.arange(len(bor_names))
plt.bar(y_pos, bor_pick, align='center', alpha=0.5)
plt.xticks(y_pos, bor_names, rotation=70)
plt.ylabel('Number of Uber pickups')
plt.title('Number of pickups per NYC boroughs')
 
plt.show()


# In[266]:

y_pos = np.arange(len(location))
plt.bar(y_pos, top_freq, align='center', alpha=0.5)
plt.xticks(y_pos, location, rotation=70)
plt.ylabel('Number of Uber pickups')
plt.title('Most popular Uber pickup locations New York City, January-June in 2015')
 
plt.show()


# In[ ]:



