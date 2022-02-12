import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# setting base url for web scraping and creating dataframe
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

# exports dataframe to a top420.csv file, which contains the 420 names fetched through this process (loss of 80)
df.to_csv('top420.csv',index=False)