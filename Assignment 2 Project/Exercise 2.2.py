import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from scipy.io import loadmat
from numpy import reshape
from sklearn.preprocessing import StandardScaler

# Load Matlab data file to python dict structure
mat_data = loadmat('./Data/zipdata.mat')

# Extract variables of interest
traindata = mat_data['traindata']
traindata = traindata[traindata[:,0]<=1., :]

X = traindata[:,1:]
y = traindata[:,0]

# Standardize and normalize data
X = StandardScaler().fit_transform(X)
X = (X - np.mean(X)) / np.std(X)

cov_mat = np.cov(X.T)
eig_vals, eig_vecs = np.linalg.eig(cov_mat)

# U = eig vecs of cov matrix
# s = singular values of the data matrix  are equal to the square roots of the eigenvalues of the covariance matrix
# V = Principal components
U,s,Vt = np.linalg.svd(X.T)
V = Vt.T

#Z = X*V[:,:4]

#print Z

# Visualize the i'th digit as an image
''''for i in range (1,11):
    plt.subplot(3,4,i);
    I = reshape(X[i,:],(16,16))
    plt.imshow(I, extent=(0,16,0,16), cmap=cm.gray_r);
    title = str("Digit " + str(i) + " as an image")
    plt.title(title);
plt.subplots_adjust(hspace=.7)
plt.show()'''''
