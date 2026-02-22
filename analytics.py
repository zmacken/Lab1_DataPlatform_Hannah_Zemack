import pandas as pd

def analytics_summary(df):
    df_without_outliers = df[df['price'] < 10000] #after manually checking all flags this is good based on the dataset

    pd.DataFrame({ #create new dataframe for these columns

        'snittpris': [df_without_outliers['price'].mean()],
        'medianpris': [df_without_outliers['price'].median()],
        'antal_produkter': [df_without_outliers['price'].count()],
        'antal_produkter_saknat_pris': [df_without_outliers['price'].isna().sum()]

    }).to_csv('analytics_summary.csv', index=False)

def price_analysis(df):
    df_without_outliers = df[df['price'] < 10000].reset_index(drop=True)

    top_10_expensive = df_without_outliers.nlargest(10, 'price').copy()
    top_10_expensive['category'] = 'most expensive' #creating a label so the file is easier to read later

    top_10_deviating = df_without_outliers.iloc[
        df_without_outliers['price'].sub(df_without_outliers['price'].mean()).abs().nlargest(10).index
    ].copy() #making a copy of df with outliers by calculating who is the most deviating from the mean
    top_10_deviating['category'] = 'most deviating' #creating a label so the file is easier to read later

    pd.concat([top_10_expensive, top_10_deviating]).sort_values(
        by=['category', 'price'], ascending=[True, False]
    ).to_csv('price_analysis.csv', index=False)

def rejected_products(df): #redundant in this case but for bigger projects can be good to have separate
    df.to_csv('rejected_products.csv', index=False)