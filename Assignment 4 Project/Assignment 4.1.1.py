import numpy as np
import scipy.io as spio
import sklearn.cluster as cl
import Toolbox.clusterPlot as cp
import matplotlib.pyplot as plt
''''%matplotlib inline'''
'''--------SYNTH1----------'''

synth1_data = spio.loadmat('Data/synth1.mat',squeeze_me=True)

X = np.array(synth1_data['X'])
Y = cl.k_means(X,4)
centroids = Y[0]
clusters = Y[1]


cp.clusterPlot(X,clusters)
plt.xlabel('X data')
plt.ylabel('Y data')
plt.title('Synth1')
plt.show()
print('(FIG) The following image shows the data from the synth1 dataset. This data contains points in a 2D space. The points in the data are assigned to a cluster with the K-means algoritm, with a total of 4 possible clusters. The above image is the result after applying the algoritm.')

'''--------SYNTH2----------'''

synth2_data = spio.loadmat('Data/synth2.mat',squeeze_me=True)

X_2 = np.array(synth2_data['X'])
Y_2 = cl.k_means(X_2,4)
clusters_2 = Y_2[1]

cp.clusterPlot(X_2,clusters_2)
plt.xlabel('X data')
plt.ylabel('Y data')
plt.title('Synth2')
plt.show()
print('(FIG) The following image shows the data from the synth2 dataset. This data contains points in a 2D space. The points in the data are assigned to a cluster with the K-means algoritm, with a total of 4 possible clusters. The above image is the result after applying the algoritm.')


'''--------SYNTH3----------'''

synth3_data = spio.loadmat('Data/synth3.mat',squeeze_me=True)

X_3 = np.array(synth3_data['X'])
Y_3 = cl.k_means(X_3,4)
clusters_3 = Y_3[1]

cp.clusterPlot(X_3,clusters_3)
plt.xlabel('X data')
plt.ylabel('Y data')
plt.title('Synth3')
plt.show()
print('(FIG) The following image shows the data from the synth3 dataset. This data contains points in a 2D space. The points in the data are assigned to a cluster with the K-means algoritm, with a total of 4 possible clusters. The above image is the result after applying the algoritm.')


'''--------SYNTH4----------'''

synth4_data = spio.loadmat('Data/synth4.mat',squeeze_me=True)

X_4 = np.array(synth4_data['X'])
Y_4 = cl.k_means(X_4,4)
clusters_4 = Y_4[1]

cp.clusterPlot(X_4,clusters_4)
plt.xlabel('X data')
plt.ylabel('Y data')
plt.title('Synth4')
plt.show()
print('(FIG) The following image shows the data from the synth4 dataset. This data contains points in a 2D space. The points in the data are assigned to a cluster with the K-means algoritm, with a total of 4 possible clusters. The above image is the result after applying the algoritm.')
