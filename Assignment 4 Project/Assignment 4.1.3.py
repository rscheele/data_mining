import scipy.io as spio
import sklearn.cluster as cl
import numpy as np
from matplotlib.pyplot import imshow

faces = spio.loadmat('Data/wildfaces.mat',squeeze_me=True)
X = faces['X']

Y = cl.k_means(X,10)
centroids = Y[0]
clusters = Y[1]

imshow(np.reshape(X[1,:],(centroids,clusters)).T)