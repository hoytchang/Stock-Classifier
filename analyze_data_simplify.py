# This python script reads in financial data and makes some plots

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Read in financial data
data = pd.read_csv('SP500_financial_data.csv', index_col = False)

# Use only Consumer Discretionary or Utilities
data1 = data.loc[data['Sector'] == 'Consumer Discretionary']
data2 = data.loc[data['Sector'] == 'Utilities']
data = pd.concat([data1, data2])

# Histogram plots
plt.figure(1)

plt.subplot(231)
plt.hist(data['ROE'], bins = 50, facecolor='green')
plt.xlabel('ROE')
plt.ylabel('Frequency')

plt.subplot(232)
plt.hist(data['ROA'], bins = 50, facecolor='blue')
plt.xlabel('ROA')
plt.ylabel('Frequency')

plt.subplot(233)
plt.hist(data['PB_ratio'], bins = 50, facecolor='orange')
plt.xlabel('PB ratio')
plt.ylabel('Frequency')

plt.subplot(234)
plt.hist(data['PE_ratio'], bins = 50, facecolor='red', range = (0, 600))
plt.xlabel('PE ratio')
plt.ylabel('Frequency')

plt.subplot(235)
plt.hist(data['Net_margin'], bins = 50, facecolor='purple')
plt.xlabel('Net margin')
plt.ylabel('Frequency')

plt.subplot(236)
plt.hist(data['Asset_turn'], bins = 50, facecolor='brown')
plt.xlabel('Asset Turnover')
plt.ylabel('Frequency')

plt.suptitle("S&P 500 Stock Feature Histograms")

plt.figure(2)

plt.subplot(231)
plt.hist(data['Div_payout_ratio'], bins = 50, facecolor='green', range = (0, 5))
plt.xlabel('Dividend Payout Ratio')
plt.ylabel('Frequency')

plt.subplot(232)
plt.hist(data['LT_debt_to_equity'], bins = 50, facecolor='blue')
plt.xlabel('LT debt to equity ratio')
plt.ylabel('Frequency')

plt.subplot(233)
plt.hist(data['Equity_to_assets'], bins = 50, facecolor='orange')
plt.xlabel('Equity to assets ratio')
plt.ylabel('Frequency')

plt.subplot(234)
plt.hist(data['Current_ratio'], bins = 50, facecolor='red')
plt.xlabel('Current ratio')
plt.ylabel('Frequency')

plt.subplot(235)
plt.hist(data['Div_yield'], bins = 50, facecolor='purple')
plt.xlabel('Dividend yield')
plt.ylabel('Frequency')

plt.subplot(236)
plt.hist(data['Capex_to_revenue'], bins = 50, facecolor='brown', range = (0, 1))
plt.xlabel('Capex to Revenue Ratio')
plt.ylabel('Frequency')

plt.suptitle("S&P 500 Stock Feature Histograms")

# Create a dictionary of how often a sector appears
sector_freq = {}
for i in range(len(data)):
	sector = data.iloc[i].loc['Sector']
	if sector in list(sector_freq.keys()):
		sector_freq[sector] += 1
	else:
		sector_freq[sector] = 1

# Plot frequencies of sectors
x = list(sector_freq.keys())
y = list(sector_freq.values())
for i in range(len(x)):
	x[i] = x[i].replace(' ','\n')
plt.figure(3)
plt.rc('xtick', labelsize = 7)
plt.bar(x, y)
plt.ylabel('Frequency')
plt.title('S&P 500 Sector Frequency')

# Separate data by sector
data_Materials = data[data.loc[:,'Sector']=='Materials']
data_Real_Estate = data[data.loc[:,'Sector']=='Real Estate']
data_Staples = data[data.loc[:,'Sector']=='Consumer Staples']
data_Industrials = data[data.loc[:,'Sector']=='Industrials']
data_IT = data[data.loc[:,'Sector']=='Information Technology']
data_Health_Care = data[data.loc[:,'Sector']=='Health Care']
data_Energy = data[data.loc[:,'Sector']=='Energy']
data_Discretionary = data[data.loc[:,'Sector']=='Consumer Discretionary']
data_Financials = data[data.loc[:,'Sector']=='Financials']
data_Utilities = data[data.loc[:,'Sector']=='Utilities']
data_Telecom = data[data.loc[:,'Sector']=='Telecommunication Services']

