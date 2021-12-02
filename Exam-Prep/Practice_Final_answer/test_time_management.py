import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from time_management import calculate_stats, read_data, generate_plot

def test_calculate_stats():
    
    df = read_data(file='testfile.csv')
    
    out_M = calculate_stats(df, 'M')  
    print(out_M)
    assert isinstance(out_M, pd.Series)
    assert set(list(out_M.index)) == set(['Neither', 'Agree'])
    assert set(list(out_M.values)) == set([0.6, 0.4])
    
    out_F = calculate_stats(df, 'F')
    print(out_F)
    assert isinstance(out_F, pd.Series)
    assert set(list(out_F.index)) == set(['Disagree', 'Strong Agree', 'Agree'])
    assert set(list(out_F.values)) == set([0.4, 0.4, 0.2])
    
    
def test_read_data():
    df = read_data('testfile.csv')

    assert type(df) == pd.DataFrame
    assert df.shape == (10, 2)

    assert 'gender' in df.columns
    assert 'last_minute' in df.columns
    
    assert df.loc[0, 'gender'] ==  'M'
    assert df.loc[1, 'last_minute'] == 'Neither'
