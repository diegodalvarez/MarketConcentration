# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 09:07:42 2023

@author: Diego
"""

import os
import pandas as pd
import yfinance as yf
import datetime as dt

parent_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
data_path = os.path.join(parent_path, "data")
out_path = os.path.join(data_path, "dm_prices.parquet")

try: 
    
    df = pd.read_parquet(
        path = out_path, engine = "pyarrow")
    
    print("Data Already downloaded")
    
except: 

    start_date = dt.date(year = 1970, month = 1, day = 1)
    end_date = dt.date.today()
    
    tickers = ["SPY", "RSP", "QQQ", "IWM", "IWB", "IWV", "EQAL", "EQWS"]
    
    df_tmp = (yf.download(
        tickers = tickers, start_date = start_date, end_date = end_date).
        reset_index().
        melt(id_vars = "Date"))
    
    (df_tmp.to_parquet(
        path = out_path,
        engine = "pyarrow"))
    
    print("Data Collected and saved")