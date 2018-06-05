# This python script reads in a list of stocks, then for each stock, gets some financial data, and stores the results in a csv.

import pandas as pd
import numpy as np

# Read in csv file containing list of stocks.
data = pd.read_csv('SP500_list.csv', index_col = False)
print('Number of stocks in list: ' + str(len(data)))

# Add new columns to 'data'
data['ROE'] = np.zeros(len(data)) #return on equity
data['ROA'] = np.zeros(len(data)) #return on assets
data['PB_ratio'] = np.zeros(len(data)) #price to book ratio
data['PE_ratio'] = np.zeros(len(data)) #price to earnings ratio
data['Net_margin'] = np.zeros(len(data)) #net margin
data['Asset_turn'] = np.zeros(len(data)) #asset turn

data['Div_payout_ratio'] = np.zeros(len(data)) #dividend payout ratio
data['LT_debt_to_equity'] = np.zeros(len(data)) #Long term debt to equity ratio
data['Equity_to_assets'] = np.zeros(len(data)) #Equity to assets ratio
data['Current_ratio'] = np.zeros(len(data)) #Current ratio
data['Div_yield'] = np.zeros(len(data)) #Dividend yield
data['Capex_to_revenue'] = np.zeros(len(data)) #Capital expenditures to revenue ratio

# Loop through each stock
delete_index = []
count_Zeros = 0
for index in range(len(data)):
	# Get ticker symbol
	ticker = data.loc[index]['Symbol']

	# Fix ticker mis-matches.  This is a result of getting data from two different sources.
	# This solution is cumbersome, but will do for now.
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

		Div_payout_ratio = latest['Dividend payout ratio']
		LT_debt_to_equity = latest['Long-term debt to equity ratio']
		Equity_to_assets = latest['Equity to assets ratio']
		Current_ratio = latest['Current ratio']
		Div_per_share = latest['Dividend per share']
		Price = latest['Price']
		Capex = latest['Capital expenditures']
		Revenue = latest['Revenue']

		Div_yield = float(Div_per_share) / float(Price)
		Capex_to_revenue = float(Capex) / float(Revenue)

		# Store financial data into "data"
		data.loc[index, 'ROE'] = ROE
		data.loc[index, 'ROA'] = ROA
		data.loc[index, 'PB_ratio'] = PB_ratio
		data.loc[index, 'PE_ratio'] = PE_ratio
		data.loc[index, 'Net_margin'] = Net_margin
		data.loc[index, 'Asset_turn'] = Asset_turn

		data.loc[index, 'Div_payout_ratio'] = Div_payout_ratio
		data.loc[index, 'LT_debt_to_equity'] = LT_debt_to_equity
		data.loc[index, 'Equity_to_assets'] = Equity_to_assets
		data.loc[index, 'Current_ratio'] = Current_ratio
		data.loc[index, 'Div_yield'] = Div_yield
		data.loc[index, 'Capex_to_revenue'] = Capex_to_revenue
	except:
		count_Zeros += 1
		delete_index.append(index)

# Data from stockpup is spotty.  There are fields with 'None' entries.
# Remove rows if any of the entries are 'None'.
# Remove rows if all the entries are 0, meaning the csv was not found.
count_None = 0
for index in range(len(data)):
	if data.iloc[index].loc['ROE'] == 'None' or \
		data.iloc[index].loc['ROA'] == 'None' or \
		data.iloc[index].loc['PB_ratio'] == 'None' or \
		data.iloc[index].loc['PE_ratio'] == 'None' or \
		data.iloc[index].loc['Net_margin'] == 'None' or \
		data.iloc[index].loc['Asset_turn'] == 'None' or \
		data.iloc[index].loc['Div_payout_ratio'] == 'None' or \
		data.iloc[index].loc['LT_debt_to_equity'] == 'None' or \
		data.iloc[index].loc['Equity_to_assets'] == 'None' or \
		data.iloc[index].loc['Current_ratio'] == 'None' or \
		data.iloc[index].loc['Div_yield'] == 'None' or \
		data.iloc[index].loc['Capex_to_revenue'] == 'None':
		count_None += 1
		delete_index.append(index)
data = data.drop(delete_index)

# Summarize stocks that were removed
print('Number of stocks with missing data entries: ' + str(count_None))
print('Number of stocks with no data at all: ' + str(count_Zeros))
print('Number of stocks with data: ' + str(len(data)))

# Save data as 'SP500_financials.csv'
data.to_csv('SP500_financial_data.csv',index = False)