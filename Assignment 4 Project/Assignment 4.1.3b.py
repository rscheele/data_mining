import scipy.io as spio
import sklearn.cluster as cl
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow

faces = spio.loadmat('Data/wildfaces.mat',squeeze_me=True)
X = faces['X']

Y = cl.k_means(X, 2)
centroids_lowest = Y[0]

imshow(np.reshape(X[0,:],(3,40,40)).T)
plt.show()
print '(FIG) This figure shows an image from the wildfaces.mat datset. The image corresponds to an unaltered face.'

imshow(np.reshape(centroids_lowest[0,:],(3,40,40)).T)
plt.show()
print '(FIG) This figure shows the centroids belonging to the wildfaces.mat dataset after performing K-means clustering with 2 clusters on the wildfaces datset.'

Y = cl.k_means(X, 5)
centroids_lower = Y[0]

imshow(np.reshape(centroids_lower[0,:],(3,40,40)).T)
plt.show()
print '(FIG) This figure shows the centroids belonging to the wildfaces.mat dataset after performing K-means clustering with 5 clusters on the wildfaces datset.'

Y = cl.k_means(X, 10)
centroids_mid = Y[0]

imshow(np.reshape(centroids_mid[0,:],(3,40,40)).T)
plt.show()
print '(FIG) This figure shows the centroids belonging to the wildfaces.mat dataset after performing K-means clustering with 10 clusters on the wildfaces datset.'

Y = cl.k_means(X, 50)
centroids_higher = Y[0]

imshow(np.reshape(centroids_higher[0,:],(3,40,40)).T)
plt.show()
print '(FIG) This figure shows the centroids belonging to the wildfaces.mat dataset after performing K-means clustering with 50 clusters on the wildfaces datset.'

Y = cl.k_means(X, 100)
centroids_highest = Y[0]

imshow(np.reshape(centroids_highest[0,:],(3,40,40)).T)
plt.show()
print '(FIG) This figure shows the centroids belonging to the wildfaces.mat dataset after performing K-means clustering with 100 clusters on the wildfaces dataset.'


