# This python script reads in financial data and makes some plots

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Read in financial data
data = pd.read_csv('SP500_financial_data.csv', index_col = False)

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

# Show histogram plots
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
plt.figure(2)
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
colors = ['green', 'blue', 'orange', 'red', 'purple', 'brown', 'grey', 'cyan', 'magenta', 'royalblue', 'darksalmon']
labels = ['Materials', 'Real Estate', 'Consumer Staples', 'Industrials', 'Information Technology', 'Health Care', 'Energy', 'Consumer Discretionary', 'Financials', 'Utilities', 'Telecom']

def organize_feature_by_sector(feature):
	feature_by_sector = [data_Materials[feature], 
		data_Real_Estate[feature], 
		data_Staples[feature], 
		data_Industrials[feature],
		data_IT[feature],
		data_Health_Care[feature],
		data_Energy[feature],
		data_Discretionary[feature],
		data_Financials[feature],
		data_Utilities[feature],
		data_Telecom[feature]]
	return feature_by_sector

ROE_by_sector = organize_feature_by_sector('ROE')
ROA_by_sector = organize_feature_by_sector('ROA')
PB_by_sector = organize_feature_by_sector('PB_ratio')
PE_by_sector = organize_feature_by_sector('PE_ratio')
Net_margin_by_sector = organize_feature_by_sector('Net_margin')
Asset_turn_by_sector = organize_feature_by_sector('Asset_turn')

plt.figure(3)
plt.rc('xtick', labelsize = 10)
plt.hist(ROE_by_sector, bins = 30, histtype = 'bar', stacked = True, color = colors, label = labels)
plt.title('ROE Histogram by Sector')
plt.xlabel('ROE')
plt.ylabel('Frequency')
plt.legend(loc = 'upper right')

plt.figure(4)
plt.hist(ROA_by_sector, bins = 30, histtype = 'bar', stacked = True, color = colors, label = labels)
plt.title('ROA Histogram by Sector')
plt.xlabel('ROA')
plt.ylabel('Frequency')
plt.legend(loc = 'upper right')

plt.figure(5)
plt.hist(PB_by_sector, bins = 30, histtype = 'bar', stacked = True, color = colors, label = labels)
plt.title('PB Ratio Histogram by Sector')
plt.xlabel('PB Ratio')
plt.ylabel('Frequency')
plt.legend(loc = 'upper right')

plt.figure(6)
plt.hist(PE_by_sector, bins = 30, histtype = 'bar', stacked = True, color = colors, label = labels, range = (0, 600))
plt.title('PE Ratio Histogram by Sector')
plt.xlabel('PE Ratio')
plt.ylabel('Frequency')
plt.legend(loc = 'upper right')

plt.figure(7)
plt.hist(Net_margin_by_sector, bins = 30, histtype = 'bar', stacked = True, color = colors, label = labels)
plt.title('Net margin Histogram by Sector')
plt.xlabel('Net margin')
plt.ylabel('Frequency')
plt.legend(loc = 'upper right')

plt.figure(8)
plt.hist(Asset_turn_by_sector, bins = 30, histtype = 'bar', stacked = True, color = colors, label = labels)
plt.title('Asset Turnover Histogram by Sector')
plt.xlabel('Asset Turnover')
plt.ylabel('Frequency')
plt.legend(loc = 'upper right')

# Generate scatter plots
plt.figure(9)
for i in range(len(ROE_by_sector)):
	plt.scatter(ROE_by_sector[i], ROA_by_sector[i], c = colors[i], s = 5, label = labels[i])
plt.xlabel('ROE')
plt.ylabel('ROA')
plt.legend(loc = 'best', fontsize = 6)

plt.figure(10)
for i in range(len(PB_by_sector)):
	plt.scatter(PB_by_sector[i], PE_by_sector[i], c = colors[i], s = 5, label = labels[i])
plt.xlabel('PB ratio')
plt.ylabel('PE ratio')
plt.legend(loc = 'best', fontsize = 6)
plt.ylim(0,100)

plt.figure(11)
for i in range(len(Net_margin_by_sector)):
	plt.scatter(Net_margin_by_sector[i], Asset_turn_by_sector[i], c = colors[i], s = 5, label = labels[i])
plt.xlabel('Net Margin')
plt.ylabel('Asset Turnover')
plt.legend(loc = 'best', fontsize = 6)
plt.xlim(0,0.6)

# Show plots
plt.show()