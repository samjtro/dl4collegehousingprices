import pandas as pd

final_204 = pd.read_csv(r'data/final_204.csv')
RDC_historical_inventory = pd.read_csv(r'data/RDC_Historical_Inventory.csv')
RDC_inventory = pd.read_csv(r'data/RDC_Inventory.csv')
RDC_hotness_inventory = pd.read_csv(r'data/RDC_Hotness_History.csv')
columns_inventory = ['month_date_yyyymm', 'postal_code', 'zip_name', 'median_listing_price', 'median_listing_price_mm', 'median_listing_price_yy', 'active_listing_count', 'active_listing_count_mm', 'active_listing_count_yy', 'median_days_on_market', 'median_days_on_market_mm', 'median_days_on_market_yy', 'new_listing_count', 'new_listing_count_mm', 'new_listing_count_yy', 'price_increased_count', 'price_increased_count_mm', 'price_increased_count_yy', 'price_reduced_count', 'price_reduced_count_mm', 'price_reduced_count_yy', 'pending_listing_count', 'pending_listing_count_mm', 'pending_listing_count_yy', 'median_listing_price_per_square_foot', 'median_listing_price_per_square_foot_mm', 'median_listing_price_per_square_foot_yy', 'median_square_feet', 'median_square_feet_mm', 'median_square_feet_yy', 'average_listing_price', 'average_listing_price_mm', 'average_listing_price_yy', 'total_listing_count', 'total_listing_count_mm', 'total_listing_count_yy', 'pending_ratio', 'pending_ratio_mm', 'pending_ratio_yy', 'quality_flag']
columns_hotness = ['month_date_yyyymm', 'postal_code', 'zip_name', 'nielsen_hh_rank', 'hotness_rank', 'hotness_rank_mm', 'hotness_rank_yy', 'hotness_score', 'supply_score', 'demand_score', 'median_days_on_market', 'median_days_on_market_mm', 'median_dom_mm_day', 'median_days_on_market_yy', 'median_dom_yy_day', 'median_dom_vs_us', 'ldp_unique_viewers_per_property_mm', 'ldp_unique_viewers_per_property_yy', 'ldp_unique_viewers_per_property_vs_us', 'median_listing_price', 'median_listing_price_mm', 'median_listing_price_yy', 'median_listing_price_vs_us', 'quality_flag']

indexes_inventory = []
for x in range(len(final_204)):
	school_name = final_204['School'][x]
	zip_code = final_204['Zip'][x]

	for y in range(len(RDC_inventory)):
		zip_code2 = RDC_inventory['postal_code'][y]

		if zip_code == zip_code2:
			print(RDC_inventory['median_listing_price'][y])
			indexes_inventory.append(y)