from .context import currencyconverter

import pandas as pd
import networkx as nx

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test case per provided code exercise specification - importantly noting the specified assumptions."""

    def test_should_convert_to_aud(self):
        #sample_df_input = pd.DataFrame([[1,12.3,'USD'], [2,45.6,'EUR']])
        #sample_df_conversion_db = pd.DataFrame([['USD','AUD',1.54], ['EUR','USD',1.07]])
        result = currencyconverter.convert_to_aud('input/input.csv', 'input/currencyconversiondata.csv')
        expected_result = [(1, 18.94), (2, 75.14)]
        assert result == expected_result

    def test_should_read_input(self):
        #sample_df_input = pd.DataFrame([[1,12.3,'USD'], [2,45.6,'EUR']])
        result = currencyconverter.read_input('input/input.csv')
        expected_result = pd.DataFrame([[1,12.3,'USD'], [2,45.6,'EUR']], columns=['Index', 'Amount', 'Currency'])
        assert result.equals(expected_result)

    def test_should_read_conversion_db(self):
        #sample_df_conversion_db = pd.DataFrame([['USD','AUD',1.54], ['EUR','USD',1.07]])
        result = currencyconverter.read_conversion_database('input/currencyconversiondata.csv')
        expected_result = nx.Graph()
        expected_result.add_nodes_from(['USD', 'AUD', 'EUR'])
        expected_result.add_edges_from([('USD', 'AUD', {'Amount': 1.54}), ('EUR', 'USD', {'Amount': 1.07})])
        expected_result = expected_result.to_directed()
        assert nx.utils.graphs_equal(result, expected_result)


if __name__ == '__main__':
    unittest.main()