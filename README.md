# dl4collegehousingprices
### what is this project

Deep Learning for College Housing Price Forecasting
Contact: fguattari-dev@protonmail.com

this is a project to fetch price histories for college housing markets, then use either a PPO or a TD3 machine learning algorithm to forecast future housing prices.the purpose is twofold; first, i'm a college student going to school for ml/ai and am interested in the college housing market as i've gotten plenty of exposure to it. second, college market rental properties are fantastic investments. as a result, being able to spot low cost properties with high rental value is a critical asset. that is precisely what this project aims to do.

### what do i need?

you will need this github repo, plus all of the data needed for the model. the total RDC data alone is > 600MB, once compressed the .zip is 187.7MB which is still too unreasonable for github. once i get lfs going it will be hosted here but until then, you can download the .zip from dropbox:

https://www.dropbox.com/s/y2qjp6lpgfj37bl/Final_Data.zip?dl=0

simply extract the .zip, copy the .csv files into the data dir, then run the model. easy!

### what can i do with this project?

see the license. anything you want, as long as you credit me.

### file descriptions + local build notes

1. data.py
  desc: all web scraping / data gathering functions
    - fetches school names for top 500 public schools in the country
    - fetches zip codes
    - drops rows with empty zip codes
    - drops duplicate school rows and duplicate zip codes
    - fetches data from RDC_Inventory.csv (current housing market data by zip from RDC), uses a matching algorithm to make matches between the zip codes in both dataframes and creates a final dataframe with the School, Zip, and market data
