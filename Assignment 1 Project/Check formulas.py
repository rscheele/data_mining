import numpy as np
from scipy.stats import zscore

def similarity(X, Y, method):
    # type: (object, object, object) -> object
    X = np.mat(X)
    Y = np.mat(Y)
    N1, M = np.shape(X)
    N2, M = np.shape(Y)

    method = method[:3].lower()
    if method == 'ext':  # Extended Jaccard
        XYt = X * Y.T
        sim = XYt / (np.log(np.exp(sum(np.power(X.T, 2))).T * np.exp(sum(np.power(Y.T, 2)))) - XYt)
    elif method == 'cos':  # Cosine
        sim = (X * Y.T) / (np.sqrt(sum(np.power(X.T, 2))).T * np.sqrt(sum(np.power(Y.T, 2))))
    elif method == 'cor':  # Correlation
        X_ = zscore(X, axis=1, ddof=1)
        Y_ = zscore(Y, axis=1, ddof=1)
        sim = (X_ * Y_.T) / (M - 1)
    return sim

#First three formulas where a*x
#Cosine
if similarity(1, 2, 'cos') == similarity(2*1, 2, 'cos'):
    print('True for Cosine')
else:
    print('False for Cosine')

#Extended Jaccard
if similarity(1, 2, 'ext') == similarity(2*1, 2, 'ext'):
    print('True for Extended Jaccard')
else:
    print('False for Extended Jaccard')

#Correlation
if similarity(1, 2, 'cor') == similarity(2*1, 2, 'cor'):
    print('True for Correlation')
else:
    print('False for Correlation')

# Last three formulas where b+x
# Cosine
if similarity(1, 2, 'cos') == similarity(2+1, 2, 'cos'):
    print('True for Cosine')
else:
    print('False for Cosine')

# Extended Jaccard
if similarity(1, 2, 'ext') == similarity(2+1, 2, 'ext'):
    print('True for Extended Jaccard')
else:
    print('False for Extended Jaccard')

# Correlation
if similarity(1, 2, 'cor') == similarity(2+1, 2, 'cor'):
    print('True for Correlation')
else:
    print('False for Correlation')