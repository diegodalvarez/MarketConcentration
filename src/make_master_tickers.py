# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 14:47:16 2023

@author: Diego Alvarez
"""

import os
import pandas as pd
import datetime as dt
import yfinance as yf
import dask.dataframe as dd 

def combine_tickers():

    spx_raw = (pd.read_csv(
        "spx_members.csv").
        assign(ticker = lambda x: x.Ticker.str.split(" ").str[0])
        [["ticker"]].
        assign(index = "SPX"))
    
    russell_size = [1000, 2000, 3000]
    russell_members = ["members", "value_members", "growth_members"]
    
    df_out = spx_raw
    
    for size in russell_size:
        for member in russell_members:
            
            name = "russell_{}_{}".format(size, member)
            
            print("Woring on", name)
            
            file_name = name + ".csv"
            df_tmp = (pd.read_csv(
                file_name).
                assign(ticker = lambda x: x.Ticker.str.split(" ").str[0])
                [["ticker"]].
                assign(index = name))
            
            df_out = pd.concat([df_tmp, df_out])
        
    df_out.to_csv("tickers.csv")
    
    
def collect_data():
    
    end_date = dt.date.today()
    start_date = dt.date(year = end_date.year - 50, month = 1, day = 1)
    
    parent_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    data_path = os.path.join(parent_path, "data")
    tickers_path = os.path.join(data_path, "tickers.csv")
    
    tickers = pd.read_csv(tickers_path).ticker.dropna().drop_duplicates().to_list()
    df = (yf.download(
        tickers = tickers,
        start = start_date,
        end = end_date)
        ["Adj Close"].
        reset_index().
        melt(id_vars = "Date").
        dropna())
    
    print("Starting to Write File")
    
    df.to_parquet(
        path = "prices.parquet",
        engine = "pyarrow")
    
    print("Done Writing File")
    

collect_data()