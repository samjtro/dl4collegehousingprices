import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

df = pd.read_csv(r'top420.csv')
url_base = 'https://www.google.com/search?q={}+Address'

for x in range(len(df['School'])):
	school_name = df['School'][x]
	spliced_school_name = school_name.split(" ")
	formatted_school_name = '+'.join(spliced_school_name)
	url_formatted = url_base.format(formatted_school_name)

	r = requests.get(url_formatted)
	soup = bs(r.content,'html.parser')
	content = soup.text
	spliced_soup = content.split(" ")

	zip_codes = ''
	
	for y in spliced_soup:
		if len(y) == 5:
			if y.isdigit() == True:
				zip_codes += ',' + y

	df['Zip'][x] = zip_codes
	print('*added zip*')

df.to_csv('top420f.csv',index=False)