def flag_data(df):
    df = df.copy() #function for flagging wrong data
    df['flag'] = '' #empty flag column

    df.loc[df['currency'].isna(), 'flag'] += 'missing currency,' #flag missing currency

    df.loc[df['price'] == 0 , 'flag'] += 'price is zero,' #flag price is zero

    df.loc[df['price'] >= 10000, 'flag'] += 'price is greater than 10000,' #flag high prices

    df.loc[df['id'].isna(), 'flag'] += 'missing id,' #flag missing id

    df.loc[df['name'].isna(), 'flag'] += 'missing name,' #flag missing name

    df.loc[df['price'] < 0, 'flag'] += 'negative price,' #flag negative prices

    df.loc[df['created_at'].isna(), 'flag'] += 'missing created_at,' #flag missing created at

    return df