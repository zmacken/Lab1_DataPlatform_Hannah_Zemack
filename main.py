import pandas as pd

def transform_data(df):#function for cleaning up raw data
    df = df.copy()
    for col in df.columns: #remove blankspaces and into lowercase for uniformity
        if df[col].dtype == 'object':
            df[col] = df[col].str.strip()
            df[col] = df[col].str.lower()

    #transform so that currency always is upper
    df["currency"] = df["currency"].str.upper()

    #transform the price column into numeric value. Using coerce to make sure the program doesn't crash
    df['price'] = pd.to_numeric(df['price'], errors='coerce')

    #tranform the date to a correct date using coerce to not crash the program
    df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce')

    return df

def flag_data(df):
    df = df.copy() #function for flagging wrong data
    df['flag'] = '' #empty flag column

    df.loc[df['currency'].isna(), 'flag'] = 'missing currency' #flag missing currency



    return df



# import data
raw_df = pd.read_csv('lab 1 - csv.csv', sep= ';')

#print(raw_df)
# print(raw_df.info())
# print(raw_df.dtypes)

#use the function to transform data
clean_df = transform_data(raw_df)

flagged_df = flag_data(clean_df)

#print(clean_df)

print("=== RAW ===")
print(raw_df)

print("=== CLEAN ===")
print(clean_df)

print("=== FLAGGED ===")
print(flagged_df)
