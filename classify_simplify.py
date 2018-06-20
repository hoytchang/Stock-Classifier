# This script prepares the training data, then builds a knn model, and tests it
import pandas as pd
from sklearn.utils import shuffle
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn import svm
import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve
from sklearn.model_selection import validation_curve

# Read in financial data
data = pd.read_csv('SP500_financial_data.csv', index_col = False)

# Use only Consumer Discretionary or Utilities
data1 = data.loc[data['Sector'] == 'Consumer Discretionary']
data2 = data.loc[data['Sector'] == 'Utilities']
data = pd.concat([data1, data2])

# Encode categories
le = preprocessing.LabelEncoder()
le.fit(data['Sector'])
data['Sector Encoded'] = le.transform(data['Sector'])

# Separate the data into 80% training and 20% validation data sets
accuracy_array_knn = []
accuracy_array_svm = []
for i in range(10):
	data = shuffle(data)
	cutoff = int(len(data)*0.8) 
	training_data = data.iloc[0: cutoff]
	test_data = data.iloc[cutoff:len(data)]
	
	# Use only 2 features
	X_train = training_data[['Asset_turn','Capex_to_revenue']]
	X_test = test_data[['Asset_turn','Capex_to_revenue']]

	# Labels
	Y_train = training_data['Sector Encoded']
	Y_test = test_data['Sector Encoded']

	# Create K nearest neighbor model
	n_neighbors = 3
	neigh = KNeighborsClassifier(n_neighbors = n_neighbors)
	neigh.fit(X_train, Y_train)
	Y_predict = neigh.predict(X_test)

	# Compute accuracy of KNN
	n_correct = np.sum(Y_predict == Y_test)
	accuracy = n_correct / len(Y_predict)
	accuracy_array_knn.append(accuracy)

	# Create SVM classification model
	kernel = 'rbf'
	clf = svm.SVC(kernel = kernel)
	clf.fit(X_train, Y_train)
	Y_predict = clf.predict(X_test)

	# Compute accuracy of SVM
	n_correct = np.sum(Y_predict == Y_test)
	accuracy = n_correct / len(Y_predict)
	accuracy_array_svm.append(accuracy)

print('Accuracy of K = ' + str(n_neighbors) + ' nearest neighbors, average of 10 cross validations: ' + str(np.mean(accuracy_array_knn))[0:5])
print('Accuracy of SVM with ' + kernel + ' kernel, average of 10 cross validations: ' + str(np.mean(accuracy_array_svm))[0:5])

# Plot learning curve
def plot_learning_curve(estimator, title, X, y, ylim = None, cv = None, n_jobs = 1, train_sizes = np.linspace(0.1, 1.0, 10)):
	plt.figure()
	plt.title(title)
	if ylim is not None:
		plt.ylim(*ylim)
	plt.xlabel("Training examples")
	plt.ylabel("Score")
	train_sizes, train_scores, test_scores = learning_curve(estimator, X, y, cv = cv, n_jobs = n_jobs, train_sizes = train_sizes)
	train_scores_mean = np.mean(train_scores, axis = 1)
	train_scores_std = np.std(train_scores, axis = 1)
	test_scores_mean = np.mean(test_scores, axis = 1)
	test_scores_std = np.std(test_scores, axis = 1)
	plt.grid()
	plt.fill_between(train_sizes, train_scores_mean - train_scores_std, train_scores_mean + train_scores_std, alpha = 0.1, color = "r")
	plt.fill_between(train_sizes, test_scores_mean - test_scores_std, test_scores_mean + test_scores_std, alpha = 0.1, color = 'g')
	plt.plot(train_sizes, train_scores_mean, 'o-', color = 'r', label = 'Training score')
	plt.plot(train_sizes, test_scores_mean, 'o-', color = 'g', label = 'Validation score')
	plt.legend(loc = 'best')
	#return plt

# Plot validation curve
def plot_validation_curve(estimator, title, X, y, param_name, param_range, ylim = None, cv = None, n_jobs = 1, train_size = np.linspace(0.1, 1.0, 5)):
	plt.figure()
	plt.title(title)
	train_scores, test_scores = validation_curve(estimator, X, y, param_name, param_range, cv)
	train_mean = np.mean(train_scores, axis = 1)
	train_std = np.std(train_scores, axis = 1)
	test_mean = np.mean(test_scores, axis = 1)
	test_std = np.std(test_scores, axis = 1)
	plt.plot(param_range, train_mean, 'o-', color = 'r',  markersize = 5, label = 'Training score')
	plt.fill_between(param_range, train_mean + train_std, train_mean - train_std, alpha = 0.15, color = 'r')
	plt.plot(param_range, test_mean, 'o-', color = 'g',  marker = 's', markersize = 5, label = 'Validation score')
	plt.fill_between(param_range, test_mean + test_std, test_mean - test_std, alpha = 0.15, color = 'g')
	plt.grid()
	#plt.xscale('log')
	plt.legend(loc = 'best')
	plt.xlabel('Parameter')
	plt.ylabel('Score')
	plt.ylim(ylim)

# Create K nearest neighbor model using full data set
X_train = data[['Asset_turn','Capex_to_revenue']]
y_train = data['Sector Encoded']
n_neighbors = 3
neigh = KNeighborsClassifier(n_neighbors = n_neighbors)
neigh.fit(X_train, y_train)

# Plot learning curves
title = 'Learning Curves (KNN)'
plot_learning_curve(neigh, title, X_train, y_train, ylim=(0.1, 1.01), cv=10, n_jobs=1)

# Plot validation curves
title = 'Validation Curve (KNN)'
param_name = 'n_neighbors'
param_range = [1, 2, 3, 4, 5, 6]
plot_validation_curve(neigh, title, X_train, y_train, param_name = param_name, param_range = param_range)

# Show plots
plt.show()