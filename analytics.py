import pandas as pd

def analytics(df):
    df_without_outliers = df[df['price'] < 10000]

    analytics_summary = pd.DataFrame({

        'snittpris': [df_without_outliers['price'].mean()],
        'medianpris': [df_without_outliers['price'].median()],
        'antal_produkter': [df_without_outliers['price'].count()],
        'antal_produkter_saknat_pris': [df_without_outliers['price'].isna().sum()]

    }).to_csv('analytics_summary.csv', index=False)
