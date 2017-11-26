import scipy.io as spio
import sklearn.cluster as cl
import numpy as np
import matplotlib.pyplot as plt

digits = spio.loadmat('Data/digits.mat',squeeze_me=True)
X = digits['X']

plt.imshow(np.reshape(X[5,:],(16,16)), cmap='Greys')
plt.show()
print '(FIG) This figure shows an image from the digits.mat datset. The image corresponds to an unaltered digit.'

Y = cl.k_means(X, 10)
centroids_mid = Y[0]

plt.imshow(np.reshape(centroids_mid[5,:],(16,16)), cmap='Greys')
plt.show()
print '(FIG) This figure shows the centroids belonging to the digits.mat dataset after performing K-means clustering with 10 clusters on the digits datset.'

Y = cl.k_means(X, 25)
centroids_higher = Y[0]

plt.imshow(np.reshape(centroids_higher[5,:],(16,16)), cmap='Greys')
plt.show()
print '(FIG) This figure shows the centroids belonging to the digits.mat dataset after performing K-means clustering with 25 clusters on the digits datset.'

Y = cl.k_means(X, 50)
centroids_highest = Y[0]

plt.imshow(np.reshape(centroids_highest[5,:],(16,16)), cmap='Greys')
plt.show()
print '(FIG) This figure shows the centroids belonging to the digits.mat dataset after performing K-means clustering with 50 clusters on the digits dataset.'

Y = cl.k_means(X, 100)
centroids_highestest = Y[0]

plt.imshow(np.reshape(centroids_highestest[5,:],(16,16)), cmap='Greys')
plt.show()
print '(FIG) This figure shows the centroids belonging to the digits.mat dataset after performing K-means clustering with 100 clusters on the digits dataset.'
