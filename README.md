# Deep Learning for College Housing Price Forecasting
### what is this project

this is a project to fetch price histories for college housing markets, then use a deep learning algorithm to forecast future housing prices.

the purpose is twofold; first, i'm a college student going to school for ml/ai and am interested in the college housing market. second, college market rental properties are fantastic investment vehicles; being able to spot low cost properties with high rental value is a critical asset. that is precisely what this project aims to do.

### what do i need?

** this is changing, you will no longer need to locally compile this data **

you will need this github repo, plus all of the data needed for the model. the total RDC data alone is > 600MB, once compressed the .zip is 187.7MB which is still too unreasonable for github. once i get lfs going it will be hosted here but until then, you can download the .zip from dropbox:

https://www.dropbox.com/s/y2qjp6lpgfj37bl/Final_Data.zip?dl=0

simply extract the .zip, copy the .csv files into the data dir, then run the model. easy!

### what can i do with this project?

see the license. anything you want, as long as you credit me.

### file descriptions + local build notes

1. src/data/data.py
  desc: all web scrapinggathering functions:
    - fetches school names for top 500 public schools in the country
    - fetches zip codes
    - drops rows with empty zip codes
    - drops duplicate school rows and duplicate zip codes
    - fetches data from RDC_Inventory.csv (current housing market data by zip from RDC), uses a matching algorithm to make matches between the zip codes in both dataframes and creates a final dataframe with the School, Zip, and market data
2. src/data/scrape.py
  desc: rdc selenium web scraping
  functions: