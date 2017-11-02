import numpy as np
import scipy.io as spio
import sklearn.model_selection as ms
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn import metrics
import matplotlib.patches as mpatches

wine_data = spio.loadmat('Data/wine.mat',squeeze_me=True)

X = np.array(wine_data['X'])
y = np.array(wine_data['y'])
attributeNames = np.array(wine_data['attributeNames'])
classNames = np.array(wine_data['classNames'])

X_train, X_test, y_train, y_test = ms.train_test_split(X, y)

clf = tree.DecisionTreeClassifier(criterion='gini', min_samples_split=100)
clf = clf.fit(X_train, y_train)

error_rates_test = []
error_rates_train = []
depth = []

for i in range(2,21):
    clf = tree.DecisionTreeClassifier(criterion='gini',min_samples_split=100,max_depth=i)
    clf = clf.fit(X_train, y_train)
    X_pred = clf.predict(X_test)
    accuracy = metrics.accuracy_score(y_test,X_pred)
    error_rate = (1 - accuracy)*100
    depth.append(i)
    error_rates_test.append(error_rate)

for i in range(2,21):
    clf = tree.DecisionTreeClassifier(criterion='gini',min_samples_split=100,max_depth=i)
    clf = clf.fit(X_train, y_train)
    X_pred = clf.predict(X_train)
    accuracy = metrics.accuracy_score(y_train,X_pred)
    error_rate = (1 - accuracy)*100
    error_rates_train.append(error_rate)

plt.plot(depth, error_rates_test,c='red')
plt.plot(depth, error_rates_train,c='green')
plt.xticks(np.arange(1, 21))
plt.axis([0, 21, 0, 10])
plt.title('Test and training set pruning');
plt.ylabel('Error rate in %')
plt.xlabel('Decision tree depth')
red_patch = mpatches.Patch(color='red', label='Test data')
green_patch = mpatches.Patch(color='green', label='Training data')
plt.legend(handles=[red_patch,green_patch])
plt.show()