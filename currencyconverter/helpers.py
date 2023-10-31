import pandas as pd
import networkx as nx

def read_csv_to_df(filepath: str, schema: dict) -> pd.DataFrame:
    '''
    Returns a dataframe reading from csv file and applying datatype dictated by schema.

    Parameters
    ----------
    filepath : str
        File path to comma-delimited csv file
    schema : dict
        Dictionary describing columns and datatypes

    Returns
    -------
    pandas.DataFrame
        Dataframe with applied schema
    '''
    cols = schema.keys()
    df = pd.read_csv(filepath, delimiter=',', header=None, names=cols, dtype=schema)
    return df

def translate_df_to_graph(df_data: pd.DataFrame) -> nx.Graph:
    '''
    Generates and returns a graph from input DataFrame.

    Parameters
    ----------
    df_data : pandas.DataFrame
        Dataframe with applied schema of currencyconversiondata

    Returns
    -------
    networkx.Graph
        Directed graph
    '''
    graph = nx.from_pandas_edgelist(df_data, 'FromCurrency', 'ToCurrency', 'Amount')
    # must be a directed graph given the one-way factual relationship between from-to currency
    graph = graph.to_directed()
    return graph

def get_path(graph: nx.Graph, source: str, target: str) -> []:
    '''
    Query graph given start (source) and end (target) points

    Parameters
    ----------
    graph : nx.Graph
        Directed graph
    source : str
        3-character currency code.
    target : str
        3-character currency code.

    Returns
    -------
    array
        array list of nodes visited by the path
    '''
    if(nx.has_path(graph, source, target)):
        path = nx.shortest_path(graph, source, target)
        return path
    else:
        return []