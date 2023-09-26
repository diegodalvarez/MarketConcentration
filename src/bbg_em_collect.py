# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 08:20:51 2023

@author: Diego
"""

import os
import pdblp
import datetime as dt

start_date = dt.date(year = 1970, month = 1, day = 1)
end_date = dt.date.today()

end_date_input  = end_date.strftime("%Y%m%d")
start_date_input = start_date.strftime("%Y%m%d")

parent_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
data_path = os.path.join(parent_path, "data")
out_path = os.path.join(data_path, "em_prices.parquet")

tickers = ["M1WOEW Index", "MXWO Index", "MXWOSC Index"]

con = pdblp.BCon(debug = False, port = 8194, timeout = 5_000)
con.start()

df_tmp = (con.bdh(
    tickers = tickers,
    flds = ["PX_LAST"],
    start_date = start_date_input,
    end_date = end_date_input).
    reset_index().
    melt(id_vars = "date"))

(df_tmp.to_parquet(
    path = out_path,
    engine = "pyarrow"))