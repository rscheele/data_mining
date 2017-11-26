import scipy.io as spio
import sklearn.cluster as cl
import numpy as np
import matplotlib.pyplot as plt

digits = spio.loadmat('Data/digits.mat',squeeze_me=True)
X = digits['X']

Y = cl.k_means(X, 10)
centroids_mid = Y[0]

for i in range(0,10):
    plt.subplot(3, 4, i + 1)
    plt.imshow(np.reshape(centroids_mid[i,:],(16,16)), cmap='Greys')
plt.show()
print '(FIG) This figure shows the all centroids belonging to the digits.mat dataset after performing K-means clustering with 10 clusters on the digits datset.'

Y = cl.k_means(X, 20)
centroids_mid = Y[0]

for i in range(0,20):
    plt.subplot(4, 5, i + 1)
    plt.imshow(np.reshape(centroids_mid[i,:],(16,16)), cmap='Greys')
plt.show()
print '(FIG) This figure shows the all centroids belonging to the digits.mat dataset after performing K-means clustering with 20 clusters on the digits datset.'

