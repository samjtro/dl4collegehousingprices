from data import data
from datetime import datetime as t
from scrape import scrape

class setup:
	def __init__(self):
		start = t.now()

		print("**now initiating setup for historical data**\n")
		data()
		print("\n**now initiating setup for realtime data**")
		o1 = input("where would you like to scan \n[Example: Fort-Collins_CO  OR  California]   ")
		o2 = input("set your upper price bound   ")
		o3 = int(input("how many pages would you like to search through?   "))
		scrape(o1,o2,o3)

		end = t.now()-start
		print("complete -- elapsed time: ",end)

setup()