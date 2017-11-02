import numpy as np
import scipy.io as spio
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from sklearn.model_selection import KFold
from sklearn import tree
from sklearn import metrics

wine_data = spio.loadmat('Data/wine.mat',squeeze_me=True)

X = np.array(wine_data['X'])
y = np.array(wine_data['y'])
attributeNames = np.array(wine_data['attributeNames'])
classNames = np.array(wine_data['classNames'])

depth = []
for i in range(2,21):
    depth.append(i)
color = ['','red','green','purple','orange','blue','yellow','cyan','brown','pink','grey']
patches = []
j = 1

plt.figure(figsize=(15,8))

kf = KFold(n_splits=10)
for train, test in kf.split(X):
    X_train, X_test, y_train, y_test = X[train], X[test], y[train], y[test]
    error_ele = []
    for i in range(2, 21):
        clf = tree.DecisionTreeClassifier(criterion='gini', min_samples_split=100, max_depth=i)
        clf = clf.fit(X_train, y_train)
        X_pred = clf.predict(X_test)
        accuracy = metrics.accuracy_score(y_test, X_pred)
        error_rate = (1 - accuracy) * 100
        error_ele.append(error_rate)
    plt.plot(depth, error_ele, c=color[j])
    patches.append(mpatches.Patch(color=color[j], label=str('Training set ' + str(j))))
    j = j+1

plt.xticks(np.arange(1, 21))
plt.axis([0, 21, 0, 25])
plt.title('Test and training set pruning');
plt.ylabel('Error rate in %')
plt.xlabel('Decision tree depth')
plt.legend(handles=patches)
plt.show()
