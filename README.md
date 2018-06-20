# Stock-Classifier
Classify stocks in the S&P 500 using machine learning.  The features will be financial data, and the label will be the sector the stock belongs to.  <br>

The idea here is that financial ratios such as return on equity and profit margin should give us clues to what type of company the stock is.  For example, software companies might have higher margins, while a manufacturing company might have lower margins.  <br>

Scikit-learn will be used to build machine learning models.  <br>

### Data

First, run `download_SP500_list.py`, which will download a list of companies in the S&P 500 index, including ticker symbol, company name, and the sector it belongs in.  The data is from datahub.io and is saved in `SP500_list.csv`.  <br>

Next, run `get_financial_data.py`, which will cycle through each company in the list, and get financial data from stockpup.com.  The data is spotty: some companies are missing, and some companies have certain data entries that are missing.  Twelve financial metrics are selected as potential features that could be meaningful in describing the company: 
* ROE (return on equity)
* ROA (return on assets)
* PB_ratio (price to book ratio)
* PE_ratio (price to equity ratio)
* Net_margin (net margin)
* Asset_turn (asset turnover) 
* Div_payout_ratio (dividend payout ratio)
* LT_debt_to_equity (long term debt to equity ratio)
* Equity_to_assets (Equity to assets ratio)
* Current_ratio (Current ratio)
* Div_yield (dividend yield)
* Capex_to_revenue (capital expenditures to revenue ratio) <br>

The companies with missing data are moved, and the data is saved in `SP500_financial_data.csv`.  <br>

Eye-balling the data, we see that the PE_ratio column has data that fluctuates wildly.  In particular, Salesforce has a PE_ratio many orders of magnitude higher than any other company.  This is likely due to an very low denominator (earnings) and high numerator (price).  This extreme outlier may cause problems in training the machine learning model, so it will be removed.  <br>

### Analysis

We create histogram and scatter plots on the data to see if there are any obvious patterns.  This is done by running `analyze_data.py`.  In the histogram below, we see that of the 11 sectors, the telecom sector only has 3 stocks.  This is not enough data points to build a model, so this sector will not be used.  Financials and Real Estate will also be removed due to lack of data.  As a side note, the original list of companies had a lot of financial stocks, but most were removed due to lack of data.

![alt text](https://github.com/hoytchang/Stock-Classifier/blob/master/figures/Figure_3.png)

In the ROA vs ROE scatter plot below, we see some correlation between those two features.  This is not surprising, because ROA and ROE have the same numerator, which is earnings.

![alt text](https://github.com/hoytchang/Stock-Classifier/blob/master/figures/Figure_16.png)

In the PE ratio vs PB ratio scatter plot below, we don't see as much of a correlation as I would have expected, since both are valuation ratios with stock price in the numerator.  This may be because earnings has much more variability than book value.  It appears sectors tend to be in narrower ranges of PB than PE.  The PE ratio chart stops at 100, but there are some outliers with PE ratio above 100.

![alt text](https://github.com/hoytchang/Stock-Classifier/blob/master/figures/Figure_17.png)

The next scatter plot is asset turnover and net margin.  We notice that some sectors, such as real estate and utilities tend to be clustered in narrow ranges for asset turnover.  This uniformity within a sector may be due to government regulation or some other factor.  In contrast, consumer discretionary appears to have more variability in asset turnover.

![alt text](https://github.com/hoytchang/Stock-Classifier/blob/master/figures/Figure_18.png)

In general, the scatter plots look very noisy, and visually it does not appear to readily seperate the data points into sectors.  <br>

### K-Nearest Neighbors Model

Running `classify.py` will clean up the data, and build a model and test it.  First, it removes outliers, then removes the sectors with too few data points.  The data is split into 80% training and 20% test.  Using scikit-learn, a K-Nearest Neighbor model is built using the training data, and is tested using test data.  This process is done 10 times for cross-validation.  The average accuracy is around 0.23.  Considering there are 8 sectors, random guessing would result in 1/8 = 0.125.  So the model we built is a bit better than random guessing, but not by much.

### How to improve the model

Better feature selection might come a long way towards improving the accuracy of the model.  The data is very noisy, and some of the features look like they have more predictive power than other features.  Finding newer better features, or maybe even removing useless features could help.  <br>

The features PE_ratio, Net_margin and Div_payout_ratio were removed because they don't visually look like they separate the data in the scatter plots.  This results in the model accuracy increasing to about 0.29.  This seems to be a significant improvement, for doing almost no additional work. This confirms the importance of feature selection. If removing useless features can help, then almost certainly adding better features would help even more.  <br> 

The learning curve is plotted below. With the maximum number of training examples, the validation score is about 0.3, which matches the 0.29 which was calculated using a manual cross validation.  The training score remains significantly higher than the validation score, which suggests the model is overfit.  However, the training score is not high either, suggesting the model is underfit.  Either way, the model has difficulty fitting the data.

![alt text](https://github.com/hoytchang/Stock-Classifier/blob/master/figures/Figure_22.png)

Instead of using only the latest quarter's financial data, historic financial data could be used.  We could also use the standard deviation of a financial ratio, because we expect some types of companies to be stable over time, while other companies are more variable over time, due to seasonality or market cycles.  <br>

There could be a lot of variability within a sector.  For example, the IT sector contains both software and hardware.  So instead of predicting sector, we could predict the industry within a sector.  However, this would increase the number of categories, and we would need to make sure we have enough data points. <br>

A more sophisticated model might help.  A neural network, for example, might be able to use complex relationships in the data that a simple model cannot.

An easy way to improve the model would be to simplify the problem by using only sectors that are clearly seperated by the features.  For example, Asset Turnover seems to clearly seperate Consumer Discretionary from Utilities.  So if we use only data points from those two sectors, the model we build would have high accuracy.

### Support vector machine classification

In addition to the k-nearest neighbor, a support vector machine classification model is also included in `classify.py`.  Depending on which features are used, the linear kernel gave somewhat better results (accuracy around 0.32) than the rbf kernel, and also somewhat better than the KNN model.

### Simplified model

To get a model with higher accuracy, we simplify the problem by limiting the data to 2 features, Asset Turnover and Capex to Revenue, and 2 labels, Consumer Discretionary and Utilities.  Running analyze_data_simplify.py and classify_simplify.py, we get the figures below.  The features appear to do a good job of seperating the data, and the learning curve shows a much improved accuracy compared to before.

![alt text](https://github.com/hoytchang/Stock-Classifier/blob/master/figures/Figure_24.png)

![alt text](https://github.com/hoytchang/Stock-Classifier/blob/master/figures/Figure_25.png)
