# This script downloads a list of companies in the SP500.  
# It has the ticker symbol, company name, and sector.
# Data is saved to csv file.

#Code from: https://datahub.io/core/s-and-p-500-companies#pandas
import datapackage
import pandas as pd

data_url = 'https://datahub.io/core/s-and-p-500-companies/datapackage.json'

# to load data package into storage
package = datapackage.Package(data_url)

# to load only tabular data
resources = package.resources
for resource in resources:
	if resource.tabular:
		data = pd.read_csv(resource.descriptor['path'])
		data.to_csv('SP500_list.csv',index = False)
