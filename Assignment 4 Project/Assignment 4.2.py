import matplotlib.pyplot as plt
import numpy as np
import scipy.cluster.hierarchy as hr
import scipy.io as spio
import Toolbox.clusterPlot as cp
import matplotlib.patches as mpatches

synth1_data = spio.loadmat('Data/synth1.mat',squeeze_me=True)
X = np.array(synth1_data['X'])

patch_1 = mpatches.Patch(color='green', label='Cluster 1')
patch_2 = mpatches.Patch(color='red', label='Cluster 2')
patch_3 = mpatches.Patch(color='cyan', label='Cluster 3')
patch_4 = mpatches.Patch(color='purple', label='Cluster 4')
patches = [patch_1, patch_2, patch_3, patch_4]

cluster = hr.linkage(X, method='single', metric='euclidean')
cls = hr.fcluster(cluster, criterion='maxclust', t=4)

plt.figure()
hr.dendrogram(cluster, color_threshold=.5)
plt.xlabel('X data values')
plt.ylabel('Y data')
plt.title('Synth1 dendogram')
plt.legend(handles=patches)
plt.show()
print '(FIG) This figure shows a dendogram after single linkage using euclidean distance on the synth1.mat dataset. The legs represent clusters.'

cp.clusterPlot(X,cls)
plt.xlabel('X data')
plt.ylabel('Cluster threshold')
plt.title('Synth1 scatterplot')
plt.show()
print('(FIG) The following image shows the data from the synth1 dataset. This data contains points in a 2D space. The points in the data are assigned to a cluster with the the single linkage algoritm using eclidean distance, with a total of 4 possible clusters. The above image is the result after applying the algoritm and finding the clusters.')

