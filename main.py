import pandas as pd

def transform_data(df): #function for cleaning up raw data
    for col in df.columns: #remove blankspaces and into lowercase for uniformity
        if df[col].dtype == 'object':
            df[col] = df[col].str.strip()
            df[col] = df[col].str.lower()

    #transform the price column into numeric value. Using coerce to make sure the program doesn't crash
    df['price'] = pd.to_numeric(df['price'], errors='coerce')

    #tranform the date to a correct date using coerce to not crash the program
    df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce')



# import data
raw_df = pd.read_csv('lab 1 - csv.csv', sep= ';')

print(raw_df.head())
print(raw_df.info())
print(raw_df.dtypes)

#transform data

