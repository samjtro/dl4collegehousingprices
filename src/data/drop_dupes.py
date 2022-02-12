import pandas as pd

# declaration, reading csvs, etc.
final_212 = pd.read_csv(r'final212.csv')
df = pd.DataFrame(columns=['School','Zip'])
schools_zips = {}
schools = []

for x in range(len(final_212)):
	# more declaration and formatting
	zips_new = []
	school_name = final_212['School'][x]
	zips = final_212['Zip'][x]
	zips_split = zips.split(',')		

	# this for loop and subsequent if statement iterates through zips_split (a list of the zips for each school), adding each unique zip to an array used later in the if statement for each unique school name. sounds confusing, really just drops all duplicate school names and zips in the same function. pretty nifty.
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

# as you can see, this only resulted in 8 drops. that isn't bad, but we shouldn't have had any dupes realistically. i don't know if that is a problem with the website i pulled from listing them twice or a bug somewhere in my code but it has happened every time so far with that source, later iterations will definitely be using a different source.
df.to_csv('final_204.csv',index=False)