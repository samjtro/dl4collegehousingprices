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
