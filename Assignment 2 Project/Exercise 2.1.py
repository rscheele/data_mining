import numpy as np
import scipy.io as spio
import matplotlib.pyplot as plt

mat = spio.loadmat('wine.mat',squeeze_me=True)
data = np.array(mat['X'])

'''plt.subplot(431)
plt.hist(data[:, 0],bins=100)
plt.xlabel('Fixed acidity (tartaric) g/dm3')
plt.ylabel('Count')
plt.title('Count of fixed acidity (tartaric)')
plt.grid(True)

plt.subplot(432)
plt.hist(data[:, 1],bins=100)
plt.xlabel('Volatile acidity (acetic) g/dm3')
plt.ylabel('Count')
plt.title('Count of volatile acidity (acetic)')
plt.grid(True)

plt.subplot(433)
plt.hist(data[:, 2],bins=100)
plt.xlabel('Citric acid g/dm3')
plt.ylabel('Count')
plt.title('Count of citric acid')
plt.grid(True)

plt.subplot(434)
plt.hist(data[:, 3],bins=100)
plt.xlabel('Residual sugar g/dm3')
plt.ylabel('Count')
plt.title('Count of residual sugar')
plt.grid(True)

plt.subplot(435)
plt.hist(data[:, 4],bins=100)
plt.xlabel('Chlorides g/dm3')
plt.ylabel('Count')
plt.title('Count of chlorides')
plt.grid(True)

plt.subplot(436)
plt.hist(data[:, 5],bins=100)
plt.xlabel('Free sulfur dioxide mg/dm3')
plt.ylabel('Count')
plt.title('Count of free sulfur dioxide')
plt.grid(True)

plt.subplot(437)
plt.hist(data[:, 6],bins=100)
plt.xlabel('Total sulfur dioxide mg/dm3')
plt.ylabel('Count')
plt.title('Count of total sulfur dioxide')
plt.grid(True)

plt.subplot(438)
plt.hist(data[:, 7],bins=100)
plt.xlabel('Density g/cm3')
plt.ylabel('Count')
plt.title('Count of density')
plt.grid(True)

plt.subplot(439)
plt.hist(data[:, 8],bins=100)
plt.xlabel('pH')
plt.ylabel('Count')
plt.title('Count of pH')
plt.grid(True)

plt.subplot(4,3,10)
plt.hist(data[:, 9],bins=100)
plt.xlabel('Sulphates g/dm3')
plt.ylabel('Count')
plt.title('Count of sulphates')
plt.grid(True)

plt.subplot(4,3,11)
plt.hist(data[:, 10],bins=100)
plt.xlabel('Alcohol %')
plt.ylabel('Count')
plt.title('Count alcohol %')
plt.grid(True)

plt.subplot(4,3,12)
plt.hist(data[:, 11],bins=100)
plt.xlabel('Quality score 1-10')
plt.ylabel('Count')
plt.title('Count of scores')
plt.grid(True)

plt.subplots_adjust(hspace=.7)
plt.show()'''

plt.boxplot(data[:, 0])
plt.xlabel('Fixed acidity (tartaric) g/dm3')
plt.ylabel('Count')
plt.title('Count of fixed acidity (tartaric)')
plt.grid(True)

plt.show()