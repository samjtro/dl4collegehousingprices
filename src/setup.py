from data import data as d
import datetime as time
from scrape import scrape as s

class setup:
	def __init__(self):
		start = time.datetime.now()

		print("**now initiating setup for historical data**\n")
		d.__realtor__()
		print("\n**now initiating setup for realtime data**")
		o1 = input("where would you like to scan \n[Example: Fort-Collins_CO  OR  California]   ")
		o2 = input("set your upper price bound   ")
		o3 = int(input("how many pages would you like to search through?   "))
		s.__realtor__(o1,o2,o3)

		end = time.datetime.now()-start
		print("complete. elapsed time: ",end)

setup()