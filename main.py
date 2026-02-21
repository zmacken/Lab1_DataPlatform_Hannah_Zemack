import pandas as pd



def rejected_data(df):
    df = df.copy()




# import data
raw_df = pd.read_csv('lab 1 - csv.csv', sep= ';')

#use the function to transform data
transformed_df = transform_data(raw_df)

flagged_df = flag_data(transformed_df)



#prints so that you can test what works and what doesn't
print("=== RAW ===")
print(raw_df)

print("=== CLEAN ===")
print(transformed_df)

print("=== FLAGGED ===")
print(flagged_df)
