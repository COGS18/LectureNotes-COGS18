import pandas as pd
import matplotlib.pyplot as plt

from data_analysis import read_data, calculate_stats

def test_calculate_stats():
    
    df = read_data(file='testfile.csv')
    out = calculate_stats(df)
    
    assert type(out) == tuple
    assert len(out) == 2
    assert out == (5, 0)
    
def test_read_data():

    df = read_data(file='testfile.csv')
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (5, 9)
    assert 'birth_year' in list(df.columns)
    assert all(df.birth_year >= 1900) and all(df.birth_year) <= 1999
    assert all(df.still_alive == 'deceased')

    