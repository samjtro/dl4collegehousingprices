import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

url_base = 'https://www.stateuniversity.com/rank/score_rank_by_pubc/{}'

df = pd.DataFrame(columns=['School'])

for x in range(25):
	r = requests.get(url_base.format(p))
	soup = bs(r.content,'html.parser')
	find_tbody = soup.find('tbody')
	content = find_tbody.find_all('td',class_=False)

	for a in content:
		for b in a:
			for c in b:
				if len(c) > 2:
					df.loc[len(df.index)] = c
