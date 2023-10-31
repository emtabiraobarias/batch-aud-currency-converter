import numpy as np
from . import helpers

def convert_to_aud(inputfilepath, conversiondatafilepath):
    df_input = read_input(inputfilepath)
    currency_graph = read_conversion_database(conversiondatafilepath)
    # for each row in input file, get converted aud value
    df_input['AUD'] = df_input.apply(lambda x : get_currency_value(currency_graph, x['Amount'], x['Currency']), axis=1)
    return list(zip(df_input['Index'], df_input['AUD']))

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