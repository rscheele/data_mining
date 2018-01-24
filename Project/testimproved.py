import improvedapriorimining as iap
from time import time

t0 = time()
iap.improved_apriori('Data/transactions_D01_5000.txt', .5, .2, 50)
t1 = time()
iap.improved_apriori('Data/transactions_D01_15000.txt', .5, .2, 50)
t2 = time()
iap.improved_apriori('Data/transactions_D01_29901.txt', .5, .2, 50)
t3 = time()
iap.improved_apriori('Data/transactions_D01D02_60952.txt', .5, .2, 50)
t4 = time()
iap.improved_apriori('Data/transactions_D01D02D11D12_119578.txt', .5, .2, 50)
t5 = time()

print '5000 transactions takes %f' %(t1-t0)
print '15000 transactions takes %f' %(t2-t1)
print '29901 transactions takes %f' %(t3-t2)
print '60952 transactions takes %f' %(t4-t3)
print '119578 transactions takes %f' %(t5-t4)
