import numpy as np
import scipy.io as spio
import sklearn.cluster as cl
import Toolbox.clusterVal as cv
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

K = [1,2,3,4,5,6,7,8,9,10]

entropy_patch = mpatches.Patch(color='blue', label='Entropy')
purity_patch = mpatches.Patch(color='red', label='Purity')
rand_patch = mpatches.Patch(color='green', label='Rand')
jaccard_patch = mpatches.Patch(color='orange', label='Jaccard')
patches = [entropy_patch, purity_patch, rand_patch, jaccard_patch]

for j in range(1,5):
    title = str('Synth' + str(j))
    path = str('Data/synth' + str(j) + '.mat')
    synth_data = spio.loadmat(path,squeeze_me=True)
    values = []

    for i in range(1,11):
        X = synth_data['X']
        Y = synth_data['y']
        Z = cl.k_means(X,i)
        clusters = Z[1]
        values.append(cv.clusterVal(Y, clusters))

    plt.plot(K, values)
    plt.legend(handles=patches)
    plt.xticks(np.arange(1, 11))
    plt.xlabel('Number of clusters')
    plt.ylabel('Cluster validity')
    plt.title(title)
    plt.show()
    print '(FIG) This figure shows the validity of the clusters from previous exercise. The validity is calculated using four measures, Entropy, Purity, Rand and Jaccard. It is calculated for the cluster sizes 1 to 10.'

