import numpy as np
import pandas as pa
import matplotlib.pyplot as plt

df = pa.read_excel('nanonose.xls', index_col=(0,1))

df = df.drop(df.columns[[0]], axis=1)
df = df.drop(df.index[0])
df.index.names=['Sample Type', 'Concentration']

matrix = np.array(df.as_matrix())

#print(df)
#print(matrix[:,0])
#print(df.ix['Water'])
col_A = matrix[:,0]
col_B = matrix[:,1]
col_C = matrix[:,2]
col_D = matrix[:,3]
col_E = matrix[:,4]
col_F = matrix[:,5]
col_G = matrix[:,6]
col_H = matrix[:,7]

def plot_A_B():
    plt.subplot(221)
    plt.plot(col_A, col_B, 'ro')
    plt.xlabel('A')
    plt.ylabel('B')
    plt.grid(True)
    plt.title('A and B')

def plot_C_D():
    plt.subplot(222)
    plt.plot(col_C, col_D, 'ro')
    plt.xlabel('C')
    plt.ylabel('D')
    plt.grid(True)
    plt.title('C and D')

def plot_E_F():
    plt.subplot(223)
    plt.plot(col_E, col_F, 'ro')
    plt.xlabel('E')
    plt.ylabel('F')
    plt.grid(True)
    plt.title('E and F')

def plot_G_H():
    plt.subplot(224)
    plt.plot(col_G, col_H, 'ro')
    plt.xlabel('G')
    plt.ylabel('H')
    plt.grid(True)
    plt.title('G and H')

plot_A_B()
plot_C_D()
plot_E_F()
plot_G_H()
plt.axis([-5, 100, -5, 100])
plt.tight_layout()
plt.show()
