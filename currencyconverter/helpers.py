import pandas as pd

def read_csv_to_df(filepath, schema):
    cols = schema.keys()
    df = pd.read_csv(filepath, delimiter=',', header=None, names=cols, dtype=schema)
    return df

def zip_df(df1, df2):
    df3 = pd.concat([df1, df2], axis=1, join='inner')
    return df3