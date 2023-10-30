import numpy as np

from . import helpers

def convert_to_aud(inputfilepath, conversiondatafilepath):
    df_input = read_input(inputfilepath)
    print('df_input: \n', df_input)
    df_conversion_db = read_conversion_database(conversiondatafilepath)
    print('df_conversion_db: \n', df_conversion_db)
    return ''

def read_input(filepath):
    schema = { 
        'Index' :  np.int64, 
        'Amount' : np.float64, 
        'Currency' : str
    }
    df_input = helpers.read_csv_to_df(filepath, schema) 
    return df_input

def read_conversion_database(filepath):
    schema = { 
        'FromCurrency' : str,
        'ToCurrency' : str,
        'Amount' : np.float64
    }
    df_conversion_db = helpers.read_csv_to_df(filepath, schema) 
    return df_conversion_db

