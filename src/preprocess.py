import pandas as pd

RDC_inventory = pd.read_csv('data/RDC_Inventory.csv')
columns_inventory = ['month_date_yyyymm', 'postal_code', 'zip_name', 'median_listing_price', 'median_listing_price_mm', 'median_listing_price_yy', 'active_listing_count', 'active_listing_count_mm', 'active_listing_count_yy', 'median_days_on_market', 'median_days_on_market_mm', 'median_days_on_market_yy', 'new_listing_count', 'new_listing_count_mm', 'new_listing_count_yy', 'price_increased_count', 'price_increased_count_mm', 'price_increased_count_yy', 'price_reduced_count', 'price_reduced_count_mm', 'price_reduced_count_yy', 'pending_listing_count', 'pending_listing_count_mm', 'pending_listing_count_yy', 'median_listing_price_per_square_foot', 'median_listing_price_per_square_foot_mm', 'median_listing_price_per_square_foot_yy', 'median_square_feet', 'median_square_feet_mm', 'median_square_feet_yy', 'average_listing_price', 'average_listing_price_mm', 'average_listing_price_yy', 'total_listing_count', 'total_listing_count_mm', 'total_listing_count_yy', 'pending_ratio', 'pending_ratio_mm', 'pending_ratio_yy', 'quality_flag']
# creating dataframe and declaring arrays for each datapoint i want to fetch from RDC as well as final_204.csv
df = pd.DataFrame(columns=['zip_code','median_listing_price_mm','median_listing_price_yy','active_listing_count_mm','active_listing_count_yy','median_days_on_market_mm','median_days_on_market_yy','new_listing_count_mm','new_listing_count_yy','price_increased_count_mm','price_increased_count_yy','pending_listing_count_mm','pending_listing_count_yy','average_listing_price_mm','average_listing_price_yy','total_listing_count_mm','total_listing_count_yy','pending_ratio_mm','pending_ratio_yy'])

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

for a in range(len(RDC_inventory)):
    	zips_test.append(RDC_inventory['postal_code'][a])
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
df['zip_code'] = zips_test
df['median_listing_price_mm'] = median_listing_price_mm_test
df['median_listing_price_yy'] = median_listing_price_yy_test
df['active_listing_count_mm'] = active_listing_count_mm_test
df['active_listing_count_yy'] = active_listing_count_yy_test
df['median_days_on_market_mm'] = median_days_on_market_mm_test
df['median_days_on_market_yy'] = median_days_on_market_yy_test
df['new_listing_count_mm'] = new_listing_count_mm_test
df['new_listing_count_yy'] = new_listing_count_yy_test
df['price_increased_count_mm'] = price_increased_count_mm_test
df['price_increased_count_yy'] = price_increased_count_yy_test
df['pending_listing_count_mm'] = pending_listing_count_mm_test
df['pending_listing_count_yy'] = pending_listing_count_yy_test
df['average_listing_price_mm'] = average_listing_price_mm_test
df['average_listing_price_yy'] = average_listing_price_yy_test
df['total_listing_count_mm'] = total_listing_count_mm_test
df['total_listing_count_yy'] = total_listing_count_yy_test
df['pending_ratio_mm'] = pending_ratio_mm_test
df['pending_ratio_yy'] = pending_ratio_yy_test

df = df.dropna(axis=0)

df.to_csv('realtor.csv',index=False)
