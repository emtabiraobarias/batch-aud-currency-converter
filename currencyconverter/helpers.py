import pandas as pd
import networkx as nx

def read_csv_to_df(filepath, schema):
    cols = schema.keys()
    df = pd.read_csv(filepath, delimiter=',', header=None, names=cols, dtype=schema)
    return df

# Create graph from df
def translate_df_to_graph(df_data):
    graph = nx.from_pandas_edgelist(df_data, 'FromCurrency', 'ToCurrency', 'Amount')
    return graph

# Query graph given start and end point
def get_path(graph, source, target):
    if(nx.has_path(graph, source, target)):
        path = nx.shortest_path(graph, source, target)
        return path
    else:
        return []
    
def format_return_to_string_list(df):
    set_list = list(zip(df['Index'], df['AUD']))
    print(set_list)
    