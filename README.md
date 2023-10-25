# Market Concentration
Recently (at the time of this Readme 06/25/2023 18:31) there has been a noticeable difference between larger cap companies outperforming smaller cap companies. This is particularly of focus since common market indices (SPX, NASDAQ, and others) are cap weighted. This analysis will look at the spread between cap weighted SPX and equal weighted SPX and attempt to describe the market effects of this difference.

Ultimately it is found that smaller cap index members tend to “catch-up” to their larger cap members historically. 

Examining the difference between SPX cap-weighted vs. equal weighted returns
![image](https://github.com/diegodalvarez/MarketConcentration/assets/48641554/e80c7ea5-df47-4430-aa35-80f47e5cc64a)

And their distributions
![image](https://github.com/diegodalvarez/MarketConcentration/assets/48641554/7a92b698-7d1f-433d-a0fa-05fc661d7ca7)

Running a regression between the returns spread and Russell 1000, 2000, and 3000
![image](https://github.com/diegodalvarez/MarketConcentration/assets/48641554/e5583e05-f7f3-468d-9ee7-e8b81ab89ef4)
![image](https://github.com/diegodalvarez/MarketConcentration/assets/48641554/d942d336-8da0-474b-bd0c-00c3689e4fd6)
![image](https://github.com/diegodalvarez/MarketConcentration/assets/48641554/b9088d7b-98a1-475c-b6bd-fd299b040f04)

## International Equities
The same approach was used with international equities measuring the spread between equal weight and market weight indices. Unfortuantely via Regression the relationship is less pronounced. 
![image](https://github.com/diegodalvarez/MarketConcentration/assets/48641554/3242367c-a5e5-4f86-ac00-ccee02bebe0f)
![image](https://github.com/diegodalvarez/MarketConcentration/assets/48641554/f368515e-3bd1-440a-be3e-694b47b1bbbc)

## Simple Backtesting Results
If we use the z-score as a buy/sell indicator for the index we can play back the results. Although the results make money they don't necessarily outperform the index. 
![image](https://github.com/diegodalvarez/MarketConcentration/assets/48641554/7f81d3cc-d497-4b1a-8008-63033c0aff8d)

## Z-Score Window approach
If we use a simple z-score approach where we buy a Z-Score greater than 2 hold for 3 months. We get the following
![image](https://github.com/diegodalvarez/MarketConcentration/assets/48641554/a1fb20f5-9537-4d1d-9504-17c4db573524)
![image](https://github.com/diegodalvarez/MarketConcentration/assets/48641554/502f018f-512c-4f0a-a656-716f8f783ac3)
![image](https://github.com/diegodalvarez/MarketConcentration/assets/48641554/a113fee6-b954-4fd0-ac04-3d9d44e7111a)
Although the returns do well, they don't happen frequently. One could use it to add exposure. But again the indices don't outperform SPX. 
![image](https://github.com/diegodalvarez/MarketConcentration/assets/48641554/ded39701-8f75-452a-846b-cb56f36931e4)

# Repo layout
```bash
    MarketConcentration
      └───src
          │   DataManager.py
          |   bbg_em_collect.py
          |   yf_dm_collect.py
      └───notebooks
          |   SPX_model.ipynb
          |   ARReturnsDifferential.ipynb
          |   EM_model.ipynb
          |   ReturnsPlayback.ipynb
          |   RegimeAnalysis.ipynb
          |   IndexRegimeCompare.ipynb
      └───data
          │   tickers.csv
          │   dm_prices.parquet
          │   em_prices.parquet
```

src files:
* ```DataManager.py```: Calculates returns differential and returns for index
* ```bbg_em_collect.py```: Collects Emerging Market data from Bloomberg 
* ```yf_dm_collect.py```: Collects SPX Market data from Yahoo Finance

notebook files:
* ```SPX_model.ipynb```: Examining the relationship between SPX and cap weighted SPX and running regressions against small caps indices
* ```ARReturnsDifferential.ipynb```: Attempts to fit an AR model to the returns differential
* ```EM_model.ipynb```: Examining Returns differential and regression internationally
* ```ReturnsPlayback.ipynb```: Examining different simple backtesting ideas to look at the returns
* ```RegimeAnalysis.ipynb```: Compares statistics of each return stream by splitting data by z-score
* ```IndexRegimeCompare.ipynb```: Compares returns characteristics of regime split by Z-Score

  
data files:
* ```dm_prices.parquet```: Data for Domestic SPX and Equal-Cap SPX
* ```dm_prices.parquet```: Data for MSCI Equity World Index and Equal-Cap MSCI Equity World Index
