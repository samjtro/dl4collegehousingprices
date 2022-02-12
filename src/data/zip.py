import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

# setting base url for web scraping and creating dataframe from previous file
df = pd.read_csv(r'top420.csv')
url_base = 'https://www.google.com/search?q={}+Address'

for x in range(len(df['School'])):
	# all formatting functions, declarations, etc.
	school_name = df['School'][x]
	spliced_school_name = school_name.split(" ")
	formatted_school_name = '+'.join(spliced_school_name)
	url_formatted = url_base.format(formatted_school_name)
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

df.to_csv('top420f.csv',index=False)