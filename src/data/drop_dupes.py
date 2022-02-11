import pandas as pd

final_212 = pd.read_csv(r'final212.csv')
df = pd.DataFrame(columns=['School','Zip'])
schools_zips = {}
schools = []

for x in range(len(final_212)):
	zips_new = []
	school_name = final_212['School'][x]
	zips = final_212['Zip'][x]

	for y in range(len(zips)):
		zips_split = zips.split(',')
		for z in range(len(zips_split)):
			zip_code = zips_split[z]
			if (zip_code in zips_new):
				continue
			else:
				zips_new.append(zip_code)

	if (school_name in schools_zips.keys()):
		continue
	else:
		schools_zips[school_name] = zips_new

df['School'] = schools_zips.keys()
df['Zip'] = schools_zips.values()

df.to_csv('final_204.csv',index=False)