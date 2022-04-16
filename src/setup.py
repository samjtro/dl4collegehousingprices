from data import data as d
from scrape import scrape as s

class setup:
	def __init__(self):
		print("**now initiating setup for historical data**\n")
		#d.__realtor__()
		print("**now initiating setup for realtime data**")
		o1 = input("where would you like to scan \n[Example: Fort-Collins_CO  OR  Colorado]   ")
		o2 = input("there are a number of customizations you can make to your search \n[Example: type-single-family-home/price-na-1000000 (seperate with '/')] --or leave blank!\n")
		o3 = int(input("how many pages would you like to search through?   "))
		
		s.__realtor__(o1,o2,o3)

setup()