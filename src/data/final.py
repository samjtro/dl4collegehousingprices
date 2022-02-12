import pandas as pd
import re

final_204 = pd.read_csv(r'final_204.csv')
RDC_historical_inventory = pd.read_csv(r'RDC_Historical_Inventory.csv')
RDC_inventory = pd.read_csv(r'RDC_Inventory.csv')
RDC_hotness_inventory = pd.read_csv(r'RDC_Hotness_History.csv')
columns_inventory = ['month_date_yyyymm', 'postal_code', 'zip_name', 'median_listing_price', 'median_listing_price_mm', 'median_listing_price_yy', 'active_listing_count', 'active_listing_count_mm', 'active_listing_count_yy', 'median_days_on_market', 'median_days_on_market_mm', 'median_days_on_market_yy', 'new_listing_count', 'new_listing_count_mm', 'new_listing_count_yy', 'price_increased_count', 'price_increased_count_mm', 'price_increased_count_yy', 'price_reduced_count', 'price_reduced_count_mm', 'price_reduced_count_yy', 'pending_listing_count', 'pending_listing_count_mm', 'pending_listing_count_yy', 'median_listing_price_per_square_foot', 'median_listing_price_per_square_foot_mm', 'median_listing_price_per_square_foot_yy', 'median_square_feet', 'median_square_feet_mm', 'median_square_feet_yy', 'average_listing_price', 'average_listing_price_mm', 'average_listing_price_yy', 'total_listing_count', 'total_listing_count_mm', 'total_listing_count_yy', 'pending_ratio', 'pending_ratio_mm', 'pending_ratio_yy', 'quality_flag']
columns_hotness = ['month_date_yyyymm', 'postal_code', 'zip_name', 'nielsen_hh_rank', 'hotness_rank', 'hotness_rank_mm', 'hotness_rank_yy', 'hotness_score', 'supply_score', 'demand_score', 'median_days_on_market', 'median_days_on_market_mm', 'median_dom_mm_day', 'median_days_on_market_yy', 'median_dom_yy_day', 'median_dom_vs_us', 'ldp_unique_viewers_per_property_mm', 'ldp_unique_viewers_per_property_yy', 'ldp_unique_viewers_per_property_vs_us', 'median_listing_price', 'median_listing_price_mm', 'median_listing_price_yy', 'median_listing_price_vs_us', 'quality_flag']

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

for x in range(len(final_204)):
	school_name = final_204['School'][x]
	zips = final_204['Zip'][x]
	zips_split = zips.split(',')

	for a in range(len(RDC_inventory)):
		zip_code2 = RDC_inventory['postal_code'][a]

		for b in range(len(zips_split)):
			raw = zips_split[b]
			zip_code = re.sub('[^0-9]','', raw)
			
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

df_test.to_csv('final_college_housing_data.csv',index=False)