# Stock-Classifier
Classify stocks in the S&P 500 using machine learning.  The features will be financial data, and the label will be the sector the stock belongs to.  <br>

The idea here is that financial ratios such as return on equity and profit margin should give us clues to what type of company the stock is.  For example, software companies might have higher margins, while a manufacturing company might have lower margins.  <br>

Sci Kit Learn and TensorFlow will be used to build a machine learning model.  <br>

### Data

First, run download_SP500_list.py, which will download a list of companies in the S&P 500 index, including ticker symbol, company name, and the sector it belongs in.  The data is from datahub.io and is saved in SP500_list.csv.  <br>

Next, run get_financial_data.py, which will cycle through each company in the list, and get financial data from stockpup.com.  The data is spotty: some companies are missing, and some companies have certain data entries that are missing.  Six financial metrics are selected: ROE, ROA, PB_ratio, PE_ratio, Net_margin, Asset_turn.  The companies with missing data are moved, and the data is saved in SP500_financial_data.csv.  <br>
