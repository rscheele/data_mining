import numpy as np
import pandas as pd

'''DateTime, CustomerID, Product Subclass, ProductID'''
D01 = pd.DataFrame(pd.read_csv('Data/D01.txt', sep=';', header=0, names=['DateTime','CustomerID','ProductSubclass', 'ProductID'], usecols=(0,1,4,5)))
groupedData = np.asmatrix(D01.groupby(['DateTime','CustomerID']))

transationData = []
print groupedData.item(1)

for i in range(0,groupedData.shape[0]*2):
    transaction = np.asmatrix(groupedData.item(i))
    if transaction.shape[1] == 4:
        list = []
        for j in range(0,transaction[:,3].size):
            list.append(transaction[j,3])
        transationData.append(list)

df = pd.DataFrame(transationData)
df.to_excel('Data/D01_transactions.xls')