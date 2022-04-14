import torch as t
import pandas as pd
import numpy as np
from data.scrape import scrape as s
from data.preprocess import preprocess as pp
from sklearn.linear_model import LinearRegression

#s.__realtor__('Colorado','type-single-family-home/price-na-1000000',25)
data = pd.read_csv("data/active_homes.csv")
df = pd.read_csv("data/realtor.csv")
df2 = pp.__df__(data)

for i in range(len(df2)):
    	row = df2.iloc[i]
    
    	blob = {
        	'address': row['Address'],
        	'price': row['Price'],
        	'bed': row['Bed'],
        	'bath': row['Bath'],
        	'sqft': row['Sqft']
    	}

for i in range(len(df)):
	row = df.iloc[i]
	if(row['median_listing_price_yy']>=2):
		print(row)
	
print(df['median_listing_price_mm'].max())
