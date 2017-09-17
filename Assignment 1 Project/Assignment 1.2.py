import numpy as np
import pandas as pa
import matplotlib.pyplot as plt

df = pa.read_excel('nanonose.xls', index_col=(0,1))

df = df.drop(df.columns[[0]], axis=1)
df = df.drop(df.index[0])
df.index.names=['Sample Type', 'Concentration']

matrix = np.array(df.as_matrix())

#print(df)
#print(array)
#print(df.ix['Water'])
X = matrix[1]
Y = matrix[1]

plt.scatter(X, Y)
#plt.colorbar()
plt.show