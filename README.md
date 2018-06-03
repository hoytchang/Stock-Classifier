# Stock-Classifier
Classify stocks in the S&P 500 using machine learning.  The features will be financial data, and the label will be the sector the stock belongs to.  <br>

The idea here is that financial ratios such as return on equity and profit margin should give us clues to what type of company the stock is.  For example, software companies might have higher margins, while a manufacturing company might have lower margins.  <br>

Sci Kit Learn and TensorFlow will be used to build a machine learning model.  <br>

### Data

First, run `download_SP500_list.py`, which will download a list of companies in the S&P 500 index, including ticker symbol, company name, and the sector it belongs in.  The data is from datahub.io and is saved in `SP500_list.csv`.  <br>

Next, run `get_financial_data.py`, which will cycle through each company in the list, and get financial data from stockpup.com.  The data is spotty: some companies are missing, and some companies have certain data entries that are missing.  Six financial metrics are selected as potential features that could be meaningful in describing the company: 
* ROE (return on equity)
* ROA (return on assets)
* PB_ratio (price to book ratio)
* PE_ratio (price to equity ratio)
* Net_margin (net margin)
* Asset_turn (asset turnover) <br>

The companies with missing data are moved, and the data is saved in `SP500_financial_data.csv`.  <br>

Eye-balling the data, we see that the PE_ratio column has data that fluctuates wildly.  In particular, Salesforce has a PE_ratio many orders of magnitude higher than any other company.  This is likely due to an very low denominator (earnings) and high numerator (price).  This extreme outlier may cause problems in training the machine learning model, so it will be removed.  <br>

### Analysis

We create histogram and scatter plots on the data to see if there are any obvious patterns.  This is done by running `analyze_data.py`.  In the histogram below, we see that of the 11 sectors, the telecom sector only has 3 stocks.  This is not enough data points to build a model, so this sector will not be used.

![alt text](https://github.com/hoytchang/Stock-Classifier/blob/master/Figure_2.png)

In the ROA vs ROE scatter plot below, we see some correlation between those two features.  This is not surprising, because ROA and ROE have the same numerator, which is earnings.

![alt text](https://github.com/hoytchang/Stock-Classifier/blob/master/Figure_9.png)

In the PE ratio vs PB ratio scatter plot below, we don't see as much of a correlation as I would have expected, since both are valuation ratios with stock price in the numerator.  This may be because earnings has much more variability than book value.  It appears sectors tend to be in narrower ranges of PB than PE.  The PE ratio chart stops at 100, but there are some outliers with PE ratio above 100.

![alt text](https://github.com/hoytchang/Stock-Classifier/blob/master/Figure_10.png)

The next scatter plot is asset turnover and net margin.  We notice that some sectors, such as real estate and finance tend to be clustered in narrow ranges for asset turnover.  This uniformity within a sector may be due to government regulation or some other factor.  In contrast, consumer discretionary appears to have more variability in asset turnover.

![alt text](https://github.com/hoytchang/Stock-Classifier/blob/master/Figure_11.png)
