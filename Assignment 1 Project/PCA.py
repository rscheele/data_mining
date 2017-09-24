import numpy as np
import pandas as pa
import matplotlib.pyplot as plt
import numpy.linalg as la

df = pa.read_excel('nanonose.xls', index_col=(0,1))

df = df.drop(df.columns[[0]], axis=1)
df = df.drop(df.index[0])
df.index.names=['Sample Type', 'Concentration']

X = np.array(df.as_matrix()) #Matrix with data

u = X.mean(axis=1) #Mean of the data rows
Y = X - u[:, np.newaxis] #Centered matrix

#C = Y.T.dot(Y)/(X.shape[0]-1) #Covariance Matrix example
#C = np.cov(Y) #Covariance Matrix lazy way
#L, V = np.linalg.eig(C) #Eigenvalues and vectors

u, s, v = np.linalg.svd(Y)

Z = Y * v[:,1]

plt.plot(Z, 'ro')
plt.xlabel('PC0')
plt.ylabel('PC1')
plt.grid(True)
plt.title('Principal Component Analysis PC0 and PC1')
plt.show()