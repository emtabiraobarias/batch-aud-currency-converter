import numpy as np
from . import helpers

def convert_to_aud(inputfilepath: str, conversiondatafilepath: str):
    '''
    Takes two input filepaths and return a list of tuples of AUD converted amounts.
    The first file defines the values to be converted and has three columns:
    (1) Integer ID; (2) Numeric value; (3) 3-character currency code.
    The seocnd file defines currency conversion data and has three columns:
    (1) Currency converting from; (2) Currency converting to; (3) Conversion rate.

    Parameters
    ----------
    inputfilepath : str
        File path to input.csv
    conversiondatafilepath : str
        File path to currencyconversiondata.csv

    Returns
    -------
    list
        list of tuples in (index: int, currency_converted_amount: float64) format
    '''
    return convert_to_currency(inputfilepath, conversiondatafilepath, 'AUD')

def convert_to_currency(inputfilepath: str, conversiondatafilepath: str, to_currency: str):
    '''
    Takes two input filepaths and return a list of tuples of AUD converted amounts.
    The first file defines the values to be converted and has three columns:
    (1) Integer ID; (2) Numeric value; (3) 3-character currency code.
    The second file defines currency conversion data and has three columns:
    (1) Currency converting from; (2) Currency converting to; (3) Conversion rate.

    Parameters
    ----------
    inputfilepath : str
        File path to input.csv
    conversiondatafilepath : str
        File path to currencyconversiondata.csv
    to_currency : str
        3-character currency code to convert the currency to.

    Returns
    -------
    list
        list of tuples in (index: int, currency_converted_amount: float64) format
    '''
    df_input = read_input(inputfilepath)
    currency_graph = read_conversion_database(conversiondatafilepath)
    # for each row in input file, get converted amount
    df_input[to_currency] = df_input.apply(lambda x : get_currency_value(currency_graph, x['Amount'], x['Currency'], to_currency), axis=1)
    return list(zip(df_input['Index'], df_input[to_currency]))

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
    # Create graph from df_conversion_db
    currency_graph = helpers.translate_df_to_graph(df_conversion_db)
    return currency_graph

def get_currency_value(graph, inputamount, fromcurrency, tocurrency='AUD'):
    if fromcurrency == tocurrency:
        return round(inputamount, 2)
    output_amount = 0.0
    graph_path = helpers.get_path(graph, fromcurrency, tocurrency)
    len_graph_path = len(graph_path)
    if(len_graph_path > 0):
        output_amount = inputamount
        for index in range(len_graph_path - 1):
            output_amount *= graph[graph_path[index]][graph_path[index + 1]]['Amount']
    # round-up to nearest .01
    return round(output_amount, 2)
