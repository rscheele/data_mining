import numpy as np
from itertools import combinations

limbs = [2,3,6,8,11,18]
print 'Mean is ' , np.mean(limbs)
print 'Standard deviation is ' , np.std(limbs).tostring()

array_n2 = []
array_n4 = []

print 'Combinations for two aliens are'
for i,j in list(combinations(limbs, 2)):
    print str(str(i) + ' and '  + str(j))
    mean = (i+j)/2.
    array_n2.append(mean)
    print str('With mean ' + str(mean))

print 'Combinations for four aliens are'
for i,j,k,l in list(combinations(limbs, 4)):
    print str(str(i) + ','  + str(j) + ','+ str(k) + ','  + str(l))
    mean = (i+j+k+l)/4.
    array_n4.append(mean)
    print str('With mean ' + str(mean))

mean_n2 = np.mean(array_n2)
mean_n4 = np.mean(array_n4)

print 'Mean for N2 is ' , str(mean_n2)
print 'Mean for N4 is ' , str(mean_n4)

print np.std(array_n2)
print np.std(array_n4)
print np.sqrt(2)*np.sqrt(((6-2)*(6-1)))
print np.sqrt(4)*np.sqrt(((6-4)*(6-1)))