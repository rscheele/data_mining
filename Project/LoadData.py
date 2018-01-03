import numpy as np
from datetime import datetime

'DateTime, CustomerID, Product Subclass, ProductID'
D01 = np.loadtxt('Data/D01.txt', dtype=[('f0',datetime),('f1',int),('f4',int),('f5',long)], delimiter=';', skiprows=1, usecols=(0,1,4,5))
print D01