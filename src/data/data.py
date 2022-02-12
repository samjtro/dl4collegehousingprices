import requests
import re
import pandas as pd
from bs4 import BeautifulSoup as bs

# web scraping round 1
url_base = 'https://www.stateuniversity.com/rank/score_rank_by_pubc/{}'
df = pd.DataFrame(columns=['School','Zip'])

for x in range(25):
	# web scraping - first two lines fetch html data, find_tbody finds the <tbody> tag in which the table of schools resides, and content finds all <td> elements in <tbody>
	r = requests.get(url_base.format(x))
	soup = bs(r.content,'html.parser')
	find_tbody = soup.find('tbody')
	content = find_tbody.find_all('td',class_=False)

	# for loop that iterates over the <td> tags, splits them into their individual elements and grabs all lines > 2 - then appending them to the dataframe
	# this method is sloppy, but was the best fix i could figure out for fetching these names without pulling my hair out
	for a in content:
		for b in a:
			for c in b:
				if len(c) > 2:
					df.loc[len(df.index)] = c

# web scraping round 2
url_base2 = 'https://www.google.com/search?q={}+Address'

for x in range(len(df['School'])):
	school_name = df['School'][x]
	spliced_school_name = school_name.split(" ")
	formatted_school_name = '+'.join(spliced_school_name)
	url_formatted = url_base2.format(formatted_school_name)
	zip_codes = ''

	# web scraping - pretty simple, grabs google search results for school name + address using the formatted_school_name from before
	r = requests.get(url_formatted)
	soup = bs(r.content,'html.parser')
	content = soup.text
	spliced_soup = content.split(" ")
	
	# this for loop splits the google search results into individual words, finds if they are digits > 5, and if yes it adds it to the zip_codes variable with a , before
	# this makes comma splicing easier later, but this method as a whole is very sloppy - out of the 420 results started with, you'll see that after the matching algorithm is done only about 38 results made it through. expanding your list of schools to be greater than 500 is probably required for any substantive data collection (something i'll add once the concept iteration of this project has been tested)
	for y in spliced_soup:
		if len(y) == 5:
			if y.isdigit() == True:
				zip_codes += ',' + y

	df['Zip'][x] = zip_codes
	print('*added zip*')

# just a function to drop rows with an empty zip, only neccesary because pd.dropna() doesn't work here
for x in range(len(df['Zip'])):
	if pd.isna(df['Zip'][x]) == True:
		df = df.drop(index=x)

schools_zips = {}
schools = []
df2 = pd.DataFrame(columns=['School','Zip'])

# function to drop duplicate schools / zips
for x in range(len(df)):
	zips_new = []
	school_name = df['School'][x]
	zips = df['Zip'][x]
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

df2['School'] = schools_zips.keys()
df2['Zip'] = schools_zips.values()

# the rest of this file is the most important part
# next few lines reads in the RDC_Inventory data. RDC files can be downloaded seperately (see the readme)
# columns_inventory and columns_hotness are the columns for the data. columns_inventory corresponds with both historical and regular inventory. this is for personal use to remember what file has which columns.
RDC_inventory = pd.read_csv(r'RDC_Inventory.csv')
columns_inventory = ['month_date_yyyymm', 'postal_code', 'zip_name', 'median_listing_price', 'median_listing_price_mm', 'median_listing_price_yy', 'active_listing_count', 'active_listing_count_mm', 'active_listing_count_yy', 'median_days_on_market', 'median_days_on_market_mm', 'median_days_on_market_yy', 'new_listing_count', 'new_listing_count_mm', 'new_listing_count_yy', 'price_increased_count', 'price_increased_count_mm', 'price_increased_count_yy', 'price_reduced_count', 'price_reduced_count_mm', 'price_reduced_count_yy', 'pending_listing_count', 'pending_listing_count_mm', 'pending_listing_count_yy', 'median_listing_price_per_square_foot', 'median_listing_price_per_square_foot_mm', 'median_listing_price_per_square_foot_yy', 'median_square_feet', 'median_square_feet_mm', 'median_square_feet_yy', 'average_listing_price', 'average_listing_price_mm', 'average_listing_price_yy', 'total_listing_count', 'total_listing_count_mm', 'total_listing_count_yy', 'pending_ratio', 'pending_ratio_mm', 'pending_ratio_yy', 'quality_flag']
# creating dataframe and declaring arrays for each datapoint i want to fetch from RDC as well as final_204.csv
df_test = pd.DataFrame(columns=['school_name','zip_code','median_listing_price_mm','median_listing_price_yy','active_listing_count_mm','active_listing_count_yy','median_days_on_market_mm','median_days_on_market_yy','new_listing_count_mm','new_listing_count_yy','price_increased_count_mm','price_increased_count_yy','pending_listing_count_mm','pending_listing_count_yy','average_listing_price_mm','average_listing_price_yy','total_listing_count_mm','total_listing_count_yy','pending_ratio_mm','pending_ratio_yy'])

