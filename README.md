# DL4CollegeHousingPrices

### what do i need?

you will need this github repo, plus all of the data needed for the model. the total RDC data alone is > 600MB, once compressed the .zip is 187.7MB which is still too unreasonable for github. once i get lfs going it will be hosted here but until then, you can download the .zip from dropbox:

https://www.dropbox.com/s/y2qjp6lpgfj37bl/Final_Data.zip?dl=0

simply extract the .zip, copy the .csv files into the data dir, then run the model. easy!

### what is this project

this is a project to fetch price histories for college housing markets, then use either a PPO or a TD3 machine learning algorithm to forecast future housing prices.the purpose is twofold; first, i'm a college student going to school for ml/ai and am interested in the college housing market as i've gotten plenty of exposure to it. second, college market rental properties are fantastic investments. as a result, being able to spot low cost properties with high rental value is a critical asset. that is precisely what this project aims to do.

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

keep in mind that the zip fetching function is inaccurate; while it grabs all zip codes on the page, some are wrong; this is because it simply makes a google search request for an address and fetches strings that are digits & == len(5). it is an ugly way of doing things, but i needed a way to effectively query for an address and there is nothing of that nature available else. i went through and manually cleaned the data for subsequent further use; if you build the project locally, you will either need to do so yourself OR just replace the final_204.csv file with the one included in the repo.

keep in mind that NONE OF THE ABOVE STEPS ARE REQUIRED. if you download the Final_Data.zip folder, included will be the current_college_housing_data.csv file, which is used for the model. you are not required to go through the preliminary steps of generating 4 other .csvs to get to this final one. all you need to do is to get the .csv from the Final_Data.zip folder, place it into the data dir and start rocking.

however, you are more than welcome to do a local build if you'd like to see exactly what the code is doing.
