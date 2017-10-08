import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from scipy.io import loadmat
from numpy import reshape
from itertools import combinations

# Load Matlab data file to python dict structure
mat_data = loadmat('./Data/zipdata.mat')

# Extract variables of interest
traindata = mat_data['traindata']
traindata = traindata[traindata[:,0]<=1., :]

X = traindata[:,1:]
y = traindata[:,0]

for i in range (1,11):
    plt.subplot(3,4,i);
    I = reshape(X[i,:],(16,16))
    plt.imshow(I, extent=(0,16,0,16), cmap=cm.gray_r);
    title = str("Digit " + str(i) + " as an image")
    plt.title(title);
plt.subplots_adjust(hspace=.7)
plt.show()

# Normalize data
u = np.mean(X)
X = np.asmatrix(X - u)

U, s, V = np.linalg.svd(X,full_matrices=False)

Xpca = np.array(X * V[:, :4])
X = Xpca * V[:, :4].T + u

# Visualize the i'th digit as an image
for i in range (1,11):
    plt.subplot(3,4,i);
    I = reshape(X[i,:],(16,16))
    plt.imshow(I, extent=(0,16,0,16), cmap=cm.gray_r);
    title = str("Digit " + str(i) + " as an image")
    plt.title(title);
plt.subplots_adjust(hspace=.7)
plt.show()

# PCA combinations
k = 1
for i,j in list(combinations([0,1,2,3], 2)):
    plt.subplot(2, 3, k);
    k = k+1
    plt.scatter(Xpca[:,i],Xpca[:,j],norm=True,s=2)
    plt.title(str('PC' + str(i) + ' to PC' + str(j)));
    plt.ylabel(str('PC' + str(j)))
    plt.xlabel(str('PC' + str(i)))
plt.subplots_adjust(hspace=.7)
plt.show()


fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.scatter(Xpca[:,0], Xpca[:,1], Xpca[:,2], c='blue')
plt.show()