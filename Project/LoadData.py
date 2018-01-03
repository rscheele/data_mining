import numpy as np
import pandas as pd

'''DateTime, CustomerID, Product Subclass, ProductID'''
D01 = pd.read_csv('Data/D01.txt', sep=';', header=0, names=['DateTime','CustomerID','ProductSubclass', 'ProductID'], usecols=(0,1,4,5))
groupedData = np.asmatrix(D01.groupby(['DateTime','CustomerID']))

print np.asmatrix(groupedData)