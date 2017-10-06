import numpy as np
import scipy.io as spio
import matplotlib.pyplot as plt
import scipy.stats as spst

mat = spio.loadmat('Data\wine.mat',squeeze_me=True)
data = np.array(mat['X'])

label_score = 'Score'
label_attribute = ['Fixed acidity','Volatile acidity (acetic)','Citric acid',
          'Residual sugar','Chlorides','Free sulfur dioxide','Total sulfur dioxide',
          'Density','pH','Sulphates','Alcohol','Quality score']
label_title_hist = ['Count of fixed acidity (tartaric)','Count of volatile acidity (acetic)','Count of citric acid',
             'Count of residual sugar','Count of chlorides','Count of free sulfur dioxide','Count of total sulfur dioxide',
             'Count of density','Count of pH','Count of sulphates','Count alcohol %','Count of scores']
label_title_scatter = ['Scatterplot for fixed acidity (tartaric)','Scatterplot for volatile acidity (acetic)','Scatterplot for citric acid',
             'Scatterplot for residual sugar','Scatterplot for chlorides','Scatterplot for free sulfur dioxide','Scatterplot for total sulfur dioxide',
             'Scatterplot for density','Scatterplot for pH','Scatterplot for sulphates','Scatterplot for alcohol %','Scatterplot for scores']

def reject_outliers(array):
    array = array[abs(array[:,1]) < 20]
    array = array[abs(array[:,7]) < 10]
    array = array[abs(array[:,10]) < 200]
    return array

data = reject_outliers(data)

plt.figure(figsize=(15,8))
plt.hold = True
for i in range(0,11):
    plt.subplot(4,3,i+1)
    plt.ylabel(label_score)
    plt.xlabel(label_attribute[i])
    plt.title(label_title_scatter[i])
    plt.scatter(data[:,i],data[:,11],norm=True,s=1.5)
    plt.grid(True)
plt.subplots_adjust(hspace=.7)

plt.show()