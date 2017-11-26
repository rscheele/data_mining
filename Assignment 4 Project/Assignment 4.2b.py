import matplotlib.pyplot as plt
import numpy as np
import scipy.cluster.hierarchy as hr
import scipy.io as spio
import Toolbox.clusterPlot as cp
import matplotlib.patches as mpatches

patch_1 = mpatches.Patch(color='green', label='Cluster 1')
patch_2 = mpatches.Patch(color='red', label='Cluster 2')
patch_3 = mpatches.Patch(color='cyan', label='Cluster 3')
patch_4 = mpatches.Patch(color='purple', label='Cluster 4')
patches = [patch_1, patch_2, patch_3, patch_4]

cutoff = [.5, 1.5, 2, .056, .2, .4, 7, 40, 75, .5, 2.16, 5.5]
j = 0

for i in range(1,5):
    title = str('Synth' + str(i))
    path = str('Data/synth' + str(i) + '.mat')
    synth_data = spio.loadmat(path,squeeze_me=True)
    X = np.array(synth_data['X'])

    single_cluster = hr.linkage(X, method='single', metric='euclidean')

    plt.figure()
    hr.dendrogram(single_cluster, color_threshold=cutoff[j])
    plt.xlabel('X data values')
    plt.ylabel('Y data')
    plt.title(title + ' dendogram (Single linkage)')
    plt.legend(handles=patches)
    plt.show()
    print '(FIG) This figure shows a dendogram after single linkage using euclidean distance on the ' + title + '.mat dataset. The legs represent clusters.'
    j = j+1

    average_cluster = hr.linkage(X, method='average', metric='euclidean')
    plt.figure()
    hr.dendrogram(average_cluster, color_threshold=cutoff[j])
    plt.xlabel('X data values')
    plt.ylabel('Y data')
    plt.title(title + ' dendogram (Average linkage)')
    plt.legend(handles=patches)
    plt.show()
    print '(FIG) This figure shows a dendogram after average linkage using euclidean distance on the ' + title + '.mat dataset. The legs represent clusters.'
    j = j+1

    complete_cluster = hr.linkage(X, method='complete', metric='euclidean')
    plt.figure()
    hr.dendrogram(complete_cluster, color_threshold=cutoff[j])
    plt.xlabel('X data values')
    plt.ylabel('Y data')
    plt.title(title + ' dendogram (Complete linkage)')
    plt.legend(handles=patches)
    plt.show()
    print '(FIG) This figure shows a dendogram after complete linkage using euclidean distance on the ' + title + '.mat dataset. The legs represent clusters.'
    j = j+1

    cls = hr.fcluster(complete_cluster, criterion='maxclust', t=4)
    cp.clusterPlot(X, cls)
    plt.xlabel('X data')
    plt.ylabel('Cluster threshold')
    plt.title(title + ' scatterplot')
    plt.show()
    print(
    '(FIG) The following image shows the data from the ' + title + ' dataset. This data contains points in a 2D space. The points in the data are assigned to a cluster with a hierarchical clustering algoritm, with a total of 4 possible clusters. The above image is the result after applying the algoritm and finding the clusters shown as a scatterplot.')


