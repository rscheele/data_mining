import numpy as np
import scipy.io as spio
import treeprint as tp
from sklearn import tree
from sklearn import metrics

wine_data = spio.loadmat('Data/wine.mat',squeeze_me=True)

X = np.array(wine_data['X'])
y = np.array(wine_data['y'])
attributeNames = np.array(wine_data['attributeNames'])
classNames = np.array(wine_data['classNames'])

clf = tree.DecisionTreeClassifier(criterion='gini',min_samples_split=100)
clf = clf.fit(X, y)

tp.tree_print(clf, attributeNames, classNames)

wine_element = np.asmatrix([6.9,1.09,0.06,2.1,0.0061,12,31,0.99,3.5,0.64,12])
wine_element_classified = clf.predict(wine_element)
print classNames[wine_element_classified]

wine_data_pred = clf.predict(X)
accuracy = metrics.accuracy_score(y,wine_data_pred)
print str('Accuracy = ' + str(accuracy*100) + '%')


