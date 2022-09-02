import pickle as pkl
import pandas as pd


def open_pkl(path: str):
    with open(path, 'rb') as o:
        pkl_file = pkl.load(o)
    return pkl_file


def aggregate(df,
              key='time',
              freq='h',
              how='mean'):
    """
    function aggregating a Pandas dataframe, it needs to have a time column
    input:
        - df: pandas DataFrame
        - key: name of time column
        - freq: time aggregation
        - how: 'mean', 'max', 'min'
    """
    if how == 'mean':
        agg_df = df.groupby([pd.Grouper(key=key, freq=freq)]).mean()
    elif how == 'max':
        agg_df = df.groupby([pd.Grouper(key=key, freq=freq)]).max()
    elif how == 'min':
        agg_df = df.groupby([pd.Grouper(key=key, freq=freq)]).min()
    elif how == 'count':
        agg_df = df.groupby([pd.Grouper(key=key, freq=freq)]).count()
    return agg_df
