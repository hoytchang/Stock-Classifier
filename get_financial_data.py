# This python script reads in a list of stocks, then for each stock, gets some financial data, and stores the results in a csv.

import pandas as pd
import numpy as np

# Read in csv file containing list of stocks.
data = pd.read_csv('SP500_list.csv', index_col = False)

# Both classes of Alphabet (GOOGL and GOOG) are listed.  Remove GOOGL.  Keep GOOG.
index = data[data['Symbol']=='GOOGL'].index.item()
data = data.drop([index])
data = data.reset_index() # Reset the index so you don't have a gap where the row was dropped.

# Add new columns to 'data'
data['ROE'] = np.zeros(len(data)) #return on equity
data['ROA'] = np.zeros(len(data)) #return on assets
data['PB_ratio'] = np.zeros(len(data)) #price to book ratio
data['PE_ratio'] = np.zeros(len(data)) #price to earnings ratio
data['Net_margin'] = np.zeros(len(data)) #net margin
data['Asset_turn'] = np.zeros(len(data)) #asset turn

# Loop through each stock
delete_index = []
for index in range(len(data['Symbol'])):
	# Get ticker symbol
	ticker = data.loc[index]['Symbol']

	# Fix ticker mis-matches.  This solution is cumbersome, but will do for now.
	if ticker == 'AAL':
		ticker = 'AMR'
	if ticker == 'ANDV':
		ticker = 'TSO'
	if ticker == 'ANTM':
		ticker = "WLP"
	if ticker == 'AON':
		ticker = 'AOC'
	if ticker == 'ARNC':
		ticker = 'AA'
	if ticker == 'BRK.B':
		ticker = 'BRK.A'
	if ticker == 'CBRE':
		ticker = 'CBG'
	if ticker == 'DG':
		ticker = 'DG_1'
	if ticker == 'DWDP':
		ticker = 'DOW'
	if ticker == 'DXC':
		ticker = 'CSC'
	if ticker == 'EA':
		ticker = 'ERTS'
	if ticker == 'ES':
		ticker = 'NU'
	if ticker == 'IQV':
		ticker = 'Q_1'
	if ticker == 'LB':
		ticker = 'LTD'
	if ticker == 'L':
		ticker = 'LTR'
	if ticker == 'MDLZ':
		ticker = 'KFT'
	if ticker == 'MSI':
		ticker = 'MOT'
	if ticker == 'NEE':
		ticker = 'FPL'
	if ticker == 'SPGI':
		ticker = 'MHP'
	if ticker == 'FOX':
		ticker = 'NWS'
	if ticker == 'ZBH':
		ticker = 'ZMH'

	# Create URL
	url = 'http://www.stockpup.com/data/' + ticker + '_quarterly_financial_data.csv'

	# Get data from stockpup.  Use data from latest quarter.
	try:
		# Grab url csv
		quarterly = pd.read_csv(url)
		latest = quarterly.loc[0]
		
		# Get financial data
		ROE = latest['ROE']
		ROA = latest['ROA']
		PB_ratio = latest['P/B ratio']
		PE_ratio = latest['P/E ratio']
		Net_margin = latest['Net margin']
		Asset_turn = latest['Asset turnover']

		# Store financial data into "data"
		data.loc[index, 'ROE'] = ROE
		data.loc[index, 'ROA'] = ROA
		data.loc[index, 'PB_ratio'] = PB_ratio
		data.loc[index, 'PE_ratio'] = PE_ratio
		data.loc[index, 'Net_margin'] = Net_margin
		data.loc[index, 'Asset_turn'] = Asset_turn

	except:
		print('could not get url: ' + url)
		# For tickers where url csv was not found, delete that row from 'data'
		delete_index.append(index)

# Remove rows where data was not found
print('Could not find ' + len(delete_index) + ' stocks out of '+ len(data) + '.')
for i in delete_index:
	print('could not find: '+data.loc[i]['Symbol'])

# Save data as 'SP500_financials.csv'