# Plot feature histogram by sector
colors = ['blue', 'orange']
labels = ['Consumer Discretionary','Utilities']

def organize_feature_by_sector(feature):
	feature_by_sector = [data_Discretionary[feature],
		data_Utilities[feature]]
	return feature_by_sector

ROE_by_sector = organize_feature_by_sector('ROE')
ROA_by_sector = organize_feature_by_sector('ROA')
PB_by_sector = organize_feature_by_sector('PB_ratio')
PE_by_sector = organize_feature_by_sector('PE_ratio')
Net_margin_by_sector = organize_feature_by_sector('Net_margin')
Asset_turn_by_sector = organize_feature_by_sector('Asset_turn')

plt.figure(4)
plt.rc('xtick', labelsize = 10)
plt.hist(ROE_by_sector, bins = 30, histtype = 'bar', stacked = True, color = colors, label = labels)
plt.title('ROE Histogram by Sector')
plt.xlabel('ROE')
plt.ylabel('Frequency')
plt.legend(loc = 'upper right')

plt.figure(5)
plt.hist(ROA_by_sector, bins = 30, histtype = 'bar', stacked = True, color = colors, label = labels)
plt.title('ROA Histogram by Sector')
plt.xlabel('ROA')
plt.ylabel('Frequency')
plt.legend(loc = 'upper right')

plt.figure(6)
plt.hist(PB_by_sector, bins = 30, histtype = 'bar', stacked = True, color = colors, label = labels)
plt.title('PB Ratio Histogram by Sector')
plt.xlabel('PB Ratio')
plt.ylabel('Frequency')
plt.legend(loc = 'upper right')

plt.figure(7)
plt.hist(PE_by_sector, bins = 30, histtype = 'bar', stacked = True, color = colors, label = labels, range = (0, 600))
plt.title('PE Ratio Histogram by Sector')
plt.xlabel('PE Ratio')
plt.ylabel('Frequency')
plt.legend(loc = 'upper right')

plt.figure(8)
plt.hist(Net_margin_by_sector, bins = 30, histtype = 'bar', stacked = True, color = colors, label = labels)
plt.title('Net margin Histogram by Sector')
plt.xlabel('Net margin')
plt.ylabel('Frequency')
plt.legend(loc = 'upper right')

plt.figure(9)
plt.hist(Asset_turn_by_sector, bins = 30, histtype = 'bar', stacked = True, color = colors, label = labels)
plt.title('Asset Turnover Histogram by Sector')
plt.xlabel('Asset Turnover')
plt.ylabel('Frequency')
plt.legend(loc = 'upper right')

Div_payout_by_sector = organize_feature_by_sector('Div_payout_ratio')
LT_debt_equity_by_sector = organize_feature_by_sector('LT_debt_to_equity')
Equity_assets_by_sector = organize_feature_by_sector('Equity_to_assets')
Current_ratio_by_sector = organize_feature_by_sector('Current_ratio')
Div_yield_by_sector = organize_feature_by_sector('Div_yield')
Capex_rev_by_sector = organize_feature_by_sector('Capex_to_revenue')

plt.figure(10)
plt.hist(Div_payout_by_sector, bins = 30, histtype = 'bar', stacked = True, color = colors, label = labels, range = (0, 5))
plt.title('Dividend payout Histogram by Sector')
plt.xlabel('Dividend Payout Ratio')
plt.ylabel('Frequency')
plt.legend(loc = 'upper right')

plt.figure(11)
plt.hist(LT_debt_equity_by_sector, bins = 30, histtype = 'bar', stacked = True, color = colors, label = labels)
plt.title('LT debt to equity Histogram by Sector')
plt.xlabel('LT debt to equity ratio')
plt.ylabel('Frequency')
plt.legend(loc = 'upper right')

