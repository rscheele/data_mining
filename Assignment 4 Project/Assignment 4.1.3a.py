import scipy.io as spio
import sklearn.cluster as cl
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow

faces = spio.loadmat('Data/wildfaces.mat',squeeze_me=True)
X = faces['X']

Y = cl.k_means(X, 10)
centroids = Y[0]

imshow(np.reshape(X[4,:],(3,40,40)).T)
plt.show()
print '(FIG) This figure shows an image from the wildfaces.mat datset. The image corresponds to a face.'
imshow(np.reshape(centroids[4,:],(3,40,40)).T)
plt.show()
print '(FIG) This figure shows the centroids belonging to the wildfaces.mat dataset after performing K-means clustering with 10 clusters on the datset. The image corresponds to the centroids of the previous image/face'

imshow(np.reshape(X[5,:],(3,40,40)).T)
plt.show()
print '(FIG) This figure shows an image from the wildfaces.mat datset. The image corresponds to a face.'
imshow(np.reshape(centroids[5,:],(3,40,40)).T)
plt.show()
print '(FIG) This figure shows the centroids belonging to the wildfaces.mat dataset after performing K-means clustering with 10 clusters on the datset. The image corresponds to the centroids of the previous image/face'

imshow(np.reshape(X[6,:],(3,40,40)).T)
plt.show()
print '(FIG) This figure shows an image from the wildfaces.mat datset. The image corresponds to a face.'
imshow(np.reshape(centroids[6,:],(3,40,40)).T)
plt.show()
print '(FIG) This figure shows the centroids belonging to the wildfaces.mat dataset after performing K-means clustering with 10 clusters on the datset. The image corresponds to the centroids of the previous image/face'