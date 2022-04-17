import torch as t
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# historical == training data
# realtime == testing data

df = pd.read_csv("data/r_historical.csv")
df1 = pd.read_csv("data/r_realtime.csv")

X,y = train_test_split(df,df1)

RandomForestClassifier()

print(df)
print(df1)
