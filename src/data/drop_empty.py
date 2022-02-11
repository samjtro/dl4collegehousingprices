import pandas as pd

df = pd.read_csv(r'top420f.csv')

for x in range(len(df['Zip'])):
	if pd.isna(df['Zip'][x]) == True:
		df = df.drop(index=x)

df.to_csv('final212.csv',index=False)

