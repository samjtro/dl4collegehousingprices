import pandas as pd
import numpy as np

class preprocess:
        def __init__(self):
                ...
                
        def __df__(df):
                beds = []
                baths = []
                sqfts = []

                for entry in df['Meta']:
                        bedI = entry.find("bed")
                        bathI = entry.find("bath")
                        sqftI = entry.find("sqft")
                        beds.append(entry[bedI - 1])
                        baths.append(entry[bathI - 1])
                        sqft = ''
                        i = bathI + 4
                        
                        while(i<sqftI):
                                sqft += entry[i]
                                i += 1
                                
                        sqfts.append(sqft)

                del df['Meta']
                df['Bed'] = beds
                df['Bath'] = baths
                df['Sqft'] = sqfts
                df.sort_values(by=['Price'],inplace=True)
                df = df.dropna()

                return df
