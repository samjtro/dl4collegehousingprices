import pandas as pd

class data:
	def __init__(self):
		...

	def __realtor__():
		url = 'https://econdata.s3-us-west-2.amazonaws.com/Reports/Core/RDC_Inventory_Core_Metrics_Zip_History.csv'
		RDC_inventory = pd.read_csv(url)
		print("fetched data from {}".format(url))
		columns_inventory = ['month_date_yyyymm', 'postal_code', 'zip_name', 'median_listing_price', 'median_listing_price_mm', 'median_listing_price_yy', 'active_listing_count', 'active_listing_count_mm', 'active_listing_count_yy', 'median_days_on_market', 'median_days_on_market_mm', 'median_days_on_market_yy', 'new_listing_count', 'new_listing_count_mm', 'new_listing_count_yy', 'price_increased_count', 'price_increased_count_mm', 'price_increased_count_yy', 'price_reduced_count', 'price_reduced_count_mm', 'price_reduced_count_yy', 'pending_listing_count', 'pending_listing_count_mm', 'pending_listing_count_yy', 'median_listing_price_per_square_foot', 'median_listing_price_per_square_foot_mm', 'median_listing_price_per_square_foot_yy', 'median_square_feet', 'median_square_feet_mm', 'median_square_feet_yy', 'average_listing_price', 'average_listing_price_mm', 'average_listing_price_yy', 'total_listing_count', 'total_listing_count_mm', 'total_listing_count_yy', 'pending_ratio', 'pending_ratio_mm', 'pending_ratio_yy', 'quality_flag']
		# creating dataframe and declaring arrays for each datapoint i want to fetch from RDC as well as final_204.csv
		df = pd.DataFrame(columns=['zip_code','median_listing_price_mm','median_listing_price_yy','active_listing_count_mm','active_listing_count_yy','median_days_on_market_mm','median_days_on_market_yy','new_listing_count_mm','new_listing_count_yy','price_increased_count_mm','price_increased_count_yy','pending_listing_count_mm','pending_listing_count_yy','average_listing_price_mm','average_listing_price_yy','total_listing_count_mm','total_listing_count_yy','pending_ratio_mm','pending_ratio_yy'])

		zips = []
		median_listing_price_mm = []
		median_listing_price_yy = []
		active_listing_count_mm = []
		active_listing_count_yy = []
		median_days_on_market_mm = []
		median_days_on_market_yy = []
		new_listing_count_mm = []
		new_listing_count_yy = []
		price_increased_count_mm = []
		price_increased_count_yy = []
		pending_listing_count_mm = []
		pending_listing_count_yy = []
		average_listing_price_mm = []
		average_listing_price_yy = []
		total_listing_count_mm = []
		total_listing_count_yy = []
		pending_ratio_mm = []
		pending_ratio_yy = []

		for a in range(len(RDC_inventory)):
		    zips.append(RDC_inventory['postal_code'][a])
		    median_listing_price_mm.append(RDC_inventory['median_listing_price_mm'][a])
		    median_listing_price_yy.append(RDC_inventory['median_listing_price_yy'][a])
		    active_listing_count_mm.append(RDC_inventory['active_listing_count_mm'][a])
		    active_listing_count_yy.append(RDC_inventory['active_listing_count_yy'][a])
		    median_days_on_market_mm.append(RDC_inventory['median_days_on_market_mm'][a])
		    median_days_on_market_yy.append(RDC_inventory['median_days_on_market_yy'][a])
		    new_listing_count_mm.append(RDC_inventory['new_listing_count_mm'][a])
		    new_listing_count_yy.append(RDC_inventory['new_listing_count_yy'][a])
		    price_increased_count_mm.append(RDC_inventory['price_increased_count_mm'][a])
		    price_increased_count_yy.append(RDC_inventory['price_increased_count_yy'][a])
		    pending_listing_count_mm.append(RDC_inventory['pending_listing_count_mm'][a])
		    pending_listing_count_yy.append(RDC_inventory['pending_listing_count_yy'][a])
		    average_listing_price_mm.append(RDC_inventory['average_listing_price_mm'][a])
		    average_listing_price_yy.append(RDC_inventory['average_listing_price_yy'][a])
		    total_listing_count_mm.append(RDC_inventory['total_listing_count_mm'][a])
		    total_listing_count_yy.append(RDC_inventory['total_listing_count_yy'][a])
		    pending_ratio_mm.append(RDC_inventory['pending_ratio_mm'][a])
		    pending_ratio_yy.append(RDC_inventory['pending_ratio_yy'][a])
		    if(a%100000==0):
		    	print("adding data to new dataframe {}/{}".format(a,len(RDC_inventory)))

		# dataframe assignment!
		print("formatting new dataframe")
		df['zip_code'] = zips
		df['median_listing_price_mm'] = median_listing_price_mm
		df['median_listing_price_yy'] = median_listing_price_yy
		df['active_listing_count_mm'] = active_listing_count_mm
		df['active_listing_count_yy'] = active_listing_count_yy
		df['median_days_on_market_mm'] = median_days_on_market_mm
		df['median_days_on_market_yy'] = median_days_on_market_yy
		df['new_listing_count_mm'] = new_listing_count_mm
		df['new_listing_count_yy'] = new_listing_count_yy
		df['price_increased_count_mm'] = price_increased_count_mm
		df['price_increased_count_yy'] = price_increased_count_yy
		df['pending_listing_count_mm'] = pending_listing_count_mm
		df['pending_listing_count_yy'] = pending_listing_count_yy
		df['average_listing_price_mm'] = average_listing_price_mm
		df['average_listing_price_yy'] = average_listing_price_yy
		df['total_listing_count_mm'] = total_listing_count_mm
		df['total_listing_count_yy'] = total_listing_count_yy
		df['pending_ratio_mm'] = pending_ratio_mm
		df['pending_ratio_yy'] = pending_ratio_yy

		df = df.dropna(axis=0)

		df.to_csv('data/r_historical.csv',index=False)
