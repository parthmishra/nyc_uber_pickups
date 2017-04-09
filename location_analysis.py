"""
Location Analysis - Examing Boroughs
"""

import pandas as pd

loc_puma = pd.read_csv('locations_with_puma.csv')
gis_pop = pd.read_csv('gis_pop.csv')
gis_inc = pd.read_csv('gis_inc.csv')

#pd.to_numeric(loc_puma["PUMA"])

for i, row in loc_puma.iterrows():
    puma = row['PUMA']
    #print(puma)
    for j, jrow in gis_pop.iterrows():
        gis_puma = jrow['PUMA_ID']
        if gis_puma == puma:
            totalPop = jrow['Pop16plE']
            percentPub = jrow['CW_PbTrnsP']
            perWalked = jrow['CW_WlkdP']
            loc_puma.set_value(i, 'totalPop', totalPop)
            loc_puma.set_value(i, 'percentPub', percentPub)
            loc_puma.set_value(i, 'perWalked', perWalked)
            #i['percentPub'] = j['CW_PbTrnsP']
            #i['perWalked'] = j['CW_WlkdP']
    for k, krow in gis_inc.iterrows():
        gis_puma = krow['PUMA_ID']
        if gis_puma == puma:
            medIncome = krow['MdHHIncE']
            loc_puma.set_value(i, 'medIncome', medIncome)

loc_puma.to_csv('locations_with_puma_gen.csv')
