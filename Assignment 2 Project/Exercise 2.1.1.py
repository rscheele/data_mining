import numpy as np
import scipy.io as spio
import scipy.stats as spst
import matplotlib.pyplot as plt

mat = spio.loadmat('Data\wine.mat',squeeze_me=True)
data = np.array(mat['X'])
#data = spst.zscore(data)

label_count = 'Count'
label_attribute = ['Fixed acidity (tartaric g/dm3','Volatile acidity (acetic) g/dm3','Citric acid g/dm3',
          'Residual sugar g/dm3','Chlorides g/dm3','Free sulfur dioxide mg/dm3','Total sulfur dioxide mg/dm3',
          'Density g/cm3','pH','Sulphates g/dm3','Alcohol %','Quality score 1-10']
label_title_hist = ['Count of fixed acidity (tartaric)','Count of volatile acidity (acetic)','Count of citric acid',
             'Count of residual sugar','Count of chlorides','Count of free sulfur dioxide','Count of total sulfur dioxide',
             'Count of density','Count of pH','Count of sulphates','Count alcohol %','Count of scores']
label_title_box = ['Boxplot for fixed acidity (tartaric)','Boxplot for volatile acidity (acetic)','Boxplot for citric acid',
             'Boxplot for residual sugar','Boxplot for chlorides','Boxplot for free sulfur dioxide','Boxplot for total sulfur dioxide',
             'Boxplot for density','Boxplot for pH','Boxplot for sulphates','Boxplot for alcohol %','Boxplot for scores']

plt.figure(figsize=(15,8))
plt.hold = True
for i in range(0,12):
    plt.subplot(4,3,i+1)
    plt.ylabel(label_count)
    plt.xlabel(label_attribute[i])
    plt.title(label_title_hist[i])
    plt.hist(data[:,i],bins=100)
    plt.grid(True)
plt.subplots_adjust(hspace=.7)

plt.figure(figsize=(15,8))
plt.hold = True
for i in range(0,12):
    plt.subplot(4,3,i+1)
    plt.xlabel(label_attribute[i])
    plt.title(label_title_box[i])
    plt.boxplot(data[:,i],vert=False)
    plt.grid(True)
plt.subplots_adjust(hspace=.7)

def reject_outliers(array):
    array = array[abs(array[:,1]) < 20]
    array = array[abs(array[:,7]) < 10]
    array = array[abs(array[:,10]) < 200]
    return array

data = reject_outliers(data)

plt.figure(figsize=(15,8))
plt.hold = True
j = 1;
for i in (1,7,10):
    plt.subplot(3,2,j)
    j = j+1
    plt.boxplot(data[:,i],vert=False)
    plt.xlabel(label_attribute[i])
    plt.title(label_title_box[i])
    plt.grid(True)
    plt.subplot(3,2,j)
    j = j+1
    plt.hist(data[:,i],bins=100)
    plt.xlabel(label_attribute[i])
    plt.title(label_title_hist[i])
    plt.ylabel(label_count)
    plt.grid(True)
plt.subplots_adjust(hspace=.7)

plt.show()
