# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 09:58:46 2023

@author: Diego
"""

import os 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class DataManager():
    
    def __init__(self):
        
        self.parent_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
        self.data_path = os.path.join(os.path.join(self.parent_path, "data"))
        self.df_path = os.path.join(os.path.join(self.data_path, "dm_prices.parquet"))
        
        self.df_raw = pd.read_parquet(path = self.df_path, engine = "pyarrow")
        
    def calc_return_differential(self, lookback_window = 30 * 3) -> pd.DataFrame:
        
        tickers = ["RSP", "SPY"]
        df_spread = (self.df_raw.query(
            "variable_0 == 'Adj Close' & variable_1 == @tickers").
            drop(columns = ["variable_0"]).
            rename(columns = {"variable_1": "ticker"}).
            pivot(index = "Date", columns = "ticker", values = "value").
            pct_change(periods = lookback_window).
            dropna().
            assign(
                spread_diff = lambda x: x.SPY - x.RSP,
                z_score = lambda x: (x.spread_diff - x.spread_diff.rolling(window = lookback_window).mean()) / x.spread_diff.rolling(window = lookback_window).std())
            [["spread_diff", "z_score"]])
        
        return df_spread
    
def main():
    
    data_manager = DataManager()
    df_calcs = data_manager.calc_return_differential()
    out_path = os.path.join(data_manager.data_path, "rtns.parquet")
    
    (df_calcs.to_parquet(
        path = out_path,
        engine = "pyarrow"))
    
if __name__ == "__main__":
    main()