schools_test = []
zips_test = []
median_listing_price_mm_test = []
median_listing_price_yy_test = []
active_listing_count_mm_test = []
active_listing_count_yy_test = []
median_days_on_market_mm_test = []
median_days_on_market_yy_test = []
new_listing_count_mm_test = []
new_listing_count_yy_test = []
price_increased_count_mm_test = []
price_increased_count_yy_test = []
pending_listing_count_mm_test = []
pending_listing_count_yy_test = []
average_listing_price_mm_test = []
average_listing_price_yy_test = []
total_listing_count_mm_test = []
total_listing_count_yy_test = []
pending_ratio_mm_test = []
pending_ratio_yy_test = []

for x in range(len(df2)):
	school_name = df2['School'][x]
	zips = df2['Zip'][x]

	for a in range(len(RDC_inventory)):
		zip_code2 = RDC_inventory['postal_code'][a]

		for b in range(len(zips)):
			raw = zips[b]
			zip_code = re.sub('[^0-9]','', raw)
		
		# all of the above iterates through df2 and RDC_inventory in order to fetch zip codes from both. if they match, the data is appended to each array.
		if zip_code == zip_code2:
			schools_test.append(school_name)
			zips_test.append(zip_code2)
			median_listing_price_mm_test.append(RDC_inventory['median_listing_price_mm'][a])
			median_listing_price_yy_test.append(RDC_inventory['median_listing_price_yy'][a])
			active_listing_count_mm_test.append(RDC_inventory['active_listing_count_mm'][a])
			active_listing_count_yy_test.append(RDC_inventory['active_listing_count_yy'][a])
			median_days_on_market_mm_test.append(RDC_inventory['median_days_on_market_mm'][a])
			median_days_on_market_yy_test.append(RDC_inventory['median_days_on_market_yy'][a])
			new_listing_count_mm_test.append(RDC_inventory['new_listing_count_mm'][a])
			new_listing_count_yy_test.append(RDC_inventory['new_listing_count_yy'][a])
			price_increased_count_mm_test.append(RDC_inventory['price_increased_count_mm'][a])
			price_increased_count_yy_test.append(RDC_inventory['price_increased_count_yy'][a])
			pending_listing_count_mm_test.append(RDC_inventory['pending_listing_count_mm'][a])
			pending_listing_count_yy_test.append(RDC_inventory['pending_listing_count_yy'][a])
			average_listing_price_mm_test.append(RDC_inventory['average_listing_price_mm'][a])
			average_listing_price_yy_test.append(RDC_inventory['average_listing_price_yy'][a])
			total_listing_count_mm_test.append(RDC_inventory['total_listing_count_mm'][a])
			total_listing_count_yy_test.append(RDC_inventory['total_listing_count_yy'][a])
			pending_ratio_mm_test.append(RDC_inventory['pending_ratio_mm'][a])
			pending_ratio_yy_test.append(RDC_inventory['pending_ratio_yy'][a])

# dataframe assignment!
df_test['school_name'] = schools_test
df_test['zip_code'] = zips_test
df_test['median_listing_price_mm_test'] = median_listing_price_mm_test
df_test['median_listing_price_yy_test'] = median_listing_price_yy_test
df_test['active_listing_count_mm'] = active_listing_count_mm_test
df_test['active_listing_count_yy'] = active_listing_count_yy_test
df_test['median_days_on_market_mm'] = median_days_on_market_mm_test
df_test['median_days_on_market_yy'] = median_days_on_market_yy_test
df_test['new_listing_count_mm'] = new_listing_count_mm_test
df_test['new_listing_count_yy'] = new_listing_count_yy_test
df_test['price_increased_count_mm'] = price_increased_count_mm_test
df_test['price_increased_count_yy'] = price_increased_count_yy_test
df_test['pending_listing_count_mm'] = pending_listing_count_mm_test
df_test['pending_listing_count_yy'] = pending_listing_count_yy_test
df_test['average_listing_price_mm'] = average_listing_price_mm_test
df_test['average_listing_price_yy'] = average_listing_price_yy_test
df_test['total_listing_count_mm'] = total_listing_count_mm_test
df_test['total_listing_count_yy'] = total_listing_count_yy_test
df_test['pending_ratio_mm'] = pending_ratio_mm_test
df_test['pending_ratio_yy'] = pending_ratio_yy_test

# to_csv shows that only 39 schools were a match for the RDC data. this is fine; enough for a preliminary sample, but we will need many more matches if we want to identify more opportunities
# a suggestion would be to use this matching algorithms on multiple datasets, with similar data, and as previously mentioned have more and higher quality zip code data
df_test.to_csv('current_college_housing_data.csv',index=False)