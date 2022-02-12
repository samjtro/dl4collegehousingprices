import pandas as pd

df = pd.read_csv(r'top420f.csv')

# just a function to drop rows with an empty zip, only neccesary because pd.dropna() doesn't work here
for x in range(len(df['Zip'])):
	if pd.isna(df['Zip'][x]) == True:
		df = df.drop(index=x)

# as noted, our data is halved during this step alone. this means more than half of our searches came up empty for zips. this is more of a result of the sloppy collection than a reflection of the actual results turned by google, but it was also impossibly hard to parse the responses given by google so this will do for now.
df.to_csv('final212.csv',index=False)