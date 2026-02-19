import pandas as pd

# import data
raw_df = pd.read_csv('lab 1 - csv.csv', sep= ';')

print(raw_df.head())
print(raw_df.info())
print(raw_df.dtypes)

#transform data

