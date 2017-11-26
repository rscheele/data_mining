import scipy.io as spio
import sklearn.cluster as cl
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow
import Toolbox.clusterPlot as cp

faces = spio.loadmat('Data/wildfaces.mat',squeeze_me=True)
X = faces['X']

Y = cl.k_means(X, 10)
centroids = Y[0]
clusters = Y[1]

imshow(np.reshape(X[4,:],(3,40,40)).T)
plt.show()

cp.clusterPlot(X,clusters,centroids)
plt.show()
