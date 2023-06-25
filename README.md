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

# Conclusion
It is somewhat clear that there is negative linear relationship between spread of the returns differential and small caps. This implies that the less concentrated companies "catch-up". The regressions are not as solid as I'd like them to be given that the maximum  $R^2$ is 0.38, although markets won't fit perfectly.

I'd like to further examin this via rolling regression.
In terms of factor space there are two directions to look into the large cap vs. small cap factors. A possible idea would be to use rolling returns (and later rolling OLS variables) for each factor and then comparing a lagged small caps to large cap, since we expect the small caps to "catch-up" to the large caps. One of the problems with this model is that it is very easy to overfit, given that we would need to find a suitable period to lag. Although the results from this model may be promising and we can enhance the model with latent-factor models, which opens up the world of many other more complex models, we can easily overfit our original data, and greatly overfit our latent-model factor.
