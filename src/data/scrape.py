import pandas as pd
import re
import time
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By

df = pd.DataFrame(columns=['Address','Status','Price','Meta'])

statuses = []
prices = []
metas = []
addresses = []

class scrape:
        def __init__(self):
                ...

        def __realtor__(form,options,pages):
                '''
form -
        for states:     'Colorado' or 'California'
        for cities:     'city1-city2_state'   i.e.    'Los-Angeles_CA' or 'Denver_CO'

options - 
        'type-single-family-home' or 'type-single-family-home/price-na-500000'
        only single family homes      only single family homes < 500000 in price

pages - the amount of pages to cycle through
                '''
                url = 'https://www.realtor.com/realestateandhomes-search/{}/{}/pg-{}'
                for i in range(1,pages+1):
                        print('**working {}/{}**'.format(i,pages))
                        display = Display(visible=0, size=(800, 600))
                        display.start()
                        browser = webdriver.Firefox(executable_path='/home/sam/geckodriver')
                        browser.get(url.format(form,options,i))

                        status = browser.find_elements(By.XPATH,"//div[@class='jsx-3853574337']")
                        for x in status: statuses.append(x.text)

                        meta = browser.find_elements(By.XPATH,"//div[@data-testid='property-meta-container']")
                        for x in meta: metas.append(x.text)

                        price = browser.find_elements(By.XPATH,"//span[@data-label='pc-price']")
                        for x in price: 
                                p1 = x.text
                                p2 = re.sub('[^0-9]','',p1)
                                prices.append(p2)

                        address = browser.find_elements(By.XPATH,"//div[@data-label='pc-address']")
                        for x in address: addresses.append(x.text.replace('\n',' '))

                        browser.quit()
                        display.stop()
                        time.sleep(3)

                df['Address'] = addresses
                df['Status'] = statuses
                df['Price'] = prices
                df['Meta'] = metas

                df.to_csv("data/active_homes.csv",index=False)