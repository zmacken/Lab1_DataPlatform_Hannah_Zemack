import pandas as pd
from transform import transform_data
from flag import flag_data
from rejected import rejected_data
from analytics import analytics_summary, price_analysis

# import data
raw_df = pd.read_csv('lab 1 - csv.csv', sep= ';')

#use the function to transform data
transformed_df = transform_data(raw_df)

#use the function to flag data
flagged_df = flag_data(transformed_df)

#use the function to reject data
rejected_df, clean_df = rejected_data(flagged_df)

#use the function to create new file with analytics no need to make it a variable
analytics_summary(clean_df)

#use the function to create file no need to make it a variable
price_analysis(clean_df)

#prints so that you can test what works and what doesn't
print("=== RAW ===")
print(raw_df)

print("=== TRANSFORMED ===")
print(transformed_df)

print("=== FLAGGED ===")
print(flagged_df)

print("=== REJECTED ===")
print(rejected_df)

print("=== CLEAN ===")
print(clean_df)
