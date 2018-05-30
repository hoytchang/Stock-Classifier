# This python script reads in a list of stocks, then for each stock, gets some financial data, and stores the results in a csv.

import pandas as pd

# Read in csv file containing list of stocks.
data = pd.read_csv('SP500_list.csv')

# Both classes of Alphabet (GOOGL and GOOG) are listed.  Remove GOOGL.  Keep GOOG.
index = data[data['Symbol']=='GOOGL'].index.item()
data = data.drop([index])
data = data.reset_index() # Reset the index so you don't have a gap where the row was dropped.

# Loop through each stock
for index in range(len(data['Symbol'])):
	# Get ticker symbol
	print('index = ' + str(index))
	ticker = data.loc[index]['Symbol']
	print('ticker = ' + ticker)

	if ticker == 'AAL':
		ticker = 'AMR' # On stockpup AAL is listed as AMR

	# Create URL
	url = 'http://www.stockpup.com/data/' + ticker + '_quarterly_financial_data.csv'
	print('url = ' + url)

	# Get data from stockpup.  Use data from latest quarter.
	quarterly = pd.read_csv(url)
	latest = quarterly.loc[0]
	ROE = latest['ROE'] #return on equity
	ROA = latest['ROA'] #return on assets
	PB_ratio = latest['P/B ratio'] #price to book ratio
	PE_ratio = latest['P/E ratio'] #price to earnings ratio
	Net_margin = latest['Net margin'] #net margin
	Asset_turn = latest['Asset turnover'] #asset turnover
	
	# Store financial data into "data"


# Save data as 'SP500_financials.csv'
