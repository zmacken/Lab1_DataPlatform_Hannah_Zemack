def rejected_data(df): #this function handles everything that is not approved and impossible to process
    df = df.copy()

    invalid_rows = (
        (df['price'] < 0) |
        (df['created_at'].isna()) |
        (df['id'].isna())
    )

    rejected_df = df[invalid_rows]
    clean_df = df[~invalid_rows]

    return rejected_df, clean_df
