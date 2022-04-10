import pandas as pd
import numpy as np

df = pd.read_csv('active_homes.csv')
beds = []
baths = []
sqfts = []

for entry in df['Meta']:
        bedI = entry.find("bed")
        bathI = entry.find("bath")
        sqftI = entry.find("sqft")
        beds.append(entry[bedI-1])
        baths.append(entry[bathI-1])
        sqft = ''
        i = bathI+4
        while(i<sqftI):
                sqft += entry[i]
                i+=1
        sqfts.append(sqft)

del df['Meta']
df['Bed'] = beds
df['Bath'] = baths
df['Sqft'] = sqfts
df.to_csv('active_homes.csv',index=False)