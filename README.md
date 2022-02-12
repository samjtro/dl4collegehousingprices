### file descriptions

1. school.py
  desc: fetches school names for top 500 public schools in the country
2. zip.py
  desc: fetches zip codes
3. drop_empty.py
  desc: drops rows with empty zip codes
4. drop_dupes.py
  desc: drops duplicate schools - you are left with 203, hence the name final_203.csv

final_203.csv is used for the market modelling. keep in mind that the zip fetching function is inaccurate; while it grabs all zip codes on the page, some are wrong. this is uncommon, but still happens. i went through and manually cleaned the data for subsequent further use; if you build the file locally, you will either need to do so yourself OR just replace the final_203.csv file with the one included in the repo.

### what is this project

this is a project to fetch price histories for college housing markets, then use either a PPO or a TD3 machine learning algorithm to forecast future housing prices.the purpose is twofold; first, i'm a college student going to school for ml/ai and am interested in the college housing market as i've gotten plenty of exposure to it. second, college market rental properties are fantastic investments. as a result, being able to spot low cost properties with high rental value is a critical asset. that is precisely what this project aims to do.

### what can i do with this project?

see the license. anything you want, as long as you credit me.
