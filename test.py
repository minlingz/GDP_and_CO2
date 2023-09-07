# These are our import statements
import pandas as pd
import matplotlib

# This opens the csv document and saves it
df = pd.read_csv(
    "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv"
)

# This actually plots the requested information
df[
    [
        "Mortality rate, infant (per 1,000 live births)",
        "GDP per capita (constant 2010 US$)",
    ]
].plot()
