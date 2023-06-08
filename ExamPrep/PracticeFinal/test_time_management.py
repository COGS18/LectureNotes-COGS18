import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from time_management import read_data, calculate_stats

def test_read_data():

    df = read_data('testfile.csv')
    
    assert type(df) == pd.DataFrame
    assert df.shape == (10, 2)
    assert list(df.columns) == ['gender', 'last_minute']


def test_calculate_stats():
    
    df = read_data(file='testfile.csv')
    
    out_M = calculate_stats(df, 'M')  
    assert isinstance(out_M, pd.Series)
    assert set(list(out_M.index)) == set(['Neither', 'Agree'])
    assert set(list(out_M.values)) == set([0.6, 0.4])
    
    out_F = calculate_stats(df, 'F')
    assert isinstance(out_F, pd.Series)
    assert set(list(out_F.index)) == set(['Disagree', 'Strong Agree', 'Agree'])
    assert set(list(out_F.values)) == set([0.4, 0.4, 0.2])