plt.figure(12)
plt.hist(Equity_assets_by_sector, bins = 30, histtype = 'bar', stacked = True, color = colors, label = labels)
plt.title('Equity to assets Histogram by Sector')
plt.xlabel('Equity to assets ratio')
plt.ylabel('Frequency')
plt.legend(loc = 'upper right')

plt.figure(13)
plt.hist(Current_ratio_by_sector, bins = 30, histtype = 'bar', stacked = True, color = colors, label = labels)
plt.title('Current ratio Histogram by Sector')
plt.xlabel('Current ratio')
plt.ylabel('Frequency')
plt.legend(loc = 'upper right')

plt.figure(14)
plt.hist(Div_yield_by_sector, bins = 30, histtype = 'bar', stacked = True, color = colors, label = labels)
plt.title('Dividend Yield Histogram by Sector')
plt.xlabel('Dividend Yield')
plt.ylabel('Frequency')
plt.legend(loc = 'upper right')

plt.figure(15)
plt.hist(Capex_rev_by_sector, bins = 30, histtype = 'bar', stacked = True, color = colors, label = labels, range = (0,1))
plt.title('Capex to Revenue Histogram by Sector')
plt.xlabel('Capex to Revenue ratio')
plt.ylabel('Frequency')
plt.legend(loc = 'upper right')

# Generate scatter plots
plt.figure(16)
for i in range(len(ROE_by_sector)):
	plt.scatter(ROE_by_sector[i], ROA_by_sector[i], c = colors[i], s = 5, label = labels[i])
plt.xlabel('ROE')
plt.ylabel('ROA')
plt.legend(loc = 'best', fontsize = 6)

plt.figure(17)
for i in range(len(PB_by_sector)):
	plt.scatter(PB_by_sector[i], PE_by_sector[i], c = colors[i], s = 5, label = labels[i])
plt.xlabel('PB ratio')
plt.ylabel('PE ratio')
plt.legend(loc = 'best', fontsize = 6)
plt.ylim(0,100)

plt.figure(18)
for i in range(len(Net_margin_by_sector)):
	plt.scatter(Net_margin_by_sector[i], Asset_turn_by_sector[i], c = colors[i], s = 5, label = labels[i])
plt.xlabel('Net Margin')
plt.ylabel('Asset Turnover')
plt.legend(loc = 'best', fontsize = 6)
plt.xlim(0,0.6)

plt.figure(19)
for i in range(len(Div_payout_by_sector)):
	plt.scatter(Div_payout_by_sector[i], Div_yield_by_sector[i], c = colors[i], s = 5, label = labels[i])
plt.xlabel('Dividend Payout Ratio')
plt.ylabel('Dividend Yield')
plt.legend(loc = 'best', fontsize = 6)
plt.xlim(0,5)

plt.figure(20)
for i in range(len(LT_debt_equity_by_sector)):
	plt.scatter(LT_debt_equity_by_sector[i], Equity_assets_by_sector[i], c = colors[i], s = 5, label = labels[i])
plt.xlabel('LT debt to equity ratio')
plt.ylabel('Equity to assets ratio')
plt.legend(loc = 'best', fontsize = 6)

plt.figure(21)
for i in range(len(Current_ratio_by_sector)):
	plt.scatter(Current_ratio_by_sector[i], Capex_rev_by_sector[i], c = colors[i], s = 5, label = labels[i])
plt.xlabel('Current Ratio')
plt.ylabel('Capex to Revenue Ratio')
plt.legend(loc = 'best', fontsize = 6)
plt.ylim(0,1)

plt.figure(22)
for i in range(len(Asset_turn_by_sector)):
	plt.scatter(Asset_turn_by_sector[i], Capex_rev_by_sector[i], c = colors[i], s = 5, label = labels[i])
plt.xlabel('Asset Turnover')
plt.ylabel('Capex to Revenue Ratio')
plt.legend(loc = 'best', fontsize = 6)

# Show plots
plt.show()