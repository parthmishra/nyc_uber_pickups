"""
Location Analysis - Examing Boroughs
"""

import pandas as pd

puma_rides = pd.read_csv('puma_rides.csv')
gis_pop = pd.read_csv('gis_pop.csv')
gis_inc = pd.read_csv('gis_inc.csv')

#pd.to_numeric(loc_puma["PUMA"])
"""
for i, row in puma_rides.iterrows():
    puma = row['PUMA']
    #print(puma)
    for j, jrow in gis_pop.iterrows():
        gis_puma = jrow['PUMA_ID']
        if gis_puma == puma:

            #i['percentPub'] = j['CW_PbTrnsP']

           #i['perWalked'] = j['CW_WlkdP']
    for k, krow in gis_inc.iterrows():
        gis_puma = krow['PUMA_ID']
        if gis_puma == puma:
            medIncome = krow['MdHHIncE']
            loc_puma.set_value(i, 'medIncome', medIncome)
"""


gis_pop['num_rides'] = puma_rides['num_rides']


#print(len(gis_pop.columns))
gis_pop.drop(['Pop16plZ','CvLFZ','PctUEmE','PctUEmM','F16plZ','MnTrvTmP','MnTrvTmZ','CvEm16plZ','CvEm16plZ'],1,inplace=True)
#print(len(gis_pop.columns))
#loc_puma.to_csv('locations_with_puma_gen.csv')
gis_pop.to_csv('gis_pop_rides.csv')
